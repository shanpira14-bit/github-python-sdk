"""
Modules for teams.
"""
from typing import Any, Dict

class Members:
    """
    Members module that contains members.
    """
    def __init__(self, parent: Any) -> None:
        # Initialize the Members module with a parent object.
        self._parent = parent

    def list_pending_team_invitations(self, team_slug: str, **kwargs: Any) -> Any:
        """
        List pending team invitations.

        :param team_slug: The slug of the team.
        :param per_page: The number of results per page (max 100).
        :param page: The page number of the results to fetch.
        :return: A list of pending team invitations.
        """
        endpoint = f"/orgs/{self._parent.org}/teams/{team_slug}/invitations"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self._parent.make_request("GET", endpoint, params=params)

    def list_team_members(self, team_slug: str, **kwargs: Any) -> Any:
        """
        List team members.

        :param team_slug: The slug of the team.
        :param role: The role of the members to list (e.g., "all", "member", "maintainer").
        :param per_page: The number of results per page (max 100).
        :param page: The page number of the results to fetch.
        :return: A list of team members.
        """
        endpoint = f"/orgs/{self._parent.org}/teams/{team_slug}/members"
        params: Dict[str, Any] = {
            "role": kwargs.get("role", "all"),
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self._parent.make_request("GET", endpoint, params=params)

    def get_team_membership(self, team_slug: str, username: str) -> Any:
        """
        Get team membership for a user.

        :param team_slug: The slug of the team.
        :param username: The username of the member.
        :return: The team membership details for the user.
        """
        endpoint = f"/orgs/{self._parent.org}/teams/{team_slug}/memberships/{username}"
        return self._parent.make_request("GET", endpoint)

    def add_or_update_team_membership(self, team_slug: str, username: str, **kwargs:Any) -> Any:
        """
        Add or update team membership for a user.

        :param team_slug: The slug of the team.
        :param username: The username of the member.
        :param role: The role of the member (e.g., "member", "maintainer"). Default is "member".
        :return: The updated team membership details for the user.
        """
        endpoint = f"/orgs/{self._parent.org}/teams/{team_slug}/memberships/{username}"
        data: Dict[str, Any] = {
          "role": kwargs.get("role", "member")
        }
        return self._parent.make_request("PUT", endpoint, json=data)

    def remove_team_membership(self, team_slug: str, username: str) -> Any:
        """
        Remove team membership for a user.

        :param team_slug: The slug of the team.
        :param username: The username of the member.
        :return: A boolean indicating whether the membership was successfully removed.
        """
        endpoint = f"/orgs/{self._parent.org}/teams/{team_slug}/memberships/{username}"
        return self._parent.make_request("DELETE", endpoint)


class Teams:
    """
    Teams module that contains teams.
    """
    def __init__(self, parent: Any) -> None:
        # Initialize the Teams module with a parent object.
        self._parent = parent

    def list_teams(self, **kwargs: Any) -> Any:
        """
        List teams in the organization.

        :param per_page: The number of results per page (max 100).
        :param page: The page number of the results to fetch.
        :return: A list of teams in the organization.
        """
        endpoint = f"/orgs/{self._parent.org}/teams"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self._parent.make_request("GET", endpoint, params=params)

    def create_team(self, name: str, **kwargs: Any) -> Any:
        """
        Create a new team in the organization.

        :param name: The name of the team.
        :param description: The description of the team.
        :param maintainers: A list of usernames to set as team maintainers.
        :param repo_names: A list of repository names to add the team to.
        :param privacy: The level of privacy for the team ("closed" or "secret").
        :param notification_setting: The notification setting for the team
          ("notifications_enabled" or "notifications_disabled").
        :param permission: The permission level for the team ("pull", "push", or "admin").
        :param parent_team_id: The ID of the parent team, if creating a child team
        :return: The created team details.
        """
        endpoint = f"/orgs/{self._parent.org}/teams"
        data: Dict[str, Any] = {
            "name": name,
            "description": kwargs.get("description", ""),
            "maintainers": kwargs.get("maintainers", []),
            "repo_names": kwargs.get("repo_names", []),
            "privacy": kwargs.get("privacy", "closed"),
            "notification_setting": kwargs.get("notification_setting", "notifications_enabled"),
            "permission": kwargs.get("permission", "pull"),
            "parent_team_id": kwargs.get("parent_team_id", None)
        }
        return self._parent.make_request("POST", endpoint, json=data)

    def get_team_by_name(self, team_slug: str) -> Any:
        """
        Get a team by its slug.

        :param team_slug: The slug of the team.
        :return: The team details.
        """
        endpoint = f"/orgs/{self._parent.org}/teams/{team_slug}"
        return self._parent.make_request("GET", endpoint)

    def update_team(self, team_slug: str, **kwargs: Any) -> Any:
        """
        Update a team's details.

        :param team_slug: The slug of the team.
        :param name: The new name of the team.
        :param description: The new description of the team.
        :param privacy: The new level of privacy for the team ("closed" or "secret").
        :param permission: The new permission level for the team ("pull", "push", or "admin").
        :return: The updated team details.
        """
        endpoint = f"/orgs/{self._parent.org}/teams/{team_slug}"
        data: Dict[str, Any] = {
            "name": kwargs.get("name"),
            "description": kwargs.get("description"),
            "privacy": kwargs.get("privacy"),
            "notification_setting": kwargs.get("notification_setting"),
            "permission": kwargs.get("permission"),
            "parent_team_id": kwargs.get("parent_team_id")
        }
        # Remove keys with None values
        data = {k: v for k, v in data.items() if v is not None}
        return self._parent.make_request("PATCH", endpoint, json=data)

    def delete_team(self, team_slug: str) -> Any:
        """
        Delete a team.

        :param team_slug: The slug of the team.
        :return: A boolean indicating whether the team was successfully deleted.
        """
        endpoint = f"/orgs/{self._parent.org}/teams/{team_slug}"
        return self._parent.make_request("DELETE", endpoint)

    def list_team_repositories(self, team_slug: str, **kwargs: Any) -> Any:
        """
        List repositories for a team.

        :param team_slug: The slug of the team.
        :param per_page: The number of results per page (max 100).
        :param page: The page number of the results to fetch.
        :return: A list of repositories for the team.
        """
        endpoint = f"/orgs/{self._parent.org}/teams/{team_slug}/repos"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self._parent.make_request("GET", endpoint, params=params)

    def check_team_permission_for_repository(self, team_slug: str, owner: str, repo: str) -> Any:
        """
        Check team permission for a repository.

        :param team_slug: The slug of the team.
        :param owner: The owner of the repository.
        :param repo: The name of the repository.
        :return: The permission details for the team on the repository.
        """
        endpoint = f"/orgs/{self._parent.org}/teams/{team_slug}/repos/{owner}/{repo}"
        return self._parent.make_request("GET", endpoint)

    def add_or_update_team_repository_permission(self, team_slug: str, owner: str,
                                                 repo: str, **kwargs: Any) -> Any:
        """
        Add or update team repository permission.

        :param team_slug: The slug of the team.
        :param owner: The owner of the repository.
        :param repo: The name of the repository.
        :param permission: The permission level for the team ("pull", "push", or "admin").
        :return: The updated permission details for the team on the repository.
        """
        endpoint = f"/orgs/{self._parent.org}/teams/{team_slug}/repos/{owner}/{repo}"
        data: Dict[str, Any] = {
            "permission": kwargs.get("permission", "pull")
        }
        return self._parent.make_request("PUT", endpoint, json=data)

    def remove_team_repository(self, team_slug: str, owner: str, repo: str) -> Any:
        """
        Remove a repository from a team.

        :param team_slug: The slug of the team.
        :param owner: The owner of the repository.
        :param repo: The name of the repository.
        :return: A boolean indicating whether the repository was successfully removed from the team.
        """
        endpoint = f"/orgs/{self._parent.org}/teams/{team_slug}/repos/{owner}/{repo}"
        return self._parent.make_request("DELETE", endpoint)

    def list_child_teams(self, team_slug: str, **kwargs: Any) -> Any:
        """
        List child teams of a team.

        :param team_slug: The slug of the parent team.
        :param per_page: The number of results per page (max 100).
        :param page: The page number of the results to fetch.
        :return: A list of child teams.
        """
        endpoint = f"/orgs/{self._parent.org}/teams/{team_slug}/teams"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self._parent.make_request("GET", endpoint, params=params)


class Team:
    """
    Team module that contains members and teams.
    """
    def __init__(self, parent: Any) -> None:
        # Initialize the Team module with a parent object.
        self.members = Members(parent)
        self.teams = Teams(parent)
