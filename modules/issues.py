"""
Issue module for managing issues in a repository.
"""
from typing import Any, Dict

class Assignees:
    """
    Submodule for managing issue assignees.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def list_assignees(self, repo: str, **kwargs: Any) -> Dict[str, Any]:
        """
        List assignees for a given repository.

        :param repo: Repository name
        :param per_page: Number of results per page (optional)
        :param page: Page number of the results to fetch (optional)

        :return: Dictionary containing the list of assignees
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/assignees"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page"),
            "page": kwargs.get("page"),
        }
        response = self.parent.make_request("GET", endpoint, params=params)
        return response

    def check_if_user_can_be_assigned(self, repo: str, username: str) -> Dict[str, Any]:
        """
        Check if a user can be assigned to issues in a given repository.

        :param repo: Repository name
        :param username: GitHub username to check

        :return: True if the user can be assigned, False otherwise
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/assignees/{username}"
        response = self.parent.make_request("GET", endpoint)

        if response.status_code == 204:
            response_payload: Dict[str, Any] = {
                "can_be_assigned": True }
        else:
            response_payload: Dict[str, Any] = {
                "can_be_assigned": False }

        return response_payload

    def add_assignee(self, repo: str, issue_number: int,
                     **kwargs: Any) -> Dict[str, Any]:
        """
        Add assignees to a given issue.

        :param repo: Repository name
        :param issue_number: Issue number
        :param assignees: List of usernames to assign to the issue
        :return: Dictionary containing the updated issue information
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/issues/{issue_number}/assignees"
        data: Dict[str, Any] = {
            "assignees": kwargs.get("assignees", []),
        }
        response = self.parent.make_request("POST", endpoint, json=data)
        return response

    def remove_assignee(self, repo: str, issue_number: int,
                        **kwargs: Any) -> Dict[str, Any]:
        """
        Remove assignees from a given issue.

        :param repo: Repository name
        :param issue_number: Issue number
        :param assignees: List of usernames to remove from the issue
        :return: Dictionary containing the updated issue information
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/issues/{issue_number}/assignees"
        data: Dict[str, Any] = {
            "assignees": kwargs.get("assignees", []),
        }
        response = self.parent.make_request("DELETE", endpoint, json=data)
        return response

    def check_if_user_can_be_assigned_to_issue(self, repo: str, issue_number: int,
                                        username: str) -> Dict[str, Any]:
        """
        Check if a user is assigned to a specific issue.

        :param repo: Repository name
        :param issue_number: Issue number
        :param username: GitHub username to check

        :return: True if the user is assigned to the issue, False otherwise
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/issues/{issue_number}/assignees/{username}"
        response = self.parent.make_request("GET", endpoint)

        if response.status_code == 204:
            response_payload: Dict[str, Any] = {
                "is_assigned": True }
        else:
            response_payload: Dict[str, Any] = {
                "is_assigned": False }

        return response_payload


