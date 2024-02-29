import requests


def get_github_info(username):
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url)

    if response.status_code == 200:
        user_data = response.json()
        print(f"Name: {user_data['name']}")
        print(f"Bio: {user_data['bio']}")
        print(f"Public Repositories: {user_data['public_repos']}")
    else:
        print("Failed to fetch GitHub user data.")

    github_username = input("Enter Github username: ")
    get_github_info(github_username)
