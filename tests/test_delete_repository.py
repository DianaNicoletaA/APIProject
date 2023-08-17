import unittest
from api.api_helper import GitHubAPIHelper

class TestDeleteRepository(unittest.TestCase):
    def test_delete_repo(self):
        github_helper = GitHubAPIHelper()
        response = github_helper.delete_repo("TestRepo")
        self.assertEqual(response.status_code, 204, "Failed to delete repository")
