"""
Apps Submodule
"""
from typing import Any, Dict

class GitHubApps:
    """
    GitHub Apps Submodule

    Attributes:
        parent: The parent object that contains the make_request method.
    """
    def __init__(self, parent: Any):
        self.parent = parent

    def get_authenticated_app(self) -> Dict[str, Any]:
        """
        Returns the GitHub App associated with the authentication credentials used.
        """
        endpoint = "/app"
        return self.parent.make_request("GET", endpoint)

    def create_app_from_manifest(self, code: str) -> Dict[str, Any]:
        """
        Creates a GitHub App from a manifest code.

        :param code: The code received from the GitHub App creation flow.
        :return: JSON response containing the created app details.
        """
        endpoint = f"/app-manifests/{code}/conversions"
        return self.parent.make_request("POST", endpoint)

    def list_installation_requests_for_authenticated_app(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Lists installation requests for the authenticated GitHub App.

        :param per_page: Number of results per page (max 100).
        :param page: Page number of the results to fetch.
        :return: JSON response containing the list of installation requests.
        """
        endpoint = "/app/installations-requests"
        params = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def list_installations_for_authenticated_app(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Lists installations for the authenticated GitHub App.

        param per_page: Number of results per page (max 100).
        param page: Page number of the results to fetch.
        param since: Only show installations updated at or after this time (ISO 8601 format).
        param outdated: If true, only show installations that are outdated.
        :return: JSON response containing the list of installations.
        """
        endpoint = "/app/installations"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1),
            "since": kwargs.get("since", None),
            "outdated": kwargs.get("outdated", None)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def get_an_installation_for_authenticated_app(self, installation_id: int) -> Dict[str, Any]:
        """
        Gets a specific installation for the authenticated GitHub App.

        :param installation_id: The ID of the installation to retrieve.
        :return: JSON response containing the installation details.
        """
        endpoint = f"/app/installations/{installation_id}"
        return self.parent.make_request("GET", endpoint)

    def delete_an_installation_for_authenticated_app(self, installation_id: int) -> None:
        """
        Deletes a specific installation for the authenticated GitHub App.

        :param installation_id: The ID of the installation to delete.
        :return: None
        """
        endpoint = f"/app/installations/{installation_id}"
        self.parent.make_request("DELETE", endpoint)

    def create_installation_access_token(
            self,
            installation_id: int, 
            **kwargs: Any) -> Dict[str, Any]:
        """
        Creates an installation access token for a specific installation of the GitHub App.

        :param installation_id: The ID of the installation.
        :param permissions: (optional) A dictionary specifying permissions for the token.
        :param repositories: (optional) A list of repository names to limit the token's access.
        :param repository_ids: (optional) A list of repository IDs to limit the token's access.
        :return: JSON response containing the access token details.
        """
        endpoint = f"/app/installations/{installation_id}/access_tokens"
        data: Dict[str, Any] = {
            "permissions": kwargs.get("permissions", {}),
            "repositories": kwargs.get("repositories", []),
            "repository_ids": kwargs.get("repository_ids", [])
        }
        return self.parent.make_request("POST", endpoint, json=data)

    def suspend_installation(self, installation_id: int) -> None:
        """
        Suspends a specific installation of the GitHub App.

        :param installation_id: The ID of the installation to suspend.
        :return: None
        """
        endpoint = f"/app/installations/{installation_id}/suspend"
        self.parent.make_request("PUT", endpoint)

    def unsuspend_installation(self, installation_id: int) -> None:
        """
        Unsuspends a specific installation of the GitHub App.

        :param installation_id: The ID of the installation to unsuspend.
        :return: None
        """
        endpoint = f"/app/installations/{installation_id}/unsuspend"
        self.parent.make_request("PUT", endpoint)

    def create_scoped_access_token(self, client_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Creates a scoped token for a specific installation of the GitHub App.

        :param client_id: The ID of the installation.
        :param access_token: The access token of the installation.
        :param target: The target type for the scoped token (e.g., "repository", "organization").
        :param target_id: The ID of the target (repository or organization).
        :param repositories: (optional) A list of repository names to limit the token's access.
        :param repository_ids: (optional) A list of repository IDs to limit the token's access.
        :param permissions: (optional) A dictionary specifying permissions for the token.
        :return: JSON response containing the scoped access token details.
        """
        endpoint = f"/applications/{client_id}/token/scoped"
        data: Dict[str, Any] = {
            "access_token": kwargs.get("access_token", ""),
            "target": kwargs.get("target", ""),
            "target_id": kwargs.get("target_id", 0),
            "repositories": kwargs.get("repositories", []),
            "repository_ids": kwargs.get("repository_ids", []),
            "permissions": kwargs.get("permissions", "")
        }
        return self.parent.make_request("POST", endpoint, json=data)

    def get_an_app(self, app_slug: str) -> Dict[str, Any]:
        """
        Gets a GitHub App by its slug.

        :param app_slug: The slug of the GitHub App.
        :return: JSON response containing the app details.
        """
        endpoint = f"/apps/{app_slug}"
        return self.parent.make_request("GET", endpoint)

    def get_org_installation_for_authenticated_app(self) -> Dict[str, Any]:
        """
        Gets the installation of the authenticated GitHub App for a specific organization.

        :return: JSON response containing the installation details.
        """
        endpoint = f"/orgs/{self.parent.org}/installation"
        return self.parent.make_request("GET", endpoint)

    def get_repo_installation_for_authenticated_app(self, repo: str) -> Dict[str, Any]:
        """
        Gets the installation of the authenticated GitHub App for a specific repository.

        :param repo: The repository name.
        :return: JSON response containing the installation details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/installation"
        return self.parent.make_request("GET", endpoint)

    def get_user_installation_for_authenticated_app(self) -> Dict[str, Any]:
        """
        Gets the installation of the authenticated GitHub App for a specific user.

        :return: JSON response containing the installation details.
        """
        endpoint = f"/users/{self.parent.username}/installation"
        return self.parent.make_request("GET", endpoint)


class Installations:
    """
    Installations Submodule

    Attributes:
        parent: The parent object that contains the make_request method.
    """
    def __init__(self, parent: Any):
        self.parent = parent

    def list_repositories_accessible_to_app_installation(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Lists repositories accessible to a specific installation of the GitHub App.

        :param installation_id: The ID of the installation.
        :param per_page: Number of results per page (max 100).
        :param page: Page number of the results to fetch.
        :return: JSON response containing the list of accessible repositories.
        """
        endpoint = "/installation/repositories"
        params = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def revoke_installation_access_token(self) -> None:
        """
        Revokes the installation access token for the authenticated installation.

        :return: None
        """
        endpoint = "/installation/token"
        self.parent.make_request("DELETE", endpoint)

    def list_app_installation_user_access_token(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Lists app installation user access tokens for the authenticated installation.

        :param per_page: Number of results per page (max 100).
        :param page: Page number of the results to fetch.
        :return: JSON response containing the list of app installation user access tokens.
        """
        endpoint = "user/installations"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def list_repositories_accessible_to_user_access_token(
        self,
        installation_id: int,
        **kwargs: Any
        ) -> Dict[str, Any]:
        """
        Lists repositories accessible to a user access token for a specific installation.

        :param installation_id: The ID of the installation.
        :param per_page: Number of results per page (max 100).
        :param page: Page number of the results to fetch.
        :return: JSON response containing the list of accessible repositories.
        """
        endpoint = f"/user/installations/{installation_id}/repositories"
        params = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def add_repository_to_installation(self, installation_id: int, repo_id: int) -> None:
        """
        Adds a repository to a specific installation of the GitHub App.

        :param installation_id: The ID of the installation.
        :param repo_id: The ID of the repository to add.
        :return: None
        """
        endpoint = f"/installations/{installation_id}/repositories/{repo_id}"
        self.parent.make_request("PUT", endpoint)

    def remove_repository_from_installation(self, installation_id: int, repo_id: int) -> None:
        """
        Removes a repository from a specific installation of the GitHub App.

        :param installation_id: The ID of the installation.
        :param repo_id: The ID of the repository to remove.
        :return: None
        """
        endpoint = f"/installations/{installation_id}/repositories/{repo_id}"
        self.parent.make_request("DELETE", endpoint)

class Oauth:
    """
    Oauth Submodule

    Attributes:
        parent: The parent object that contains the make_request method.
    """
    def __init__(self, parent: Any):
        self.parent = parent

    def delete_app_authorization(self, client_id: str, access_token: str) -> None:
        """
        Deletes a GitHub App authorization.

        :param client_id: The client ID of the GitHub App.
        :param access_token: The access token to delete.
        :return: None
        """
        endpoint = f"/applications/{client_id}/grant"
        data = {
            "access_token": access_token
        }
        self.parent.make_request("DELETE", endpoint, json=data)

    def check_app_token(self, client_id: str, access_token: str) -> Dict[str, Any]:
        """
        Checks a GitHub App token.

        :param client_id: The client ID of the GitHub App.
        :param access_token: The access token to check.
        :return: JSON response containing the token details.
        """
        endpoint = f"/applications/{client_id}/token"
        data = {
            "access_token": access_token
        }
        return self.parent.make_request("POST", endpoint, json=data)

    def reset_app_token(self, client_id: str, access_token: str) -> Dict[str, Any]:
        """
        Resets a GitHub App token.

        :param client_id: The client ID of the GitHub App.
        :param client_secret: The client secret of the GitHub App.
        :param access_token: The access token to reset.
        :return: JSON response containing the new token details.
        """
        endpoint = f"/applications/{client_id}/token"
        data = {
            "access_token": access_token,
        }
        return self.parent.make_request("PATCH", endpoint, json=data)

    def delete_app_token(self, client_id: str, access_token: str) -> None:
        """
        Deletes a GitHub App token.

        :param client_id: The client ID of the GitHub App.
        :param access_token: The access token to delete.
        :return: None
        """
        endpoint = f"/applications/{client_id}/token"
        data = {
            "access_token": access_token
        }
        self.parent.make_request("DELETE", endpoint, json=data)

class Webhook:
    """
    Webhook Submodule

    Attributes:
        parent: The parent object that contains the make_request method.
    """
    def __init__(self, parent: Any):
        self.parent = parent

    def get_webhook_config_for_app(self) -> Dict[str, Any]:
        """
        Gets a webhook configuration for a GitHub App.

        :return: JSON response containing the webhook configuration details.
        """
        endpoint = "/app/hook/config"
        return self.parent.make_request("GET", endpoint)

    def update_webhook_config_for_app(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Updates a webhook configuration for a GitHub App.

        :param url: The URL to which the payloads will be delivered.
        :param content_type: The media type used to serialize the payloads (e.g., "json").
        :param secret: The secret used to generate the HMAC hex digest value for delivery signature headers.
        :param insecure_ssl: Whether to disable SSL verification for the webhook URL (0 or 1).
        :return: JSON response containing the updated webhook configuration details.
        """
        endpoint = "/app/hook/config"
        data: Dict[str, Any] = {
            "url": kwargs.get("url", ""),
            "content_type": kwargs.get("content_type", "json"),
            "secret": kwargs.get("secret", ""),
            "insecure_ssl": kwargs.get("insecure_ssl", "0")
        }
        return self.parent.make_request("PATCH", endpoint, json=data)

    def list_webhook_deliveries_for_app(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Lists webhook deliveries for a GitHub App.

        :param per_page: Number of results per page (max 100).
        :param cursor: Cursor for pagination.
        :return: JSON response containing the list of webhook deliveries.
        """
        endpoint = "/app/hook/deliveries"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "cursor": kwargs.get("cursor", None)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def get_a_webhook_delivery_for_app(self, delivery_id: int) -> Dict[str, Any]:
        """
        Gets a specific webhook delivery for a GitHub App.

        :param delivery_id: The ID of the webhook delivery to retrieve.
        :return: JSON response containing the webhook delivery details.
        """
        endpoint = f"/app/hook/deliveries/{delivery_id}"
        return self.parent.make_request("GET", endpoint)

    def redeliver_webhook_delivery_for_app(self, delivery_id: int) -> None:
        """
        Redelivers a specific webhook delivery for a GitHub App.

        :param delivery_id: The ID of the webhook delivery to redeliver.
        :return: None
        """
        endpoint = f"/app/hook/deliveries/{delivery_id}/attempts"
        self.parent.make_request("POST", endpoint)
class Apps:
    """
    Apps Submodule

    Attributes:
        parent: The parent object that contains the make_request method.
    """
    def __init__(self, parent: Any):
        self.parent = parent

        # Instantiate Sub-Submodules
        self.github_apps = GitHubApps(parent)
        self.installations = Installations(parent)
        self.oauth = Oauth(parent)
        self.webhook = Webhook(parent)
