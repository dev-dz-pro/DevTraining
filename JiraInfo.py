from jira import JIRA
import dash_html_components as html
import os


jiraOptions = {'server': "https://ayoub02.atlassian.net"}  #comment
jira = JIRA(options=jiraOptions, basic_auth=(os.environ["jira_email"], os.environ["jira_token"]))



def get_jira_data():

    pointes = 0
    num_tasks = 0
    num_issues = 0
    sprints = set()
    issues = []

    for singleIssue in jira.search_issues(jql_str='project=VIFBOX-Project'):
        issue_type = singleIssue.fields.issuetype.name
        story_points = singleIssue.fields.customfield_10016
        if singleIssue.fields.customfield_10020 is None:
            sprint_name = 'Backlog'
        else:
            sprint_name = singleIssue.fields.customfield_10020[0].name
            sprints.add(sprint_name)

        if issue_type == "Task":
            issue_tp = html.Img(src="assets/static/view_task.svg", style={"height": "25", "width": "25"})
        elif issue_type == "Bug":
            issue_tp = html.Img(src="assets/static/view_bug.svg", style={"height": "25", "width": "25"})
        else:
            issue_tp = html.Img(src="assets/static/view_story.svg", style={"height": "25", "width": "25"})

        htmll = html.Li([
                    html.Div(
                        [issue_tp,
                            html.Div([
                                html.P(singleIssue.fields.summary, className="task_name"),
                                html.P(singleIssue.fields.status.name, className="task_des")
                            ], className="task_name_des", style={"width": "30%"}),
                            html.P(f"Story points: {story_points}", className="task_points"), #, style={"width": "100px"}
                            html.P(sprint_name, className="task_sprint_name")
                        ], className="taskticket")
                ], style={"list-style-type": "none"}) 
        issues.append(htmll)

        if story_points is not None:
            pointes += story_points
        if issue_type == "Task":
            num_tasks += 1
        num_issues += 1

    return issues, (num_issues, pointes, num_tasks, len(sprints))
