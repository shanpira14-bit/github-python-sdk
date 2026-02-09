"""
Pull Requests Module
"""
from typing import Any, Dict, List

class PullRequests:
    """
    A class to manage pull requests.
    """
    def __init__(self, parent: Any) -> None:
        self._parent = parent

    def list_pull_requests(self, repo: str, **kwargs: Any) -> Any:
        """
        List all pull requests.

        :param repository: The repository name.
        :param state: Filter by state (open, closed, all). Default is open.
        :param head: Filter by head branch.
        :param base: Filter by base branch.
        :param sort: Sort by (created, updated, popularity, long-running). Default is created.
        :param direction: Direction of sort (asc, desc). Default is desc.
        :param per_page: Number of pull requests per page. Default is 30.
        :param page: Page number to retrieve. Default is 1.
        :return: A list of pull requests.
        """
        endpoint= f"/repos/{self._parent.org}/{repo}/pulls"
        params: Dict[str, Any] = {
            "state": kwargs.get("state", "open"),
            "head": kwargs.get("head"),
            "base": kwargs.get("base"),
            "sort": kwargs.get("sort", "created"),
            "direction": kwargs.get("direction", "desc"),
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self._parent.make_request("GET", endpoint, params=params)

    def create_pull_request(self, repo: str, head: str, base: str, **kwargs: Any) -> Any:
        """
        Create a new pull request.

        :param repository: The repository name.
        :param head: The name of the branch where your changes are implemented.
        :param head_repo: (Optional) The repository that contains the head branch.
        :param base: The name of the branch you want the changes pulled into.
        :param title: Title of the pull request.
        :param body: (Optional) Body description of the pull request.
        :param draft: (Optional) Whether the pull request is a draft. Default is False.
        :param maintainer_can_modify: (Optional) Whether maintainers can modify the pull request.
          Default is True.
        :param issue: (Optional) Issue number to link the pull request to.
        :return: The created pull request details.
        """
        endpoint = f"/repos/{self._parent.org}/{repo}/pulls"
        data: Dict[str, Any] = {
            "title": kwargs.get("title", "New Pull Request"),
            "head": head,
            "head_repo": kwargs.get("head_repo"),
            "base": base,
            "body": kwargs.get("body", ""),
            "maintainer_can_modify": kwargs.get("maintainer_can_modify", True),
            "draft": kwargs.get("draft", False),
            "issue": kwargs.get("issue")
        }
        return self._parent.make_request("POST", endpoint, json=data)

    def get_pull_request(self, repo: str, pull_number: int) -> Any:
        """
        Get details of a specific pull request.

        :param repository: The repository name.
        :param pull_number: The number of the pull request.
        :return: The pull request details.
        """
        endpoint = f"/repos/{self._parent.org}/{repo}/pulls/{pull_number}"
        return self._parent.make_request("GET", endpoint)

    def update_pull_request(self, repo: str, pull_number: int, **kwargs: Any) -> Any:
        """
        Update an existing pull request.

        :param repository: The repository name.
        :param pull_number: The number of the pull request.
        :param title: (Optional) New title of the pull request.
        :param body: (Optional) New body description of the pull request.
        :param state: (Optional) State of the pull request (open, closed).
        :param base: (Optional) New base branch for the pull request.
        :param maintainer_can_modify: (Optional) Whether maintainers can modify the pull request.
        :return: The updated pull request details.
        """
        endpoint = f"/repos/{self._parent.org}/{repo}/pulls/{pull_number}"
        data: Dict[str, Any] = {
            "title": kwargs.get("title"),
            "body": kwargs.get("body"),
            "state": kwargs.get("state"),
            "base": kwargs.get("base"),
            "maintainer_can_modify": kwargs.get("maintainer_can_modify")
        }
        # Remove keys with None values
        data = {k: v for k, v in data.items() if v is not None}
        return self._parent.make_request("PATCH", endpoint, json=data)

    def list_commits_on_pull_request(self, repo: str, pull_number: int, **kwargs: Any) -> Any:
        """
        List commits on a specific pull request.

        :param repository: The repository name.
        :param pull_number: The number of the pull request.
        :param per_page: Number of commits per page. Default is 30.
        :param page: Page number to retrieve. Default is 1.
        :return: A list of commits on the pull request.
        """
        endpoint = f"/repos/{self._parent.org}/{repo}/pulls/{pull_number}/commits"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self._parent.make_request("GET", endpoint, params=params)

    def list_pull_requests_files(self, repo: str, pull_number: int, **kwargs: Any) -> Any:
        """
        List files changed in a specific pull request.

        :param repository: The repository name.
        :param pull_number: The number of the pull request.
        :param per_page: Number of files per page. Default is 30.
        :param page: Page number to retrieve. Default is 1.
        :return: A list of files changed in the pull request.
        """
        endpoint = f"/repos/{self._parent.org}/{repo}/pulls/{pull_number}/files"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self._parent.make_request("GET", endpoint, params=params)

    def check_if_pull_request_merged(self, repo: str, pull_number: int) -> Any:
        """
        Check if a specific pull request has been merged.

        :param repository: The repository name.
        :param pull_number: The number of the pull request.
        :return: True if merged, False otherwise.
        """
        endpoint = f"/repos/{self._parent.org}/{repo}/pulls/{pull_number}/merge"
        response = self._parent.make_request("GET", endpoint)
        if response["status_code"] == 204:
            return True
        elif response["status_code"] == 404:
            return False
        else:
            return response

    def merge_pull_request(self, repo: str, pull_number: int, **kwargs: Any) -> Any:
        """
        Merge a specific pull request.

        :param repository: The repository name.
        :param pull_number: The number of the pull request.
        :param commit_title: (Optional) Title for the merge commit.
        :param commit_message: (Optional) Message for the merge commit.
        :param sha: (Optional) SHA that pull request head must match to allow merge.
        :param merge_method: (Optional) Merge method to use (merge, squash, rebase).
          Default is merge.
        :return: The result of the merge operation.
        """
        endpoint = f"/repos/{self._parent.org}/{repo}/pulls/{pull_number}/merge"
        data: Dict[str, Any] = {
            "commit_title": kwargs.get("commit_title"),
            "commit_message": kwargs.get("commit_message"),
            "sha": kwargs.get("sha"),
            "merge_method": kwargs.get("merge_method", "merge")
        }
        return self._parent.make_request("PUT", endpoint, json=data)

    def update_pull_request_branch(self, repo: str, pull_number: int, **kwargs: Any) -> Any:
        """
        Update the branch of a specific pull request.

        :param repository: The repository name.
        :param pull_number: The number of the pull request.
        :param expected_head_sha: (Optional) SHA of the head branch to ensure it is up to date.
        :return: The result of the branch update operation.
        """
        endpoint = f"/repos/{self._parent.org}/{repo}/pulls/{pull_number}/update-branch"
        data: Dict[str, Any] = {
            "expected_head_sha": kwargs.get("expected_head_sha")
        }
        return self._parent.make_request("PUT", endpoint, json=data)


class ReviewComments:
    """
    A class to manage review comments on pull requests.
    """
    def __init__(self, parent: Any) -> None:
        self._parent = parent

    def list_review_comments_in_repository(self, repo: str, **kwargs: Any) -> Any:
        """
        List review comments on a specific pull request.

        :param repository: The repository name.
        :param sort: Sort by (created, updated). Default is created.
        :param direction: Direction of sort (asc, desc). Default is desc.
        :param since: Only comments updated at or after this time are returned (ISO 8601 format).
        :param per_page: Number of comments per page. Default is 30.
        :param page: Page number to retrieve. Default is 1.
        :return: A list of review comments on the pull request.
        """
        endpoint = f"/repos/{self._parent.org}/{repo}/pulls/comments"
        params: Dict[str, Any] = {
            "sort": kwargs.get("sort", "created"),
            "direction": kwargs.get("direction", "desc"),
            "since": kwargs.get("since"),
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self._parent.make_request("GET", endpoint, params=params)

    def get_review_comment(self, repo: str, comment_id: int) -> Any:
        """
        Get details of a specific review comment.

        :param repository: The repository name.
        :param comment_id: The ID of the review comment.
        :return: The review comment details.
        """
        endpoint = f"/repos/{self._parent.org}/{repo}/pulls/comments/{comment_id}"
        return self._parent.make_request("GET", endpoint)

    def update_review_comment(self, repo: str, comment_id: int, body: str) -> Any:
        """
        Update a specific review comment.

        :param repository: The repository name.
        :param comment_id: The ID of the review comment.
        :param body: The updated text of the review comment.
        :return: The updated review comment details.
        """
        endpoint = f"/repos/{self._parent.org}/{repo}/pulls/comments/{comment_id}"
        data: Dict[str, Any] = {
            "body": body
        }
        return self._parent.make_request("PATCH", endpoint, json=data)

    def delete_review_comment(self, repo: str, comment_id: int) -> Any:
        """
        Delete a specific review comment.

        :param repository: The repository name.
        :param comment_id: The ID of the review comment.
        :return: The result of the delete operation.
        """
        endpoint = f"/repos/{self._parent.org}/{repo}/pulls/comments/{comment_id}"
        return self._parent.make_request("DELETE", endpoint)

    def list_review_comments_on_pull_request(self, repo: str,
                                             pull_number: int, **kwargs: Any) -> Any:
        """
        List review comments on a specific pull request.

        :param repository: The repository name.
        :param pull_number: The number of the pull request.
        :param sort: Sort by (created, updated). Default is created.
        :param direction: Direction of sort (asc, desc). Default is desc.
        :param since: Only comments updated at or after this time are returned (ISO 8601 format).
        :param per_page: Number of comments per page. Default is 30.
        :param page: Page number to retrieve. Default is 1.
        :return: A list of review comments on the pull request.
        """
        endpoint = f"/repos/{self._parent.org}/{repo}/pulls/{pull_number}/comments"
        params: Dict[str, Any] = {
            "sort": kwargs.get("sort", "created"),
            "direction": kwargs.get("direction", "desc"),
            "since": kwargs.get("since"),
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self._parent.make_request("GET", endpoint, params=params)

    def create_review_comment(self, repo: str, pull_number: int, body: str,
                              commit_id: str, path: str, **kwargs: Any) -> Any:
        """
        Create a review comment on a specific pull request.

        :param repository: The repository name.
        :param pull_number: The number of the pull request.
        :param body: The text of the review comment.
        :param commit_id: The commit ID the comment is associated with.
        :param path: The relative path of the file to comment on.
        :param position: (Optional) The position in the diff to comment on.
        :param side: (Optional) The side of the diff to comment on (LEFT, RIGHT).
        :param line: (Optional) The line number in the file to
            comment on (required if position is not provided).
        :param start_line: (Optional) The starting line of a multi-line comment.
        :param start_side: (Optional) The side of the starting line (LEFT, RIGHT).
        :param in_reply_to: (Optional) The ID of the comment to reply to.
        :param subject_type: (Optional) The type of the comment subject (LINE, FILE).
        :return: The created review comment details.
        """
        endpoint = f"/repos/{self._parent.org}/{repo}/pulls/{pull_number}/comments"
        data: Dict[str, Any] = {
            "body": body,
            "commit_id": commit_id,
            "path": path,
            "position": kwargs.get("position"),
            "side": kwargs.get("side"),
            "line": kwargs.get("line"),
            "start_line": kwargs.get("start_line"),
            "start_side": kwargs.get("start_side"),
            "in_reply_to": kwargs.get("in_reply_to"),
            "subject_type": kwargs.get("subject_type")
        }
        return self._parent.make_request("POST", endpoint, json=data)

    def create_reply_to_review_comment(self, repo: str, pull_number: int,
                                       comment_id: int, body: str) -> Any:
        """
        Create a reply to a review comment on a specific pull request.

        :param repository: The repository name.
        :param pull_number: The number of the pull request.
        :param comment_id: The ID of the review comment to reply to.
        :param body: The text of the reply comment.
        :return: The created reply comment details.
        """
        endpoint = f"/repos/{self._parent.org}/{repo}/pulls/{pull_number}/comments/{comment_id}/replies"
        data: Dict[str, Any] = {
            "body": body
        }
        return self._parent.make_request("POST", endpoint, json=data)


class ReviewRequests:
    """
    A class to manage review requests on pull requests.
    """
    def __init__(self, parent: Any) -> None:
        self._parent = parent

    def get_all_requested_reviewers(self, repo: str, pull_number: int) -> Any:
        """
        Get all requested reviewers for a specific pull request.

        :param repository: The repository name.
        :param pull_number: The number of the pull request.
        :return: A list of requested reviewers.
        """
        endpoint = f"/repos/{self._parent.org}/{repo}/pulls/{pull_number}/requested_reviewers"
        return self._parent.make_request("GET", endpoint)

    def request_reviewers(self, repo: str, pull_number: int, **kwargs: Any) -> Any:
        """
        Request reviewers for a specific pull request.

        :param repository: The repository name.
        :param pull_number: The number of the pull request.
        :param reviewers: A list of reviewer usernames to request review from.
        :param team_reviewers: A list of team slugs to request review from.
        :return: The result of the review request operation.
        """
        endpoint = f"/repos/{self._parent.org}/{repo}/pulls/{pull_number}/requested_reviewers"
        data: Dict[str, Any] = {
            "reviewers": kwargs.get("reviewers", []),
            "team_reviewers": kwargs.get("team_reviewers", [])
        }
        return self._parent.make_request("POST", endpoint, json=data)

    def remove_reviewers(self, repo: str, pull_number: int,
                         reviewers: List[Dict[str, Any]], **kwargs: Any) -> Any:
        """
        Remove requested reviewers from a specific pull request.

        :param repository: The repository name.
        :param pull_number: The number of the pull request.
        :param reviewers: A list of reviewer usernames to remove from review request.
        :param team_reviewers: A list of team slugs to remove from review request.
        :return: The result of the review removal operation.
        """
        endpoint = f"/repos/{self._parent.org}/{repo}/pulls/{pull_number}/requested_reviewers"
        data: Dict[str, Any] = {
            "reviewers": reviewers,
            "team_reviewers": kwargs.get("team_reviewers", [])
        }
        return self._parent.make_request("DELETE", endpoint, json=data)


class Reviews: #TODO: Reviews Module
    """
    A class to manage reviews on pull requests.
    """
    def __init__(self, parent: Any) -> None:
        self._parent = parent

    def list_reviews(self, repo: str, pull_number: int, **kwargs: Any) -> Any:
        """
        List reviews on a specific pull request.

        :param repository: The repository name.
        :param pull_number: The number of the pull request.
        :param per_page: Number of reviews per page. Default is 30.
        :param page: Page number to retrieve. Default is 1.
        :return: A list of reviews on the pull request.
        """
        endpoint = f"/repos/{self._parent.org}/{repo}/pulls/{pull_number}/reviews"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self._parent.make_request("GET", endpoint, params=params)

    def create_review(self, repo: str, pull_number: int, **kwargs: Any) -> Any:
        """
        Create a review on a specific pull request.

        :param repository: The repository name.
        :param pull_number: The number of the pull request.
        :param body: The text of the review comment.
        :param event: The review action to perform (APPROVE, REQUEST_CHANGES, COMMENT).
        :param comments: (Optional) A list of review comment objects for inline comments.
            Refer to GitHub API documentation for the structure of review comment objects.
            https://docs.github.com/en/rest/pulls/reviews?apiVersion=2022-11-28#create-a-review-for-a-pull-request
        :return: The created review details.
        """
        endpoint = f"/repos/{self._parent.org}/{repo}/pulls/{pull_number}/reviews"
        data: Dict[str, Any] = {
            "commit_id": kwargs.get("commit_id"),
            "body": kwargs.get("body", ""),
            "event": kwargs.get("event", ""),
            "comments": kwargs.get("comments", [])
        }
        return self._parent.make_request("POST", endpoint, json=data)

    def get_review(self, repo: str, pull_number: int, review_id: int) -> Any:
        """
        Get details of a specific review.

        :param repository: The repository name.
        :param pull_number: The number of the pull request.
        :param review_id: The ID of the review.
        :return: The review details.
        """
        endpoint = f"/repos/{self._parent.org}/{repo}/pulls/{pull_number}/reviews/{review_id}"
        return self._parent.make_request("GET", endpoint)

    def update_review(self, repo: str, pull_number: int, review_id: int, **kwargs: Any) -> Any:
        """
        Update a specific review.

        :param repository: The repository name.
        :param pull_number: The number of the pull request.
        :param review_id: The ID of the review.
        :param body: The updated text of the review comment.
        :return: The updated review details.
        """
        endpoint = f"/repos/{self._parent.org}/{repo}/pulls/{pull_number}/reviews/{review_id}"
        data: Dict[str, Any] = {
            "body": kwargs.get("body")
        }
        return self._parent.make_request("PUT", endpoint, json=data)

    def delete_pending_review(self, repo: str, pull_number: int, review_id: int) -> Any:
        """
        Delete a pending review.

        :param repository: The repository name.
        :param pull_number: The number of the pull request.
        :param review_id: The ID of the pending review.
        :return: The result of the delete operation.
        """
        endpoint = f"/repos/{self._parent.org}/{repo}/pulls/{pull_number}/reviews/{review_id}"
        return self._parent.make_request("DELETE", endpoint)

    def list_comments_on_review(self, repo: str, pull_number: int,
                                review_id: int, **kwargs: Any) -> Any:
        """
        List comments on a specific review.

        :param repository: The repository name.
        :param pull_number: The number of the pull request.
        :param review_id: The ID of the review.
        :param per_page: Number of comments per page. Default is 30.
        :param page: Page number to retrieve. Default is 1.
        :return: A list of comments on the review.
        """
        endpoint = f"/repos/{self._parent.org}/{repo}/pulls/{pull_number}/reviews/{review_id}/comments"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self._parent.make_request("GET", endpoint, params=params)

    def dismiss_review(self, repo: str, pull_number: int, review_id: int, **kwargs: Any) -> Any:
        """
        Dismiss a specific review.

        :param repository: The repository name.
        :param pull_number: The number of the pull request.
        :param review_id: The ID of the review.
        :param message: The message for dismissing the review.
        :return: The result of the dismiss operation.
        """
        endpoint = f"/repos/{self._parent.org}/{repo}/pulls/{pull_number}/reviews/{review_id}/dismissals"
        data: Dict[str, Any] = {
            "message": kwargs.get("message", "Review dismissed.")
        }
        return self._parent.make_request("POST", endpoint, json=data)

    def submit_review(self, repo: str, pull_number: int, review_id: int,
                      event: str, **kwargs: Any) -> Any:
        """
        Submit a pending review.

        :param repository: The repository name.
        :param pull_number: The number of the pull request.
        :param review_id: The ID of the pending review.
        :param event: The review action to perform (APPROVE, REQUEST_CHANGES, COMMENT).
        :param body: (Optional) The text of the review comment.
        :return: The result of the submit operation.
        """
        endpoint = f"/repos/{self._parent.org}/{repo}/pulls/{pull_number}/reviews/{review_id}/events"
        data: Dict[str, Any] = {
            "event": event,
            "body": kwargs.get("body", "")
        }
        return self._parent.make_request("POST", endpoint, json=data)


class PullRequest:
    """
    A class to represent a single pull request.
    """
    def __init__(self, parent: Any) -> None:

        # Initialize Sub-modules
        self.pull_requests = PullRequests(parent)
        self.review_comments = ReviewComments(parent)
        self.review_requests = ReviewRequests(parent)
        self.reviews = Reviews(parent)
