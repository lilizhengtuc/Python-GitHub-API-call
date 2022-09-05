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

# examine the first repo
repo_dict = repo_dicts[0]
print(f"\nKeys:{len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)
