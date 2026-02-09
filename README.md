# GitHub Python SDK
A Python SDK for interacting with the GitHub REST API. This library provides a modular, object-oriented approach to managing GitHub resources including repositories, organizations, teams, actions, and more.

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Authentication](#authentication)
- [Available Modules](#available-modules)
- [Usage Examples](#usage-examples)
  - [Repository Operations](#repository-operations)
  - [Organization Management](#organization-management)
  - [Actions & Secrets](#actions--secrets)
  - [Teams Management](#teams-management)
  - [Pull Requests](#pull-requests)
  - [Issues](#issues)
  - [Branches](#branches)
  - [Releases](#releases)
  - [Copilot Management](#copilot-management)
  - [Dependabot](#dependabot)
- [Response Format](#response-format)
- [Error Handling](#error-handling)
- [Contributing](#contributing)

## Installation

### Prerequisites

- Python 3.8+
- A GitHub Personal Access Token (PAT) with appropriate permissions

### Dependencies

```bash
pip install requests pynacl
```

### Setup

Clone the repository:

```bash
git clone https://github.com/shanpira14-bit/github-python-sdk.git
cd github-python-sdk
```

## Quick Start

```python
from github import GitHubModules

# Initialize with your GitHub token
github = GitHubModules(
    token="your_github_token",
    org="your-organization",      # For organization-level operations
    owner="your-username",        # For owner-level operations
    username="your-username",     # For user-level operations
    log_level="INFO"              # Optional: DEBUG, INFO, WARNING, ERROR
)

# List repositories
repos = github.repository.repositories.list_org_repos()
print(repos)
```

## Authentication

The SDK requires a GitHub Personal Access Token (PAT) for authentication. You can create one in your [GitHub Settings](https://github.com/settings/tokens).

```python
import os
from github import GitHubModules

# Recommended: Use environment variables
github_token = os.environ.get("GH_TOKEN")

github = GitHubModules(
    token=github_token,
    org="my-organization"
)
```

### Required Scopes

Depending on the operations you want to perform, you may need the following token scopes:

| Operation | Required Scopes |
|-----------|-----------------|
| Read repositories | `repo` |
| Manage secrets | `admin:org` |
| Manage teams | `admin:org`, `write:org` |
| Copilot management | `manage_billing:copilot` |
| Dependabot | `security_events` |

## Available Modules

| Module | Description | Access via |
|--------|-------------|------------|
| **Actions** | Manage workflows, artifacts, secrets, variables, runners | `github.actions` |
| **Apps** | GitHub Apps management | `github.apps` |
| **Billing** | Billing information | `github.billing` |
| **Branch** | Branch management and protection rules | `github.branch` |
| **Collaborator** | Repository collaborator management | `github.collaborator` |
| **Copilot** | Copilot seat management and metrics | `github.copilot` |
| **Dependabot** | Dependabot alerts and secrets | `github.dependabot` |
| **Deployment** | Deployment management | `github.deployment` |
| **Git Database** | Low-level Git operations | `github.git_database` |
| **GitIgnore** | GitIgnore templates | `github.gitignore` |
| **Issue** | Issue management | `github.issue` |
| **Organization** | Organization settings and members | `github.organization` |
| **Packages** | Package management | `github.packages` |
| **Private Registries** | Private registry configuration | `github.private_registries` |
| **Pull Request** | Pull request management | `github.pull_request` |
| **Rate Limit** | API rate limit information | `github.rate_limit` |
| **Release** | Release management | `github.release` |
| **Repository** | Repository CRUD operations | `github.repository` |
| **Team** | Team management | `github.team` |

## Usage Examples

### Repository Operations

#### List Organization Repositories

```python
from github import GitHubModules

github = GitHubModules(token="your_token", org="my-org")

# List all repositories
repos = github.repository.repositories.list_org_repos(per_page=50, page=1)

# Get a specific repository
repo = github.repository.repositories.get_repository(repo="my-repo")
print(f"Repository: {repo['data']['name']}")
```

#### Manage Repository Contents

```python
import base64

# Get file contents
content = github.repository.contents.get_repository_content(
    repo="my-repo",
    path="README.md"
)

# Create or update a file
encoded_content = base64.b64encode("# My New File".encode()).decode()
result = github.repository.contents.create_or_update_file_contents(
    repo="my-repo",
    path="docs/example.md",
    message="Add example documentation",
    content=encoded_content,
    branch="main"
)
```

#### Repository Autolinks

```python
# List autolinks
autolinks = github.repository.autolinks.list_autolinks(repo="my-repo")

# Create an autolink
github.repository.autolinks.create_autolink(
    repo="my-repo",
    key_prefix="TICKET-",
    url_template="https://jira.company.com/browse/TICKET-<num>"
)
```

### Organization Management

#### API Insights

```python
github = GitHubModules(token="your_token", org="my-org")

# Get organization API summary stats
stats = github.organization.api_insights.get_summary_stats(
    min_timestamp="2024-01-01T00:00:00Z",
    max_timestamp="2024-01-31T23:59:59Z"
)

# Get time-based statistics
time_stats = github.organization.api_insights.get_time_stats(
    min_timestamp="2024-01-01T00:00:00Z",
    timestamp_increment="1h"
)
```

### Actions & Secrets

#### Manage Organization Secrets

```python
github = GitHubModules(token="your_token", org="my-org")

# List organization secrets
secrets = github.actions.secrets.list_org_secrets(per_page=100)

# Get the public key for encryption
public_key = github.actions.secrets.get_org_public_key()

# Encrypt and create a secret
encrypted_value = github.encrypt_secret(
    public_key=public_key["data"]["key"],
    secret_value="my-secret-value"
)

github.actions.secrets.create_or_update_org_secret(
    secret_name="MY_SECRET",
    encrypted_secret_value=encrypted_value,
    visibility="selected",
    selected_repository_ids=[123456, 789012]
)

# Add repository access to a secret
github.actions.secrets.add_repo_access_to_org_secret(
    secret_name="MY_SECRET",
    repo_id=123456
)
```

#### Manage Artifacts

```python
# List artifacts for a repository
artifacts = github.actions.artifacts.list_artifacts(repo="my-repo")

# Get a specific artifact
artifact = github.actions.artifacts.get_an_artifact(
    repo="my-repo",
    artifact_id=12345
)

# Delete an artifact
github.actions.artifacts.delete_an_artifact(
    repo="my-repo",
    artifact_id=12345
)
```

### Teams Management

#### Team Operations

```python
github = GitHubModules(token="your_token", org="my-org")

# List all teams
teams = github.team.teams.list_teams()

# Create a new team
new_team = github.team.teams.create_team(
    name="backend-developers",
    description="Backend development team",
    privacy="closed",
    permission="push"
)

# Get team by slug
team = github.team.teams.get_team_by_name(team_slug="backend-developers")

# Update team
github.team.teams.update_team(
    team_slug="backend-developers",
    description="Updated description"
)

# Delete team
github.team.teams.delete_team(team_slug="old-team")
```

#### Team Membership

```python
# List team members
members = github.team.members.list_team_members(
    team_slug="backend-developers",
    role="all"
)

# Add a member to a team
github.team.members.add_or_update_team_membership(
    team_slug="backend-developers",
    username="new-developer",
    role="member"  # or "maintainer"
)

# Remove a member from a team
github.team.members.remove_team_membership(
    team_slug="backend-developers",
    username="former-developer"
)
```

### Pull Requests

```python
github = GitHubModules(token="your_token", org="my-org")

# List pull requests
prs = github.pull_request.pull_requests.list_pull_requests(
    repo="my-repo",
    state="open"
)

# Create a pull request
new_pr = github.pull_request.pull_requests.create_pull_request(
    repo="my-repo",
    head="feature-branch",
    base="main",
    title="Add new feature",
    body="This PR adds a new feature...",
    draft=False
)

# Get pull request details
pr = github.pull_request.pull_requests.get_pull_request(
    repo="my-repo",
    pull_number=42
)

# List files changed in a PR
files = github.pull_request.pull_requests.list_pull_requests_files(
    repo="my-repo",
    pull_number=42
)

# Check if PR is merged
is_merged = github.pull_request.pull_requests.check_if_pull_request_merged(
    repo="my-repo",
    pull_number=42
)
```

### Issues

#### Managing Issues

```python
github = GitHubModules(token="your_token", org="my-org")

# List assignees for a repository
assignees = github.issue.assignees.list_assignees(repo="my-repo")

# Check if user can be assigned
can_assign = github.issue.assignees.check_if_user_can_be_assigned(
    repo="my-repo",
    username="developer"
)

# Add assignees to an issue
github.issue.assignees.add_assignee(
    repo="my-repo",
    issue_number=123,
    assignees=["developer1", "developer2"]
)
```

#### Issue Comments

```python
# List comments for a repository
comments = github.issue.comments.list_comments_for_repository(
    repo="my-repo",
    sort="created",
    direction="desc"
)

# Get a specific comment
comment = github.issue.comments.get_comment(
    repo="my-repo",
    comment_id=456789
)
```

### Branches

#### Branch Operations

```python
github = GitHubModules(token="your_token", org="my-org")

# List branches
branches = github.branch.branches.list_branches(
    repo="my-repo",
    protected=True  # Filter protected branches only
)

# Get a specific branch
branch = github.branch.branches.get_branch(
    repo="my-repo",
    branch="main"
)

# Rename a branch
github.branch.branches.rename_branch(
    repo="my-repo",
    old_branch="master",
    new_branch="main"
)

# Merge branches
github.branch.branches.merge_branch(
    repo="my-repo",
    base="main",
    head="feature-branch",
    commit_message="Merge feature-branch into main"
)

# Sync fork with upstream
github.branch.branches.sync_fork_branch_upstream(
    repo="my-forked-repo",
    branch="main"
)
```

### Releases

```python
github = GitHubModules(token="your_token", owner="my-username")

# List releases
releases = github.release.releases.list_releases(repo="my-repo")

# Create a release
new_release = github.release.releases.create_release(
    repo="my-repo",
    tag_name="v1.0.0",
    name="Version 1.0.0",
    body="## What's New\n- Feature A\n- Bug fix B",
    draft=False,
    prerelease=False,
    generate_release_notes=True
)

# Get the latest release
latest = github.release.releases.get_latest_release(repo="my-repo")

# Get release by tag
release = github.release.releases.get_release_by_tag(
    repo="my-repo",
    tag="v1.0.0"
)
```

### Copilot Management

#### Seat Management

```python
github = GitHubModules(token="your_token", org="my-org")

# Get Copilot billing info
billing = github.copilot.user_management.get_org_seat_info_settings()

# List seat assignments
seats = github.copilot.user_management.list_org_seat_assignments(per_page=100)

# Assign Copilot seats to users
github.copilot.user_management.add_users_seat_assignments(
    selected_usernames=["developer1", "developer2"]
)

# Remove Copilot seats from users
github.copilot.user_management.remove_users_seat_assignments(
    selected_usernames=["former-employee"]
)

# Assign seats to teams
github.copilot.user_management.add_teams_seat_assignments(
    selected_teams=["engineering-team", "devops-team"]
)
```

#### Copilot Metrics

```python
# Get organization-wide metrics
metrics = github.copilot.metrics.get_org_metrics(
    since="2024-01-01T00:00:00Z",
    until="2024-01-31T23:59:59Z"
)

# Get team-specific metrics
team_metrics = github.copilot.metrics.get_team_metrics(
    team_slug="engineering-team",
    since="2024-01-01T00:00:00Z"
)
```

### Dependabot

#### Alerts Management

```python
github = GitHubModules(token="your_token", org="my-org", owner="my-username")

# List organization Dependabot alerts
org_alerts = github.dependabot.alerts.list_org_dependabot_alerts(
    state="open",
    severity="high"
)

# List repository Dependabot alerts
repo_alerts = github.dependabot.alerts.list_repository_dependabot_alerts(
    repo="my-repo",
    state="open",
    ecosystem="npm"
)

# Get a specific alert
alert = github.dependabot.alerts.get_dependabot_alert(
    repo="my-repo",
    alert_number=42
)

# Dismiss an alert
github.dependabot.alerts.update_dependabot_alert(
    repo="my-repo",
    alert_number=42,
    state="dismissed",
    dismissal_reason="not_used",
    dismissal_message="This dependency is not used in production"
)
```

## Response Format

All API responses follow a consistent format:

```python
{
    "status_code": 200,  # HTTP status code
    "data": { ... }      # Response payload (dict, list, or primitive type)
}
```

### Example Response Handling

```python
response = github.repository.repositories.get_repository(repo="my-repo")

if response["status_code"] == 200:
    repo_data = response["data"]
    print(f"Repository: {repo_data['name']}")
    print(f"Stars: {repo_data['stargazers_count']}")
else:
    print(f"Error: {response['data']}")
```

## Error Handling

```python
from github import GitHubModules

github = GitHubModules(token="your_token", org="my-org", log_level="DEBUG")

try:
    response = github.repository.repositories.get_repository(repo="non-existent-repo")
    
    if response["status_code"] == 404:
        print("Repository not found")
    elif response["status_code"] == 403:
        print("Access forbidden - check your token permissions")
    elif response["status_code"] == 401:
        print("Authentication failed - invalid token")
    elif response["status_code"] >= 400:
        print(f"Error: {response['data']}")
    else:
        print(f"Success: {response['data']}")
        
except Exception as e:
    print(f"Request failed: {e}")
```

## Real-World Example: Add Repository Access to Secrets

Here's a complete example script that adds repository access to organization secrets:

```python
import os
from typing import List
from github import GitHubModules

def get_secret_names(github: GitHubModules) -> List[str]:
    """Retrieve all organization secret names."""
    secrets_list: List[str] = []
    page = 1
    while True:
        response = github.actions.secrets.list_org_secrets(per_page=100, page=page)
        secrets = response.get("data", {}).get("secrets", [])
        for secret in secrets:
            secrets_list.append(secret["name"])
        if len(secrets) < 100:
            break
        page += 1
    return secrets_list

def add_repo_access_to_secrets(
    secrets_list: List[str],
    repo_id: int,
    github: GitHubModules,
    prefix_filter: str = ""
) -> None:
    """Add repository access to organization secrets."""
    for secret_name in secrets_list:
        if prefix_filter and prefix_filter not in secret_name:
            continue
        response = github.actions.secrets.add_repo_access_to_org_secret(
            secret_name=secret_name,
            repo_id=repo_id
        )
        if response.get("status_code") == 204:
            print(f"✓ Added access to '{secret_name}'")
        else:
            print(f"✗ Failed for '{secret_name}': {response}")

def main():
    github_token = os.environ.get("GH_TOKEN")
    github = GitHubModules(
        github_token,
        org="my-organization",
        log_level="INFO"
    )
    
    # Get repository ID
    repo_response = github.repository.repositories.get_repository(repo="my-repo")
    repo_id = repo_response["data"]["id"]
    
    # Get all secrets and add access
    secrets = get_secret_names(github)
    add_repo_access_to_secrets(secrets, repo_id, github)

if __name__ == "__main__":
    main()
```

## License

This project is open source and available under the [MIT License](LICENSE).
