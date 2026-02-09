"""
Actions Module.
"""
from typing import Any, Dict, List

# -------------------- Actions Section -------------------- #
class Artifacts:
    """
    Docstring for Artifacts
    """
    def __init__(self, parent: Any):
        self.parent = parent

    # ----- Artifacts Section---- #
    def list_artifacts(self, repo: str, **kwargs: Any) -> Dict[str, Any]:
        """
        List artifacts for a repository.

        :param repo: Repository name.
        :param per_page: (optional) Number of results per page (max 100).
        :param page: (optional) Page number of the results to fetch.
        :param name: (optional) Filter artifacts by name.
        :return: JSON response containing the list of artifacts.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/artifacts"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1),
            "name": kwargs.get("name", None)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def get_an_artifact(self, repo: str, artifact_id: int) -> Dict[str, Any]:
        """
        Get a specific artifact for a repository.

        :param repo: Repository name.
        :param artifact_id: ID of the artifact to retrieve.
        :return: JSON response containing the artifact details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/artifacts/{artifact_id}"
        return self.parent.make_request("GET", endpoint)

    def delete_an_artifact(self, repo: str, artifact_id: int) -> Dict[str, Any]:
        """
        Delete a specific artifact for a repository.

        :param repo: Repository name.
        :param artifact_id: ID of the artifact to delete.
        :return: JSON response confirming deletion.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/artifacts/{artifact_id}"
        return self.parent.make_request("DELETE", endpoint)

    def download_an_artifact(self, repo: str, artifact_id: int) -> Dict[str, Any]:
        """
        Download a specific artifact for a repository.

        :param repo: Repository name.
        :param artifact_id: ID of the artifact to download.
        :return: JSON response containing the download link.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/artifacts/{artifact_id}/zip"
        return self.parent.make_request("GET", endpoint)

    def list_workflow_run_artifacts(self, repo: str, run_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        List artifacts for a specific workflow run.

        :param repo: Repository name.
        :param run_id: ID of the workflow run.
        :param per_page: (optional) Number of results per page (max 100).
        :param page: (optional) Page number of the results to fetch.
        :param name: (optional) Filter artifacts by name.
        :return: JSON response containing the list of artifacts.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/runs/{run_id}/artifacts"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1),
            "name": kwargs.get("name", None)
        }
        return self.parent.make_request("GET", endpoint, params=params)


