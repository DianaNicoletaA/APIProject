import unittest
from api.api_helper import GitHubAPIHelper

class TestUpdateRepositoryWithInvalidData(unittest.TestCase):
    def test_update_repo_with_invalid_data(self):
        github_helper = GitHubAPIHelper()
        long_name = "a" * 101  # GitHub repo name limit is 100 characters
        response = github_helper.update_repo("NonexistentRepo", name=long_name)
        self.assertEqual(response.status_code, 404, "Expected repository not found")

if __name__ == '__main__':
    unittest.main()
