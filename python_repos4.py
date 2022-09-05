import requests

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {'Accept': 'application/vnd.github.v3+json'}
request = requests.get(url, headers=headers)

response = request.json()

# find out the total number of repos
print(f"Total repositories: {response['total_count']}")

# explore details about the repos
repo_dicts = response['items']
print(f"Repositories returned: {len(repo_dicts)}")

print("\nSelected information about each repo:")
for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Description: {repo_dict['description']}")