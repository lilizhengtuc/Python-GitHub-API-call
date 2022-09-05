import requests

from plotly.graph_objs import Bar
from plotly import offline

# make an API call and store the response
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {'Accept': 'application/vnd.github.v3+json'}
request = requests.get(url, headers=headers)
print(f"Status code: {request.status_code}")

# process results
response_dict = request.json()
repo_dicts = response_dict['items']
repo_names, stars = [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# make visulization
data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars,
}]

my_layout = {
    'title': "GitHub Python projects with most stars",
    'xaxis': {'title': 'Repository'},
    'yaxis': {'title': 'Stars'},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename="python_repos_visual1.html")

