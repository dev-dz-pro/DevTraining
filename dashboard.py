import dash
import dash_core_components as dcc
import dash_html_components as html
from  JiraInfo import *
from GithubInfo import *
import flask

server = flask.Flask(__name__)
app = dash.Dash(server=server)

def serve_layout():

    issues, (num_issues, pointes, num_tasks, num_sprints) = get_jira_data()
    pullrequests, num_puuls = get_pull_requests()
    data = {"Number of issues": num_issues, "Total Story points": pointes, "Number of tasks": num_tasks, "Number of sprints": num_sprints, "Pull Requests": num_puuls}
    html1, html2, html3, html4, html5 = [html.Div([html.H3(v), html.P(k)], className="single_list_counter") for k, v in data.items()]

    return html.Div([
                    html.Div([
                        html.Div([
                            html.H1("VIFBOX Dashbourd Test", id="titlee", style={"height": "50px"}),
                            html.Div([
                                dcc.Graph(figure = {
                                    "data": [{"x": ["issues", "Total Story Pointes", "tasks", "sprints", "pull requests"], "y": [num_issues, pointes, num_tasks, num_sprints, num_puuls], "name": 'Rest of world',
                                            "marker": {"color": 'rgb(79, 105, 209)'}, 'line': {'shape': 'spline', 'smoothing': 1.3}}],
                                    "layout": {"title": 'Jira & Github Info', "showlegend": True, "legend": {"x": 0.8, "y": 0.9}, "margin": {"l": 40, "r": 0, "t": 40, "b": 30}}
                                    }, style={'height': "50vh"})], id='my-graph'),
                            html.Div([
                                html.Div([
                                    html.H3("JIRA Issues", className="ticketstitle"),
                                    html.Div([html.Ul(issues, style={"overflow":"hidden", "overflow-y":"scroll", "height": "230px", "padding": 0})], className="task_info"),
                                ], style={"width": "50%"}),
                                html.Div([
                                    html.H3("Pull Requests", className="ticketstitle"),
                                    html.Div([html.Ul(pullrequests, style={"overflow":"hidden", "overflow-y":"scroll", "height": "230px", "padding": 0})], className="task_info")
                                ], id="pulls_info", style={"width": "50%"})
                            ], className="ticket_info"),
                        ]),

                        html.Div([
                            html1, html2, html3, html4, html5,
                            html.Div([
                                dcc.Graph(figure = {
                                        "data": [{"labels": ["issues", "Pointes", "tasks", "sprints", "requests"],  # , "pull requests"
                                                "values": [num_issues, pointes, num_tasks, num_sprints, num_puuls], "type": "pie", "hole": .3}],
                                        "layout": { "title": "<b>JIRA Info</b>" } } )], id="pie-chart"),
                        ], id="tickets", style={"margin-top": "85px"})] # 50 H1height + 25 textheight + 10  padding
                    , id="container")

            ], id='mydash')

app.layout = serve_layout



if __name__ == '__main__':
    app.run_server(debug=True)
