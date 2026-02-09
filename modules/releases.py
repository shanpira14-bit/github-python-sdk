from typing import Any, Dict

class Releases:
    """
    Handles GitHub Releases API endpoints.
    """
    def __init__ (self, parent: Any) -> None:
        self.parent = parent

    def list_releases(self, repo: str, **kwargs: Any) -> Any:
        """
        List all releases for a given repository.
        """
        endpoint = f"/repos/{self.parent.owner}/{repo}/releases"
        params = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def create_release(self, repo: str, tag_name: str, **kwargs: Any) -> Any:
        """
        Create a new release for a given repository.

        :param repo: Repository name.
        :param tag_name: The name of the tag for the release.
        :param target_commitish: (optional) The commitish value that determines
          where the Git tag is created from.
        :param name: (optional) The name of the release.
        :param body: (optional) Text describing the contents of the release.
        :param draft: (optional) True to create a draft release, false to create a published one.
        :param prerelease: (optional) True to identify the release as a pre-release.
        :param discussion_category_name: (optional) The discussion category name for the release.
        :param generate_release_notes: (optional) True to automatically generate release notes.
        :param make_latest: (optional) Set to "true", "false", or "earliest" to
          control the "latest" tag behavior.
        :return: API response.
        """
        endpoint = f"/repos/{self.parent.owner}/{repo}/releases"
        data: Dict[str, Any] = {
            "tag_name": tag_name,
            "target_commitish": kwargs.get("target_commitish"),
            "name": kwargs.get("name", tag_name),
            "body": kwargs.get("body", ""),
            "draft": kwargs.get("draft", False),
            "prerelease": kwargs.get("prerelease", False),
            "discussion_category_name": kwargs.get("discussion_category_name", None),
            "generate_release_notes": kwargs.get("generate_release_notes", False),
            "make_latest": kwargs.get("make_latest", "false")
        }
        return self.parent.make_request("POST", endpoint, json=data)

    def generate_release_notes(self, repo: str, tag_name: str, **kwargs: Any) -> Any:
        """
        Generate release notes for a given tag in a repository.

        :param repo: Repository name.
        :param tag_name: The name of the tag for which to generate release notes.
        :param previous_tag_name: (optional) The previous tag name to compare against.
        :return: API response.
        """
        endpoint = f"/repos/{self.parent.owner}/{repo}/releases/generate-notes"
        data: Dict[str, Any] = {
            "tag_name": tag_name,
            "target_commitish": kwargs.get("target_commitish"),
            "previous_tag_name": kwargs.get("previous_tag_name", None),
            "configuration_file_path": kwargs.get("configuration_file_path", None)
        }
        return self.parent.make_request("POST", endpoint, json=data)

    def get_latest_release(self, repo: str) -> Any:
        """
        Get the latest release for a given repository.

        :param repo: Repository name.
        :return: API response.
        """
        endpoint = f"/repos/{self.parent.owner}/{repo}/releases/latest"
        return self.parent.make_request("GET", endpoint)

    def get_release_by_tag(self, repo: str, tag: str) -> Any:
        """
        Get a release by tag name for a given repository.

        :param repo: Repository name.
        :param tag: Tag name of the release.
        :return: API response.
        """
        endpoint = f"/repos/{self.parent.owner}/{repo}/releases/tags/{tag}"
        return self.parent.make_request("GET", endpoint)

    def get_release(self, repo: str, release_id: int) -> Any:
        """
        Get a release by its ID for a given repository.

        :param repo: Repository name.
        :param release_id: ID of the release.
        :return: API response.
        """
        endpoint = f"/repos/{self.parent.owner}/{repo}/releases/{release_id}"
        return self.parent.make_request("GET", endpoint)

    def update_release(self, repo: str, release_id: int, **kwargs: Any) -> Any:
        """
        Update a release for a given repository.

        :param repo: Repository name.
        :param release_id: ID of the release to update.
        :param tag_name: (optional) The name of the tag for the release.
        :param target_commitish: (optional) The commitish value that determines
          where the Git tag is created from.
        :param name: (optional) The name of the release.
        :param body: (optional) Text describing the contents of the release.
        :param draft: (optional) True to create a draft release, false to create a published one.
        :param prerelease: (optional) True to identify the release as a pre-release.
        :param discussion_category_name: (optional) The discussion category name for the release.
        :param make_latest: (optional) Set to "true", "false", or "earliest" to
          control the "latest" tag behavior.
        :return: API response.
        """
        endpoint = f"/repos/{self.parent.owner}/{repo}/releases/{release_id}"
        data: Dict[str, Any] = {
            "tag_name": kwargs.get("tag_name"),
            "target_commitish": kwargs.get("target_commitish"),
            "name": kwargs.get("name"),
            "body": kwargs.get("body"),
            "draft": kwargs.get("draft"),
            "prerelease": kwargs.get("prerelease"),
            "discussion_category_name": kwargs.get("discussion_category_name"),
            "make_latest": kwargs.get("make_latest")
        }
        return self.parent.make_request("PATCH", endpoint, json=data)

    def delete_release(self, repo: str, release_id: int) -> Any:
        """
        Delete a release for a given repository.

        :param repo: Repository name.
        :param release_id: ID of the release to delete.
        :return: API response.
        """
        endpoint = f"/repos/{self.parent.owner}/{repo}/releases/{release_id}"
        return self.parent.make_request("DELETE", endpoint)


