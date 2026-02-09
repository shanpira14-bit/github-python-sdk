"""
Private Registries Module
"""
from typing import Any, Dict

class PrivateRegistries:
    """
    A class to manage private registries.
    """
    def __init__(self, parent: Any) -> None:
        self._parent = parent

    def list_registries(self) -> Any:
        """
        List all private registries.

        :param per_page: Number of registries to return per page.
        :param page: Page number to return.
        :return: A list of private registries.
        """
        endpoint= f"/orgs/{self._parent.org}/private-registries"
        return self._parent.make_request("GET", endpoint)

    def create_private_registry(self, registry_type: str, url: str, encrypted_value: str,
                                key_id: str, visibility: str, **kwargs: Any) -> Any:
        """
        Create a new private registry.

        :param registry_type: Type of the registry (e.g., "docker", "maven").
        :param url: (Optional) URL of the registry.
        :param username: (Optional) Username for the registry.
        :param replaces_base: (Optional) Whether to replace the base registry (default is False).
        :param encrypted_value: Encrypted password or token for the registry.
        :param key_id: Key ID used for encryption.
        :param visibility: Visibility of the registry ("all", "private", "selected").
        :param selected_repositories: (Optional) List of repository IDs if visibility is "selected".
        :return: The created private registry details.
        """
        endpoint = f"/orgs/{self._parent.org}/private-registries"
        data: Dict[str, Any] = {
            "registry_type": registry_type,
            "url": url,
            "username": kwargs.get("username"),
            "replaces_base": kwargs.get("replaces_base", False),
            "encrypted_value": encrypted_value,
            "key_id": key_id,
            "visibility": visibility,
            "selected_repositories": kwargs.get("selected_repositories", [])
        }
        return self._parent.make_request("POST", endpoint, json=data)

    def get_private_registry_public_key(self) -> Any:
        """
        Get the public key for encrypting private registry credentials.

        :return: The public key details.
        """
        endpoint = f"/orgs/{self._parent.org}/private-registries/public-key"
        return self._parent.make_request("GET", endpoint)

    def get_private_registry(self, registry_name: str) -> Any:
        """
        Get details of a specific private registry.

        :param registry_id: ID of the private registry.
        :return: The private registry details.
        """
        endpoint = f"/orgs/{self._parent.org}/private-registries/{registry_name}"
        return self._parent.make_request("GET", endpoint)

    def update_private_registry(self, registry_name: str, visibility: str, **kwargs: Any) -> Any:
        """
        Update an existing private registry.

        :param registry_id: ID of the private registry.
        :param url: (Optional) URL of the registry.
        :param username: (Optional) Username for the registry.
        :param replaces_base: (Optional) Whether to replace the base registry (default is False).
        :param encrypted_value: (Optional) Encrypted password or token for the registry.
        :param key_id: (Optional) Key ID used for encryption.
        :param visibility: Visibility of the registry ("all", "private", "selected").
        :param selected_repositories: (Optional) List of repository IDs if visibility is "selected".
        :return: The updated private registry details.
        """
        endpoint = f"/orgs/{self._parent.org}/private-registries/{registry_name}"
        data: Dict[str, Any] = {
            "registry_name": registry_name,
            "url": kwargs.get("url"),
            "username": kwargs.get("username"),
            "replaces_base": kwargs.get("replaces_base", False),
            "encrypted_value": kwargs.get("encrypted_value"),
            "key_id": kwargs.get("key_id"),
            "visibility": visibility,
            "selected_repositories": kwargs.get("selected_repositories", [])
        }
        return self._parent.make_request("PATCH", endpoint, json=data)

    def delete_private_registry(self, registry_name: str) -> Any:
        """
        Delete a specific private registry.

        :param registry_id: ID of the private registry.
        :return: Response from the delete operation.
        """
        endpoint = f"/orgs/{self._parent.org}/private-registries/{registry_name}"
        return self._parent.make_request("DELETE", endpoint)
