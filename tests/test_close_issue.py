import unittest
import random
import string
from api.api_helper import GitHubAPIHelper


class TestCloseIssue(unittest.TestCase):
    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    def test_close_issue(self):
        github_helper = GitHubAPIHelper()

        # Crearea unui repository temporar
        unique_repo_name = f"TestRepo_{self.generate_random_string(6)}"
        response_create_repo = github_helper.create_repo(unique_repo_name)
        self.assertEqual(response_create_repo.status_code, 201, "Failed to create repository")

        # Crearea unui issue in repository-ul temporar
        issue_title = "Test Issue"
        issue_body = "This is a test issue"
        response_create_issue = github_helper.create_issue(unique_repo_name, issue_title, issue_body)
        self.assertEqual(response_create_issue.status_code, 201, "Failed to create issue")
        issue_number = response_create_issue.json()["number"]

        # Incercarea de inchidere a issue-ului
        response_close_issue = github_helper.close_issue(unique_repo_name, issue_number)
        self.assertEqual(response_close_issue.status_code, 200, "Failed to close issue")
        self.assertEqual(response_close_issue.json()["state"], "closed", "Issue was not closed")


if __name__ == '__main__':
    unittest.main()
