# API Project

This is an automated testing framework for the GitHub API. The framework is written in Python and uses pytest for automated testing and HTML report generation.

## Installation

1. **Clone this repository to your local machine:**
   git clone https://github.com/DianaNicoletaA/APIProject.git

2. **Navigate to the project directory:**
   cd APIProject

3. **Install project dependencies using pip:**
   pip install -r requirements.txt

## Configuring GitHub API Access

To access and test the GitHub API, you will need a personal access token and your GitHub account username. These details need to be entered into `api_helper.py`.

## Project Structure

- `pytest.py`: Script for running all tests and generating reports.
- `tests/`: Directory containing all individual test files.
- `api/`: Directory containing helpers and functionalities for interacting with the API.
- `reports/`: Directory where HTML reports are generated.

Additionally, the project includes the following additional features:

- `list_repos.py`: A script that lists the repositories generated after running the tests. This script allows you to display the complete list of repositories created during the tests.

- `delete_repos.py`: A script that deletes the repositories generated during the tests. This script is useful for cleaning up the environment after running the tests and removing unused resources.

Make sure to be careful when using these functionalities, especially when it comes to deleting repositories, to avoid loss of important data.

## Running Tests

- **To run all tests and generate HTML reports in the "reports" directory:**
pytest --html=reports/report.html


- **To run a specific test:**

For example, to run the `test_create_issue.py` test:
pytest tests/test_create_issue.py


## Project Structure

- `pytest.py`: Script for running all tests and generating reports.
- `tests/`: Directory containing all individual test files.
- `api/`: Directory containing helpers and functionalities for interacting with the API.
- `reports/`: Directory where HTML reports are generated.

## Uninstallation

Uninstall Python dependencies:
pip uninstall -r requirements.txt
This will uninstall all packages listed in `requirements.txt`.

