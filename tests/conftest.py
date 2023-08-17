import pytest
from api.api_helper import GitHubAPIHelper


@pytest.fixture
def create_and_delete_test_repo():
    github_helper = GitHubAPIHelper()
    repo_name = "TestNewRepo"

    # Create the repository
    response = github_helper.create_repository(repo_name)
    assert response.status_code == 201, "Failed to create repository"

    yield repo_name

    # Delete the repository
    delete_response = github_helper.delete_repository(repo_name)
    assert delete_response.status_code == 204, "Failed to delete repository"
