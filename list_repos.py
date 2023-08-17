import requests

username = "DianaNicoletaA"
token = "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"  # Înlocuiește cu propriul tău token de autentificare

headers = {
    "Authorization": f"token {token}"
}

url = f"https://api.github.com/users/{username}/repos"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    repos = response.json()  # Transformă răspunsul într-un dicționar Python

    # Filtrăm și listăm doar repository-urile cu numele care începe cu "TestRepo"
    test_repos = [repo["name"] for repo in repos if repo["name"].startswith("TestRepo")]
    for repo_name in test_repos:
        print(repo_name)
else:
    print(f"Request failed with status code: {response.status_code}")
