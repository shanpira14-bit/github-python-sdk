"""
Copilot module for managing GitHub Copilot settings and seat assignments.
"""
from typing import Any, Dict

class Metrics:
    """
    Manages Copilot metrics for an organization and its teams.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def get_org_metrics(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Get Copilot metrics for the organization.
        :param since: (optional) Start date for metrics in ISO 8601 format.
            e.g., 2023-01-01T00:00:00Z
        :param until: (optional) End date for metrics in ISO 8601 format.
            e.g., 2023-01-31T23:59:59Z
        :param per_page: (optional) Number of results per page (default is 100).
        :param page: (optional) Page number of the results to fetch (default is 1).
        :return: Dictionary containing the Copilot metrics.
        """
        endpoint = f"/orgs/{self.parent.org}/copilot/metrics"
        params = {
            "since": kwargs.get("since", ""),
            "until": kwargs.get("until", ""),
            "per_page": kwargs.get("per_page", 100),
            "page": kwargs.get("page", 1)
        }
        response = self.parent.make_request("GET", endpoint, params=params)
        return response

    def get_team_metrics(self, team_slug: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Get Copilot metrics for a specific team.
        :param team_id: ID of the team.
        :param since: (optional) Start date for metrics in ISO 8601 format.
            e.g., 2023-01-01T00:00:00Z
        :param until: (optional) End date for metrics in ISO 8601 format.
            e.g., 2023-01-31T23:59:59Z
        :param per_page: (optional) Number of results per page (default is 100).
        :param page: (optional) Page number of the results to fetch (default is 1).
        :return: Dictionary containing the Copilot metrics for the team.
        """
        endpoint = f"/teams/{team_slug}/copilot/metrics"
        params = {
            "since": kwargs.get("since", ""),
            "until": kwargs.get("until", ""),
            "per_page": kwargs.get("per_page", 100),
            "page": kwargs.get("page", 1)
        }
        response = self.parent.make_request("GET", endpoint, params=params)
        return response


class UserManagement:
    """
    Manages Copilot seat assignments for users and teams within an organization.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def get_org_seat_info_settings(self) -> Dict[str, Any]:
        """
        Gets information about an organization's Copilot subscription,
        including seat breakdown and feature policies.

        :return: Dictionary containing the organization's Copilot seat info and settings.
        """
        endpoint = f"/orgs/{self.parent.org}/copilot/billing"
        response = self.parent.make_request("GET", endpoint)
        return response

    def list_org_seat_assignments(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Lists all Copilot seat assignments for an organization.

        :param per_page: (optional) Number of results per page (default is 100).
        :param page: (optional) Page number of the results to fetch (default is 1).
        :return: Dictionary containing the list of Copilot seat assignments.
        """
        endpoint = f"/orgs/{self.parent.org}/copilot/billing/seats"
        params = {
            "per_page": kwargs.get("per_page", 100),
            "page": kwargs.get("page", 1)
        }
        response = self.parent.make_request("GET", endpoint, params=params)
        return response

    def add_teams_seat_assignments(self, selected_teams: list[int]) -> Dict[str, Any]:
        """
        Assigns Copilot seats to specified teams within the organization.

        :param selected_teams: List of team Slugs to assign Copilot seats to.
            e.g., ["team-slug-1", "team-slug-2"]
        :return: Dictionary containing the result of the seat assignment operation.
        """
        endpoint = f"/orgs/{self.parent.org}/copilot/billing/selected_teams"
        json_data = {
            "selected_teams": selected_teams
        }
        response = self.parent.make_request("POST", endpoint, json=json_data)
        return response

    def remove_teams_seat_assignments(self, selected_teams: list[int]) -> Dict[str, Any]:
        """
        Removes Copilot seat assignments from specified teams within the organization.

        :param selected_teams: List of team Slugs to remove Copilot seats from.
            e.g., ["team-slug-1", "team-slug-2"]
        :return: Dictionary containing the result of the seat removal operation.
        """
        endpoint = f"/orgs/{self.parent.org}/copilot/billing/selected_teams"
        json_data = {
            "selected_teams": selected_teams
        }
        response = self.parent.make_request("DELETE", endpoint, json=json_data)
        return response

    def add_users_seat_assignments(self, selected_usernames: list[str]) -> Dict[str, Any]:
        """
        Assigns Copilot seats to specified users within the organization.

        :param selected_usernames: List of usernames to assign Copilot seats to.
            e.g., ["username1", "username2"]
        :return: Dictionary containing the result of the seat assignment operation.
        """
        endpoint = f"/orgs/{self.parent.org}/copilot/billing/selected_users"
        json_data = {
            "selected_usernames": selected_usernames
        }
        response = self.parent.make_request("POST", endpoint, json=json_data)
        return response

    def remove_users_seat_assignments(self, selected_usernames: list[str]) -> Dict[str, Any]:
        """
        Removes Copilot seat assignments from specified users within the organization.

        :param selected_usernames: List of usernames to remove Copilot seats from.
            e.g., ["username1", "username2"]
        :return: Dictionary containing the result of the seat removal operation.
        """
        endpoint = f"/orgs/{self.parent.org}/copilot/billing/selected_users"
        json_data = {
            "selected_usernames": selected_usernames
        }
        response = self.parent.make_request("DELETE", endpoint, json=json_data)
        return response

    def seat_details_for_user(self, username: str) -> Dict[str, Any]:
        """
        Gets Copilot seat details for a specific user within the organization.

        :param username: Username of the user to get seat details for.
        :return: Dictionary containing the Copilot seat details for the user.
        """
        endpoint = f"/orgs/{self.parent.org}/members/{username}/copilot"
        response = self.parent.make_request("GET", endpoint)
        return response


class Copilot:
    """
    Copilot module for managing GitHub Copilot settings and seat assignments.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

        self.metrics = Metrics(parent)
        self.user_management = UserManagement(parent)