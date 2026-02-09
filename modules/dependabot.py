"""
Dependabot module for managing GitHub Dependabot settings and alerts.
"""

from typing import Any, Dict, List

class Alerts:
    """
    Manages Dependabot alerts for an organization or repository.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def list_org_dependabot_alerts(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Lists Dependabot alerts for the organization.

        :param state: (optional) Filter alerts by state (e.g., "open", "fixed", "dismissed").
        :param severity: (optional) Filter alerts by severity
            (e.g., "low", "medium", "high", "critical").
        :param ecosystem: (optional) Filter alerts by ecosystem (e.g., "npm", "pip", "maven").
        :param package: (optional) Filter alerts by package name.
        :param epss_percentage: (optional) Filter alerts by EPSS percentage.
        :param artifact_registry_url: (optional) Filter alerts by artifact registry URL.
        :param artifact_registry: (optional) Filter alerts by artifact registry type.
        :param has: (optional) Filter alerts that have specific attributes
            (e.g., "fix_available", "vulnerable_dependency").
        :param runtime_risk: (optional) Filter alerts by runtime risk level.
        :param scope: (optional) Filter alerts by scope (e.g., "repository", "organization").
        :param sort: (optional) Sort alerts by a specific field (e.g., "created_at", "updated_at").
        :param direction: (optional) Sort direction ("asc" or "desc").
        :param before: (optional) Cursor for pagination to get results before a specific point.
        :param after: (optional) Cursor for pagination to get results after a specific point.
        :param per_page: (optional) Number of results per page (default is 30).

        :return: Dictionary containing the list of Dependabot alerts.
        """
        endpoint = f"/orgs/{self.parent.org}/dependabot/alerts"
        params: Dict[str, Any] = {
            "state": kwargs.get("state"),
            "severity": kwargs.get("severity"),
            "ecosystem": kwargs.get("ecosystem"),
            "package": kwargs.get("package"),
            "epss_percetage": kwargs.get("epss_percentage"),
            "artifact_registry_url": kwargs.get("artifact_registry_url"),
            "artifact_registry": kwargs.get("artifact_registry"),
            "has": kwargs.get("has"),
            "runtime_risk": kwargs.get("runtime_risk"),
            "scope": kwargs.get("scope"),
            "sort": kwargs.get("sort"),
            "direction": kwargs.get("direction"),
            "before": kwargs.get("before"),
            "after": kwargs.get("after"),
            "per_page": kwargs.get("per_page", 30),
        }
        response = self.parent.make_request("GET", endpoint, params=params)
        return response

    def list_repository_dependabot_alerts(self, repo: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Lists Dependabot alerts for a specific repository.

        :param repo: Repository name.
        :param state: (optional) Filter alerts by state (e.g., "open", "fixed", "dismissed").
        :param severity: (optional) Filter alerts by severity
            (e.g., "low", "medium", "high", "critical").
        :param ecosystem: (optional) Filter alerts by ecosystem (e.g., "npm", "pip", "maven").
        :param package: (optional) Filter alerts by package name.
        :param epss_percentage: (optional) Filter alerts by EPSS percentage.
        :param artifact_registry_url: (optional) Filter alerts by artifact registry URL.
        :param artifact_registry: (optional) Filter alerts by artifact registry type.
        :param has: (optional) Filter alerts that have specific attributes
            (e.g., "fix_available", "vulnerable_dependency").
        :param scope: (optional) Filter alerts by scope (e.g., "repository", "organization").
        :param sort: (optional) Sort alerts by a specific field (e.g., "created_at", "updated_at").
        :param direction: (optional) Sort direction ("asc" or "desc").
        :param before: (optional) Cursor for pagination to get results before a specific point.
        :param after: (optional) Cursor for pagination to get results after a specific point.
        :param per_page: (optional) Number of results per page (default is 30).

        :return: Dictionary containing the list of Dependabot alerts for the repository.
        """
        endpoint = f"/repos/{self.parent.owner}/{repo}/dependabot/alerts"
        params: Dict[str, Any] = {
            "state": kwargs.get("state"),
            "severity": kwargs.get("severity"),
            "ecosystem": kwargs.get("ecosystem"),
            "package": kwargs.get("package"),
            "epss_percetage": kwargs.get("epss_percentage"),
            "artifact_registry_url": kwargs.get("artifact_registry_url"),
            "artifact_registry": kwargs.get("artifact_registry"),
            "has": kwargs.get("has"),
            "scope": kwargs.get("scope"),
            "sort": kwargs.get("sort"),
            "direction": kwargs.get("direction"),
            "before": kwargs.get("before"),
            "after": kwargs.get("after"),
            "per_page": kwargs.get("per_page", 30),
        }
        response = self.parent.make_request("GET", endpoint, params=params)
        return response

    def get_dependabot_alert(self, repo: str, alert_number: int) -> Dict[str, Any]:
        """
        Retrieves a specific Dependabot alert by its ID for a given repository.

        :param repo: Repository name.
        :param alert_id: ID of the Dependabot alert.

        :return: Dictionary containing the details of the specified Dependabot alert.
        """
        endpoint = f"/repos/{self.parent.owner}/{repo}/dependabot/alerts/{alert_number}"
        response = self.parent.make_request("GET", endpoint)
        return response

    def update_dependabot_alert(self, repo: str, alert_number: int,
                                state: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Updates the state of a specific Dependabot alert for a given repository.

        :param repo: Repository name.
        :param alert_id: ID of the Dependabot alert.
        :param state: New state for the alert ("open" or "dismissed").
        :param dismissal_reason: (optional) Reason for dismissing the alert.
        :param dismissal_message: (optional) Additional message for the dismissal.

        :return: Dictionary containing the updated details of the Dependabot alert.
        """
        endpoint = f"/repos/{self.parent.owner}/{repo}/dependabot/alerts/{alert_number}"
        payload: Dict[str, Any] = {
            "state": state
        }
        dismissal_reason = kwargs.get("dismissal_reason", "")
        dismissal_message = kwargs.get("dismissal_message", "")
        if state == "dismissed":
            payload["dismissal_reason"] = dismissal_reason
            if dismissal_message:
                payload["dismissal_message"] = dismissal_message

        response = self.parent.make_request("PATCH", endpoint, json=payload)
        return response


class RepositoryAccess:
    """
    Manages Dependabot repository access settings for an organization.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def list_org_repository_accessible_to_dependabot(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Lists repositories in the organization that are accessible to Dependabot.

        :param per_page: (optional) Number of results per page (default is 30).
        :param page: (optional) Page number of the results to fetch (default is 1).

        :return: Dictionary containing the list of repositories accessible to Dependabot.
        """
        endpoint = f"/orgs/{self.parent.org}/dependabot/repository-access"
        params = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        response = self.parent.make_request("GET", endpoint, params=params)
        return response

    def update_org_repository_accessible_to_dependabot(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Updates the list of repositories in the organization that are accessible to Dependabot.

        :param repository_ids_to_add: List of repository IDs to grant Dependabot access.
            eg. [123456, 789012]
        :param repository_ids_to_remove: List of repository IDs to revoke Dependabot access.
            eg. [345678, 901234]

        :return: Dictionary containing the updated list of repositories accessible to Dependabot.
        """
        endpoint = f"/orgs/{self.parent.org}/dependabot/repository-access"
        payload = {
            "repository_ids_to_add": kwargs.get("repository_ids_to_add", []),
            "repository_ids_to_remove": kwargs.get("repository_ids_to_remove", [])
        }
        response = self.parent.make_request("PATCH", endpoint, json=payload)
        return response

    def set_default_repository_access_level(self, default_level: str) -> Dict[str, Any]:
        """
        Sets the default repository access level for Dependabot in the organization.

        :param default_level: The default access level to set ("public" or "internal").

        :return: Dictionary containing the updated default repository access level.
        """
        endpoint = f"/orgs/{self.parent.org}/dependabot/repository-access/default"
        payload = {
            "default_level": default_level
        }
        response = self.parent.make_request("PUT", endpoint, json=payload)
        return response

class Secrets:

    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def list_org_secrets(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Lists Dependabot secrets for the organization.

        :param per_page: (optional) Number of results per page (default is 30).
        :param page: (optional) Page number of the results to fetch (default is 1).

        :return: Dictionary containing the list of Dependabot secrets.
        """
        endpoint = f"/orgs/{self.parent.org}/dependabot/secrets"
        params = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        response = self.parent.make_request("GET", endpoint, params=params)
        return response

    def get_org_public_key(self) -> Dict[str, Any]:
        """
        Retrieves the public key for encrypting Dependabot secrets in the organization.

        :return: Dictionary containing the public key details.
        """
        endpoint = f"/orgs/{self.parent.org}/dependabot/secrets/public-key"
        response = self.parent.make_request("GET", endpoint)
        return response

    def get_org_secret(self, secret_name: str) -> Dict[str, Any]:
        """
        Retrieves a specific Dependabot secret by its name for the organization.

        :param secret_name: Name of the Dependabot secret.

        :return: Dictionary containing the details of the specified Dependabot secret.
        """
        endpoint = f"/orgs/{self.parent.org}/dependabot/secrets/{secret_name}"
        response = self.parent.make_request("GET", endpoint)
        return response

    def create_or_update_org_secret(self, secret_name: str,
                                    visibility: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Creates or updates a Dependabot secret for the organization.

        :param secret_name: Name of the Dependabot secret.
        :param encrypted_value: Encrypted value of the secret.
        :param key_id: ID of the key used for encryption.
        :param visibility: Visibility level of the secret ("all", "private", or "selected").
        :param selected_repository_ids: (optional) List of repository IDs that can access the secret
            (required if visibility is "selected").

        :return: Dictionary containing the details of the created or updated Dependabot secret.
        """
        endpoint = f"/orgs/{self.parent.org}/dependabot/secrets/{secret_name}"
        payload: Dict[str, Any] = {
            "encrypted_value": kwargs.get("encrypted_value"),
            "key_id": kwargs.get("key_id"),
            "visibility": visibility,
        }
        if visibility == "selected":
            payload["selected_repository_ids"] = kwargs.get("selected_repository_ids", [])
        response = self.parent.make_request("PUT", endpoint, json=payload)
        return response

    def delete_org_secret(self, secret_name: str) -> None:
        """
        Deletes a specific Dependabot secret by its name for the organization.

        :param secret_name: Name of the Dependabot secret.
        """
        endpoint = f"/orgs/{self.parent.org}/dependabot/secrets/{secret_name}"
        self.parent.make_request("DELETE", endpoint)

    def list_selected_repositories_for_secret(self, secret_name: str,
                                          **kwargs: Any) -> Dict[str, Any]:
        """
        Lists repositories that have access to a specific Dependabot secret in the organization.

        :param secret_name: Name of the Dependabot secret.
        :param per_page: (optional) Number of results per page (default is 30).
        :param page: (optional) Page number of the results to fetch (default is 1).

        :return: Dictionary containing the list of repositories with access to the secret.
        """
        endpoint = f"/orgs/{self.parent.org}/dependabot/secrets/{secret_name}/repositories"
        params = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        response = self.parent.make_request("GET", endpoint, params=params)
        return response

    def set_selected_repositories_for_secret(self, secret_name: str,
                                         repository_ids: List[int]) -> Dict[str, Any]:
        """
        Sets the repositories that have access to a specific Dependabot secret in the organization.

        :param secret_name: Name of the Dependabot secret.
        :param repository_ids: List of repository IDs to grant access to the secret.
        :return: Dictionary containing the updated list of repositories with access to the secret.
        """
        endpoint = f"/orgs/{self.parent.org}/dependabot/secrets/{secret_name}/repositories"
        payload: Dict[str, Any] = {
            "repository_ids": repository_ids
        }
        response = self.parent.make_request("PUT", endpoint, json=payload)
        return response

    def add_selected_repository_for_secret(self, secret_name: str,
                                         repository_id: int) -> None:
        """
        Adds repositories that have access to a specific Dependabot secret in the organization.

        :param secret_name: Name of the Dependabot secret.
        :param repository_id: Repository ID to grant access to the secret.
        :return: Dictionary containing the updated list of repositories with access to the secret.
        """
        endpoint = f"/orgs/{self.parent.org}/dependabot/secrets/{secret_name}/repositories/{repository_id}"
        self.parent.make_request("PUT", endpoint)

    def remove_selected_repository_for_secret(self, secret_name: str,
                                            repository_id: int) -> None:
        """
        Removes a repository's access to a specific Dependabot secret in the organization.

        :param secret_name: Name of the Dependabot secret.
        :param repository_id: Repository ID to revoke access to the secret.
        """
        endpoint = f"/orgs/{self.parent.org}/dependabot/secrets/{secret_name}/repositories/{repository_id}"
        self.parent.make_request("DELETE", endpoint)

    def list_repository_secrets(self, repo: str,
                              **kwargs: Any) -> Dict[str, Any]:
        """
        Lists Dependabot secrets for a specific repository.

        :param repo: Repository name.
        :param per_page: (optional) Number of results per page (default is 30).
        :param page: (optional) Page number of the results to fetch (default is 1).

        :return: Dictionary containing the list of Dependabot secrets for the repository.
        """
        endpoint = f"/repos/{self.parent.owner}/{repo}/dependabot/secrets"
        params = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        response = self.parent.make_request("GET", endpoint, params=params)
        return response

    def get_repository_public_key(self, repo: str) -> Dict[str, Any]:
        """
        Retrieves the public key for encrypting Dependabot secrets in a specific repository.

        :param repo: Repository name.

        :return: Dictionary containing the public key details.
        """
        endpoint = f"/repos/{self.parent.owner}/{repo}/dependabot/secrets/public-key"
        response = self.parent.make_request("GET", endpoint)
        return response

    def get_repository_secret(self, repo: str, secret_name: str) -> Dict[str, Any]:
        """
        Retrieves a specific Dependabot secret by its name for a specific repository.

        :param repo: Repository name.
        :param secret_name: Name of the Dependabot secret.

        :return: Dictionary containing the details of the specified Dependabot secret.
        """
        endpoint = f"/repos/{self.parent.owner}/{repo}/dependabot/secrets/{secret_name}"
        response = self.parent.make_request("GET", endpoint)
        return response

    def create_or_update_repository_secret(self, repo: str, secret_name: str,
                                    **kwargs: Any) -> Dict[str, Any]:
        """
        Creates or updates a Dependabot secret for a specific repository.

        :param repo: Repository name.
        :param secret_name: Name of the Dependabot secret.
        :param encrypted_value: Encrypted value of the secret. (optional)
        :param key_id: ID of the key used for encryption. (optional)

        :return: Dictionary containing the details of the created or updated Dependabot secret.
        """
        endpoint = f"/repos/{self.parent.owner}/{repo}/dependabot/secrets/{secret_name}"
        payload: Dict[str, Any] = {
            "encrypted_value": kwargs.get("encrypted_value"),
            "key_id": kwargs.get("key_id")
        }
        response = self.parent.make_request("PUT", endpoint, json=payload)
        return response

    def delete_repository_secret(self, repo: str, secret_name: str) -> None:
        """
        Deletes a specific Dependabot secret by its name for a specific repository.

        :param repo: Repository name.
        :param secret_name: Name of the Dependabot secret.
        """
        endpoint = f"/repos/{self.parent.owner}/{repo}/dependabot/secrets/{secret_name}"
        self.parent.make_request("DELETE", endpoint)


class Dependabot:
    """
    Dependabot module for managing GitHub Dependabot settings and alerts.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

        # Initialize submodules
        self.alerts = Alerts(parent)
        self.repository_access = RepositoryAccess(parent)
        self.secrets = Secrets(parent)