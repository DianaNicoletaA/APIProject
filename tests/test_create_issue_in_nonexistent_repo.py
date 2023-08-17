import unittest
from api.api_helper import GitHubAPIHelper

class TestCreateIssueInNonExistentRepo(unittest.TestCase):
    def test_create_issue_in_nonexistent_repo(self):
        github_helper = GitHubAPIHelper()
        response = github_helper.create_issue("NonExistentRepo", "Test Issue", "This is a test issue.")
        self.assertEqual(response.status_code, 404, "Expected not to find the repository")
