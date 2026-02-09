"""
Repositories module for managing GitHub repositories.
"""
from typing import Any, Dict, List


# -------------------- Autolinks Section -------------------- #
class Autolinks:
    """
    Module for managing repository autolinks.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def list_autolinks(self, repo: str) -> Any:
        """
        List all autolinks for a repository.

        :param repo: The name of the repository.
        :return: Dictionary containing the list of autolinks.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/autolinks"
        return self.parent.make_request("GET", endpoint)

    def create_autolink(self, repo: str, key_prefix: str, url_template: str,
                        **kwargs: Any) -> Any:
        """
        Create an autolink reference for a repository.

        :param repo: The name of the repository.
        :param key_prefix: The prefix appended by certain characters to generate a link.
        :param url_template: The URL must contain <num> for the reference number.
        :param is_alphanumeric: (optional) Whether the link is alphanumeric. Default is True.
        :return: Dictionary containing the created autolink details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/autolinks"
        data: Dict[str, Any] = {
            "key_prefix": key_prefix,
            "url_template": url_template,
            "is_alphanumeric": kwargs.get("is_alphanumeric", True)
        }
        return self.parent.make_request("POST", endpoint, json=data)

    def get_autolink(self, repo: str, autolink_id: int) -> Any:
        """
        Get an autolink reference by ID.

        :param repo: The name of the repository.
        :param autolink_id: The unique identifier of the autolink.
        :return: Dictionary containing the autolink details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/autolinks/{autolink_id}"
        return self.parent.make_request("GET", endpoint)

    def delete_autolink(self, repo: str, autolink_id: int) -> Any:
        """
        Delete an autolink reference.

        :param repo: The name of the repository.
        :param autolink_id: The unique identifier of the autolink.
        :return: Dictionary containing the response from the API.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/autolinks/{autolink_id}"
        return self.parent.make_request("DELETE", endpoint)


# -------------------- Contents Section -------------------- #
class Contents:
    """
    Module for managing repository contents.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def get_repository_readme(self, repo: str, **kwargs: Any) -> Any:
        """
        Get the README file for a repository.

        :param repo: The name of the repository.
        :param ref: (optional) The name of the commit/branch/tag. Default is default branch.
        :return: Dictionary containing the README content.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/readme"
        params: Dict[str, Any] = {
            "ref": kwargs.get("ref")
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def get_repository_readme_for_directory(self, repo: str, directory: str,
                                             **kwargs: Any) -> Any:
        """
        Get the README file for a specific directory.

        :param repo: The name of the repository.
        :param directory: The directory path.
        :param ref: (optional) The name of the commit/branch/tag. Default is default branch.
        :return: Dictionary containing the README content.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/readme/{directory}"
        params: Dict[str, Any] = {
            "ref": kwargs.get("ref")
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def get_repository_content(self, repo: str, path: str, **kwargs: Any) -> Any:
        """
        Get the contents of a file or directory in a repository.

        :param repo: The name of the repository.
        :param path: The file or directory path.
        :param ref: (optional) The name of the commit/branch/tag. Default is default branch.
        :return: Dictionary containing the file/directory content.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/contents/{path}"
        params: Dict[str, Any] = {
            "ref": kwargs.get("ref")
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def create_or_update_file_contents(self, repo: str, path: str, message: str,
                                       content: str, **kwargs: Any) -> Any:
        """
        Create or update a file in a repository.

        :param repo: The name of the repository.
        :param path: The file path.
        :param message: The commit message.
        :param content: The new file content, using Base64 encoding.
        :param sha: (optional) Required if updating an existing file. The blob SHA of the file.
        :param branch: (optional) The branch name. Default is the repository's default branch.
        :param committer: (optional) The person that committed the file.
            Refer to GitHub API documentation for committer object structure.
            https://docs.github.com/en/rest/repos/contents?apiVersion=2022-11-28#create-or-update-file-contents
        :param author: (optional) The author of the file.
            Refer to GitHub API documentation for author object structure.
            https://docs.github.com/en/rest/repos/contents?apiVersion=2022-11-28#create-or-update-file-contents
        :return: Dictionary containing the commit details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/contents/{path}"
        data: Dict[str, Any] = {
            "message": message,
            "content": content,
            "sha": kwargs.get("sha"),
            "branch": kwargs.get("branch"),
            "committer": kwargs.get("committer"),
            "author": kwargs.get("author")
        }
        # Remove keys with None values
        data = {k: v for k, v in data.items() if v is not None}
        return self.parent.make_request("PUT", endpoint, json=data)

    def delete_file(self, repo: str, path: str, message: str, sha: str,
                    **kwargs: Any) -> Any:
        """
        Delete a file in a repository.

        :param repo: The name of the repository.
        :param path: The file path.
        :param message: The commit message.
        :param sha: The blob SHA of the file being deleted.
        :param branch: (optional) The branch name. Default is the repository's default branch.
        :param committer: (optional) The person that committed the file.
            Refer to GitHub API documentation for committer object structure.
            https://docs.github.com/en/rest/repos/contents?apiVersion=2022-11-28#create-or-update-file-contents
        :param author: (optional) The author of the file.
            Refer to GitHub API documentation for author object structure.
            https://docs.github.com/en/rest/repos/contents?apiVersion=2022-11-28#create-or-update-file-contents
        :return: Dictionary containing the commit details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/contents/{path}"
        data: Dict[str, Any] = {
            "message": message,
            "sha": sha,
            "branch": kwargs.get("branch"),
            "committer": kwargs.get("committer"),
            "author": kwargs.get("author")
        }
        # Remove keys with None values
        data = {k: v for k, v in data.items() if v is not None}
        return self.parent.make_request("DELETE", endpoint, json=data)

    def download_tarball_archive(self, repo: str, ref: str) -> Any:
        """
        Download a tarball archive of the repository.

        :param repo: The name of the repository.
        :param ref: The name of the commit/branch/tag.
        :return: Dictionary containing the download URL.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/tarball/{ref}"
        return self.parent.make_request("GET", endpoint)

    def download_zipball_archive(self, repo: str, ref: str) -> Any:
        """
        Download a zipball archive of the repository.

        :param repo: The name of the repository.
        :param ref: The name of the commit/branch/tag.
        :return: Dictionary containing the download URL.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/zipball/{ref}"
        return self.parent.make_request("GET", endpoint)


# -------------------- Forks Section -------------------- #
class Forks:
    """
    Module for managing repository forks.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def list_forks(self, repo: str, **kwargs: Any) -> Any:
        """
        List forks of a repository.

        :param repo: The name of the repository.
        :param sort: (optional) Sort by ('newest', 'oldest', 'stargazers', 'watchers').
            Default is 'newest'.
        :param per_page: (optional) Number of results per page (max 100). Default is 30.
        :param page: (optional) Page number of the results to fetch. Default is 1.
        :return: Dictionary containing the list of forks.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/forks"
        params: Dict[str, Any] = {
            "sort": kwargs.get("sort", "newest"),
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def create_fork(self, repo: str, **kwargs: Any) -> Any:
        """
        Create a fork of a repository.

        :param repo: The name of the repository.
        :param organization: (optional) Organization to fork into.
        :param name: (optional) Name of the new forked repository.
        :param default_branch_only: (optional) Fork only the default branch. Default is False.
        :return: Dictionary containing the forked repository details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/forks"
        data: Dict[str, Any] = {
            "organization": kwargs.get("organization"),
            "name": kwargs.get("name"),
            "default_branch_only": kwargs.get("default_branch_only", False)
        }
        # Remove keys with None values
        data = {k: v for k, v in data.items() if v is not None}
        return self.parent.make_request("POST", endpoint, json=data)


# -------------------- Repositories Section -------------------- #
class Repositories:
    """
    Module for managing repositories.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def list_organization_repositories(self, **kwargs: Any) -> Any:
        """
        List all repositories for the organization.

        :param type: (optional) Filter by repository type ('all', 'public', 'private',
            'forks', 'sources', 'member'). Default is 'all'.
        :param sort: (optional) Sort by ('created', 'updated', 'pushed', 'full_name').
            Default is 'full_name'.
        :param direction: (optional) Sort direction ('asc', 'desc'). Default is 'asc'.
        :param per_page: (optional) Number of results per page (max 100). Default is 30.
        :param page: (optional) Page number of the results to fetch. Default is 1.
        :return: Dictionary containing the list of repositories.
        """
        endpoint = f"/orgs/{self.parent.org}/repos"
        params: Dict[str, Any] = {
            "type": kwargs.get("type", "all"),
            "sort": kwargs.get("sort", "full_name"),
            "direction": kwargs.get("direction", "asc"),
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def create_organization_repository(self, name: str, **kwargs: Any) -> Any:
        """
        Create a new repository in the organization.

        :param name: The name of the repository.
        :param description: (optional) A short description of the repository.
        :param homepage: (optional) A URL with more information about the repository.
        :param private: (optional) Whether the repository is private. Default is False.
        :param visibility: (optional) Visibility of the repository ('public', 'private').
        :param has_issues: (optional) Enable issues for the repository. Default is True.
        :param has_projects: (optional) Enable projects for the repository. Default is True.
        :param has_wiki: (optional) Enable wiki for the repository. Default is True.
        :param has_downloads: (optional) Enable downloads for the repository. Default is True.
        :param is_template: (optional) Make this repo available as a template. Default is False.
        :param team_id: (optional) The ID of the team with access to this repository.
        :param auto_init: (optional) Create an initial commit with README. Default is False.
        :param gitignore_template: (optional) Gitignore template to use.
        :param license_template: (optional) License template to use.
        :param allow_squash_merge: (optional) Allow squash-merging. Default is True.
        :param allow_merge_commit: (optional) Allow merge commits. Default is True.
        :param allow_rebase_merge: (optional) Allow rebase-merging. Default is True.
        :param allow_auto_merge: (optional) Allow auto-merge. Default is False.
        :param delete_branch_on_merge: (optional) Delete branch on merge. Default is False.
        :return: Dictionary containing the created repository details.
        """
        endpoint = f"/orgs/{self.parent.org}/repos"
        data: Dict[str, Any] = {
            "name": name,
            "description": kwargs.get("description"),
            "homepage": kwargs.get("homepage"),
            "private": kwargs.get("private", False),
            "visibility": kwargs.get("visibility"),
            "has_issues": kwargs.get("has_issues", True),
            "has_projects": kwargs.get("has_projects", True),
            "has_wiki": kwargs.get("has_wiki", True),
            "has_downloads": kwargs.get("has_downloads", True),
            "is_template": kwargs.get("is_template", False),
            "team_id": kwargs.get("team_id"),
            "auto_init": kwargs.get("auto_init", False),
            "gitignore_template": kwargs.get("gitignore_template"),
            "license_template": kwargs.get("license_template"),
            "allow_squash_merge": kwargs.get("allow_squash_merge", True),
            "allow_merge_commit": kwargs.get("allow_merge_commit", True),
            "allow_rebase_merge": kwargs.get("allow_rebase_merge", True),
            "allow_auto_merge": kwargs.get("allow_auto_merge", False),
            "delete_branch_on_merge": kwargs.get("delete_branch_on_merge", False)
        }
        # Remove keys with None values
        data = {k: v for k, v in data.items() if v is not None}
        return self.parent.make_request("POST", endpoint, json=data)

    def get_repository(self, repo: str) -> Any:
        """
        Get a repository by name.

        :param repo: The name of the repository.
        :return: Dictionary containing the repository details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}"
        return self.parent.make_request("GET", endpoint)

    def update_repository(self, repo: str, **kwargs: Any) -> Any:
        """
        Update a repository.

        :param repo: The name of the repository.
        :param name: (optional) The new name of the repository.
        :param description: (optional) A short description of the repository.
        :param homepage: (optional) A URL with more information about the repository.
        :param private: (optional) Whether the repository is private.
        :param visibility: (optional) Visibility of the repository ('public', 'private').
        :param security_and_analysis: (optional) Security and analysis settings.
            Refer to GitHub API documentation for security_and_analysis object structure.
            https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#update-a-repository
        :param has_issues: (optional) Enable issues for the repository.
        :param has_projects: (optional) Enable projects for the repository.
        :param has_wiki: (optional) Enable wiki for the repository.
        :param is_template: (optional) Make this repo available as a template.
        :param default_branch: (optional) The default branch for this repository.
        :param allow_squash_merge: (optional) Allow squash-merging.
        :param allow_merge_commit: (optional) Allow merge commits.
        :param allow_rebase_merge: (optional) Allow rebase-merging.
        :param allow_auto_merge: (optional) Allow auto-merge.
        :param delete_branch_on_merge: (optional) Delete branch on merge.
        :param allow_update_branch: (optional) Allow updating pull request branches.
        :param use_squash_pr_title_as_default: (optional) Use squash PR title as default.
        :param squash_merge_commit_title: (optional) The default title for squash merges.
        :param squash_merge_commit_message: (optional) The default commit message for squash merges.
        :param merge_commit_title: (optional) The default title for merge commits.
        :param merge_commit_message: (optional) The default commit message for merge commits.
        :param archived: (optional) Whether the repository is archived.
        :param allow_forking: (optional) Allow forking the repository.
        :param web_commit_signoff_required: (optional) Require commit signoff.
        :return: Dictionary containing the updated repository details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}"
        data: Dict[str, Any] = {
            "name": kwargs.get("name"),
            "description": kwargs.get("description"),
            "homepage": kwargs.get("homepage"),
            "private": kwargs.get("private"),
            "visibility": kwargs.get("visibility"),
            "security_and_analysis": kwargs.get("security_and_analysis"),
            "has_issues": kwargs.get("has_issues"),
            "has_projects": kwargs.get("has_projects"),
            "has_wiki": kwargs.get("has_wiki"),
            "is_template": kwargs.get("is_template"),
            "default_branch": kwargs.get("default_branch"),
            "allow_squash_merge": kwargs.get("allow_squash_merge"),
            "allow_merge_commit": kwargs.get("allow_merge_commit"),
            "allow_rebase_merge": kwargs.get("allow_rebase_merge"),
            "allow_auto_merge": kwargs.get("allow_auto_merge"),
            "delete_branch_on_merge": kwargs.get("delete_branch_on_merge"),
            "allow_update_branch": kwargs.get("allow_update_branch"),
            "use_squash_pr_title_as_default": kwargs.get("use_squash_pr_title_as_default"),
            "squash_merge_commit_title": kwargs.get("squash_merge_commit_title"),
            "squash_merge_commit_message": kwargs.get("squash_merge_commit_message"),
            "merge_commit_title": kwargs.get("merge_commit_title"),
            "merge_commit_message": kwargs.get("merge_commit_message"),
            "archived": kwargs.get("archived"),
            "allow_forking": kwargs.get("allow_forking"),
            "web_commit_signoff_required": kwargs.get("web_commit_signoff_required")
        }
        # Remove keys with None values
        data = {k: v for k, v in data.items() if v is not None}
        return self.parent.make_request("PATCH", endpoint, json=data)

    def delete_repository(self, repo: str) -> Any:
        """
        Delete a repository.

        :param repo: The name of the repository.
        :return: Dictionary containing the response from the API.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}"
        return self.parent.make_request("DELETE", endpoint)

    def list_repository_activities(self, repo: str, **kwargs: Any) -> Any:
        """
        List repository activities.

        :param repo: The name of the repository.
        :param direction: (optional) Sort direction ('asc', 'desc'). Default is 'desc'.
        :param per_page: (optional) Number of results per page (max 100). Default is 30.
        :param before: (optional) Filter activities before this time (ISO 8601 format).
        :param after: (optional) Filter activities after this time (ISO 8601 format).
        :param ref: (optional) Filter activities by reference (branch, tag, or SHA).
        :param actor: (optional) Filter activities by actor's username.
        :param time_period: (optional) Filter activities by time period ('day', 'week', 'month').
        :param activity_type: (optional) Filter activities by type ('push', 'pull_request',
        :return: Dictionary containing the list of activities.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/activity"
        params: Dict[str, Any] = {
            "direction": kwargs.get("direction", "desc"),
            "per_page": kwargs.get("per_page", 30),
            "before": kwargs.get("before"),
            "after": kwargs.get("after"),
            "ref": kwargs.get("ref"),
            "actor": kwargs.get("actor"),
            "time_period": kwargs.get("time_period"),
            "activity_type": kwargs.get("activity_type")
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def check_if_dependabot_security_updates_enabled(self, repo: str) -> Any:
        """
        Check if Dependabot security updates are enabled for a repository.

        :param repo: The name of the repository.
        :return: Dictionary containing the status of Dependabot security updates.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/automated-security-fixes"
        return self.parent.make_request("GET", endpoint)

    def enable_dependabot_security_updates(self, repo: str) -> Any:
        """
        Enable Dependabot security updates for a repository.

        :param repo: The name of the repository.
        :return: Dictionary containing the response from the API.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/automated-security-fixes"
        return self.parent.make_request("PUT", endpoint)

    def disable_dependabot_security_updates(self, repo: str) -> Any:
        """
        Disable Dependabot security updates for a repository.

        :param repo: The name of the repository.
        :return: Dictionary containing the response from the API.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/automated-security-fixes"
        return self.parent.make_request("DELETE", endpoint)

    def list_codeowners_errors(self, repo: str, **kwargs: Any) -> Any:
        """
        List CODEOWNERS errors for a repository.

        :param repo: The name of the repository.
        :param ref: (optional) The name of the commit/branch/tag. Default is default branch.
        :return: Dictionary containing the list of CODEOWNERS errors.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/codeowners/errors"
        params: Dict[str, Any] = {
            "ref": kwargs.get("ref")
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def list_repository_contributors(self, repo: str, **kwargs: Any) -> Any:
        """
        List contributors for a repository.

        :param repo: The name of the repository.
        :param anon: (optional) Include anonymous contributors. Default is False.
        :param per_page: (optional) Number of results per page (max 100). Default is 30.
        :param page: (optional) Page number of the results to fetch. Default is 1.
        :return: Dictionary containing the list of contributors.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/contributors"
        params: Dict[str, Any] = {
            "anon": kwargs.get("anon", False),
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def create_repository_dispatch_event(self, repo: str, event_type: str, **kwargs: Any) -> Any:
        """
        Create a repository dispatch event.

        :param repo: The name of the repository.
        :param event_type: A custom event type to trigger the workflow.
        :param client_payload: (optional) A JSON payload with extra information about the event.
        :return: Dictionary containing the response from the API.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/dispatches"
        data: Dict[str, Any] = {
            "event_type": event_type,
            "client_payload": kwargs.get("client_payload")
        }
        # Remove keys with None values
        data = {k: v for k, v in data.items() if v is not None}
        return self.parent.make_request("POST", endpoint, json=data)

    def check_immutable_releases_enabled(self, repo: str) -> Any:
        """
        Check if immutable releases are enabled for a repository.

        :param repo: The name of the repository.
        :return: Dictionary containing the status of immutable releases.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/immutable-releases"
        return self.parent.make_request("GET", endpoint)

    def enable_immutable_releases(self, repo: str) -> Any:
        """
        Enable immutable releases for a repository.

        :param repo: The name of the repository.
        :return: Dictionary containing the response from the API.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/immutable-releases"
        return self.parent.make_request("PUT", endpoint)

    def disable_immutable_releases(self, repo: str) -> Any:
        """
        Disable immutable releases for a repository.

        :param repo: The name of the repository.
        :return: Dictionary containing the response from the API.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/immutable-releases"
        return self.parent.make_request("DELETE", endpoint)

    def list_repository_languages(self, repo: str) -> Any:
        """
        List languages for a repository.

        :param repo: The name of the repository.
        :return: Dictionary containing the languages and their byte counts.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/languages"
        return self.parent.make_request("GET", endpoint)


    def check_if_private_vulnerability_reporting_enabled(self, repo: str) -> Any:
        """
        Check if private vulnerability reporting is enabled for a repository.

        :param repo: The name of the repository.
        :return: Dictionary containing the status of private vulnerability reporting.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/private-vulnerability-reporting"
        return self.parent.make_request("GET", endpoint)

    def enable_private_vulnerability_reporting(self, repo: str) -> Any:
        """
        Enable private vulnerability reporting for a repository.

        :param repo: The name of the repository.
        :return: Dictionary containing the response from the API.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/private-vulnerability-reporting"
        return self.parent.make_request("PUT", endpoint)

    def disable_private_vulnerability_reporting(self, repo: str) -> Any:
        """
        Disable private vulnerability reporting for a repository.

        :param repo: The name of the repository.
        :return: Dictionary containing the response from the API.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/private-vulnerability-reporting"
        return self.parent.make_request("DELETE", endpoint)

    def list_repository_tags(self, repo: str, **kwargs: Any) -> Any:
        """
        List tags for a repository.

        :param repo: The name of the repository.
        :param per_page: (optional) Number of results per page (max 100). Default is 30.
        :param page: (optional) Page number of the results to fetch. Default is 1.
        :return: Dictionary containing the list of tags.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/tags"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def list_repository_teams(self, repo: str, **kwargs: Any) -> Any:
        """
        List teams for a repository.

        :param repo: The name of the repository.
        :param per_page: (optional) Number of results per page (max 100). Default is 30.
        :param page: (optional) Page number of the results to fetch. Default is 1.
        :return: Dictionary containing the list of teams.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/teams"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def get_all_repository_topics(self, repo: str, **kwargs: Any) -> Any:
        """
        Get all topics for a repository.

        :param repo: The name of the repository.
        :return: Dictionary containing the list of topics.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/topics"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def replace_all_repository_topics(self, repo: str, names: List[str]) -> Any:
        """
        Replace all topics for a repository.

        :param repo: The name of the repository.
        :param names: List of topic names to set.
        :return: Dictionary containing the updated list of topics.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/topics"
        data: Dict[str, Any] = {
            "names": names
        }
        return self.parent.make_request("PUT", endpoint, json=data)

    def transfer_repository(self, repo: str, new_owner: str, **kwargs: Any) -> Any:
        """
        Transfer a repository to another user or organization.

        :param repo: The name of the repository.
        :param new_owner: The username or organization to transfer to.
        :param new_name: (optional) The new name for the repository.
        :param team_ids: (optional) List of team IDs to add to the repository.
        :return: Dictionary containing the transfer response.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/transfer"
        data: Dict[str, Any] = {
            "new_owner": new_owner,
            "new_name": kwargs.get("new_name"),
            "team_ids": kwargs.get("team_ids", [])
        }
        # Remove keys with None values
        data = {k: v for k, v in data.items() if v is not None}
        return self.parent.make_request("POST", endpoint, json=data)

    def check_vulnerability_alerts_enabled(self, repo: str) -> Any:
        """
        Check if vulnerability alerts are enabled for a repository.

        :param repo: The name of the repository.
        :return: Dictionary containing the status of vulnerability alerts.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/vulnerability-alerts"
        return self.parent.make_request("GET", endpoint)

    def enable_vulnerability_alerts(self, repo: str) -> Any:
        """
        Enable vulnerability alerts for a repository.

        :param repo: The name of the repository.
        :return: Dictionary containing the response from the API.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/vulnerability-alerts"
        return self.parent.make_request("PUT", endpoint)

    def disable_vulnerability_alerts(self, repo: str) -> Any:
        """
        Disable vulnerability alerts for a repository.

        :param repo: The name of the repository.
        :return: Dictionary containing the response from the API.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/vulnerability-alerts"
        return self.parent.make_request("DELETE", endpoint)

    def create_repository_using_template(self, template_owner: str, template_repo: str, name: str,
                                         **kwargs: Any) -> Any:
        """
        Create a repository using a template.

        :param template_owner: The owner of the template repository.
        :param template_repo: The name of the template repository.
        :param name: The name of the new repository.
        :param description: (optional) A short description of the repository.
        :param include_all_branches: (optional) Whether to include all branches from the template.
            Default is False.
        :param private: (optional) Whether the new repository is private.
            Default is False.
        :return: Dictionary containing the created repository details.
        """
        endpoint = f"/repos/{template_owner}/{template_repo}/generate"
        data: Dict[str, Any] = {
            "owner": kwargs.get("owner", self.parent.org),
            "name": name,
            "description": kwargs.get("description"),
            "include_all_branches": kwargs.get("include_all_branches", False),
            "private": kwargs.get("private", False),
        }
        # Remove keys with None values
        data = {k: v for k, v in data.items() if v is not None}
        return self.parent.make_request("POST", endpoint, json=data)

    def list_repositories_for_authenticated_user(self, **kwargs: Any) -> Any:
        """
        List repositories for the authenticated user.

        :param visibility: (optional) Filter by repository visibility ('all', 'public', 'private').
            Default is 'all'.
        :param affiliation: (optional) Filter by repository affiliation ('owner', 'collaborator',
            'organization_member'). Default is 'owner,collaborator,organization_member'.
        :param type: (optional) Filter by repository type ('all', 'owner', 'public',
            'private', 'member'). Default is 'owner'.
        :param sort: (optional) Sort by ('created', 'updated', 'pushed', 'full_name').
            Default is 'full_name'.
        :param direction: (optional) Sort direction ('asc', 'desc'). Default is 'asc'.
        :param per_page: (optional) Number of results per page (max 100). Default is 30.
        :param page: (optional) Page number of the results to fetch. Default is 1.
        :param since: (optional) Filter repositories updated after this time (ISO 8601 format).
        :param before: (optional) Filter repositories updated before this time (ISO 8601 format).
        :return: Dictionary containing the list of repositories.
        """
        endpoint = "/user/repos"
        params: Dict[str, Any] = {
            "visibility": kwargs.get("visibility", "all"),
            "affiliation": kwargs.get("affiliation", "owner,collaborator,organization_member"),
            "type": kwargs.get("type"),
            "sort": kwargs.get("sort"),
            "direction": kwargs.get("direction"),
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1),
            "since": kwargs.get("since"),
            "before": kwargs.get("before")
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def create_repository_for_authenticated_user(self, name: str, **kwargs: Any) -> Any:
        """
        Create a new repository for the authenticated user.

        :param name: The name of the repository.
        :param description: (optional) A short description of the repository.
        :param homepage: (optional) A URL with more information about the repository.
        :param private: (optional) Whether the repository is private. Default is False.
        :param has_issues: (optional) Enable issues for the repository. Default is True.
        :param has_projects: (optional) Enable projects for the repository. Default is True.
        :param has_wiki: (optional) Enable wiki for the repository. Default is True.
        :param has_discussions: (optional) Enable discussions for the repository. Default is False.
        :param team_id: (optional) The ID of the team with access to this repository.
        :param auto_init: (optional) Create an initial commit with README. Default is False.
        :param gitignore_template: (optional) Gitignore template to use.
        :param license_template: (optional) License template to use.
        :param allow_squash_merge: (optional) Allow squash-merging. Default is True.
        :param allow_merge_commit: (optional) Allow merge commits. Default is True.
        :param allow_rebase_merge: (optional) Allow rebase-merging. Default is True.
        :param allow_auto_merge: (optional) Allow auto-merge. Default is False.
        :param delete_branch_on_merge: (optional) Delete branch on merge. Default is False.
        :param squash_merge_commit_title: (optional) Title for squash merge commit.
        :param squash_merge_commit_message: (optional) Message for squash merge commit.
        :param merge_commit_title: (optional) Title for merge commit.
        :param merge_commit_message: (optional) Message for merge commit.
        :param has_downloads: (optional) Enable downloads for the repository. Default is True.
        :param is_template: (optional) Whether the repository is a template. Default is False.
        :return: Dictionary containing the created repository details.
        """
        endpoint = "/user/repos"
        data: Dict[str, Any] = {
            "name": name,
            "description": kwargs.get("description"),
            "homepage": kwargs.get("homepage"),
            "private": kwargs.get("private", False),
            "has_issues": kwargs.get("has_issues", True),
            "has_projects": kwargs.get("has_projects", True),
            "has_wiki": kwargs.get("has_wiki", True),
            "has_discussions": kwargs.get("has_discussions"),
            "team_id": kwargs.get("team_id"),
            "auto_init": kwargs.get("auto_init", False),
            "gitignore_template": kwargs.get("gitignore_template"),
            "license_template": kwargs.get("license_template"),
            "allow_squash_merge": kwargs.get("allow_squash_merge", True),
            "allow_merge_commit": kwargs.get("allow_merge_commit", True),
            "allow_rebase_merge": kwargs.get("allow_rebase_merge", True),
            "allow_auto_merge": kwargs.get("allow_auto_merge", False),
            "delete_branch_on_merge": kwargs.get("delete_branch_on_merge", False),
            "squash_merge_commit_title": kwargs.get("squash_merge_commit_title"),
            "squash_merge_commit_message": kwargs.get("squash_merge_commit_message"),
            "merge_commit_title": kwargs.get("merge_commit_title"),
            "merge_commit_message": kwargs.get("merge_commit_message"),
            "has_downloads": kwargs.get("has_downloads", True),
            "is_template": kwargs.get("is_template", False)
        }
        # Remove keys with None values
        data = {k: v for k, v in data.items() if v is not None}
        return self.parent.make_request("POST", endpoint, json=data)


# -------------------- Traffic Section -------------------- #
class Traffic:
    """
    Module for managing repository traffic data.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def get_repository_clones(self, repo: str, **kwargs: Any) -> Any:
        """
        Get the total number of clones and breakdown per day or week.

        :param repo: The name of the repository.
        :param per: (optional) Time frame ('day', 'week'). Default is 'day'.
        :return: Dictionary containing clone statistics.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/traffic/clones"
        params: Dict[str, Any] = {
            "per": kwargs.get("per", "day")
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def get_top_referral_paths(self, repo: str) -> Any:
        """
        Get the top 10 popular contents for the last 14 days.

        :param repo: The name of the repository.
        :return: Dictionary containing the top referral paths.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/traffic/popular/paths"
        return self.parent.make_request("GET", endpoint)

    def get_top_referral_sources(self, repo: str) -> Any:
        """
        Get the top 10 referrers over the last 14 days.

        :param repo: The name of the repository.
        :return: Dictionary containing the top referral sources.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/traffic/popular/referrers"
        return self.parent.make_request("GET", endpoint)

    def get_repository_views(self, repo: str, **kwargs: Any) -> Any:
        """
        Get the total number of views and breakdown per day or week.

        :param repo: The name of the repository.
        :param per: (optional) Time frame ('day', 'week'). Default is 'day'.
        :return: Dictionary containing view statistics.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/traffic/views"
        params: Dict[str, Any] = {
            "per": kwargs.get("per", "day")
        }
        return self.parent.make_request("GET", endpoint, params=params)


# -------------------- Rulesets Section -------------------- #
class Rules:
    """
    Module for managing repository rulesets.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def get_rules_for_branch(self, repo: str, branch: str) -> Any:
        """
        Get the rules that apply to a specific branch.

        :param repo: The name of the repository.
        :param branch: The name of the branch.
        :return: Dictionary containing the rules that apply to the branch.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/rule/branches/{branch}"
        return self.parent.make_request("GET", endpoint)

    def list_repository_rulesets(self, repo: str, **kwargs: Any) -> Any:
        """
        List rulesets for a repository.

        :param repo: The name of the repository.
        :param per_page: (optional) Number of results per page (max 100). Default is 30.
        :param page: (optional) Page number of the results to fetch. Default is 1.
        :param includes_parents: (optional) Include rulesets from parent orgs.
        :param targets: (optional) Filter rulesets by target ('branch', 'tag').
        :return: Dictionary containing the list of rulesets.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/rulesets"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1),
            "includes_parents": kwargs.get("includes_parents", True),
            "targets": kwargs.get("targets")
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def create_repository_ruleset(self, repo: str, name: str, enforcement: str,
                                   **kwargs: Any) -> Any:
        """
        Create a ruleset for a repository.

        :param repo: The name of the repository.
        :param name: The name of the ruleset.
        :param enforcement: The enforcement level ('disabled', 'active', 'evaluate').
        :param target: (optional) The target of the ruleset ('branch', 'tag').
        :param bypass_actors: (optional) List of actors that can bypass the ruleset.
            Refer to GitHub API documentation for bypass_actors object structure.
            https://docs.github.com/en/rest/repos/rules?apiVersion=2022-11-28#create-a-repository-ruleset
        :param conditions: (optional) Conditions for the ruleset.
            Refer to GitHub API documentation for conditions object structure.
            https://docs.github.com/en/rest/repos/rules?apiVersion=2022-11-28#create-a-repository-ruleset
        :param rules: (optional) List of rules for the ruleset.
            Refer to GitHub API documentation for rules object structure.
            https://docs.github.com/en/rest/repos/rules?apiVersion=2022-11-28#create-a-repository-ruleset
        :return: Dictionary containing the created ruleset details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/rulesets"
        data: Dict[str, Any] = {
            "name": name,
            "enforcement": enforcement,
            "target": kwargs.get("target", "branch"),
            "bypass_actors": kwargs.get("bypass_actors", []),
            "conditions": kwargs.get("conditions"),
            "rules": kwargs.get("rules", [])
        }
        # Remove keys with None values
        data = {k: v for k, v in data.items() if v is not None}
        return self.parent.make_request("POST", endpoint, json=data)

    def get_repository_ruleset(self, repo: str, ruleset_id: int,
                               **kwargs: Any) -> Any:
        """
        Get a ruleset for a repository.

        :param repo: The name of the repository.
        :param ruleset_id: The unique identifier of the ruleset.
        :param includes_parents: (optional) Include rulesets from parent orgs.
        :return: Dictionary containing the ruleset details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/rulesets/{ruleset_id}"
        params: Dict[str, Any] = {
            "includes_parents": kwargs.get("includes_parents", True)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def update_repository_ruleset(self, repo: str, ruleset_id: int,
                                   **kwargs: Any) -> Any:
        """
        Update a ruleset for a repository.

        :param repo: The name of the repository.
        :param ruleset_id: The unique identifier of the ruleset.
        :param name: (optional) The name of the ruleset.
        :param enforcement: (optional) The enforcement level.
        :param target: (optional) The target of the ruleset.
        :param bypass_actors: (optional) List of actors that can bypass the ruleset.
            Refer to GitHub API documentation for bypass_actors object structure.
            https://docs.github.com/en/rest/repos/rules?apiVersion=2022-11-28#update-a-repository-ruleset
        :param conditions: (optional) Conditions for the ruleset.
            Refer to GitHub API documentation for conditions object structure.
            https://docs.github.com/en/rest/repos/rules?apiVersion=2022-11-28#update-a-repository-ruleset
        :param rules: (optional) List of rules for the ruleset.
            Refer to GitHub API documentation for rules object structure.
            https://docs.github.com/en/rest/repos/rules?apiVersion=2022-11-28#update-a-repository-ruleset
        :return: Dictionary containing the updated ruleset details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/rulesets/{ruleset_id}"
        data: Dict[str, Any] = {
            "name": kwargs.get("name"),
            "enforcement": kwargs.get("enforcement"),
            "target": kwargs.get("target"),
            "bypass_actors": kwargs.get("bypass_actors"),
            "conditions": kwargs.get("conditions"),
            "rules": kwargs.get("rules")
        }
        # Remove keys with None values
        data = {k: v for k, v in data.items() if v is not None}
        return self.parent.make_request("PUT", endpoint, json=data)

    def delete_repository_ruleset(self, repo: str, ruleset_id: int) -> Any:
        """
        Delete a ruleset for a repository.

        :param repo: The name of the repository.
        :param ruleset_id: The unique identifier of the ruleset.
        :return: Dictionary containing the response from the API.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/rulesets/{ruleset_id}"
        return self.parent.make_request("DELETE", endpoint)

    def get_repository_rule_history(self, repo: str, ruleset_id: int, **kwargs: Any) -> Any:
        """
        Get the rule execution history for a ruleset.

        :param repo: The name of the repository.
        :param ruleset_id: The unique identifier of the ruleset.
        :param per_page: (optional) Number of results per page (max 100). Default is 30.
        :param page: (optional) Page number of the results to fetch. Default is 1.
        :return: Dictionary containing the rule execution history.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/rulesets/{ruleset_id}/history"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def get_repository_ruleset_version(self, repo: str, ruleset_id: int, version_id: int) -> Any:
        """
        Get a specific version of a ruleset.

        :param repo: The name of the repository.
        :param ruleset_id: The unique identifier of the ruleset.
        :param version_id: The unique identifier of the ruleset version.
        :return: Dictionary containing the ruleset version details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/rulesets/{ruleset_id}/versions/{version_id}"
        return self.parent.make_request("GET", endpoint)


# -------------------- Webhooks Section -------------------- #
class Webhooks:
    """
    Module for managing repository webhooks.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def list_repository_webhooks(self, repo: str, **kwargs: Any) -> Any:
        """
        List webhooks for a repository.

        :param repo: The name of the repository.
        :param per_page: (optional) Number of results per page (max 100). Default is 30.
        :param page: (optional) Page number of the results to fetch. Default is 1.
        :return: Dictionary containing the list of webhooks.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/hooks"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def create_repository_webhook(self, repo: str, config: Dict[str, Any],
                                   **kwargs: Any) -> Any:
        """
        Create a webhook for a repository.

        :param repo: The name of the repository.
        :param config: Key/value pairs to provide settings for this webhook.
            Refer to GitHub API documentation for config object structure.
            https://docs.github.com/en/rest/repos/webhooks?apiVersion=2022-11-28#create-a-repository-webhook
        :param events: (optional) List of events that trigger the webhook.
            Default is ['push'].
        :param active: (optional) Whether the webhook is active. Default is True.
        :return: Dictionary containing the created webhook details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/hooks"
        data: Dict[str, Any] = {
            "name": "web",
            "config": config,
            "events": kwargs.get("events", ["push"]),
            "active": kwargs.get("active", True)
        }
        return self.parent.make_request("POST", endpoint, json=data)

    def get_repository_webhook(self, repo: str, hook_id: int) -> Any:
        """
        Get a webhook for a repository.

        :param repo: The name of the repository.
        :param hook_id: The unique identifier of the hook.
        :return: Dictionary containing the webhook details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/hooks/{hook_id}"
        return self.parent.make_request("GET", endpoint)

    def update_repository_webhook(self, repo: str, hook_id: int,
                                   **kwargs: Any) -> Any:
        """
        Update a webhook for a repository.

        :param repo: The name of the repository.
        :param hook_id: The unique identifier of the hook.
        :param config: (optional) Key/value pairs to provide settings for this webhook.
            Refer to GitHub API documentation for config object structure.
            https://docs.github.com/en/rest/repos/webhooks?apiVersion=2022-11-28#update-a-repository-webhook
        :param events: (optional) List of events that trigger the webhook.
        :param add_events: (optional) List of events to add to the webhook.
        :param remove_events: (optional) List of events to remove from the webhook.
        :param active: (optional) Whether the webhook is active.
        :return: Dictionary containing the updated webhook details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/hooks/{hook_id}"
        data: Dict[str, Any] = {
            "config": kwargs.get("config"),
            "events": kwargs.get("events"),
            "add_events": kwargs.get("add_events"),
            "remove_events": kwargs.get("remove_events"),
            "active": kwargs.get("active")
        }
        # Remove keys with None values
        data = {k: v for k, v in data.items() if v is not None}
        return self.parent.make_request("PATCH", endpoint, json=data)

    def delete_repository_webhook(self, repo: str, hook_id: int) -> Any:
        """
        Delete a webhook for a repository.

        :param repo: The name of the repository.
        :param hook_id: The unique identifier of the hook.
        :return: Dictionary containing the response from the API.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/hooks/{hook_id}"
        return self.parent.make_request("DELETE", endpoint)

    def get_webhook_config(self, repo: str, hook_id: int) -> Any:
        """
        Get the configuration for a repository webhook.

        :param repo: The name of the repository.
        :param hook_id: The unique identifier of the hook.
        :return: Dictionary containing the webhook configuration.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/hooks/{hook_id}/config"
        return self.parent.make_request("GET", endpoint)

    def update_webhook_config(self, repo: str, hook_id: int,
                              **kwargs: Any) -> Any:
        """
        Update the configuration for a repository webhook.

        :param repo: The name of the repository.
        :param hook_id: The unique identifier of the hook.
        :param url: (optional) The URL to which payloads are delivered.
        :param content_type: (optional) The media type ('json', 'form').
        :param secret: (optional) The secret used to sign the payloads.
        :param insecure_ssl: (optional) Whether to allow insecure SSL.
        :return: Dictionary containing the updated webhook configuration.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/hooks/{hook_id}/config"
        data: Dict[str, Any] = {
            "url": kwargs.get("url"),
            "content_type": kwargs.get("content_type"),
            "secret": kwargs.get("secret"),
            "insecure_ssl": kwargs.get("insecure_ssl")
        }
        # Remove keys with None values
        data = {k: v for k, v in data.items() if v is not None}
        return self.parent.make_request("PATCH", endpoint, json=data)

    def list_webhook_deliveries(self, repo: str, hook_id: int,
                                **kwargs: Any) -> Any:
        """
        List deliveries for a repository webhook.

        :param repo: The name of the repository.
        :param hook_id: The unique identifier of the hook.
        :param per_page: (optional) Number of results per page (max 100). Default is 30.
        :param cursor: (optional) Cursor for pagination.
        :return: Dictionary containing the list of deliveries.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/hooks/{hook_id}/deliveries"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "cursor": kwargs.get("cursor")
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def get_webhook_delivery(self, repo: str, hook_id: int,
                             delivery_id: int) -> Any:
        """
        Get a delivery for a repository webhook.

        :param repo: The name of the repository.
        :param hook_id: The unique identifier of the hook.
        :param delivery_id: The unique identifier of the delivery.
        :return: Dictionary containing the delivery details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/hooks/{hook_id}/deliveries/{delivery_id}"
        return self.parent.make_request("GET", endpoint)

    def redeliver_webhook_delivery(self, repo: str, hook_id: int,
                                   delivery_id: int) -> Any:
        """
        Redeliver a delivery for a repository webhook.

        :param repo: The name of the repository.
        :param hook_id: The unique identifier of the hook.
        :param delivery_id: The unique identifier of the delivery.
        :return: Dictionary containing the response from the API.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/hooks/{hook_id}/deliveries/{delivery_id}/attempts"
        return self.parent.make_request("POST", endpoint)

    def ping_repository_webhook(self, repo: str, hook_id: int) -> Any:
        """
        Ping a repository webhook.

        :param repo: The name of the repository.
        :param hook_id: The unique identifier of the hook.
        :return: Dictionary containing the response from the API.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/hooks/{hook_id}/pings"
        return self.parent.make_request("POST", endpoint)

    def test_push_repository_webhook(self, repo: str, hook_id: int) -> Any:
        """
        Test the push repository webhook.

        :param repo: The name of the repository.
        :param hook_id: The unique identifier of the hook.
        :return: Dictionary containing the response from the API.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/hooks/{hook_id}/tests"
        return self.parent.make_request("POST", endpoint)


# -------------------- Main Repository Class -------------------- #
class Repository:
    """
    Repository module that contains all repository-related submodules.
    """
    def __init__(self, parent: Any) -> None:
        # Initialize Submodules
        self.repositories = Repositories(parent)
        self.autolinks = Autolinks(parent)
        self.contents = Contents(parent)
        self.forks = Forks(parent)
        self.traffic = Traffic(parent)
        self.webhooks = Webhooks(parent)
        self.rulesets = Rules(parent)
