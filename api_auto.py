import requests

import json

username ="bibekbajagain074"
# Define the GitHub API URL for listing all repositories of a user
url = f"https://api.github.com/users/{username}/repos"
print (url)
response =requests.get(url)

print(response)

# Send a GET request to the GitHub API to get the list of repositories
response = requests.get(url)


# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    repos_data = response.json()


    # Initialize a list to hold details of all repositories
    all_repos_info = []

    # Loop through each repository in the response
    for repo in repos_data:
        # Extract relevant data for each repository
        repo_info = {
            "name": repo.get("name"),
            "full_name": repo.get("full_name"),
            "description": repo.get("description"),
            "stars": repo.get("stargazers_count"),
            "forks": repo.get("forks_count"),
            "open_issues": repo.get("open_issues_count"),
            "owner": repo["owner"].get("login"),
            "html_url": repo.get("html_url")
        }
        
                # Append the repo info to the list
        all_repos_info.append(repo_info)

    # Save the details of all repositories to a JSON file
    with open(f"{username}_repos_info.json", "w", encoding="utf-8") as f:
        json.dump(all_repos_info, f, ensure_ascii=False, indent=4)

    print(f"Repository information saved to {username}_repos_info.json")
else:
    print("Failed to retrieve data:", response.status_code)