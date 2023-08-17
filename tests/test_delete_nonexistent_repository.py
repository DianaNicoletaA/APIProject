import unittest
from api.api_helper import GitHubAPIHelper

class TestDeleteNonExistentRepository(unittest.TestCase):
    def test_delete_nonexistent_repo(self):
        github_helper = GitHubAPIHelper()
        response = github_helper.delete_repo("NonExistentRepo")
        self.assertEqual(response.status_code, 404, "Expected not to find the repository")
