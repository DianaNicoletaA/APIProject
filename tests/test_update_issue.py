import unittest
from api.api_helper import GitHubAPIHelper


class TestUpdateIssue(unittest.TestCase):
    def test_update_nonexistent_issue(self):
        github_helper = GitHubAPIHelper()
        new_title = "Updated Test Issue"
        # Utilizeaza un numar de issue inexistent (de exemplu, 9999)
        response = github_helper.update_issue("TestRepo", 9999, title=new_title)

        # Verifica ca primim un status code 404, indicand ca resursa nu a fost gasita
        self.assertEqual(response.status_code, 404, "Expected issue not found")


if __name__ == '__main__':
    unittest.main()
