import requests
import json
import os

# Your GitHub personal access token
TOKEN = os.environ['GITHUB_PAT']
with open('packages.json', 'r') as f:
    # Load the JSON data from the file
    data = json.load(f)

# Extract unique repos
repos = set()
for item in data:
    repos.add(item['repo'])
    for dep in item['dependencies']:
        repos.add(dep)
        

# Set up headers for requests
headers = {
    'Authorization': f'token {TOKEN}',
    'Accept': 'application/vnd.github.v3+json',
}

# Get the list of repos the user has starred
starred_repos = requests.get('https://api.github.com/user/starred', headers=headers).json()

# Get the list of repos the user is watching
watched_repos = requests.get('https://api.github.com/user/subscriptions', headers=headers).json()

# Loop through repos and star/subscribe them
for repo_url in repos:
    # Extract owner and repo from URL
    *_, owner, repo = repo_url.rstrip('/').split('/')

    
    # Star the repo
    star_url = f'https://api.github.com/user/starred/{owner}/{repo}'
    response = requests.put(star_url, headers=headers)
    if response.status_code == 204:
        print(f'Successfully starred {repo_url}')
    else:
        print(f'Failed to star {repo_url}. Status code: {response.status_code}')
    
    # Subscribe to notifications
    notifications_url = f'https://api.github.com/repos/{owner}/{repo}/subscription'
    payload = json.dumps({
        'subscribed': True,
        'ignored': False,
    })
    response = requests.put(notifications_url, headers=headers, data=payload)
    if response.status_code == 200:
        print(f'Successfully subscribed to {repo_url}')
    else:
        print(f'Failed to subscribe to {repo_url}. Status code: {response.status_code}')

# Get the list of repos the user has starred
starred_repos = []
starred_repos_url = 'https://api.github.com/user/starred'
while starred_repos_url:
    response = requests.get(starred_repos_url, headers=headers)
    starred_repos.extend(response.json())
    starred_repos_url = response.links.get('next', {}).get('url')

# The rest of your script...

# Unstar repos not in the file
for starred_repo in starred_repos:
    repo_url = f"https://github.com/{starred_repo['owner']['login']}/{starred_repo['name']}"
    if repo_url not in repos:
        # Unstar the repo
        star_url = f'https://api.github.com/user/starred/{starred_repo["owner"]["login"]}/{starred_repo["name"]}'
        response = requests.delete(star_url, headers=headers)
        if response.status_code == 204:
            print(f'Successfully unstarred {repo_url}')
        else:
            print(f'Failed to unstar {repo_url}. Status code: {response.status_code}')


# Get the list of repos the user is watching
watched_repos = []
watched_repos_url = 'https://api.github.com/user/subscriptions'
while watched_repos_url:
    response = requests.get(watched_repos_url, headers=headers)
    watched_repos.extend(response.json())
    watched_repos_url = response.links.get('next', {}).get('url')

# The rest of your script...

# Unsubscribe from repos not in the file
for watched_repo in watched_repos:
    repo_url = f"https://github.com/{watched_repo['owner']['login']}/{watched_repo['name']}"
    if repo_url not in repos:
        # Unsubscribe from the repo
        notifications_url = f'https://api.github.com/repos/{watched_repo["owner"]["login"]}/{watched_repo["name"]}/subscription'
        response = requests.delete(notifications_url, headers=headers)
        if response.status_code == 204:
            print(f'Successfully unsubscribed from {repo_url}')
        else:
            print(f'Failed to unsubscribe from {repo_url}. Status code: {response.status_code}')
