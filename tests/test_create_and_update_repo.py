import unittest
from api.api_helper import GitHubAPIHelper


class TestUpdateAndCreateRepository(unittest.TestCase):
    def test_create_and_update_repo(self):
        github_helper = GitHubAPIHelper()
        new_description = "Updated repository description"

        # Creeaza repository-ul "TestRepo" pentru a-l actualiza ulterior
        create_response = github_helper.create_repo("TestRepo", description="Initial description")
        self.assertEqual(create_response.status_code, 201, "Failed to create repository")

        # Actualizeaza repository-ul "TestRepo"
        update_response = github_helper.update_repo("TestRepo", description=new_description)
        self.assertEqual(update_response.status_code, 200, "Failed to update repository")
        self.assertEqual(update_response.json()["description"], new_description, "Repository description was not updated")

if __name__ == '__main__':
    unittest.main()
