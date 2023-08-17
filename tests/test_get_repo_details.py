import unittest
import random
import string
from api.api_helper import GitHubAPIHelper

class TestGetRepoDetails(unittest.TestCase):
    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    def test_get_repo_details(self):
        github_helper = GitHubAPIHelper()

        # Crearea unui repository temporar
        unique_repo_name = f"TestRepo_{self.generate_random_string(6)}"
        response_create_repo = github_helper.create_repo(unique_repo_name)
        self.assertEqual(response_create_repo.status_code, 201, "Failed to create repository")

        # Citirea detaliilor repository-ului temporar
        response_get_repo_details = github_helper.get_repo_details(unique_repo_name)
        self.assertEqual(response_get_repo_details.status_code, 200, "Failed to fetch repository details")

if __name__ == '__main__':
    unittest.main()