class Comments:
    """
    Submodule for managing issue comments.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    # Methods for managing comments can be added here
    def list_comments_for_repository(self, repo: str, **kwargs: Any) -> Dict[str, Any]:
        """
        List comments for a given issue.

        :param repo: Repository name
        :param sort: The property to sort comments by. Can be either 'created' or 'updated' (optional)
        :param direction: The direction of the sort. Can be either 'asc' or 'desc' (optional)
        :param since: Only comments updated at or after this time are returned (optional)
        :param per_page: Number of results per page (optional)
        :param page: Page number of the results to fetch (optional)
        :return: Dictionary containing the list of comments
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/issues/comments"
        params: Dict[str, Any] = {
            "sort": kwargs.get("sort"),
            "direction": kwargs.get("direction"),
            "since": kwargs.get("since"),
            "per_page": kwargs.get("per_page"),
            "page": kwargs.get("page"),
        }
        response = self.parent.make_request("GET", endpoint, params=params)
        return response

    def get_comment(self, repo: str, comment_id: int) -> Dict[str, Any]:
        """
        Get a specific comment by its ID.

        :param repo: Repository name
        :param comment_id: ID of the comment to retrieve

        :return: Dictionary containing the comment information
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/issues/comments/{comment_id}"
        response = self.parent.make_request("GET", endpoint)
        return response

    def update_comment(self, repo: str, comment_id: int,
                       body: str) -> Dict[str, Any]:
        """
        Update a specific comment by its ID.

        :param repo: Repository name
        :param comment_id: ID of the comment to update
        :param body: The updated text of the comment

        :return: Dictionary containing the updated comment information
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/issues/comments/{comment_id}"
        data: Dict[str, Any] = {
            "body": body,
        }
        response = self.parent.make_request("PATCH", endpoint, json=data)
        return response

    def delete_comment(self, repo: str, comment_id: int) -> Dict[str, Any]:
        """
        Delete a specific comment by its ID.

        :param repo: Repository name
        :param comment_id: ID of the comment to delete

        :return: Dictionary containing the deletion status
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/issues/comments/{comment_id}"
        response = self.parent.make_request("DELETE", endpoint)
        return response

    def list_comments(self, repo: str, issue_number: int,
                      **kwargs: Any) -> Dict[str, Any]:
        """
        List comments for a specific issue.

        :param repo: Repository name
        :param issue_number: Issue number
        :param since: Only comments updated at or after this time are returned (optional)
        :param per_page: Number of results per page (optional)
        :param page: Page number of the results to fetch (optional)

        :return: Dictionary containing the list of comments for the issue
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/issues/{issue_number}/comments"
        params: Dict[str, Any] = {
            "since": kwargs.get("since"),
            "per_page": kwargs.get("per_page"),
            "page": kwargs.get("page"),
        }
        response = self.parent.make_request("GET", endpoint, params=params)
        return response

    def create_comment(self, repo: str, issue_number: int,
                       body: str) -> Dict[str, Any]:

        """
        Create a comment on a specific issue.

        :param repo: Repository name
        :param issue_number: Issue number
        :param body: The text of the comment to create
        :return: Dictionary containing the created comment information
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/issues/{issue_number}/comments"
        data: Dict[str, Any] = {
            "body": body,
        }
        response = self.parent.make_request("POST", endpoint, json=data)
        return response


class Events:
    """
    Submodule for managing issue events.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def list_events_for_repository(self, repo: str, **kwargs: Any) -> Dict[str, Any]:
        """
        List events for a given repository.

        :param repo: Repository name
        :param per_page: Number of results per page (optional)
        :param page: Page number of the results to fetch (optional)

        :return: Dictionary containing the list of events
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/issues/events"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page"),
            "page": kwargs.get("page"),
        }
        response = self.parent.make_request("GET", endpoint, params=params)
        return response

    def get_event(self, repo: str, event_id: int) -> Dict[str, Any]:
        """
        Get a specific event by its ID.

        :param repo: Repository name
        :param event_id: ID of the event to retrieve

        :return: Dictionary containing the event information
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/issues/events/{event_id}"
        response = self.parent.make_request("GET", endpoint)
        return response

    def list_events_for_issue(self, repo: str, issue_number: int,
                              **kwargs: Any) -> Dict[str, Any]:
        """
        List events for a specific issue.

        :param repo: Repository name
        :param issue_number: Issue number
        :param per_page: Number of results per page (optional)
        :param page: Page number of the results to fetch (optional)

        :return: Dictionary containing the list of events for the issue
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/issues/{issue_number}/events"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page"),
            "page": kwargs.get("page"),
        }
        response = self.parent.make_request("GET", endpoint, params=params)
        return response


class Issues:
    """
    Issue module for managing issues in a repository.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def list_issues_for_authenticated_user(self, **kwargs: Any) -> Dict[str, Any]:
        """
        List issues assigned to the authenticated user.

        :param filter: Filter issues based on criteria like 'assigned', 'created', etc. (optional)
        :param state: State of the issues to return. Can be either 'open',
          'closed', or 'all' (optional)
        :param labels: Comma-separated list of label names. Issues must
          have all labels to be included (optional)
        :param sort: The property to sort issues by. Can be either 'created',
          'updated', 'comments' (optional)
        :param direction: The direction of the sort. Can be either 'asc' or 'desc' (optional)
        :param since: Only issues updated at or after this time are returned (optional)
        :param collab: Boolean indicating whether to include issues from
          repositories the user collaborates on (optional)
        :param orgs: Boolean indicating whether to include issues from
        organizations the user belongs to (optional)
        :param owned: Boolean indicating whether to include issues from
          repositories the user owns (optional)
        :param pulls: Boolean indicating whether to include pull requests (optional)
        :param per_page: Number of results per page (optional)
        :param page: Page number of the results to fetch (optional)

        :return: Dictionary containing the list of issues
        """
        endpoint = "/issues"
        params: Dict[str, Any] = {
            "filter": kwargs.get("filter"),
            "state": kwargs.get("state"),
            "labels": kwargs.get("labels"),
            "sort": kwargs.get("sort"),
            "direction": kwargs.get("direction"),
            "since": kwargs.get("since"),
            "collab": kwargs.get("collab"),
            "orgs": kwargs.get("orgs"),
            "owned": kwargs.get("owned"),
            "pulls": kwargs.get("pulls"),
            "per_page": kwargs.get("per_page"),
            "page": kwargs.get("page"),
        }
        response = self.parent.make_request("GET", endpoint, params=params)
        return response

    def list_organization_issues_for_authenticated_user(self, org: str,
                                              **kwargs: Any) -> Dict[str, Any]:
        """
        List issues assigned to the authenticated user within a specific organization.

        :param org: Organization name
        :param filter: Filter issues based on criteria like 'assigned', 'created', etc. (optional)
        :param state: State of the issues to return. Can be either 'open',
          'closed', or 'all' (optional)
        :param labels: Comma-separated list of label names. Issues must
          have all labels to be included (optional)
        :param type: Can be the name of an issue type.
        :param sort: The property to sort issues by. Can be either 'created',
          'updated', 'comments' (optional)
        :param direction: The direction of the sort. Can be either 'asc' or 'desc' (optional)
        :param since: Only issues updated at or after this time are returned (optional)
        :param per_page: Number of results per page (optional)
        :param page: Page number of the results to fetch (optional)

        :return: Dictionary containing the list of issues
        """
        endpoint = f"/orgs/{org}/issues"
        params: Dict[str, Any] = {
            "filter": kwargs.get("filter"),
            "state": kwargs.get("state"),
            "labels": kwargs.get("labels"),
            "type": kwargs.get("type"),
            "sort": kwargs.get("sort"),
            "direction": kwargs.get("direction"),
            "since": kwargs.get("since"),
            "per_page": kwargs.get("per_page"),
            "page": kwargs.get("page"),
        }
        response = self.parent.make_request("GET", endpoint, params=params)
        return response

    def list_repository_issues(self, repo: str,
                               **kwargs: Any) -> Dict[str, Any]:
        """
        List issues for a specific repository.

        :param repo: Repository name
        :param milestone: Milestone number to filter issues by (optional)
        :param state: State of the issues to return. Can be either 'open',
          'closed', or 'all' (optional )
        :param assignee: Filter issues assigned to a specific user (optional)
        :param type: Can be the name of an issue type. if the string * is provided,
          issues of any type are returned (optional)
        :param creator: Filter issues created by a specific user (optional)
        :param mentioned: Filter issues mentioning a specific user (optional)
        :param labels: Comma-separated list of label names. Issues must
          have all labels to be included (optional)
        :param sort: The property to sort issues by. Can be either 'created',
          'updated', 'comments' (optional)
        :param direction: The direction of the sort. Can be either 'asc' or 'desc' (optional)
        :param since: Only issues updated at or after this time are returned (optional)
        :param per_page: Number of results per page (optional)
        :param page: Page number of the results to fetch (optional)
        :return: Dictionary containing the list of issues for the repository
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/issues"
        params: Dict[str, Any] = {
            "milestone": kwargs.get("milestone"),
            "state": kwargs.get("state"),
            "assignee": kwargs.get("assignee"),
            "type": kwargs.get("type"),
            "creator": kwargs.get("creator"),
            "mentioned": kwargs.get("mentioned"),
            "labels": kwargs.get("labels"),
            "sort": kwargs.get("sort"),
            "direction": kwargs.get("direction"),
            "since": kwargs.get("since"),
            "per_page": kwargs.get("per_page"),
            "page": kwargs.get("page"),
        }
        response = self.parent.make_request("GET", endpoint, params=params)
        return response

    def create_issue(self, repo: str,
                     **kwargs: Any) -> Dict[str, Any]:
        """
        Create a new issue in a specific repository.

        :param repo: Repository name
        :param title: Title of the issue (required)
        :param body: Body content of the issue (optional)
        :param assignees: List of usernames to assign to the issue (optional)
        :param milestone: Milestone number to associate with the issue (optional)
        :param labels: List of labels to assign to the issue (optional)
        :param assignees: List of usernames to assign to the issue (optional)
        :param type: Can be the name of an issue type. if the string * is provided,
          issues of any type are returned (optional)
        :return: Dictionary containing the created issue information
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/issues"
        data: Dict[str, Any] = {
            "title": kwargs.get("title"),
            "body": kwargs.get("body"),
            "assignees": kwargs.get("assignees", []),
            "milestone": kwargs.get("milestone"),
            "labels": kwargs.get("labels", []),
            "type": kwargs.get("type"),
        }
        response = self.parent.make_request("POST", endpoint, json=data)
        return response

    def get_issue(self, repo: str, issue_number: int) -> Dict[str, Any]:
        """
        Get a specific issue by its number.

        :param repo: Repository name
        :param issue_number: Issue number

        :return: Dictionary containing the issue information
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/issues/{issue_number}"
        response = self.parent.make_request("GET", endpoint)
        return response

    def update_issue(self, repo: str, issue_number: int,
                     **kwargs: Any) -> Dict[str, Any]:
        """
        Update a specific issue by its number.

        :param repo: Repository name
        :param issue_number: Issue number
        :param title: Updated title of the issue (optional)
        :param body: Updated body content of the issue (optional)
        :param assignees: List of usernames to assign to the issue (optional)
        :param state: Updated state of the issue. Can be either 'open' or 'closed' (optional)
        :param state_reason: Reason for changing the state of the issue. Can be either
          'completed', 'not_planned', 'duplicate', or 'reopened' (optional)
        :param milestone: Milestone number to associate with the issue (optional)
        :param labels: List of labels to assign to the issue (optional)
        :param type: Can be the name of an issue type. if the string * is provided,
          issues of any type are returned (optional)
        :return: Dictionary containing the updated issue information
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/issues/{issue_number}"
        data: Dict[str, Any] = {
            "title": kwargs.get("title"),
            "body": kwargs.get("body"),
            "assignees": kwargs.get("assignees", []),
            "state": kwargs.get("state"),
            "state_reason": kwargs.get("state_reason"),
            "milestone": kwargs.get("milestone"),
            "labels": kwargs.get("labels", []),
            "type": kwargs.get("type"),
        }
        response = self.parent.make_request("PATCH", endpoint, json=data)
        return response

    def lock_issue(self, repo: str, issue_number: int,
                   **kwargs: Any) -> Dict[str, Any]:
        """
        Lock a specific issue by its number.

        :param repo: Repository name
        :param issue_number: Issue number
        :param lock_reason: Reason for locking the issue. Can be either
          'off-topic', 'too heated', 'resolved', or 'spam' (optional)

        :return: Dictionary containing the lock status
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/issues/{issue_number}/lock"
        data: Dict[str, Any] = {
            "lock_reason": kwargs.get("lock_reason"),
        }
        response = self.parent.make_request("PUT", endpoint, json=data)
        return response

    def unlock_issue(self, repo: str, issue_number: int) -> Dict[str, Any]:
        """
        Unlock a specific issue by its number.

        :param repo: Repository name
        :param issue_number: Issue number

        :return: Dictionary containing the unlock status
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/issues/{issue_number}/lock"
        response = self.parent.make_request("DELETE", endpoint)
        return response

    def list_user_account_issues_for_authenticated_user(self,
                                              **kwargs: Any) -> Dict[str, Any]:
        """
        List issues assigned to the authenticated user across all their repositories.

        :param filter: Filter issues based on criteria like 'assigned', 'created', etc. (optional)
        :param state: State of the issues to return. Can be either 'open',
          'closed', or 'all' (optional)
        :param labels: Comma-separated list of label names. Issues must
          have all labels to be included (optional)
        :param sort: The property to sort issues by. Can be either 'created',
          'updated', 'comments' (optional)
        :param direction: The direction of the sort. Can be either 'asc' or 'desc' (optional)
        :param since: Only issues updated at or after this time are returned (optional)
        :param per_page: Number of results per page (optional)
        :param page: Page number of the results to fetch (optional)

        :return: Dictionary containing the list of issues
        """
        endpoint = "/user/issues"
        params: Dict[str, Any] = {
            "filter": kwargs.get("filter"),
            "state": kwargs.get("state"),
            "labels": kwargs.get("labels"),
            "sort": kwargs.get("sort"),
            "direction": kwargs.get("direction"),
            "since": kwargs.get("since"),
            "per_page": kwargs.get("per_page"),
            "page": kwargs.get("page"),
        }
        response = self.parent.make_request("GET", endpoint, params=params)
        return response


