import unittest
from tests import (

    test_get_repo_details,
    test_create_and_update_repo,
    test_delete_repository,
    test_create_issue,
    test_get_issue_details,
    test_update_issue,
    test_close_issue,
    test_create_issue_in_nonexistent_repo,
    test_delete_nonexistent_repository,
    test_update_repository_with_invalid_data,
)

# Lista cu clasele de teste
test_classes = [
    test_get_repo_details.TestGetRepoDetails,
    test_create_and_update_repo.TestUpdateAndCreateRepository,
    test_delete_repository.TestDeleteRepository,
    test_create_issue.TestCreateIssue,
    test_get_issue_details.TestGetIssueDetails,
    test_update_issue.TestUpdateIssue,
    test_close_issue.TestCloseIssue,
    test_create_issue_in_nonexistent_repo.TestCreateIssueInNonExistentRepo,
    test_delete_nonexistent_repository.TestDeleteNonExistentRepository,
    test_update_repository_with_invalid_data.TestUpdateRepositoryWithInvalidData,
]

loader = unittest.TestLoader()
suites_list = []
for test_class in test_classes:
    suite = loader.loadTestsFromTestCase(test_class)
    suites_list.append(suite)

big_suite = unittest.TestSuite(suites_list)
runner = unittest.TextTestRunner(verbosity=2)
runner.run(big_suite)
