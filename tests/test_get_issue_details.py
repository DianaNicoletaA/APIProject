import unittest
import random
import string
from api.api_helper import GitHubAPIHelper

class TestGetIssueDetails(unittest.TestCase):
    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    def test_get_issue_details(self):
        github_helper = GitHubAPIHelper()

        # Crearea unui repository temporar
        unique_repo_name = f"TestRepo_{self.generate_random_string(6)}"
        response_create_repo = github_helper.create_repo(unique_repo_name)
        self.assertEqual(response_create_repo.status_code, 201, "Failed to create repository")

        # Crearea unui issue în repository-ul temporar
        issue_title = "Test Issue"
        issue_body = "This is a test issue"
        response_create_issue = github_helper.create_issue(unique_repo_name, issue_title, issue_body)
        self.assertEqual(response_create_issue.status_code, 201, "Failed to create issue")
        issue_number = response_create_issue.json()["number"]

        # Citirea detaliilor issue-ului creat
        response_get_issue_details = github_helper.get_issue_details(unique_repo_name, issue_number)
        self.assertEqual(response_get_issue_details.status_code, 200, "Failed to get issue details")

if __name__ == '__main__':
    unittest.main()
