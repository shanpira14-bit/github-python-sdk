"""
Collaborators module for managing GitHub repository collaborators and invitations.
"""
from typing import Any, Dict

class Collaborators:
    """
    Module for managing repository collaborators.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def list_repository_collaborators(self, repo: str, **kwargs: Any) -> Dict[str, Any]:
        """
        List collaborators for a given repository.

        :param repo: Repository name
        :param affiliation: Filter collaborators by affiliation (optional)
        :param permission: Filter collaborators by permission (optional)
        :param per_page: Number of results per page (optional)
        :param page: Page number of the results to fetch (optional)

        :return: Dictionary containing the list of collaborators
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/collaborators"
        params: Dict[str, Any] = {
            "affiliation": kwargs.get("affiliation"),
            "permission": kwargs.get("permission"),
            "per_page": kwargs.get("per_page"),
            "page": kwargs.get("page"),
        }
        response = self.parent.make_request("GET", endpoint, params=params)
        return response

    def check_if_user_is_collaborator(self, repo: str, username: str) -> Dict[str, Any]:
        """
        Check if a user is a collaborator on a given repository.

        :param repo: Repository name
        :param username: GitHub username to check

        :return: True if the user is a collaborator, False otherwise
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/collaborators/{username}"
        response = self.parent.make_request("GET", endpoint)

        if response.status_code == 204:
            response_payload: Dict[str, Any] = {
                "is_collaborator": True }
        else:
            response_payload: Dict[str, Any] = {
                "is_collaborator": False }

        return response_payload

    def add_repository_collaborator(self, repo: str, username: str,
                                    permission: str = "push") -> Dict[str, Any]:
        """
        Add a collaborator to a given repository.

        :param repo: Repository name
        :param username: GitHub username to add as collaborator
        :param permission: Permission level for the collaborator (default: "push")
            e.g., "pull", "push", "admin", "maintain", "triage"
        :return: Dictionary containing the response from the API
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/collaborators/{username}"
        data = {
            "permission": permission
        }
        response = self.parent.make_request("PUT", endpoint, json=data)
        return response

    def remove_repository_collaborator(self, repo: str, username: str) -> Dict[str, Any]:
        """
        Remove a collaborator from a given repository.

        :param repo: Repository name
        :param username: GitHub username to remove as collaborator

        :return: Dictionary containing the response from the API
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/collaborators/{username}"
        response = self.parent.make_request("DELETE", endpoint)
        return response

    def get_collaborator_permissions(self, repo: str, username: str) -> Dict[str, Any]:
        """
        Get the permissions of a collaborator on a given repository.

        :param repo: Repository name
        :param username: GitHub username of the collaborator

        :return: Dictionary containing the permissions of the collaborator
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/collaborators/{username}/permission"
        response = self.parent.make_request("GET", endpoint)
        return response


class Invitations:
    """
    Module for managing repository invitations.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def repository_invitations(self, repo: str, **kwargs: Any) -> Dict[str, Any]:
        """
        List pending repository invitations.

        :param repo: Repository name
        :param per_page: Number of results per page (optional)
        :param page: Page number of the results to fetch (optional)

        :return: Dictionary containing the list of pending invitations
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/invitations"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page"),
            "page": kwargs.get("page"),
        }
        response = self.parent.make_request("GET", endpoint, params=params)
        return response

    def update_repository_invitation(self, repo: str, invitation_id: int,
                                     **kwargs: Any) -> Dict[str, Any]:
        """
        Update a pending repository invitation.

        :param repo: Repository name
        :param invitation_id: ID of the invitation to update
        :param permission: New permission level for the invitation (optional) \n
            e.g., "pull", "push", "admin", "maintain", "triage"

        :return: Dictionary containing the response from the API
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/invitations/{invitation_id}"
        data = {
            "permission": kwargs.get("permission")
        }
        response = self.parent.make_request("PATCH", endpoint, json=data)
        return response

    def delete_repository_invitation(self, repo: str, invitation_id: int) -> Dict[str, Any]:
        """
        Delete a pending repository invitation.

        :param repo: Repository name
        :param invitation_id: ID of the invitation to delete

        :return: Dictionary containing the response from the API
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/invitations/{invitation_id}"
        response = self.parent.make_request("DELETE", endpoint)
        return response

    def list_repository_pending_invitations(self, repo: str, **kwargs: Any) -> Dict[str, Any]:
        """
        List pending invitations for a given repository.

        :param repo: Repository name
        :param per_page: Number of results per page (optional)
        :param page: Page number of the results to fetch (optional)

        :return: Dictionary containing the list of pending invitations
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/invitations"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page"),
            "page": kwargs.get("page"),
        }
        response = self.parent.make_request("GET", endpoint, params=params)
        return response


class Collaborator:
    """
    A class to manage collaborator-related submodules.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

        # Initialize Submodules
        self.collaborators = Collaborators(parent)
        self.invitations = Invitations(parent)
