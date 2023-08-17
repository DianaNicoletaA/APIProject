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

    for repo in repos:
        print(repo["name"])
else:
    print(f"Request failed with status code: {response.status_code}")
