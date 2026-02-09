"""
Module for handling GitHub Packages API endpoints.
"""
from typing import Any, Dict

class Packages:
    """
    Handles GitHub Packages API endpoints.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def list_organization_packages(self, package_type: str, **kwargs: Any) -> Any:
        """
        Lists packages for an organization.

        :param package_type: The type of package (e.g., "npm", "maven").
        :param visibility: The visibility of the packages (optional).
        :param page: Page number for pagination (optional).
        :param per_page: Number of results per page (optional).
        :return: Response from the API.
        """
        url = f"/orgs/{self.parent.org}/packages"
        params: Dict[str, Any] = {
            "package_type": package_type,
            "visibility": kwargs.get("visibility"),
            "page": kwargs.get("page"),
            "per_page": kwargs.get("per_page"),
        }
        return self.parent.make_request("GET", url, params=params)

    def get_organization_package(self, package_type: str, package_name: str) -> Any:
        """
        Gets a specific package for an organization.

        :param package_type: The type of package (e.g., "npm", "maven").
        :param package_name: The name of the package.
        :return: Response from the API.
        """
        url = f"/orgs/{self.parent.org}/packages/{package_type}/{package_name}"
        return self.parent.make_request("GET", url)

    def delete_organization_package(self, package_type: str, package_name: str) -> Any:
        """
        Deletes a specific package for an organization.

        :param package_type: The type of package (e.g., "npm", "maven").
        :param package_name: The name of the package.
        :return: Response from the API.
        """
        url = f"/orgs/{self.parent.org}/packages/{package_type}/{package_name}"
        return self.parent.make_request("DELETE", url)

    def restore_organization_package(self, package_type: str, package_name: str,
                                     **kwargs: Any) -> Any:
        """
        Restores a specific deleted package for an organization.

        :param package_type: The type of package (e.g., "npm", "maven").
        :param package_name: The name of the package.
        :param token: The restore token (optional).
        :return: Response from the API.
        """
        url = f"/orgs/{self.parent.org}/packages/{package_type}/{package_name}/restore"
        params: Dict[str, Any] = {
            "token": kwargs.get("token", "")
        }
        return self.parent.make_request("POST", url, params=params)

    def list_package_versions(self, package_type: str, package_name: str, **kwargs: Any) -> Any:
        """
        Lists versions of a specific package for an organization.

        :param package_type: The type of package (e.g., "npm", "maven").
        :param package_name: The name of the package.
        :param page: Page number for pagination (optional).
        :param per_page: Number of results per page (optional).
        :param state: The state of the package versions (optional).
        :return: Response from the API.
        """
        url = f"/orgs/{self.parent.org}/packages/{package_type}/{package_name}/versions"
        params: Dict[str, Any] = {
            "page": kwargs.get("page"),
            "per_page": kwargs.get("per_page"),
            "state": kwargs.get("state"),
        }
        return self.parent.make_request("GET", url, params=params)

    def get_package_version(self, package_type: str, package_name: str,
                            package_version_id: int) -> Any:
        """
        Gets a specific version of a package for an organization.

        :param package_type: The type of package (e.g., "npm", "maven").
        :param package_name: The name of the package.
        :param package_version_id: The ID of the package version.
        :return: Response from the API.
        """
        url = f"/orgs/{self.parent.org}/packages/{package_type}/{package_name}/versions/{package_version_id}"
        return self.parent.make_request("GET", url)

    def delete_package_version(self, package_type: str, package_name: str,
                               package_version_id: int) -> Any:
        """
        Deletes a specific version of a package for an organization.

        :param package_type: The type of package (e.g., "npm", "maven").
        :param package_name: The name of the package.
        :param package_version_id: The ID of the package version.
        :return: Response from the API.
        """
        url = f"/orgs/{self.parent.org}/packages/{package_type}/{package_name}/versions/{package_version_id}"
        return self.parent.make_request("DELETE", url)

    def restore_package_version(self, package_type: str, package_name: str,
                                package_version_id: int, **kwargs: Any) -> Any:
        """
        Restores a specific deleted version of a package for an organization.

        :param package_type: The type of package (e.g., "npm", "maven").
        :param package_name: The name of the package.
        :param package_version_id: The ID of the package version.
        :return: Response from the API.
        """
        url = f"/orgs/{self.parent.org}/packages/{package_type}/{package_name}/versions/{package_version_id}/restore"
        return self.parent.make_request("POST", url)

    def list_packages_for_authenticated_user(self, package_type: str, **kwargs: Any) -> Any:
        """
        Lists packages for the authenticated user.

        :param package_type: The type of package (e.g., "npm", "maven").
        :param visibility: The visibility of the packages (optional).
        :param page: Page number for pagination (optional).
        :param per_page: Number of results per page (optional).
        :return: Response from the API.
        """
        url = "/user/packages"
        params: Dict[str, Any] = {
            "package_type": package_type,
            "visibility": kwargs.get("visibility"),
            "page": kwargs.get("page"),
            "per_page": kwargs.get("per_page"),
        }
        return self.parent.make_request("GET", url, params=params)

    def get_authenticated_user_package(self, package_type: str, package_name: str) -> Any:
        """
        Gets a specific package for the authenticated user.

        :param package_type: The type of package (e.g., "npm", "maven").
        :param package_name: The name of the package.
        :return: Response from the API.
        """
        url = f"/user/packages/{package_type}/{package_name}"
        return self.parent.make_request("GET", url)

    def delete_authenticated_user_package(self, package_type: str, package_name: str) -> Any:
        """
        Deletes a specific package for the authenticated user.

        :param package_type: The type of package (e.g., "npm", "maven").
        :param package_name: The name of the package.
        :return: Response from the API.
        """
        url = f"/user/packages/{package_type}/{package_name}"
        return self.parent.make_request("DELETE", url)

    def restore_authenticated_user_package(self, package_type: str, package_name: str,
                                           **kwargs: Any) -> Any:
        """
        Restores a specific deleted package for the authenticated user.

        :param package_type: The type of package (e.g., "npm", "maven").
        :param package_name: The name of the package.
        :param token: The restore token (optional).
        :return: Response from the API.
        """
        url = f"/user/packages/{package_type}/{package_name}/restore"
        params: Dict[str, Any] = {
            "token": kwargs.get("token", "")
        }
        return self.parent.make_request("POST", url, params=params)

    def list_authenticated_user_package_versions(self, package_type: str, package_name: str,
                                                 **kwargs: Any) -> Any:
        """
        Lists versions of a specific package for the authenticated user.

        :param package_type: The type of package (e.g., "npm", "maven").
        :param package_name: The name of the package.
        :param page: Page number for pagination (optional).
        :param per_page: Number of results per page (optional).
        :param state: The state of the package versions (optional).
        :return: Response from the API.
        """
        url = f"/user/packages/{package_type}/{package_name}/versions"
        params: Dict[str, Any] = {
            "page": kwargs.get("page"),
            "per_page": kwargs.get("per_page"),
            "state": kwargs.get("state"),
        }
        return self.parent.make_request("GET", url, params=params)


    def get_authenticated_user_package_version(self, package_type: str, package_name: str,
                                               package_version_id: int) -> Any:
        """
        Gets a specific version of a package for the authenticated user.

        :param package_type: The type of package (e.g., "npm", "maven").
        :param package_name: The name of the package.
        :param package_version_id: The ID of the package version.
        :return: Response from the API.
        """
        url = f"/user/packages/{package_type}/{package_name}/versions/{package_version_id}"
        return self.parent.make_request("GET", url)

    def delete_authenticated_user_package_version(self, package_type: str, package_name: str,
                                                  package_version_id: int) -> Any:
        """
        Deletes a specific version of a package for the authenticated user.

        :param package_type: The type of package (e.g., "npm", "maven").
        :param package_name: The name of the package.
        :param package_version_id: The ID of the package version.
        :return: Response from the API.
        """
        url = f"/user/packages/{package_type}/{package_name}/versions/{package_version_id}"
        return self.parent.make_request("DELETE", url)

    def restore_authenticated_user_package_version(self, package_type: str, package_name: str,
                                                   package_version_id: int, **kwargs: Any) -> Any:
        """
        Restores a specific deleted version of a package for the authenticated user.

        :param package_type: The type of package (e.g., "npm", "maven").
        :param package_name: The name of the package.
        :param package_version_id: The ID of the package version.
        :return: Response from the API.
        """
        url = f"/user/packages/{package_type}/{package_name}/versions/{package_version_id}/restore"
        return self.parent.make_request("POST", url)

    def list_packages_for_user(self, package_type: str,
                               **kwargs: Any) -> Any:
        """
        Lists packages for a specified user.

        :param username: The username of the user.
        :param package_type: The type of package (e.g., "npm", "maven").
        :param visibility: The visibility of the packages (optional).
        :param page: Page number for pagination (optional).
        :param per_page: Number of results per page (optional).
        :return: Response from the API.
        """
        url = f"/users/{self.parent.username}/packages"
        params: Dict[str, Any] = {
            "package_type": package_type,
            "visibility": kwargs.get("visibility"),
            "page": kwargs.get("page"),
            "per_page": kwargs.get("per_page"),
        }
        return self.parent.make_request("GET", url, params=params)

    def get_user_package(self, package_type: str, package_name: str) -> Any:
        """
        Gets a specific package for a specified user.

        :param username: The username of the user.
        :param package_type: The type of package (e.g., "npm", "maven").
        :param package_name: The name of the package.
        :return: Response from the API.
        """
        url = f"/users/{self.parent.username}/packages/{package_type}/{package_name}"
        return self.parent.make_request("GET", url)

    def delete_package_for_user(self, package_type: str,
                             package_name: str) -> Any:
        """
        Deletes a specific package for a specified user.

        :param username: The username of the user.
        :param package_type: The type of package (e.g., "npm", "maven").
        :param package_name: The name of the package.
        :return: Response from the API.
        """
        url = f"/users/{self.parent.username}/packages/{package_type}/{package_name}"
        return self.parent.make_request("DELETE", url)

    def restore_package_for_user(self, package_type: str,
                                 package_name: str, **kwargs: Any) -> Any:
        """
        Restores a specific deleted package for a specified user.

        :param username: The username of the user.
        :param package_type: The type of package (e.g., "npm", "maven").
        :param package_name: The name of the package.
        :param token: The restore token (optional).
        :return: Response from the API.
        """
        url = f"/users/{self.parent.username}/packages/{package_type}/{package_name}/restore"
        params: Dict[str, Any] = {
            "token": kwargs.get("token", "")
        }
        return self.parent.make_request("POST", url, params=params)

    def list_user_package_versions(self, package_type: str,
                                   package_name: str, **kwargs: Any) -> Any:
        """
        Lists versions of a specific package for a specified user.

        :param username: The username of the user.
        :param package_type: The type of package (e.g., "npm", "maven").
        :param package_name: The name of the package.
        :return: Response from the API.
        """
        url = f"/users/{self.parent.username}/packages/{package_type}/{package_name}/versions"
        return self.parent.make_request("GET", url)

    def get_package_version_for_user(self, package_type: str,
                                 package_name: str,
                                 package_version_id: int) -> Any:
        """
        Gets a specific version of a package for a specified user.

        :param username: The username of the user.
        :param package_type: The type of package (e.g., "npm", "maven").
        :param package_name: The name of the package.
        :param package_version_id: The ID of the package version.
        :return: Response from the API.
        """
        url = f"/users/{self.parent.username}/packages/{package_type}/{package_name}/versions/{package_version_id}"
        return self.parent.make_request("GET", url)

    def delete_package_version_for_user(self, package_type: str,
                                      package_name: str,
                                      package_version_id: int) -> Any:
        """
        Deletes a specific version of a package for a specified user.

        :param username: The username of the user.
        :param package_type: The type of package (e.g., "npm", "maven").
        :param package_name: The name of the package.
        :param package_version_id: The ID of the package version.
        :return: Response from the API.
        """
        url = f"/users/{self.parent.username}/packages/{package_type}/{package_name}/versions/{package_version_id}"
        return self.parent.make_request("DELETE", url)

    def restore_package_version_for_user(self, package_type: str,
                                       package_name: str,
                                       package_version_id: int,
                                       **kwargs: Any) -> Any:
        """
        Restores a specific deleted version of a package for a specified user.

        :param username: The username of the user.
        :param package_type: The type of package (e.g., "npm", "maven").
        :param package_name: The name of the package.
        :param package_version_id: The ID of the package version.
        :param token: The restore token (optional).
        :return: Response from the API.
        """
        url = f"/users/{self.parent.username}/packages/{package_type}/{package_name}/versions/{package_version_id}/restore"
        return self.parent.make_request("POST", url)


































































































































































































































































































































































































































































































































































































































































































































































































































































































































