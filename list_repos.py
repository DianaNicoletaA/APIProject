import requests

username = "DianaNicoletaA"
token = "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"  # inlocuieste cu propriul tau token de autentificare

headers = {
    "Authorization": f"token {token}"
}

url = f"https://api.github.com/users/{username}/repos"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    repos = response.json()  # Transforma raspunsul intr-un dictionar Python

    # Filtram si listam doar repository-urile cu numele care incepe cu "TestRepo"
    test_repos = [repo["name"] for repo in repos if repo["name"].startswith("TestRepo")]
    for repo_name in test_repos:
        print(repo_name)
else:
    print(f"Request failed with status code: {response.status_code}")