class Secrets:
    """
    Docstring for Secrets
    """
    def __init__(self, parent: Any):
        self.parent = parent
    # ----- Secrets Section---- #
    def list_org_secrets(self, **kwargs: Any) -> Dict[str, Any]:
        """
        List organization secrets.

        :param per_page: (optional) Number of results per page (max 100).
        :param page: (optional) Page number of the results to fetch.
        :return: JSON response containing the list of organization secrets.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/secrets"
        params = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def get_org_public_key(self) -> Dict[str, Any]:
        """Get the public key for encrypting organization secrets.

        :return: JSON response containing the public key.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/secrets/public-key"
        return self.parent.make_request("GET", endpoint)

    def get_org_secret(self, secret_name: str) -> Dict[str, Any]:
        """Get a specific organization secret.

        :param secret_name: Name of the secret to retrieve.
        :return: JSON response containing the organization secret details.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/secrets/{secret_name}"
        return self.parent.make_request("GET", endpoint)

    def create_or_update_org_secret(
        self,
        secret_name: str,
        encrypted_secret_value: str,
        visibility: str,
        **kwargs: Any
    ) -> Dict[str, Any]:
        """Create a new organization secret.

        :param secret_name: Name of the secret to create.
        :param secret_value: Value of the secret to create.
        :return: JSON response containing the created organization secret details.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/secrets/{secret_name}"
        data: Dict[str, Any] = {
            "encrypted_value": encrypted_secret_value,
            "key_id": self.get_org_public_key()["key_id"],
            "visibility": visibility,
            "selected_repository_ids": kwargs.get("selected_repository_ids", [])
        }
        return self.parent.make_request("PUT", endpoint, json=data)

    def delete_org_secret(self, secret_name: str) -> Dict[str, Any]:
        """Delete a specific organization secret.

        :param secret_name: Name of the secret to delete.
        :return: JSON response confirming deletion.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/secrets/{secret_name}"
        return self.parent.make_request("DELETE", endpoint)

    def list_repo_access_to_org_secret(self, secret_name: str, **kwargs: Any) -> Dict[str, Any]:
        """
        List repositories with access to a specific organization secret.

        :param secret_name: Name of the organization secret.
        :param per_page: (optional) Number of results per page (max 100).
        :param page: (optional) Page number of the results to fetch.
        :return: JSON response containing the list of repositories.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/secrets/{secret_name}/repositories"
        params = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self.parent.make_request("GET", endpoint, params=params)


    def replace_repo_access_to_org_secret(
            self,
            secret_name: str,
            repo_ids: List[int]) -> Dict[str, Any]:
        """Replaces the list of repositories that can access a specific organization secret.

        :param secret_name: Name of the organization secret.
        :param repo_ids: List of repository IDs to add to the secret.
        \n e.g., [123456, 789012]
        :return: JSON response confirming addition.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/secrets/{secret_name}/repositories"
        data = {"selected_repository_ids": repo_ids}
        return self.parent.make_request("PUT", endpoint, json=data)

    def add_repo_access_to_org_secret(self, secret_name: str, repo_id: int) -> Any:
        """Add a repository to a specific organization secret.

        :param secret_name: Name of the organization secret.
        :param repo_id: ID of the repository to add to the secret.
        :return: JSON response confirming addition.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/secrets/{secret_name}/repositories/{repo_id}"
        return self.parent.make_request("PUT", endpoint)

    def remove_repo_access_from_org_secret(self, secret_name: str, repo_id: int) -> Dict[str, Any]:
        """Remove a repository from a specific organization secret.

        :param secret_name: Name of the organization secret.
        :param repo_id: ID of the repository to remove from the secret.
        :return: JSON response confirming removal.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/secrets/{secret_name}/repositories/{repo_id}"
        return self.parent.make_request("DELETE", endpoint)

    def list_repo_secrets(self, repo: str, **kwargs: Any) -> Dict[str, Any]:
        """List repository secrets.

        :param repo: Repository name.
        :param per_page: (optional) Number of results per page (max 100).
        :param page: (optional) Page number of the results to fetch.
        :return: JSON response containing the list of repository secrets.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/secrets"
        params = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def get_repo_public_key(self, repo: str) -> Dict[str, Any]:
        """Get the public key for encrypting repository secrets.

        :param repo: Repository name.
        :return: JSON response containing the public key.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/secrets/public-key"
        return self.parent.make_request("GET", endpoint)

    def get_repo_secret(self, repo: str, secret_name: str) -> Dict[str, Any]:
        """Get a specific repository secret.

        :param repo: Repository name.
        :param secret_name: Name of the secret to retrieve.
        :return: JSON response containing the repository secret details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/secrets/{secret_name}"
        return self.parent.make_request("GET", endpoint)

    def create_or_update_repo_secret(
        self,
        repo: str,
        secret_name: str,
        encrypted_secret_value: str
    ) -> Dict[str, Any]:
        """Create a new repository secret.

        :param repo: Repository name.
        :param secret_name: Name of the secret to create.
        :param secret_value: Value of the secret to create.
        :return: JSON response containing the created repository secret details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/secrets/{secret_name}"
        data: Dict[str, Any] = {
            "encrypted_value": encrypted_secret_value,
            "key_id": self.get_repo_public_key(repo)["key_id"]
        }
        return self.parent.make_request("PUT", endpoint, json=data)

    def delete_repo_secret(self, repo: str, secret_name: str) -> Dict[str, Any]:
        """Delete a specific repository secret.

        :param repo: Repository name.
        :param secret_name: Name of the secret to delete.
        :return: JSON response confirming deletion.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/secrets/{secret_name}"
        return self.parent.make_request("DELETE", endpoint)

    def list_environment_secrets(self, repo: str, environment_name: str,
                                 **kwargs: Any) -> Dict[str, Any]:
        """List environment secrets for a repository.

        :param repo: Repository name.
        :param environment_name: Name of the environment.
        :param per_page: (optional) Number of results per page (max 100).
        :param page: (optional) Page number of the results to fetch.
        :return: JSON response containing the list of environment secrets.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/environments/{environment_name}/secrets"
        params = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def get_environment_public_key(self, repo: str, environment_name: str) -> Dict[str, Any]:
        """Get the public key for encrypting environment secrets.

        :param repo: Repository name.
        :param environment_name: Name of the environment.
        :return: JSON response containing the public key.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/environments/{environment_name}/secrets/public-key"
        return self.parent.make_request("GET", endpoint)

    def get_environment_secret(self, repo: str, environment_name:
                                str, secret_name: str) -> Dict[str, Any]:
        """Get a specific environment secret.

        :param repo: Repository name.
        :param environment_name: Name of the environment.
        :param secret_name: Name of the secret to retrieve.
        :return: JSON response containing the environment secret details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/environments/{environment_name}/secrets/{secret_name}"
        return self.parent.make_request("GET", endpoint)

    def create_or_update_environment_secret(self, repo: str,
                    environment_name: str, secret_name: str,
                    encrypted_secret_value: str) -> Dict[str, Any]:
        """Create or update an environment secret.

        :param repo: Repository name.
        :param environment_name: Name of the environment.
        :param secret_name: Name of the secret to create or update.
        :param encrypted_secret_value: Encrypted value of the secret.
        :return: JSON response containing the created or updated environment secret details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/environments/{environment_name}/secrets/{secret_name}"
        data: Dict[str, Any] = {
            "encrypted_value": encrypted_secret_value,
            "key_id": self.get_environment_public_key(repo, environment_name)["key_id"]
        }
        return self.parent.make_request("PUT", endpoint, json=data)

    def delete_environment_secret(self, repo: str, environment_name: str,
                                   secret_name: str) -> Dict[str, Any]:
        """Delete a specific environment secret.

        :param repo: Repository name.
        :param environment_name: Name of the environment.
        :param secret_name: Name of the secret to delete.
        :return: JSON response confirming deletion.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/environments/{environment_name}/secrets/{secret_name}"
        return self.parent.make_request("DELETE", endpoint)

class SelfHostedRunners:
    """
    Docstring for SelfHostedRunners
    """
    def __init__(self, parent: Any):
        self.parent = parent
    # ----- Self-Hosted Runners Section---- #
    def list_org_runners(self, **kwargs: Any) -> Dict[str, Any]:
        """List self-hosted runners for an organization.

        :param per_page: (optional) Number of results per page (max 100).
        :param page: (optional) Page number of the results to fetch.
        :param name: (optional) Filter runners by name.
        :return: JSON response containing the list of self-hosted runners.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/runners"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1),
            "name": kwargs.get("name", None)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def list_org_runner_applications(self) -> Dict[str, Any]:
        """List self-hosted runner applications for an organization.

        :return: JSON response containing the list of self-hosted runner applications.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/runners/downloads"
        return self.parent.make_request("GET", endpoint)

    def generate_org_jitconfig(self) -> Dict[str, Any]:
        """Generate a JIT config for self-hosted runners in an organization.

        :return: JSON response containing the JIT config.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/runners/generate-jitconfig"
        return self.parent.make_request("POST", endpoint)

    def create_org_runner_token(self) -> Dict[str, Any]:
        """Create a self-hosted runner registration token for an organization.

        :return: JSON response containing the registration token.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/runners/registration-token"
        return self.parent.make_request("POST", endpoint)

    def create_org_remove_token(self) -> Dict[str, Any]:
        """Create a self-hosted runner removal token for an organization.

        :return: JSON response containing the removal token.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/runners/remove-token"
        return self.parent.make_request("POST", endpoint)

    def get_org_runner(self, runner_id: int) -> Dict[str, Any]:
        """Get a specific self-hosted runner for an organization.

        :param runner_id: ID of the self-hosted runner to retrieve.
        :return: JSON response containing the self-hosted runner details.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/runners/{runner_id}"
        return self.parent.make_request("GET", endpoint)

    def delete_org_runner(self, runner_id: int) -> Dict[str, Any]:
        """Delete a specific self-hosted runner for an organization.

        :param runner_id: ID of the self-hosted runner to delete.
        :return: JSON response confirming deletion.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/runners/{runner_id}"
        return self.parent.make_request("DELETE", endpoint)

    def list_labels_for_org_runners(self, runner_id: int) -> Dict[str, Any]:
        """List labels for a specific self-hosted runner in an organization.

        :param runner_id: ID of the self-hosted runner.
        :return: JSON response containing the list of labels.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/runners/{runner_id}/labels"
        return self.parent.make_request("GET", endpoint)

    def add_labels_to_org_runner(self, runner_id: int, labels: Dict[str, Any]) -> Dict[str, Any]:
        """Adds custom labels to a self-hosted runner configured in an organization.

        :param runner_id: ID of the self-hosted runner.
        :param labels: Dictionary containing labels to add.
        \n e.g., {"labels": ["label1", "label2"]}
        :return: JSON response containing the updated list of labels.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/runners/{runner_id}/labels"
        return self.parent.make_request("POST", endpoint, json=labels)

    def set_custom_labels_to_org_runner(self, runner_id: int,
                                         labels: Dict[str, Any]) -> Dict[str, Any]:
        """Remove all previous custom labels and set the new custom labels for
        a specific self-hosted runner configured in an organization.

        :param runner_id: ID of the self-hosted runner.
        :param labels: Dictionary containing labels to set.
        \n e.g., {"labels": ["label1", "label2"]}
        :return: JSON response containing the updated list of labels.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/runners/{runner_id}/labels"
        return self.parent.make_request("PUT", endpoint, json=labels)

    def remove_labels_from_org_runner(self, runner_id: int) -> Dict[str, Any]:
        """Remove all custom labels from a self-hosted runner configured in an organization.

        :param runner_id: ID of the self-hosted runner.
        :return: JSON response confirming removal.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/runners/{runner_id}/labels"
        return self.parent.make_request("DELETE", endpoint)

    def remove_a_label_from_org_runner(self, runner_id: int, label_name: str) -> Dict[str, Any]:
        """Remove a specific label from a self-hosted runner configured in an organization.

        :param runner_id: ID of the self-hosted runner.
        :param label_name: Name of the label to remove.
        :return: JSON response confirming removal.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/runners/{runner_id}/labels/{label_name}"
        return self.parent.make_request("DELETE", endpoint)

    def list_repository_runners(self, repo: str, **kwargs: Any) -> Dict[str, Any]:
        """List self-hosted runners for a repository.

        :param repo: Repository name.
        :param per_page: (optional) Number of results per page (max 100).
        :param page: (optional) Page number of the results to fetch.
        :param name: (optional) Filter runners by name.
        :return: JSON response containing the list of self-hosted runners.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/runners"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1),
            "name": kwargs.get("name", None)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def list_repo_runner_apps(self, repo: str) -> Dict[str, Any]:
        """List self-hosted runner applications for a repository.

        :param repo: Repository name.
        :return: JSON response containing the list of self-hosted runner applications.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/runners/downloads"
        return self.parent.make_request("GET", endpoint)

    def create_repo_jitconfig(self, repo: str) -> Dict[str, Any]:
        """Generate a JIT config for self-hosted runners in a repository.

        :param repo: Repository name.
        :return: JSON response containing the JIT config.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/runners/generate-jitconfig"
        return self.parent.make_request("POST", endpoint)

    def create_repo_runner_token(self, repo: str) -> Dict[str, Any]:
        """Create a self-hosted runner registration token for a repository.

        :param repo: Repository name.
        :return: JSON response containing the registration token.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/runners/registration-token"
        return self.parent.make_request("POST", endpoint)

    def create_repo_remove_token(self, repo: str) -> Dict[str, Any]:
        """Create a self-hosted runner removal token for a repository.

        :param repo: Repository name.
        :return: JSON response containing the removal token.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/runners/remove-token"
        return self.parent.make_request("POST", endpoint)

    def get_a_runner_for_repository(self, repo: str, runner_id: int) -> Dict[str, Any]:
        """Get a specific self-hosted runner for a repository.

        :param repo: Repository name.
        :param runner_id: ID of the self-hosted runner to retrieve.
        :return: JSON response containing the self-hosted runner details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/runners/{runner_id}"
        return self.parent.make_request("GET", endpoint)

    def delete_a_runner_for_repository(self, repo: str, runner_id: int) -> Dict[str, Any]:
        """Delete a specific self-hosted runner for a repository.

        :param repo: Repository name.
        :param runner_id: ID of the self-hosted runner to delete.
        :return: JSON response confirming deletion.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/runners/{runner_id}"
        return self.parent.make_request("DELETE", endpoint)

    def list_labels_for_runners_in_repository(self, repo: str, runner_id: int) -> Dict[str, Any]:
        """List labels for a specific self-hosted runner in a repository.

        :param repo: Repository name.
        :param runner_id: ID of the self-hosted runner.
        :return: JSON response containing the list of labels.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/runners/{runner_id}/labels"
        return self.parent.make_request("GET", endpoint)

    def add_labels_to_runner_in_repository(
    self,
    repo: str,
    runner_id: int,
    labels: Dict[str, Any]) -> Dict[str, Any]:
        """Adds custom labels to a self-hosted runner configured in a repository.

        :param repo: Repository name.
        :param runner_id: ID of the self-hosted runner.
        :param labels: Dictionary containing labels to add.
        \n e.g., {"labels": ["label1", "label2"]}
        :return: JSON response containing the updated list of labels.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/runners/{runner_id}/labels"
        return self.parent.make_request("POST", endpoint, json=labels)

    def set_custom_labels_to_runner_in_repository(
    self,
    repo: str,
    runner_id: int,
    labels: Dict[str, Any]) -> Dict[str, Any]:
        """Remove all previous custom labels and set the new custom labels for
        a specific self-hosted runner configured in a repository.

        :param repo: Repository name.
        :param runner_id: ID of the self-hosted runner.
        :param labels: Dictionary containing labels to set.
        \n e.g., {"labels": ["label1", "label2"]}
        :return: JSON response containing the updated list of labels.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/runners/{runner_id}/labels"
        return self.parent.make_request("PUT", endpoint, json=labels)

    def remove_labels_from_runner_in_repository(self, repo: str, runner_id: int) -> Dict[str, Any]:
        """Remove all custom labels from a self-hosted runner configured in a repository.

        :param repo: Repository name.
        :param runner_id: ID of the self-hosted runner.
        :return: JSON response confirming removal.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/runners/{runner_id}/labels"
        return self.parent.make_request("DELETE", endpoint)

    def remove_a_label_from_runner_in_repository(
    self,
    repo: str,
    runner_id: int,
    label_name: str) -> Dict[str, Any]:
        """Remove a specific label from a self-hosted runner configured in a repository.

        :param repo: Repository name.
        :param runner_id: ID of the self-hosted runner.
        :param label_name: Name of the label to remove.
        :return: JSON response confirming removal.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/runners/{runner_id}/labels/{label_name}"
        return self.parent.make_request("DELETE", endpoint)

class SelfHostedRunnerGroups:
    """
    Docstring for SelfHostedRunnerGroups
    """
    def __init__(self, parent: Any):
        self.parent = parent
    # ----- Self-Hosted Runner Groups Section---- #
    def list_runner_groups(self, **kwargs: Any):
        """List self-hosted runner groups for an organization.

        :param per_page: (optional) Number of results per page (max 100).
        :param page: (optional) Page number of the results to fetch.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/runner-groups"
        params = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def create_runner_group(self, **kwargs: Any):
        """Create a self-hosted runner group for an organization.

        :param name: Name of the runner group.
        :param visibility: Visibility of the runner group. Default is "selected".
        :param selected_repository_ids: List of repository IDs to include in the group.
        :param runner_ids: List of runner IDs to include in the group.
        :param allows_public_repositories: Whether to allow public repositories. Default is False.
        :param restricted_to_workflows: Whether to restrict to specific workflows. Default is False.
        :param selected_workflows: List of workflows to restrict to.
        :param network_configuration_id: ID of the network configuration to associate with the group.
        :return: JSON response containing the created runner group details.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/runner-groups"
        group_data: Dict[str, Any] = {
            "name": kwargs.get("name"),
            "visibility": kwargs.get("visibility", "selected"),
            "selected_repository_id": kwargs.get("selected_repository_ids", []),
            "runners": kwargs.get("runner_ids", []),
            "allows_public_repositories": kwargs.get("allows_public_repositories", False),
            "restricted_to_workflows": kwargs.get("restricted_to_workflows", False),
            "selected_workflows": kwargs.get("selected_workflows", []),
            "network_configuration_id": kwargs.get("network_configuration_id", None)
        }
        return self.parent.make_request("POST", endpoint, json=group_data)

    def get_org_runner_group(self, runner_group_id: int):
        """Get a specific self-hosted runner group for an organization.

        :param runner group_id: ID of the self-hosted runner group to retrieve.
        :return: JSON response containing the self-hosted runner group details.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/runner-groups/{runner_group_id}"
        return self.parent.make_request("GET", endpoint)

    def update_org_runner_group(self, runner_group_id: int, **kwargs: Any):
        """Update a specific self-hosted runner group for an organization.

        :param runner group_id: ID of the self-hosted runner group to update.
        :param name: name of the runner group to update.
        :param visibility: visibility of the runner group to update.
        :param allows_public_repositories: whether to allow public repositories.
        :param restricted_to_workflows: whether to restrict to specific workflows.
        :param selected_workflows: list of workflows to restrict to.
        :return: JSON response containing the updated runner group details.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/runner-groups/{runner_group_id}"
        update_data: Dict[str, Any] = {
            "name": kwargs.get("name"),
            "visibility": kwargs.get("visibility"),
            "allows_public_repositories": kwargs.get("allows_public_repositories", False),
            "restricted_to_workflows": kwargs.get("restricted_to_workflows", False),
            "selected_workflows": kwargs.get("selected_workflows", []),
            "network_configuration_id": kwargs.get("network_configuration_id", None)
        }
        return self.parent.make_request("PATCH", endpoint, json=update_data)

    def delete_org_runner_group(self, runner_group_id: int):
        """Delete a specific self-hosted runner group for an organization.

        :param runner group_id: ID of the self-hosted runner group to delete.
        :return: JSON response confirming deletion.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/runner-groups/{runner_group_id}"
        return self.parent.make_request("DELETE", endpoint)

    def list_github_hosted_runner_in_group(self, runner_group_id: int):
        """List GitHub-hosted runners in a specific self-hosted runner group.

        :param runner group_id: ID of the self-hosted runner group.
        :return: JSON response containing the list of GitHub-hosted runners.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/runner-groups/{runner_group_id}/hosted-runners"
        return self.parent.make_request("GET", endpoint)

    def list_repo_access_for_runner_group(self, runner_group_id: int):
        """List repositories with access to a specific self-hosted runner group.

        :param runner group_id: ID of the self-hosted runner group.
        :return: JSON response containing the list of repositories.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/runner-groups/{runner_group_id}/repositories"
        return self.parent.make_request("GET", endpoint)

    def replace_repo_access_to_runner_group(self, runner_group_id: int, repo_id: List[int]):
        """Replaces the list of repositories that can access a specific self-hosted runner group.

        :param runner group_id: ID of the self-hosted runner group.
        :param repo_id: List of repository IDs to add to the runner group.
        \n e.g., [123456, 789012]
        :return: JSON response confirming addition.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/runner-groups/{runner_group_id}/repositories"
        repository_data = {"selected_repository_ids": repo_id}
        return self.parent.make_request("PUT", endpoint, json=repository_data)

    def add_repo_access_to_runner_group(self, runner_group_id: int, repo_id: int):
        """Add a repository to a specific self-hosted runner group.

        :param runner group_id: ID of the self-hosted runner group.
        :param repo_id: ID of the repository to add to the runner group.
        :return: JSON response confirming addition.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/runner-groups/{runner_group_id}/repositories/{repo_id}"
        return self.parent.make_request("PUT", endpoint)

    def remove_repo_access_from_runner_group(self, runner_group_id: int, repo_id: int):
        """Remove a repository from a specific self-hosted runner group.

        :param runner group_id: ID of the self-hosted runner group.
        :param repo_id: ID of the repository to remove from the runner group.
        :return: JSON response confirming removal.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/runner-groups/{runner_group_id}/repositories/{repo_id}"
        return self.parent.make_request("DELETE", endpoint)

    def list_self_hosted_runners_in_group(self, runner_group_id: int):
        """List self-hosted runners in a specific self-hosted runner group.

        :param runner group_id: ID of the self-hosted runner group.
        :return: JSON response containing the list of self-hosted runners.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/runner-groups/{runner_group_id}/runners"
        return self.parent.make_request("GET", endpoint)

    def replace_self_hosted_runners_in_group(self, runner_group_id: int, runner_ids: List[int]):
        """Replaces the list of self-hosted runners in a specific self-hosted runner group.

        :param runner group_id: ID of the self-hosted runner group.
        :param runner_ids: List of self-hosted runner IDs to add to the group.
        \n e.g., [123456, 789012]
        :return: JSON response confirming addition.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/runner-groups/{runner_group_id}/runners"
        runners_data = {"runners": runner_ids}
        return self.parent.make_request("PUT", endpoint, json=runners_data)

    def add_self_hosted_runner_to_group(self, runner_group_id: int, runner_id: int):
        """Add a self-hosted runner to a specific self-hosted runner group.

        :param runner group_id: ID of the self-hosted runner group.
        :param runner_id: ID of the self-hosted runner to add to the group.
        :return: JSON response confirming addition.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/runner-groups/{runner_group_id}/runners/{runner_id}"
        return self.parent.make_request("PUT", endpoint)

    def remove_self_hosted_runner_from_group(self, runner_group_id: int, runner_id: int):
        """Remove a self-hosted runner from a specific self-hosted runner group.

        :param runner group_id: ID of the self-hosted runner group.
        :param runner_id: ID of the self-hosted runner to remove from the group.
        :return: JSON response confirming removal.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/runner-groups/{runner_group_id}/runners/{runner_id}"
        return self.parent.make_request("DELETE", endpoint)

class Variables:
    """
    Docstring for Variables
    """
    def __init__(self, parent: Any):
        self.parent = parent
    # ----- Variables Section---- #
    def list_org_variables(self, **kwargs: Any) -> Dict[str, Any]:
        """
        List organization variables.

        :param per_page: (optional) Number of results per page (max 30).
        :param page: (optional) Page number of the results to fetch.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/variables"
        params = {
            "per_page": kwargs.get("per_page", 10),
            "page": kwargs.get("page", 1)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def create_org_variable(self, name: str, value: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Create an organization variable.

        :param name: Name of the variable.
        :param value: Value of the variable.
        :param visibility: (optional) Visibility of the variable. Default is "selected".
        :param selected_repository_ids: (optional) List of repository IDs the variable is visible to.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/variables"
        variable_data: Dict[str, Any] = {
            "name": name,
            "value": value,
            "visibility": kwargs.get("visibility", "selected"),
            "selected_repository_ids": kwargs.get("selected_repository_ids", [])
        }
        return self.parent.make_request("POST", endpoint, json=variable_data)

    def get_org_variable(self, variable_name: str) -> Dict[str, Any]:
        """
        Get an organization variable.

        :param variable_name: Name of the variable to retrieve.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/variables/{variable_name}"
        return self.parent.make_request("GET", endpoint)


    def update_org_variable(self, variable_name: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Update an organization variable.

        :param variable_name: Name of the variable to update.
        :param new_name: (optional) New name for the variable.
        :param new_value: (optional) New value for the variable.
        :param visibility: (optional) Visibility of the variable. Default is "selected".
        :param selected_repository_ids: (optional) List of repository IDs the variable is visible to.
        :return: JSON response containing the updated variable details.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/variables/{variable_name}"
        variable_data = {
            "name": kwargs.get("new_name", variable_name),
            "value": kwargs.get("new_value", ""),
            "visibility": kwargs.get("visibility", "selected"),
            "selected_repository_ids": kwargs.get("selected_repository_ids", [])
        }
        return self.parent.make_request("PATCH", endpoint, json=variable_data)

    def delete_org_variable(self, variable_name: str) -> None:
        """
        Delete an organization variable.

        :param variable_name: Name of the variable to delete.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/variables/{variable_name}"
        return self.parent.make_request("DELETE", endpoint)

    def list_repo_access_to_org_variable(self, variable_name: str, **kwargs: Any) -> Dict[str, Any]:
        """
        List repositories with access to a specific organization variable.

        :param variable_name: Name of the variable.
        :return: JSON response containing the list of repositories.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/variables/{variable_name}/repositories"
        params = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def replace_repo_access_to_org_variable(self, variable_name: str, repo_id: List[int]) -> Dict[str, Any]:
        """
        Replace the list of repositories that can access a specific organization variable.

        :param variable_name: Name of the variable.
        :param repo_id: List of repository IDs to set access for the variable.
        \n e.g., [123456, 789012]
        :return: JSON response confirming the update.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/variables/{variable_name}/repositories"
        repository_data = {"selected_repository_ids": repo_id}
        return self.parent.make_request("PUT", endpoint, json=repository_data)

    def add_repo_access_to_org_variable(self, variable_name: str, repo_id: int) -> Dict[str, Any]:
        """
        Add a repository to the access list of a specific organization variable.

        :param variable_name: Name of the variable.
        :param repo_id: ID of the repository to add.
        :return: JSON response confirming addition.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/variables/{variable_name}/repositories/{repo_id}"
        return self.parent.make_request("PUT", endpoint)

    def remove_repo_access_from_org_variable(self, variable_name: str, repo_id: int) -> None:
        """
        Remove a repository from the access list of a specific organization variable.

        :param variable_name: Name of the variable.
        :param repo_id: ID of the repository to remove.
        :return: JSON response confirming removal.
        """
        endpoint = f"/orgs/{self.parent.org}/actions/variables/{variable_name}/repositories/{repo_id}"
        return self.parent.make_request("DELETE", endpoint)

    def list_org_variables_for_repo(self, repo: str, **kwargs: Any) -> Dict[str, Any]:
        """
        List organization variables available to a specific repository.

        :param repo: Repository name.
        :param per_page: (optional) Number of results per page (max 30).
        :param page: (optional) Page number of the results to fetch.
        :return: JSON response containing the list of organization variables.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/organization-variables"
        params = {
            "per_page": kwargs.get("per_page", 10),
            "page": kwargs.get("page", 1)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def list_repo_variables(self, repo: str, **kwargs: Any) -> Dict[str, Any]:
        """
        List repository variables.

        :param repo: Repository name.
        :param per_page: (optional) Number of results per page (max 30).
        :param page: (optional) Page number of the results to fetch.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/variables"
        params = {
            "per_page": kwargs.get("per_page", 10),
            "page": kwargs.get("page", 1)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def create_repo_variable(self, repo: str, name: str, value: str) -> Dict[str, Any]:
        """
        Create a repository variable.

        :param repo: Repository name.
        :param name: Name of the variable.
        :param value: Value of the variable.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/variables"
        variable_data = {
            "name": name,
            "value": value
        }
        return self.parent.make_request("POST", endpoint, json=variable_data)

    def get_repo_variable(self, repo: str, variable_name: str) -> Dict[str, Any]:
        """
        Get a repository variable.

        :param repo: Repository name.
        :param variable_name: Name of the variable to retrieve.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/variables/{variable_name}"
        return self.parent.make_request("GET", endpoint)

    def update_repo_variable(self, repo: str, variable_name: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Update a repository variable.

        :param repo: Repository name.
        :param variable_name: Name of the variable to update.
        :param new_name: (optional) New name for the variable.
        :param new_value: (optional) New value for the variable.
        :return: JSON response containing the updated variable details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/variables/{variable_name}"
        variable_data = {
            "name": kwargs.get("new_name", variable_name),
            "value": kwargs.get("new_value", "")
        }
        return self.parent.make_request("PATCH", endpoint, json=variable_data)

    def delete_repo_variable(self, repo: str, variable_name: str) -> None:
        """
        Delete a repository variable.

        :param repo: Repository name.
        :param variable_name: Name of the variable to delete.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/variables/{variable_name}"
        return self.parent.make_request("DELETE", endpoint)

    def list_environment_variables_for_repo(self, repo: str, environment_name: str, **kwargs: Any) -> Dict[str, Any]:
        """
        List environment variables for a specific environment in a repository.

        :param repo: Repository name.
        :param environment_name: Name of the environment.
        :param per_page: (optional) Number of results per page (max 30).
        :param page: (optional) Page number of the results to fetch.
        :return: JSON response containing the list of environment variables.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/environments/{environment_name}/variables"
        params = {
            "per_page": kwargs.get("per_page", 10),
            "page": kwargs.get("page", 1)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def create_environment_variable_for_repo(
        self,
        repo: str,
        environment_name: str,
        name: str,
        value: str
        ) -> Dict[str, Any]:
        """
        Create an environment variable for a specific environment in a repository.

        :param repo: Repository name.
        :param environment_name: Name of the environment.
        :param name: Name of the variable.
        :param value: Value of the variable.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/environments/{environment_name}/variables"
        variable_data = {
            "name": name,
            "value": value
        }
        return self.parent.make_request("POST", endpoint, json=variable_data)

    def get_environment_variable_for_repo(
        self,
        repo: str,
        environment_name: str,
        variable_name: str
        ) -> Dict[str, Any]:
        """
        Get an environment variable for a specific environment in a repository.

        :param repo: Repository name.
        :param environment_name: Name of the environment.
        :param variable_name: Name of the variable to retrieve.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/environments/{environment_name}/variables/{variable_name}"
        return self.parent.make_request("GET", endpoint)

    def update_environment_variable_for_repo(
        self,
        repo: str,
        environment_name: str,
        variable_name: str,
        **kwargs: Any
        ) -> Dict[str, Any]:
        """
        Update an environment variable for a specific environment in a repository.

        :param repo: Repository name.
        :param environment_name: Name of the environment.
        :param variable_name: Name of the variable to update.
        :param new_name: (optional) New name for the variable.
        :param new_value: (optional) New value for the variable.
        :return: JSON response containing the updated variable details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/environments/{environment_name}/variables/{variable_name}"
        variable_data = {
            "name": kwargs.get("new_name", variable_name),
            "value": kwargs.get("new_value", "")
        }
        return self.parent.make_request("PATCH", endpoint, json=variable_data)

    def delete_environment_variable_for_repo(
        self,
        repo: str,
        environment_name: str,
        variable_name: str
        ) -> None:
        """
        Delete an environment variable for a specific environment in a repository.

        :param repo: Repository name.
        :param environment_name: Name of the environment.
        :param variable_name: Name of the variable to delete.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/environments/{environment_name}/variables/{variable_name}"
        return self.parent.make_request("DELETE", endpoint)


class WorkflowJobs:
    """
    Docstring for WorkflowJobs
    """
    def __init__(self, parent: Any):
        self.parent = parent
    # ----- Workflow Jobs Section---- #
    def get_job_for_workflow_run(self, repo: str, job_id: int) -> Dict[str, Any]:
        """Get a specific job for a workflow run.

        :param repo: Repository name.
        :param job_id: ID of the job to retrieve.
        :return: JSON response containing the job details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/jobs/{job_id}"
        return self.parent.make_request("GET", endpoint)

    def download_workflow_job_logs(self, repo: str, job_id: int) -> bytes:
        """Download logs for a specific job.

        :param repo: Repository name.
        :param job_id: ID of the job to download logs for.
        :return: Bytes content of the job logs.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/jobs/{job_id}/logs"
        return self.parent.make_request("GET", endpoint, stream=True)

    def list_jobs_for_workflow_run_attempt(
        self,
        repo: str,
        run_id: int,
        attempt_number: int
        ) -> Dict[str, Any]:
        """List jobs for a specific workflow run attempt.

        :param repo: Repository name.
        :param run_id: ID of the workflow run.
        :param attempt_number: Attempt number of the workflow run.
        :return: JSON response containing the list of jobs.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}/jobs"
        return self.parent.make_request("GET", endpoint)

    def list_jobs_for_workflow_run(self, repo: str, run_id: int) -> Dict[str, Any]:
        """List jobs for a specific workflow run.

        :param repo: Repository name.
        :param run_id: ID of the workflow run.
        :return: JSON response containing the list of jobs.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/runs/{run_id}/jobs"
        return self.parent.make_request("GET", endpoint)


class WorkflowRuns:
    """
    Docstring for WorkflowRuns
    """

    def __init__(self, parent: Any):
        self.parent = parent
    # ----- Workflow Runs Section---- #
    def re_run_workflow_job(self, repo: str, job_id: int) -> None:
        """Re-run a specific workflow job.

        :param repo: Repository name.
        :param job_id: ID of the workflow job to re-run.
        :return: JSON response confirming the re-run.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/jobs/{job_id}/rerun"
        return self.parent.make_request("POST", endpoint)

    def list_workflow_runs_for_repo(self, repo: str, **kwargs: Any) -> Dict[str, Any]:
        """List workflow runs for a specific repository.

        :param repo: Repository name.
        :param actor: (optional) Filter by actor.
        :param branch: (optional) Filter by branch.
        :param event: (optional) Filter by event.
        :param status: (optional) Filter by status.
            e.g., "completed", "action_required", "cancelled", "failure",
            "neutral", "skipped", "stale", "success", "timed_out",
            "in_progress", "queued", "requested", "waiting", "pending"
        :param per_page: (optional) Number of results per page (max 100).
        :param page: (optional) Page number of the results to fetch.
        :param created: (optional) Filter by creation date.
            e.g., "2020-07-08T00:00:00Z..2020-07-10T00:00:00Z"
        :param exclude_pull_requests: (optional) Exclude pull request workflow runs.
        :param check_suite_id: (optional) Filter by check suite ID.
        :param head_sha: (optional) Filter by head SHA.
        :return: JSON response containing the list of workflow runs.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/runs"
        params: Dict[str, Any] = {
            "actor": kwargs.get("actor", None),
            "branch": kwargs.get("branch", None),
            "event": kwargs.get("event", None),
            "status": kwargs.get("status", None),
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1),
            "created": kwargs.get("created", None),
            "exclude_pull_requests": kwargs.get("exclude_pull_requests", False),
            "check_suite_id": kwargs.get("check_suite_id", None),
            "head_sha": kwargs.get("head_sha", None)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def get_workflow_run(self, repo: str, run_id: int) -> Dict[str, Any]:
        """Get a specific workflow run.

        :param repo: Repository name.
        :param run_id: ID of the workflow run to retrieve.
        :return: JSON response containing the workflow run details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/runs/{run_id}"
        return self.parent.make_request("GET", endpoint)

    def delete_workflow_run(self, repo: str, run_id: int) -> None:
        """Delete a specific workflow run.

        :param repo: Repository name.
        :param run_id: ID of the workflow run to delete.
        :return: JSON response confirming deletion.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/runs/{run_id}"
        return self.parent.make_request("DELETE", endpoint)

    def get_reviewed_workflow_run(self, repo: str, run_id: int) -> Dict[str, Any]:
        """Get a specific reviewed workflow run.

        :param repo: Repository name.
        :param run_id: ID of the reviewed workflow run to retrieve.
        :return: JSON response containing the reviewed workflow run details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/runs/{run_id}/approvals"
        return self.parent.make_request("GET", endpoint)

    def approve_workflow_run_fork(
        self,
        repo: str,
        run_id: int,
        approval_data: Dict[str, Any]
        ) -> Dict[str, Any]:
        """Approve a specific workflow run from a forked repository.

        :param repo: Repository name.
        :param run_id: ID of the workflow run to approve.
        :param approval_data: Dictionary containing approval details.
        :return: JSON response confirming the approval.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/runs/{run_id}/approve"
        return self.parent.make_request("POST", endpoint, json=approval_data)

    def get_workflow_run_attempt(self, repo: str, run_id: int, attempt_number: int) -> Dict[str, Any]:
        """Get a specific attempt for a workflow run.

        :param repo: Repository name.
        :param run_id: ID of the workflow run.
        :param attempt_number: Attempt number to retrieve.
        :return: JSON response containing the workflow run attempt details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}"
        return self.parent.make_request("GET", endpoint)

    def download_workflow_run_attempt_logs(
        self,
        repo: str,
        run_id: int,
        attempt_number: int
        ) -> bytes:
        """Download logs for a specific attempt of a workflow run.

        :param repo: Repository name.
        :param run_id: ID of the workflow run.
        :param attempt_number: Attempt number to download logs for.
        :return: Bytes content of the workflow run attempt logs.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}/logs"
        return self.parent.make_request("GET", endpoint, stream=True)

    def cancel_workflow_run(self, repo: str, run_id: int) -> None:
        """Cancel a specific workflow run.

        :param repo: Repository name.
        :param run_id: ID of the workflow run to cancel.
        :return: JSON response confirming cancellation.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/runs/{run_id}/cancel"
        return self.parent.make_request("POST", endpoint)

    def review_custom_deployment_for_workflow_run(
        self,
        repo: str,
        run_id: int,
        review_data: Dict[str, Any]
        ) -> Dict[str, Any]:
        """Approve or reject custom deployment protection rules
        provided by a GitHub App for a workflow run.

        :param repo: Repository name.
        :param run_id: ID of the workflow run.
        :param review_data: Dictionary containing review details.
        :return: JSON response confirming the review.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/runs/{run_id}/deployment_protection_rule"
        return self.parent.make_request("POST", endpoint, json=review_data)

    def force_cancel_workflow_run(self, repo: str, run_id: int) -> None:
        """Force cancel a specific workflow run.

        :param repo: Repository name.
        :param run_id: ID of the workflow run to force cancel.
        :return: JSON response confirming force cancellation.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/runs/{run_id}/force_cancel"
        return self.parent.make_request("POST", endpoint)

    def download_workflow_run_logs(self, repo: str, run_id: int) -> bytes:
        """Download logs for a specific workflow run.

        :param repo: Repository name.
        :param run_id: ID of the workflow run to download logs for.
        :return: Bytes content of the workflow run logs.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/runs/{run_id}/logs"
        return self.parent.make_request("GET", endpoint, stream=True)

    def delete_workflow_run_logs(self, repo: str, run_id: int) -> None:
        """Delete logs for a specific workflow run.

        :param repo: Repository name.
        :param run_id: ID of the workflow run to delete logs for.
        :return: JSON response confirming deletion.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/runs/{run_id}/logs"
        return self.parent.make_request("DELETE", endpoint)

    def get_pending_deployments_for_workflow_run(self, repo: str, run_id: int) -> Dict[str, Any]:
        """Get pending deployments for a specific workflow run.

        :param repo: Repository name.
        :param run_id: ID of the workflow run.
        :return: JSON response containing the list of pending deployments.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/runs/{run_id}/pending_deployments"
        return self.parent.make_request("GET", endpoint)

    def review_pending_deployment_for_workflow_run(
        self,
        repo: str,
        run_id: int,
        **kwargs: Any
        ) -> Dict[str, Any]:
        """Approve or reject pending deployments for a specific workflow run.

        :param repo: Repository name.
        :param run_id: ID of the workflow run.
        :param review_data: Dictionary containing review details.
        :return: JSON response confirming the review.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/runs/{run_id}/pending_deployments"
        review_data = {
            "environment_ids": kwargs.get("environment_ids", []),
            "state": kwargs.get("state", "approved"),
            "comment": kwargs.get("comment", "")
        }
        return self.parent.make_request("POST", endpoint, json=review_data)


    def re_run_workflow_run(self, repo: str, run_id: int, **kwargs: Any) -> None:
        """Re-run a specific workflow run.

        :param repo: Repository name.
        :param run_id: ID of the workflow run to re-run.
        :param rerun_type: (optional) Type of re-run. Default is "all".
            e.g., "all", "failed_jobs"
        :return: JSON response confirming the re-run.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/runs/{run_id}/rerun"
        params = {
            "rerun_type": kwargs.get("rerun_type", "all")
        }
        return self.parent.make_request("POST", endpoint, json=params)

    def re_run_failed_jobs_for_workflow_run(self, repo: str, run_id: int) -> None:
        """Re-run failed jobs for a specific workflow run.

        :param repo: Repository name.
        :param run_id: ID of the workflow run to re-run failed jobs for.
        :return: JSON response confirming the re-run.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/runs/{run_id}/rerun-failed-jobs"
        return self.parent.make_request("POST", endpoint)

    def list_workflow_runs_for_workflow(self, repo: str, workflow_id: int, **kwargs: Any) -> Dict[str, Any]:
        """List workflow runs for a specific workflow.

        :param repo: Repository name.
        :param actor: (optional) Filter by actor.
        :param branch: (optional) Filter by branch.
        :param event: (optional) Filter by event.
        :param status: (optional) Filter by status.
            e.g., "completed", "action_required", "cancelled", "failure",
            "neutral", "skipped", "stale", "success", "timed_out",
            "in_progress", "queued", "requested", "waiting", "pending"
        :param per_page: (optional) Number of results per page (max 100).
        :param page: (optional) Page number of the results to fetch.
        :param created: (optional) Filter by creation date.
            e.g., "2020-07-08T00:00:00Z..2020-07-10T00:00:00Z"
        :param exclude_pull_requests: (optional) Exclude pull request workflow runs.
        :param check_suite_id: (optional) Filter by check suite ID.
        :param head_sha: (optional) Filter by head SHA.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/workflows/{workflow_id}/runs"
        params: Dict[str, Any] = {
            "actor": kwargs.get("actor", None),
            "branch": kwargs.get("branch", None),
            "event": kwargs.get("event", None),
            "status": kwargs.get("status", None),
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1),
            "created": kwargs.get("created", None),
            "exclude_pull_requests": kwargs.get("exclude_pull_requests", False),
            "check_suite_id": kwargs.get("check_suite_id", None),
            "head_sha": kwargs.get("head_sha", None)
        }
        return self.parent.make_request("GET", endpoint, params=params)

class Workflows:
    def __init__(self, parent: Any):
        self.parent = parent
    # ----- Workflows Section---- #
    def list_workflows(self, repo: str, **kwargs: Any) -> Dict[str, Any]:
        """
        List workflows for a specific repository.

        :param repo: Repository name.
        :return: JSON response containing the list of workflows.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/workflows"
        params = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def get_workflow(self, repo: str, workflow_id: int) -> Dict[str, Any]:
        """
        Get a specific workflow for a repository.

        :param repo: Repository name.
        :param workflow_id: ID of the workflow to retrieve.
        :return: JSON response containing the workflow details.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/workflows/{workflow_id}"
        return self.parent.make_request("GET", endpoint)

    def disable_workflow(self, repo: str, workflow_id: int) -> None:
        """
        Disable a specific workflow for a repository.

        :param repo: Repository name.
        :param workflow_id: ID of the workflow to disable.
        :return: JSON response confirming the disable action.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/workflows/{workflow_id}/disable"
        return self.parent.make_request("PUT", endpoint)

    def dispatch_workflow(
        self,
        repo: str,
        workflow_id: int,
        ref: str,
        **kwargs: Any) -> None:
        """
        Dispatch (trigger) a specific workflow for a repository.

        :param repo: Repository name.
        :param workflow_id: ID of the workflow to dispatch.
        :param ref: The git reference for the workflow (branch or tag).
        :param inputs: (optional) Dictionary of input parameters for the workflow.
            e.g., {"input1": "value1", "input2": "value2"}
        :return: JSON response confirming the dispatch action.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/workflows/{workflow_id}/dispatches"
        data: Dict[str, Any] = {
            "ref": ref,
            "inputs": kwargs.get("inputs", {})
        }
        return self.parent.make_request("POST", endpoint, json=data)

    def enable_workflow(self, repo: str, workflow_id: int) -> None:
        """
        Enable a specific workflow for a repository.

        :param repo: Repository name.
        :param workflow_id: ID of the workflow to enable.
        :return: JSON response confirming the enable action.
        """
        endpoint = f"/repos/{self.parent.org}/{repo}/actions/workflows/{workflow_id}/enable"
        return self.parent.make_request("PUT", endpoint)

class Actions:
    """
    Docstring for Actions
    """
    def __init__(self, parent: Any):
        self.parent = parent

        # Instantiate submodules
        self.artifacts = Artifacts(parent)
        self.secrets = Secrets(parent)
        self.self_hosted_runners = SelfHostedRunners(parent)
        self.self_hosted_runner_groups = SelfHostedRunnerGroups(parent)
        self.variables = Variables(parent)
        self.workflow_jobs = WorkflowJobs(parent)
        self.workflow_runs = WorkflowRuns(parent)
        self.workflows = Workflows(parent)
