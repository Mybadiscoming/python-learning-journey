import requests
username = input("Enter GitHub username: ")
url = f" https://api.github.com/users/{username}/repos"
response = requests.get(url)   
data = response.json()

for repo in data:
    print(repo['name'])
