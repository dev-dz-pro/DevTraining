from github import Github
import dash_html_components as html
import os

# First create a Github instance using an access token
g = Github(os.environ["github_token"]) 

# Function thats return a list of puul requests as a tempates
def get_pull_requests():
    pull_requests = []
    for repo in g.get_user().get_repos():  # if repo.name == "DevTraining":
        pulls = repo.get_pulls(state='open', base='master')
        for i, pr in enumerate(pulls, start=1):
            htmll = html.Li([
                        html.Div([
                            html.Label(i, className="task_type", style={"width": "20px"}),
                            html.Div([
                                html.P(pr.user.login, className="task_name"),
                                html.P(pr.title, className="task_des")
                            ], className="task_name_des"),
                            html.P(str(pr.created_at)[:-3], className="date_time"),
                            html.A(html.Button("Link", className='btn'),href=pr.html_url)
                        ], className="taskticket", style={"height": "35px"})
                    ])
            pull_requests.append(htmll)
            
    return pull_requests, len(pull_requests)