class IssueDependencies:
    """
    Submodule for managing issue dependencies.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def list_dependencies_issue_is_blocked_by(self, repo: str,
                                            issue_number: int,
                                            **kwargs: Any) -> Dict[str, Any]:
        """
        List dependencies that block a specific issue.

        :param repo: Repository name
        :param issue_number: Issue number
        :param per_page: Number of results per page (optional)
        :param page: Page number of the results to fetch (optional)

        :return: Dictionary containing the list of blocking dependencies
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/issues/{issue_number}/dependencies/blocked_by"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page"),
            "page": kwargs.get("page"),
        }
        response = self.parent.make_request("GET", endpoint, params=params)
        return response

    def add_dependency_issue_is_blocked_by(self, repo: str,
                                   issue_number: int,
                                   issue_id: int) -> Dict[str, Any]:
        """
        Add a blocking dependency to a specific issue.

        :param repo: Repository name
        :param issue_number: Issue number
        :param issue_id: Issue number that blocks the specified issue

        :return: Dictionary containing the updated dependency information
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/issues/{issue_number}/dependencies/blocked_by"
        data: Dict[str, Any] = {
            "issue_id": issue_id,
        }
        response = self.parent.make_request("POST", endpoint, json=data)
        return response

    def remove_dependency_issue_is_blocked_by(self, repo: str,
                                      issue_number: int,
                                      issue_id: int) -> Dict[str, Any]:
        """
        Remove a blocking dependency from a specific issue.

        :param repo: Repository name
        :param issue_number: Issue number
        :param issue_id: Issue number that blocks the specified issue

        :return: Dictionary containing the updated dependency information
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/issues/{issue_number}/dependencies/blocked_by/{issue_id}"
        response = self.parent.make_request("DELETE", endpoint)
        return response

    def list_dependencies_issue_is_blocking(self, repo: str,
                                           issue_number: int,
                                           **kwargs: Any) -> Dict[str, Any]:
        """
        List dependencies that a specific issue is blocking.

        :param repo: Repository name
        :param issue_number: Issue number
        :param per_page: Number of results per page (optional)
        :param page: Page number of the results to fetch (optional)

        :return: Dictionary containing the list of blocking dependencies
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/issues/{issue_number}/dependencies/blocking"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page"),
            "page": kwargs.get("page"),
        }
        response = self.parent.make_request("GET", endpoint, params=params)
        return response


class Labels:
    """
    Submodule for managing issue labels.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def list_labels(self, repo: str, issue_number: int,
                    **kwargs: Any) -> Dict[str, Any]:
        """
        List labels for a specific issue.

        :param repo: Repository name
        :param issue_number: Issue number
        :param per_page: Number of results per page (optional)
        :param page: Page number of the results to fetch (optional)

        :return: Dictionary containing the list of labels for the issue
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/issues/{issue_number}/labels"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page"),
            "page": kwargs.get("page"),
        }
        response = self.parent.make_request("GET", endpoint, params=params)
        return response

    def add_labels(self, repo: str, issue_number: int,
                   **kwargs: Any) -> Dict[str, Any]:
        """
        Add labels to a specific issue.

        :param repo: Repository name
        :param issue_number: Issue number
        :param labels: (optional) List of label names to add to the issue.
        :return: Dictionary containing the updated list of labels for the issue
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/issues/{issue_number}/labels"
        data: Dict[str, Any] = {
            "labels": kwargs.get("labels", []),
        }
        response = self.parent.make_request("POST", endpoint, json=data)
        return response

    def set_labels(self, repo: str, issue_number: int,
                   **kwargs: Any) -> Dict[str, Any]:
        """
        Set labels for a specific issue, replacing existing labels.

        :param repo: Repository name
        :param issue_number: Issue number
        :param labels: (optional) List of label names to set for the issue.
        :return: Dictionary containing the updated list of labels for the issue
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/issues/{issue_number}/labels"
        data: Dict[str, Any] = {
            "labels": kwargs.get("labels", []),
        }
        response = self.parent.make_request("PUT", endpoint, json=data)
        return response

    def remove_all_labels(self, repo: str, issue_number: int) -> Dict[str, Any]:
        """
        Remove all labels from a specific issue.

        :param repo: Repository name
        :param issue_number: Issue number
        :return: Dictionary containing the status of the removal operation
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/issues/{issue_number}/labels"
        response = self.parent.make_request("DELETE", endpoint)
        return response

    def remove_label(self, repo: str, issue_number: int,
                     label_name: str) -> Dict[str, Any]:
        """
        Remove a specific label from a specific issue.

        :param repo: Repository name
        :param issue_number: Issue number
        :param label_name: Name of the label to remove from the issue.
        :return: Dictionary containing the status of the removal operation
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/issues/{issue_number}/labels/{label_name}"
        response = self.parent.make_request("DELETE", endpoint)
        return response

    def list_labels_for_repository(self, repo: str,
                                   **kwargs: Any) -> Dict[str, Any]:
        """
        List all labels for a specific repository.

        :param repo: Repository name
        :param per_page: Number of results per page (optional)
        :param page: Page number of the results to fetch (optional)
        :return: Dictionary containing the list of labels for the repository
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/labels"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page"),
            "page": kwargs.get("page"),
        }
        response = self.parent.make_request("GET", endpoint, params=params)
        return response

    def create_label(self, repo: str, name: str,
                     **kwargs: Any) -> Dict[str, Any]:
        """
        Create a new label in a specific repository.

        :param repo: Repository name
        :param name: Name of the label (required)
        :param color: Color code of the label without the leading '#' (required)
        :param description: Description of the label (optional)
        :return: Dictionary containing the created label information
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/labels"
        data: Dict[str, Any] = {
            "name": name,
            "color": kwargs.get("color"),
            "description": kwargs.get("description"),
        }
        response = self.parent.make_request("POST", endpoint, json=data)
        return response

    def get_label(self, repo: str, label_name: str) -> Dict[str, Any]:
        """
        Get a specific label by its name in a repository.

        :param repo: Repository name
        :param label_name: Name of the label to retrieve
        :return: Dictionary containing the label information
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/labels/{label_name}"
        response = self.parent.make_request("GET", endpoint)
        return response

    def update_label(self, repo: str, current_name: str,
                     **kwargs: Any) -> Dict[str, Any]:

        """
        Updates a label using its current name in a repository.

        :param repo: Repository name
        :param current_name: Current name of the label to update
        :param new_name: New name for the label (optional)
        :param color: New color code for the label without the leading '#' (optional)
        :param description: New description for the label (optional)
        :return: Dictionary containing the updated label information
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/labels/{current_name}"
        data: Dict[str, Any] = {
            "name": kwargs.get("new_name"),
            "color": kwargs.get("color"),
            "description": kwargs.get("description"),
        }
        response = self.parent.make_request("PATCH", endpoint, json=data)
        return response

    def delete_label(self, repo: str, label_name: str) -> Dict[str, Any]:
        """
        Delete a specific label by its name in a repository.

        :param repo: Repository name
        :param label_name: Name of the label to delete
        :return: Dictionary containing the deletion status
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/labels/{label_name}"
        response = self.parent.make_request("DELETE", endpoint)
        return response

    def list_labels_for_milestone(self, repo: str, milestone_number: int,
                                 **kwargs: Any) -> Dict[str, Any]:
        """
        List labels for a specific milestone.

        :param repo: Repository name
        :param milestone_number: Milestone number
        :param per_page: Number of results per page (optional)
        :param page: Page number of the results to fetch (optional)
        :return: Dictionary containing the list of labels for the milestone
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/milestones/{milestone_number}/labels"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page"),
            "page": kwargs.get("page"),
        }
        response = self.parent.make_request("GET", endpoint, params=params)
        return response


class Milestones:
    """
    Submodule for managing issue milestones.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def list_milestones(self, repo: str,
                        **kwargs: Any) -> Dict[str, Any]:
        """
        List milestones for a specific repository.

        :param repo: Repository name
        :param state: State of the milestones to return. Can be either 'open',
          'closed', or 'all' (optional)
        :param sort: The property to sort milestones by. Can be either 'due_on',
          'completeness', or 'created' (optional)
        :param direction: The direction of the sort. Can be either 'asc' or 'desc' (optional)
        :param per_page: Number of results per page (optional)
        :param page: Page number of the results to fetch (optional)
        :return: Dictionary containing the list of milestones for the repository
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/milestones"
        params: Dict[str, Any] = {
            "state": kwargs.get("state"),
            "sort": kwargs.get("sort"),
            "direction": kwargs.get("direction"),
            "per_page": kwargs.get("per_page"),
            "page": kwargs.get("page"),
        }
        response = self.parent.make_request("GET", endpoint, params=params)
        return response

    def create_milestone(self, repo: str, title: str,
                         **kwargs: Any) -> Dict[str, Any]:

        """
        Create a new milestone in a specific repository.

        :param repo: Repository name
        :param title: Title of the milestone
        :param state: State of the milestone. Can be either 'open' or 'closed' (optional)
        :param description: Description of the milestone (optional)
        :param due_on: Due date of the milestone in ISO 8601 format (optional)
        :return: Dictionary containing the created milestone information
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/milestones"
        data: Dict[str, Any] = {
            "title": title,
            "state": kwargs.get("state"),
            "description": kwargs.get("description"),
            "due_on": kwargs.get("due_on"),
        }
        response = self.parent.make_request("POST", endpoint, json=data)
        return response

    def get_milestone(self, repo: str, milestone_number: int) -> Dict[str, Any]:
        """
        Get a specific milestone by its number.

        :param repo: Repository name
        :param milestone_number: Milestone number
        :return: Dictionary containing the milestone information
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/milestones/{milestone_number}"
        response = self.parent.make_request("GET", endpoint)
        return response

    def update_milestone(self, repo: str, milestone_number: int,
                         **kwargs: Any) -> Dict[str, Any]:
        """
        Update a specific milestone by its number.

        :param repo: Repository name
        :param milestone_number: Milestone number
        :param title: Updated title of the milestone (optional)
        :param state: Updated state of the milestone. Can be either 'open' or 'closed' (optional)
        :param description: Updated description of the milestone (optional)
        :param due_on: Updated due date of the milestone in ISO 8601 format (optional)
        :return: Dictionary containing the updated milestone information
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/milestones/{milestone_number}"
        data: Dict[str, Any] = {
            "title": kwargs.get("title"),
            "state": kwargs.get("state"),
            "description": kwargs.get("description"),
            "due_on": kwargs.get("due_on"),
        }
        response = self.parent.make_request("PATCH", endpoint, json=data)
        return response

    def delete_milestone(self, repo: str, milestone_number: int) -> Dict[str, Any]:
        """
        Delete a specific milestone by its number.

        :param repo: Repository name
        :param milestone_number: Milestone number
        :return: Dictionary containing the deletion status
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/milestones/{milestone_number}"
        response = self.parent.make_request("DELETE", endpoint)
        return response


class SubIssues:
    """
    Submodule for managing sub-issues.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def get_parent_issue(self, repo: str,
                         issue_number: int) -> Dict[str, Any]:
        """
        Get the parent issue of a specific sub-issue.

        :param repo: Repository name
        :param issue_number: Sub-issue number
        :return: Dictionary containing the parent issue information
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/issues/{issue_number}/parent"
        response = self.parent.make_request("GET", endpoint)
        return response

    def remove_sub_issue(self, repo: str,
                         issue_number: int) -> Dict[str, Any]:
        """
        Remove a specific sub-issue from its parent issue.

        :param repo: Repository name
        :param issue_number: Sub-issue number
        :return: Dictionary containing the removal status
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/issues/{issue_number}/sub_issue"
        response = self.parent.make_request("DELETE", endpoint)
        return response

    def list_sub_issues(self, repo: str,
                        issue_number: int,
                        **kwargs: Any) -> Dict[str, Any]:
        """
        List sub-issues of a specific parent issue.

        :param repo: Repository name
        :param issue_number: Parent issue number
        :param per_page: Number of results per page (optional)
        :param page: Page number of the results to fetch (optional)
        :return: Dictionary containing the list of sub-issues
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/issues/{issue_number}/sub_issues"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page"),
            "page": kwargs.get("page"),
        }
        response = self.parent.make_request("GET", endpoint, params=params)
        return response

    def add_sub_issue(self, repo: str, issue_number: int,
                      sub_issue_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Add a sub-issue to a specific parent issue.

        :param repo: Repository name
        :param issue_number: Parent issue number
        :param sub_issue_id: Issue number of the sub-issue to add
        :param replace_parent: Boolean indicating whether to replace the
          parent of the sub-issue if it already has one (optional)
        :return: Dictionary containing the updated list of sub-issues
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/issues/{issue_number}/sub_issues"
        data: Dict[str, Any] = {
            "sub_issue_id": sub_issue_id,
            "replace_parent": kwargs.get("replace_parent"),
        }
        response = self.parent.make_request("POST", endpoint, json=data)
        return response

    def reprioritize_sub_issue(self, repo: str,
                             issue_number: int,
                             **kwargs: Any) -> Dict[str, Any]:
        """
        Reprioritize sub-issues of a specific parent issue.

        :param repo: Repository name
        :param issue_number: Parent issue number
        :param sub_issue_id: ID of the sub-issue to reprioritize
        :param after_id: Sub-issue number after which to place the reordered sub-issues (optional)
        :param before_id: Sub-issue number before which to place the reordered sub-issues (optional)
        :return: Dictionary containing the updated list of sub-issues
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/issues/{issue_number}/sub_issues/priority"
        data: Dict[str, Any] = {
            "sub_issue_id": kwargs.get("sub_issue_id", []),
            "after_id": kwargs.get("after_id"),
            "before_id": kwargs.get("before_id"),

        }
        response = self.parent.make_request("POST", endpoint, json=data)
        return response


class Timeline:
    """
    Submodule for managing issue timeline.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def list_timeline_events(self, repo: str,
                             issue_number: int,
                             **kwargs: Any) -> Dict[str, Any]:
        """
        List timeline events for a specific issue.

        :param repo: Repository name
        :param issue_number: Issue number
        :param per_page: Number of results per page (optional)
        :param page: Page number of the results to fetch (optional)
        :return: Dictionary containing the list of timeline events
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/issues/{issue_number}/timeline"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page"),
            "page": kwargs.get("page"),
        }
        response = self.parent.make_request("GET", endpoint, params=params)
        return response


class Issue:
    """
    Main Issue module that aggregates all issue-related submodules.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

        # Initialize Submodules
        self.assignees = Assignees(parent)
        self.comments = Comments(parent)
        self.events = Events(parent)
        self.issues = Issues(parent)
        self.issue_dependencies = IssueDependencies(parent)
        self.labels = Labels(parent)
        self.milestones = Milestones(parent)
        self.sub_issues = SubIssues(parent)
        self.timeline = Timeline(parent)
