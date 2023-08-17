from api.api_helper import GitHubAPIHelper

def test_delete_nonexistent_repository():
    github_helper = GitHubAPIHelper()
    response = github_helper.delete_repo("NonExistentRepo")
    assert response.status_code == 404, "Expected not to find the repository"
