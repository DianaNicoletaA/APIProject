import unittest
import random
import string
from api.api_helper import GitHubAPIHelper


class TestCreateIssue(unittest.TestCase):
    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    def test_create_issue(self):
        github_helper = GitHubAPIHelper()
        unique_repo_name = f"TestRepo_{self.generate_random_string(6)}"
        response = github_helper.create_repo(unique_repo_name)

        self.assertEqual(response.status_code, 201, "Failed to create repository")
        self.assertEqual(response.json()["name"], unique_repo_name, "Repository name mismatch")


if __name__ == '__main__':
    unittest.main()
