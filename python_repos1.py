import requests

# make an API call and restore the response

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {'Accept': 'application/vnd.github.v3+json'}
request = requests.get(url, headers=headers)
print(f"Status code: {request.status_code}")

# store the API response
response = request.json()

# print out the content in the response
print(response.keys())