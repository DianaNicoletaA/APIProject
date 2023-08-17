import os
import requests


class GitHubAPIHelper:
    BASE_URL = "https://api.github.com"

    def __init__(self):
        # Fetching the token from environment variable
        self.token = os.environ.get("GITHUB_API_TOKEN", "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")
        if not self.token:
            raise ValueError("GITHUB_API_TOKEN environment variable not set!")

        # Setting a default GitHub username
        self.default_user = "DianaNicoletaA"

        self.headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }

    def create_repo(self, name, description="", owner=None):
        owner = owner or self.default_user
        url = f"{self.BASE_URL}/user/repos"
        data = {
            "name": name,
            "description": description,
            "private": False
        }
        response = requests.post(url, headers=self.headers, json=data)
        return response

    def get_repo_details(self, repo, owner=None):
        owner = owner or self.default_user
        url = f"{self.BASE_URL}/repos/{owner}/{repo}"
        response = requests.get(url, headers=self.headers)
        return response

    def update_repo(self, repo, name=None, description=None, owner=None):
        owner = owner or self.default_user
        url = f"{self.BASE_URL}/repos/{owner}/{repo}"
        data = {}
        if name:
            data["name"] = name
        if description:
            data["description"] = description
        response = requests.patch(url, headers=self.headers, json=data)
        return response

    def delete_repo(self, repo, owner=None):
        owner = owner or self.default_user
        url = f"{self.BASE_URL}/repos/{owner}/{repo}"
        response = requests.delete(url, headers=self.headers)
        return response

    def create_issue(self, repo, title, body="", owner=None):
        owner = owner or self.default_user
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/issues"
        data = {
            "title": title,
            "body": body
        }
        response = requests.post(url, headers=self.headers, json=data)
        return response

    def get_issue_details(self, repo, issue_number, owner=None):
        owner = owner or self.default_user
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/issues/{issue_number}"
        response = requests.get(url, headers=self.headers)
        return response

    def update_issue(self, repo, issue_number, title=None, body=None, owner=None):
        owner = owner or self.default_user
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/issues/{issue_number}"
        data = {}
        if title:
            data["title"] = title
        if body:
            data["body"] = body
        response = requests.patch(url, headers=self.headers, json=data)
        return response

    def close_issue(self, repo, issue_number, owner=None):
        owner = owner or self.default_user
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/issues/{issue_number}"
        data = {
            "state": "closed"
        }
        response = requests.patch(url, headers=self.headers, json=data)
        return response
