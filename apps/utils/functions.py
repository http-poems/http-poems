import requests


def get_repo_contributors():
    response = requests.get(
        "https://api.github.com/repos/http-poems/http-poems/contributors"
    )
    required_fields = ["avatar_url", "html_url"]
    cleaned_response = [
        dict([(k, v) for k, v in item.items() if k in required_fields])
        for item in response.json()
    ]
    return cleaned_response
