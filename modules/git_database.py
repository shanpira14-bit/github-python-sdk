"""
Module for managing Git database operations.
"""

from typing import Any, Dict

class Blobs:
    """
    Module for managing Git blobs.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def get_blob(self, repo: str, sha: str) -> Dict[str, Any]:
        """
        Get a specific Git blob.

        :param owner: Repository owner.
        :param repo: Repository name.
        :param sha: SHA of the blob.
        :return: Blob details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/git/blobs/{sha}"
        return self.parent.make_request("GET", endpoint)

    def create_blob(self, repo: str, content: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Create a new Git blob.

        :param owner: Repository owner.
        :param repo: Repository name.
        :param content: Content of the blob.
        :param encoding: Encoding of the content (default is 'utf-8').
        :return: Created blob details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/git/blobs"
        data: Dict[str, Any] = {
            "content": content,
            "encoding": kwargs.get("encoding", "utf-8")
        }
        return self.parent.make_request("POST", endpoint, json=data)
class Commits:
    """
    Module for managing Git commits.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def create_commit(self, repo: str, message: str,
                      tree: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Create a new Git commit.

        :param owner: Repository owner.
        :param repo: Repository name.
        :param message: Commit message.
        :param tree: SHA of the tree object this commit points to.
        :param parents: List of parent commit SHAs.
        :return: Created commit details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/git/commits"
        data: Dict[str, Any] = {
            "message": message,
            "tree": tree,
            "parents": kwargs.get("parent_shas", []),
            "author": {
                "name": kwargs.get("author_name", ""),
                "email": kwargs.get("author_email", ""),
                "date": kwargs.get("author_date", "")
            },
            "committer": {
                "name": kwargs.get("committer_name", ""),
                "email": kwargs.get("committer_email", ""),
                "date": kwargs.get("committer_date", "")
            },
            "signature": kwargs.get("signature", "")
        }
        return self.parent.make_request("POST", endpoint, json=data)

    def get_commit(self, repo: str, sha: str) -> Dict[str, Any]:
        """
        Get a specific Git commit.

        :param owner: Repository owner.
        :param repo: Repository name.
        :param sha: SHA of the commit.
        :return: Commit details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/git/commits/{sha}"
        return self.parent.make_request("GET", endpoint)

class Tags:
    """
    Module for managing Git tags.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def create_tag(self, repo: str, tag: str,
                   message: str, object_sha: str, type_: str,
                   **kwargs: Any) -> Dict[str, Any]:
        """
        Create a new Git tag object.

        :param owner: Repository owner.
        :param repo: Repository name.
        :param tag: Name of the tag.
        :param message: Tag message.
        :param object_sha: SHA of the object the tag points to.
        :param type_: Type of the object (commit, tree, blob).
        :param tagger: Tagger information (name, email, date).
        :return: Created tag details.
        """
        endpoint = f"/repos/{self.parent.owner}/{repo}/git/tags"
        data: Dict[str, Any] = {
            "tag": tag,
            "message": message,
            "object": object_sha,
            "type": type_,
            "tagger": {
                "name": kwargs.get("tagger_name", ""),
                "email": kwargs.get("tagger_email", ""),
                "date": kwargs.get("tagger_date", "")
            }
        }
        return self.parent.make_request("POST", endpoint, json=data)

    def get_tag(self, repo: str, sha: str) -> Dict[str, Any]:
        """
        Get a specific Git tag object.

        :param owner: Repository owner.
        :param repo: Repository name.
        :param sha: SHA of the tag object.
        :return: Tag details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/git/tags/{sha}"
        return self.parent.make_request("GET", endpoint)

class Trees:
    """
    Module for managing Git trees.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def create_tree(self, repo: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Create a new Git tree.

        :param owner: Repository owner.
        :param repo: Repository name.
        :param tree: List of tree items.
        :param base_tree: SHA of the base tree (optional).
        :return: Created tree details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/git/trees"
        data: Dict[str, Any] = {
            "tree": {
                "path": kwargs.get("path", ""),
                "mode": kwargs.get("mode", ""),
                "type": kwargs.get("type", ""),
                "sha": kwargs.get("sha", ""),
                "content": kwargs.get("content", "")
            },
            "base_tree": kwargs.get("base_tree", "")
        }
        return self.parent.make_request("POST", endpoint, json=data)

    def get_tree(self, repo: str, sha: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Get a specific Git tree.

        :param owner: Repository owner.
        :param repo: Repository name.
        :param sha: SHA of the tree.
        :param recursive: Whether to retrieve the tree recursively (default is False).
        :return: Tree details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/git/trees/{sha}"
        params: Dict[str, Any] = {}
        if kwargs.get("recursive", False):
            params["recursive"] = "1"
        return self.parent.make_request("GET", endpoint, params=params)

class References:
    """
    Module for managing Git references.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def list_matching_refs(self, repo: str, ref: str) -> Dict[str, Any]:
        """
        List Git references matching a specific SHA.

        :param owner: Repository owner.
        :param repo: Repository name.
        :param ref: Reference name or SHA to match.
        :return: List of matching references.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/git/matching-refs/{ref}"
        return self.parent.make_request("GET", endpoint)

    def get_ref(self, repo: str, ref: str) -> Dict[str, Any]:
        """
        Get a specific Git reference.

        :param owner: Repository owner.
        :param repo: Repository name.
        :param ref: Reference name (e.g., heads/main).
        :return: Reference details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/git/ref/{ref}"
        return self.parent.make_request("GET", endpoint)

    def create_ref(self, repo: str, ref: str, sha: str) -> Dict[str, Any]:
        """
        Create a new Git reference.

        :param owner: Repository owner.
        :param repo: Repository name.
        :param ref: Reference name (e.g., refs/heads/feature-branch).
        :param sha: SHA the reference points to.
        :return: Created reference details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/git/refs"
        data = {
            "ref": ref,
            "sha": sha
        }
        return self.parent.make_request("POST", endpoint, json=data)

    def update_ref(self, repo: str, ref: str,
                   sha: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Update an existing Git reference.

        :param owner: Repository owner.
        :param repo: Repository name.
        :param ref: Reference name (e.g., heads/main).
        :param sha: New SHA the reference should point to.
        :param force: Whether to force the update (default is False).
        :return: Updated reference details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/git/refs/{ref}"
        data: Dict[str, Any] = {
            "sha": sha,
            "force": kwargs.get("force", False)
        }
        return self.parent.make_request("PATCH", endpoint, json=data)

    def delete_ref(self, repo: str, ref: str) -> None:
        """
        Delete a Git reference.

        :param owner: Repository owner.
        :param repo: Repository name.
        :param ref: Reference name (e.g., heads/feature-branch).
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/git/refs/{ref}"
        self.parent.make_request("DELETE", endpoint)

class GitDatabase:
    """
    Module for managing Git database operations.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

        # Initialize submodules
        self.blobs = Blobs(parent)
        self.commits = Commits(parent)
        self.tags = Tags(parent)
        self.trees = Trees(parent)
        self.references = References(parent)