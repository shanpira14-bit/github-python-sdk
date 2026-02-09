"""
Branches submodule.
"""
from typing import Any, Dict

class Branches:

    """
    A class to manage multiple branches.
    """

    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def list_branches(self, repo: str, **kwargs: Any) -> Dict[str, Any]:
        """
        List all branches in the repository.

        :param repo: The name of the repository.
        :param protected: (optional) Boolean to filter by protected branches.
        :param per_page: (optional) Number of results per page.
        :param page: (optional) Page number of the results to fetch.

        :return: A dictionary containing the list of branches.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/branches"
        params: Dict[str, Any] = {
            "protected": kwargs.get("protected", None),
            "per_page": kwargs.get("per_page", None),
            "page": kwargs.get("page", None),
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def get_branch(self, repo: str, branch: str) -> Dict[str, Any]:
        """
        Get a specific branch in the repository.

        :param repo: The name of the repository.
        :param branch: The name of the branch.

        :return: A dictionary containing the branch details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/branches/{branch}"
        return self.parent.make_request("GET", endpoint)

    def rename_branch(self, repo: str, old_branch: str, new_branch: str) -> Dict[str, Any]:
        """
        Rename a branch in the repository.

        :param repo: The name of the repository.
        :param old_branch: The current name of the branch.
        :param new_branch: The new name for the branch.

        :return: A dictionary containing the updated branch details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/branches/{old_branch}/rename"
        data: Dict[str, Any] = {
            "new_name": new_branch
        }
        return self.parent.make_request("POST", endpoint, json=data)

    def sync_fork_branch_upstream(self, repo: str, branch: str) -> Dict[str, Any]:
        """
        Sync a fork branch with its upstream branch.

        :param repo: The name of the repository.

        :return: A dictionary confirming the sync action.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/merge-upstream"
        data: Dict[str, Any] = {
            "branch": branch
        }
        return self.parent.make_request("POST", endpoint, json=data)

    def merge_branch(self, repo: str, base: str, head: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Merge one branch into another.

        :param repo: The name of the repository.
        :param base: The name of the base branch.
        :param head: The name of the head branch to merge from.
        :param commit_message: The commit message for the merge.

        :return: A dictionary containing the merge result.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/merges"
        data: Dict[str, Any] = {
            "base": base,
            "head": head,
            "commit_message": kwargs.get("commit_message", None)
        }
        return self.parent.make_request("POST", endpoint, json=data)


class ProtectedBranches:
    """
    A class to manage protected branches.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def get_protection(self, repo: str, branch: str) -> Dict[str, Any]:
        """
        Get protection details of a protected branch.

        :param repo: The name of the repository.
        :param branch: The name of the branch.

        :return: A dictionary containing the protection details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/branches/{branch}/protection"
        return self.parent.make_request("GET", endpoint)

    def update_protection(self, repo: str, branch: str, **kwargs: Any) -> Dict[str, Any]: #! Test this
        """
        Update protection settings of a protected branch.

        :param repo: The name of the repository.
        :param branch: The name of the branch.
        :param required_status_checks: (optional) Status checks required before merging.
        :param enforce_admins: (optional) Whether to enforce protection for admins.
        :param required_pull_request_reviews: (optional) Pull request review settings.
        :param restrictions: (optional) Restrictions on who can push to the branch.

        :return: A dictionary containing the updated protection details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/branches/{branch}/protection"
        data: Dict[str, Any] = {
            "required_status_checks": {
                "strict": kwargs.get("required_status_checks", {}).get("strict", None),
                "contexts": kwargs.get("required_status_checks", {}).get("contexts", None),
                "checks": {
                    "app_id": kwargs.get("required_status_checks", {}).get("checks", {}).get("app_id", None),
                    "context": kwargs.get("required_status_checks", {}).get("checks", {}).get("context", None),
                }
            },
            "enforce_admins": kwargs.get("enforce_admins", None),
            "required_pull_request_reviews": kwargs.get("required_pull_request_reviews", None),
            "restrictions": kwargs.get("restrictions", None),
        }
        return self.parent.make_request("PUT", endpoint, json=data)

    def delete_protection(self, repo: str, branch: str) -> Dict[str, Any]:
        """
        Delete protection from a protected branch.

        :param repo: The name of the repository.
        :param branch: The name of the branch.

        :return: A dictionary confirming the deletion of protection.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/branches/{branch}/protection"
        return self.parent.make_request("DELETE", endpoint)

    def get_admins_enforcement(self, repo: str, branch: str) -> Dict[str, Any]:
        """
        Get admin enforcement status of a protected branch.

        :param repo: The name of the repository.
        :param branch: The name of the branch.

        :return: A dictionary containing the admin enforcement status.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/branches/{branch}/protection/enforce_admins"
        return self.parent.make_request("GET", endpoint)

    def set_admins_enforcement(self, repo: str, branch: str) -> Dict[str, Any]:
        """
        Set admin enforcement status of a protected branch.

        :param repo: The name of the repository.
        :param branch: The name of the branch.

        :return: A dictionary containing the updated admin enforcement status.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/branches/{branch}/protection/enforce_admins"
        return self.parent.make_request("POST", endpoint)

    def delete_admins_enforcement(self, repo: str, branch: str) -> Dict[str, Any]:
        """
        Delete admin enforcement status of a protected branch.

        :param repo: The name of the repository.
        :param branch: The name of the branch.

        :return: A dictionary confirming the deletion of admin enforcement.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/branches/{branch}/protection/enforce_admins"
        return self.parent.make_request("DELETE", endpoint)

    def get_pr_protection(self, repo: str, branch: str) -> Dict[str, Any]:
        """
        Get pull request review protection details of a protected branch.

        :param repo: The name of the repository.
        :param branch: The name of the branch.

        :return: A dictionary containing the pull request review protection details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/branches/{branch}/protection/required_pull_request_reviews"
        return self.parent.make_request("GET", endpoint)

    def update_pr_protection(self, repo: str, branch: str, **kwargs: Any) -> Dict[str, Any]: #! Test this
        """
        Update pull request review protection settings of a protected branch.

        :param repo: The name of the repository.
        :param branch: The name of the branch.
        :param dismiss_stale_reviews: (optional) Whether to dismiss stale reviews.
        :param require_code_owner_reviews: (optional) Whether to require code owner reviews.
        :param required_approving_review_count: (optional) Number of required approving reviews.

        :return: A dictionary containing the updated pull request review protection details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/branches/{branch}/protection/required_pull_request_reviews"
        data: Dict[str, Any] = {
            "dismissal_restrictions": {
                "users": kwargs.get("dismissal_restrictions", {}).get("users", None),
                "teams": kwargs.get("dismissal_restrictions", {}).get("teams", None),
                "apps": kwargs.get("dismissal_restrictions", {}).get("apps", None),
                },
            "dismiss_stale_reviews": kwargs.get("dismiss_stale_reviews", None),
            "require_code_owner_reviews": kwargs.get("require_code_owner_reviews", None),
            "required_approving_review_count": kwargs.get("required_approving_review_count", None),
            "require_last_push_approval": kwargs.get("require_last_push_approval", None),
            "bypass_pull_request_allowances": {
                "users": kwargs.get("bypass_pull_request_allowances", {}).get("users", None),
                "teams": kwargs.get("bypass_pull_request_allowances", {}).get("teams", None),
                "apps": kwargs.get("bypass_pull_request_allowances", {}).get("apps", None),
            }
        }
        return self.parent.make_request("PATCH", endpoint, json=data)

    def delete_pr_protection(self, repo: str, branch: str) -> Dict[str, Any]:
        """
        Delete pull request review protection from a protected branch.

        :param repo: The name of the repository.
        :param branch: The name of the branch.

        :return: A dictionary confirming the deletion of pull request review protection.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/branches/{branch}/protection/required_pull_request_reviews"
        return self.parent.make_request("DELETE", endpoint)

    def get_commit_signature_protection(self, repo: str, branch: str) -> Dict[str, Any]:
        """
        Get commit signature protection details of a protected branch.

        :param repo: The name of the repository.
        :param branch: The name of the branch.

        :return: A dictionary containing the commit signature protection details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/branches/{branch}/protection/required_signatures"
        return self.parent.make_request("GET", endpoint)

    def create_commit_signature_protection(self, repo: str, branch: str) -> Dict[str, Any]:
        """
        Create commit signature protection for a protected branch.

        :param repo: The name of the repository.
        :param branch: The name of the branch.

        :return: A dictionary containing the created commit signature protection details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/branches/{branch}/protection/required_signatures"
        return self.parent.make_request("POST", endpoint)

    def delete_commit_signature_protection(self, repo: str, branch: str) -> Dict[str, Any]:
        """
        Delete commit signature protection from a protected branch.

        :param repo: The name of the repository.
        :param branch: The name of the branch.

        :return: A dictionary confirming the deletion of commit signature protection.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/branches/{branch}/protection/required_signatures"
        return self.parent.make_request("DELETE", endpoint)

    def get_status_checks_protection(self, repo: str, branch: str) -> Dict[str, Any]:
        """
        Get status checks protection details of a protected branch.

        :param repo: The name of the repository.
        :param branch: The name of the branch.

        :return: A dictionary containing the status checks protection details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/branches/{branch}/protection/required_status_checks"
        return self.parent.make_request("GET", endpoint)

    def update_status_checks_protection(self, repo: str, branch: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Update status checks protection settings of a protected branch.

        :param repo: The name of the repository.
        :param branch: The name of the branch.
        :param strict: (optional) Whether to require branches to be up to date before merging.
        :param contexts: (optional) List of status check contexts required to pass before merging.
        :param app_id: (optional) The ID of the GitHub App.
        :param context: (optional) The context of the status check.

        :return: A dictionary containing the updated status checks protection details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/branches/{branch}/protection/required_status_checks"
        data: Dict[str, Any] = {
            "strict": kwargs.get("strict", None),
            "contexts": kwargs.get("contexts", None),
            "checks": {
                "app_id": kwargs.get("checks", {}).get("app_id", None),
                "context": kwargs.get("checks", {}).get("context", None),
            }
        }
        return self.parent.make_request("PATCH", endpoint, json=data)

    def remove_status_checks_protection(self, repo: str, branch: str) -> Dict[str, Any]:
        """
        Remove status checks protection from a protected branch.

        :param repo: The name of the repository.
        :param branch: The name of the branch.

        :return: A dictionary confirming the removal of status checks protection.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/branches/{branch}/protection/required_status_checks"
        return self.parent.make_request("DELETE", endpoint)

    def get_status_check_contexts(self, repo: str, branch: str) -> Dict[str, Any]:
        """
        Get status check contexts of a protected branch.

        :param repo: The name of the repository.
        :param branch: The name of the branch.

        :return: A dictionary containing the status check contexts.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/branches/{branch}/protection/required_status_checks/contexts"
        return self.parent.make_request("GET", endpoint)

    def add_status_check_contexts(self, repo: str, branch: str, contexts: Any) -> Dict[str, Any]:
        """
        Add status check contexts to a protected branch.

        :param repo: The name of the repository.
        :param branch: The name of the branch.
        :param contexts: List of status check contexts to add.

        :return: A dictionary containing the updated status check contexts.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/branches/{branch}/protection/required_status_checks/contexts"
        data: Dict[str, Any] = {
            "contexts": contexts
        }
        return self.parent.make_request("POST", endpoint, json=data)

    def set_status_check_contexts(self, repo: str, branch: str, contexts: Any) -> Dict[str, Any]:
        """
        Set status check contexts for a protected branch.

        :param repo: The name of the repository.
        :param branch: The name of the branch.
        :param contexts: List of status check contexts to set.

        :return: A dictionary containing the updated status check contexts.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/branches/{branch}/protection/required_status_checks/contexts"
        data: Dict[str, Any] = {
            "contexts": contexts
        }
        return self.parent.make_request("PUT", endpoint, json=data)

    def remove_status_check_contexts(self, repo: str, branch: str, contexts: Any) -> Dict[str, Any]:
        """
        Remove status check contexts from a protected branch.

        :param repo: The name of the repository.
        :param branch: The name of the branch.
        :param contexts: List of status check contexts to remove.

        :return: A dictionary containing the updated status check contexts.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/branches/{branch}/protection/required_status_checks/contexts"
        data: Dict[str, Any] = {
            "contexts": contexts
        }
        return self.parent.make_request("DELETE", endpoint, json=data)

    def get_access_restrictions(self, repo: str, branch: str) -> Dict[str, Any]:
        """
        Get access restrictions of a protected branch.

        :param repo: The name of the repository.
        :param branch: The name of the branch.

        :return: A dictionary containing the access restrictions.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/branches/{branch}/protection/restrictions"
        return self.parent.make_request("GET", endpoint)

    def delete_access_restrictions(self, repo: str, branch: str) -> Dict[str, Any]:
        """
        Delete access restrictions from a protected branch.

        :param repo: The name of the repository.
        :param branch: The name of the branch.

        :return: A dictionary confirming the deletion of access restrictions.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/branches/{branch}/protection/restrictions"
        return self.parent.make_request("DELETE", endpoint)

    def get_apps_access_to_branch(self, repo: str, branch: str) -> Dict[str, Any]:
        """
        Get apps with access to a protected branch.

        :param repo: The name of the repository.
        :param branch: The name of the branch.

        :return: A dictionary containing the apps with access.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/branches/{branch}/protection/restrictions/apps"
        return self.parent.make_request("GET", endpoint)

    def add_app_access_restrictions(self, repo: str, branch: str, apps: Any) -> Dict[str, Any]:
        """
        Add app access restrictions to a protected branch.

        :param repo: The name of the repository.
        :param branch: The name of the branch.
        :param apps: List of app slugs to add.
            eg: ["my-github-app", "another-app"]

        :return: A dictionary containing the updated app access restrictions.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/branches/{branch}/protection/restrictions/apps"
        data: Dict[str, Any] = {
            "apps": apps
        }
        return self.parent.make_request("POST", endpoint, json=data)

    def set_app_access_restrictions(self, repo: str, branch: str, apps: Any) -> Dict[str, Any]:
        """
        Set app access restrictions for a protected branch.

        :param repo: The name of the repository.
        :param branch: The name of the branch.
        :param apps: List of app slugs to set.
            eg: ["my-github-app", "another-app"]

        :return: A dictionary containing the updated app access restrictions.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/branches/{branch}/protection/restrictions/apps"
        data: Dict[str, Any] = {
            "apps": apps
        }
        return self.parent.make_request("PUT", endpoint, json=data)

    def remove_app_access_restrictions(self, repo: str, branch: str, apps: Any) -> Dict[str, Any]:
        """
        Remove app access restrictions from a protected branch.

        :param repo: The name of the repository.
        :param branch: The name of the branch.
        :param apps: List of app slugs to remove.
            eg: ["my-github-app", "another-app"]

        :return: A dictionary containing the updated app access restrictions.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/branches/{branch}/protection/restrictions/apps"
        data: Dict[str, Any] = {
            "apps": apps
        }
        return self.parent.make_request("DELETE", endpoint, json=data)

    def get_teams_access_to_branch(self, repo: str, branch: str) -> Dict[str, Any]:
        """
        Get teams with access to a protected branch.

        :param repo: The name of the repository.
        :param branch: The name of the branch.

        :return: A dictionary containing the teams with access.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/branches/{branch}/protection/restrictions/teams"
        return self.parent.make_request("GET", endpoint)

    def add_team_access_restrictions(self, repo: str, branch: str, teams: Any) -> Dict[str, Any]:
        """
        Add team access restrictions to a protected branch.

        :param repo: The name of the repository.
        :param branch: The name of the branch.
        :param teams: List of team slugs to add.
            eg: ["my-team", "another-team"]

        :return: A dictionary containing the updated team access restrictions.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/branches/{branch}/protection/restrictions/teams"
        data: Dict[str, Any] = {
            "teams": teams
        }
        return self.parent.make_request("POST", endpoint, json=data)

    def set_team_access_restrictions(self, repo: str, branch: str, teams: Any) -> Dict[str, Any]:
        """
        Set team access restrictions for a protected branch.

        :param repo: The name of the repository.
        :param branch: The name of the branch.
        :param teams: List of team slugs to set.
            eg: ["my-team", "another-team"]

        :return: A dictionary containing the updated team access restrictions.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/branches/{branch}/protection/restrictions/teams"
        data: Dict[str, Any] = {
            "teams": teams
        }
        return self.parent.make_request("PUT", endpoint, json=data)

    def remove_team_access_restrictions(self, repo: str, branch: str, teams: Any) -> Dict[str, Any]:
        """
        Remove team access restrictions from a protected branch.

        :param repo: The name of the repository.
        :param branch: The name of the branch.
        :param teams: List of team slugs to remove.
            eg: ["my-team", "another-team"]

        :return: A dictionary containing the updated team access restrictions.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/branches/{branch}/protection/restrictions/teams"
        data: Dict[str, Any] = {
            "teams": teams
        }
        return self.parent.make_request("DELETE", endpoint, json=data)

    def get_users_access_to_branch(self, repo: str, branch: str) -> Dict[str, Any]:
        """
        Get users with access to a protected branch.

        :param repo: The name of the repository.
        :param branch: The name of the branch.

        :return: A dictionary containing the users with access.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/branches/{branch}/protection/restrictions/users"
        return self.parent.make_request("GET", endpoint)

    def add_user_access_restrictions(self, repo: str, branch: str, users: Any) -> Dict[str, Any]:
        """
        Add user access restrictions to a protected branch.

        :param repo: The name of the repository.
        :param branch: The name of the branch.
        :param users: List of usernames to add.
            eg: ["octocat", "another-user"]

        :return: A dictionary containing the updated user access restrictions.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/branches/{branch}/protection/restrictions/users"
        data: Dict[str, Any] = {
            "users": users
        }
        return self.parent.make_request("POST", endpoint, json=data)

    def set_user_access_restrictions(self, repo: str, branch: str, users: Any) -> Dict[str, Any]:
        """
        Set user access restrictions for a protected branch.

        :param repo: The name of the repository.
        :param branch: The name of the branch.
        :param users: List of usernames to set.
            eg: ["octocat", "another-user"]

        :return: A dictionary containing the updated user access restrictions.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/branches/{branch}/protection/restrictions/users"
        data: Dict[str, Any] = {
            "users": users
        }
        return self.parent.make_request("PUT", endpoint, json=data)

    def remove_user_access_restrictions(self, repo: str, branch: str, users: Any) -> Dict[str, Any]:
        """
        Remove user access restrictions from a protected branch.

        :param repo: The name of the repository.
        :param branch: The name of the branch.
        :param users: List of usernames to remove.
            eg: ["octocat", "another-user"]

        :return: A dictionary containing the updated user access restrictions.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/branches/{branch}/protection/restrictions/users"
        data: Dict[str, Any] = {
            "users": users
        }
        return self.parent.make_request("DELETE", endpoint, json=data)


class Branch:
    """
    A class to manage branches in a version control system.
    """

    def __init__(self, parent: Any) -> None:
        self.parent = parent

        # Initialize submodules
        self.branches = Branches(parent)
        self.protected = ProtectedBranches(parent)

