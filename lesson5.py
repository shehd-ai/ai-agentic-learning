import requests


def show_profile(username):
    url = "https://api.github.com/users/" + username
    response = requests.get(url)
    print("Status code:", response.status_code)

    if response.status_code != 200:
        print("Could not find that user.")
        return

    data = response.json()
    print("Username:", data["login"])
    print("Public repositories:", data["public_repos"])
    print("Profile link:", data["html_url"])


show_profile("shehd-ai")