class ReleaseAssets:
    """
    Handles GitHub Release Assets API endpoints.
    """
    def __init__ (self, parent: Any) -> None:
        self._parent = parent

    def get_release_asset(self, repo: str, asset_id: int) -> Any:
        """
        Get a release asset by its ID for a given repository.

        :param repo: Repository name.
        :param asset_id: ID of the release asset.
        :return: API response.
        """
        endpoint = f"/repos/{self._parent.owner}/{repo}/releases/assets/{asset_id}"
        return self._parent.make_request("GET", endpoint)

    def update_release_asset(self, repo: str, asset_id: int, name: str, label: str) -> Any:
        """
        Update a release asset for a given repository.

        :param repo: Repository name.
        :param asset_id: ID of the release asset to update.
        :param name: The new name of the asset.
        :param label: The new label of the asset.
        :return: API response.
        """
        endpoint = f"/repos/{self._parent.owner}/{repo}/releases/assets/{asset_id}"
        data: Dict[str, Any] = {
            "name": name,
            "label": label
        }
        return self._parent.make_request("PATCH", endpoint, json=data)

    def delete_release_asset(self, repo: str, asset_id: int) -> Any:
        """
        Delete a release asset for a given repository.

        :param repo: Repository name.
        :param asset_id: ID of the release asset to delete.
        :return: API response.
        """
        endpoint = f"/repos/{self._parent.owner}/{repo}/releases/assets/{asset_id}"
        return self._parent.make_request("DELETE", endpoint)

    def list_release_assets(self, repo: str, release_id: int, **kwargs: Any) -> Any:
        """
        List all release assets for a given release in a repository.

        :param repo: Repository name.
        :param release_id: ID of the release.
        :return: API response.
        """
        endpoint = f"/repos/{self._parent.owner}/{repo}/releases/{release_id}/assets"
        params = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self._parent.make_request("GET", endpoint, params=params)

    def upload_release_asset(self, repo: str, release_id: int, name: str, **kwargs: Any) -> Any:
        """
        Upload a release asset to a given release in a repository.

        :param repo: Repository name.
        :param release_id: ID of the release.
        :param file_path: Path to the file to upload.
        :param name: The name of the asset.
        :param label: (optional) The label of the asset.
        :return: API response.
        """
        endpoint = f"/repos/{self._parent.owner}/{repo}/releases/{release_id}/assets"
        params: Dict[str, Any] = {
            "name": name,
            "label": kwargs.get("label", None)
        }
        with open(kwargs.get("file_path", ""), "rb") as file_data:
            headers = self._parent.headers.copy()
            headers["Content-Type"] = "application/octet-stream"
            return self._parent.make_request("POST", endpoint, params=params,
                                             data=file_data, headers=headers)

class Release:
    """
    Handles GitHub Release related modules.
    """
    def __init__ (self, parent: Any) -> None:

        # Initialize Sub-modules
        self.releases = Releases(parent)
        self.release_assets = ReleaseAssets(parent)