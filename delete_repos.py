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
        repo_name = repo["name"]

        # Verifică dacă numele repo-ului începe cu "TestRepo" și are extensia specificată
        if repo_name.startswith("TestRepo") and repo_name.endswith("+EXTENSIE"):
            print(f"Deleting {repo_name}...")

            delete_url = f"https://api.github.com/repos/{username}/{repo_name}"
            delete_response = requests.delete(delete_url, headers=headers)

            if delete_response.status_code == 204:
                print(f"{repo_name} deleted successfully.")
            else:
                print(f"Failed to delete {repo_name}. Status code: {delete_response.status_code}")
else:
    print(f"Request failed with status code: {response.status_code}")
