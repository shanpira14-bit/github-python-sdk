"""
Module for managing deployments and related submodules.
"""

from typing import Any, Dict

class DeploymentBranchPolicies:
    """
    Submodule for managing deployment branch policies.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def list_policies(self, repo: str, environment_name: str, **kwargs: Any) -> Dict[str, Any]:
        """
        List deployment branch policies for a given repository.

        :param repo: Repository name.
        :return: JSON response from the API.
        """
        endpoint = f"/repos/{self.parent.owner}/{repo}/environments/{environment_name}/deployment-branch-policies"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        response = self.parent.make_request("GET", endpoint, params=params)
        return response

    def create_policy(self, repo: str, environment_name: str,
                      name: str,  **kwargs: Any) -> Dict[str, Any]:
        """
        Create a deployment branch policy for a given repository.

        :param repo: Repository name.
        :param policy_data: Dictionary containing policy details.
        :return: JSON response from the API.
        """
        endpoint = f"/repos/{self.parent.owner}/{repo}/environments/{environment_name}/deployment-branch-policies"
        data: Dict[str, Any] = {
            "name": name,
            "type": kwargs.get("type", ""),
        }
        response = self.parent.make_request("POST", endpoint, json=data)
        return response

    def get_deployment_policy(self, repo: str, environment_name: str,
                              policy_id: int) -> Dict[str, Any]:
        """
        Get a specific deployment branch policy by ID.

        :param repo: Repository name.
        :param policy_id: ID of the deployment branch policy.
        :return: JSON response from the API.
        """
        endpoint = f"/repos/{self.parent.owner}/{repo}/environments/{environment_name}/deployment-branch-policies/{policy_id}"
        response = self.parent.make_request("GET", endpoint)
        return response

    def update_policy(self, repo: str, environment_name: str,
                      branch_policy_id: str, name: str) -> Dict[str, Any]:
        """
        Update a deployment branch policy for a given repository.

        :param repo: Repository name.
        :param policy_id: ID of the deployment branch policy.
        :param policy_data: Dictionary containing updated policy details.
        :return: JSON response from the API.
        """
        endpoint = f"/repos/{self.parent.owner}/{repo}/environments/{environment_name}/deployment-branch-policies/{branch_policy_id}"
        data: Dict[str, Any] = {
            "name": name,
        }
        response = self.parent.make_request("PUT", endpoint, json=data)
        return response

    def delete_policy(self, repo: str, environment_name: str,
                      policy_id: int) -> None:
        """
        Delete a specific deployment branch policy by ID.

        :param repo: Repository name.
        :param policy_id: ID of the deployment branch policy.
        """
        endpoint = f"/repos/{self.parent.owner}/{repo}/environments/{environment_name}/deployment-branch-policies/{policy_id}"
        self.parent.make_request("DELETE", endpoint)


class Deployments:
    """
    Submodule for managing deployments.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def list_deployments(self, repo: str, **kwargs: Any) -> Dict[str, Any]:
        """
        List deployments for a given repository.

        :param repo: Repository name.
        :return: JSON response from the API.
        """
        endpoint = f"/repos/{self.parent.owner}/{repo}/deployments"
        params: Dict[str, Any] = {
            "sha": kwargs.get("sha", ""),
            "ref": kwargs.get("ref", ""),
            "task": kwargs.get("task", ""),
            "environment": kwargs.get("environment", ""),
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        response = self.parent.make_request("GET", endpoint, params=params)
        return response

    def create_deployment(self, repo: str, ref: str,
                          **kwargs: Any) -> Dict[str, Any]:

        """
        Create a deployment for a given repository.
        :param repo: Repository name.
        :param ref: The ref to deploy.
        :task: The task to execute (default: "deploy").
        :auto_merge: Whether to auto-merge the default branch into the ref (default:true).
        :required_contexts: List of status contexts to check before deployment (default: []).
        :payload: Optional JSON payload with extra information about the deployment (default: {}).
        :environment: The name of the environment to deploy to (default: "production").
        :description: Optional description of the deployment (default: "").
        :transient_environment: Whether the environment is transient (default: false).
        :production_environment: Whether the environment is a production environment (default: true).
        :return: JSON response from the API.
        """
        endpoint = f"/repos/{self.parent.owner}/{repo}/deployments"
        data: Dict[str, Any] = {
            "ref": ref,
            "task": kwargs.get("task", "deploy"),
            "auto_merge": kwargs.get("auto_merge", False),
            "required_contexts": kwargs.get("required_contexts", []),
            "payload": kwargs.get("payload", {}),
            "environment": kwargs.get("environment", "production"),
            "description": kwargs.get("description", ""),
            "transient_environment": kwargs.get("transient_environment", False),
            "production_environment": kwargs.get("production_environment", True)
        }
        response = self.parent.make_request("POST", endpoint, json=data)
        return response

    def get_deployment(self, repo: str, deployment_id: int) -> Dict[str, Any]:
        """
        Get a specific deployment by ID.

        :param repo: Repository name.
        :param deployment_id: ID of the deployment.
        :return: JSON response from the API.
        """
        endpoint = f"/repos/{self.parent.owner}/{repo}/deployments/{deployment_id}"
        response = self.parent.make_request("GET", endpoint)
        return response

    def delete_deployment(self, repo: str, deployment_id: int) -> None:
        """
        Delete a specific deployment by ID.

        :param repo: Repository name.
        :param deployment_id: ID of the deployment.
        """
        endpoint = f"/repos/{self.parent.owner}/{repo}/deployments/{deployment_id}"
        self.parent.make_request("DELETE", endpoint)

class Environment:
    """
    Submodule for managing deployment environments.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def list_environments(self, repo: str, **kwargs: Any) -> Dict[str, Any]:
        """
        List environments for a given repository.

        :param repo: Repository name.
        :return: JSON response from the API.
        """
        endpoint = f"/repos/{self.parent.owner}/{repo}/environments"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        response = self.parent.make_request("GET", endpoint, params=params)
        return response

    def get_environment(self, repo: str, environment_name: str) -> Dict[str, Any]:
        """
        Get a specific environment by name.

        :param repo: Repository name.
        :param environment_name: Name of the environment.
        :return: JSON response from the API.
        """
        endpoint = f"/repos/{self.parent.owner}/{repo}/environments/{environment_name}"
        response = self.parent.make_request("GET", endpoint)
        return response

    def create_or_update_environment(self, repo: str, environment_name: str,
                                 **kwargs: Any) -> Dict[str, Any]:
        """
        Create or update an environment for a given repository.

        :param repo: Repository name.
        :param environment_name: Name of the environment.
        :return: JSON response from the API.
        """
        endpoint = f"/repos/{self.parent.owner}/{repo}/environments/{environment_name}"
        data: Dict[str, Any] = {
            "wait_timer": kwargs.get("wait_timer", 0),
            "prevent_self_review": kwargs.get("prevent_self_review", False),
            "reviewers": {
                "type": kwargs.get("reviewers", ""),
                "id": kwargs.get("reviewers_id")
            },
            "deployment_branch_policy": {
                "protected_branches": kwargs.get("protected_branches", False),
                "custom_branch_policies": kwargs.get("custom_branch_policies", False)
            }
        }
        response = self.parent.make_request("PUT", endpoint, json=data)
        return response


    def delete_environment(self, repo: str, environment_name: str) -> None:
        """
        Delete a specific environment by name.

        :param repo: Repository name.
        :param environment_name: Name of the environment.
        """
        endpoint = f"/repos/{self.parent.owner}/{repo}/environments/{environment_name}"
        self.parent.make_request("DELETE", endpoint)

class ProtectionRules:
    """
    Submodule for managing deployment protection rules.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def get_all_protection_rules(self, repo: str, environment_name: str) -> Dict[str, Any]:
        """
        Get all deployment protection rules for a given environment.

        :param repo: Repository name.
        :param environment_name: Name of the environment.
        :return: JSON response from the API.
        """
        endpoint = f"/repos/{self.parent.owner}/{repo}/environments/{environment_name}/deployment_protection_rules"
        response = self.parent.make_request("GET", endpoint)
        return response

    def create_custom_deployment_protection_rule(self, repo: str, environment_name: str,
                                              **kwargs: Any) -> Dict[str, Any]:
        """
        Create a custom deployment protection rule for a given environment.

        :param repo: Repository name.
        :param environment_name: Name of the environment.
        :param rule_data: Dictionary containing rule details.
        :return: JSON response from the API.
        """
        endpoint = f"/repos/{self.parent.owner}/{repo}/environments/{environment_name}/deployment_protection_rules"
        data: Dict[str, Any] = {
            "integration_id": kwargs.get("integration_id")
        }
        response = self.parent.make_request("POST", endpoint, json=data)
        return response

    def list_custom_deployment_rule_integrations(self, repo: str, environment_name: str,
                                                 **kwargs: Any) -> Dict[str, Any]:
        """
        List custom deployment rule integrations for a given environment.

        :param repo: Repository name.
        :param environment_name: Name of the environment.
        :return: JSON response from the API.
        """
        endpoint = f"/repos/{self.parent.owner}/{repo}/environments/{environment_name}/deployment_protection_rules/apps"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        response = self.parent.make_request("GET", endpoint, params=params)
        return response

    def get_custom_deployment_protection_rule(self, repo: str, environment_name: str,
                                            rule_id: int) -> Dict[str, Any]:
        """
        Get a specific custom deployment protection rule by ID.

        :param repo: Repository name.
        :param environment_name: Name of the environment.
        :param rule_id: ID of the deployment protection rule.
        :return: JSON response from the API.
        """
        endpoint = f"/repos/{self.parent.owner}/{repo}/environments/{environment_name}/deployment_protection_rules/{rule_id}"
        response = self.parent.make_request("GET", endpoint)
        return response

    def disable_custom_deployment_protection_rule(self, repo: str, environment_name: str,
                                           rule_id: int) -> None:
        """
        Disable a specific custom deployment protection rule by ID.

        :param repo: Repository name.
        :param environment_name: Name of the environment.
        :param rule_id: ID of the deployment protection rule.
        """
        endpoint = f"/repos/{self.parent.owner}/{repo}/environments/{environment_name}/deployment_protection_rules/{rule_id}"
        self.parent.make_request("DELETE", endpoint)

class Status:
    """
    Submodule for managing deployment statuses.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def list_deployment_statuses(self, repo: str, deployment_id: int,
                                 **kwargs: Any) -> Dict[str, Any]:
        """
        List deployment statuses for a given deployment.

        :param repo: Repository name.
        :param deployment_id: ID of the deployment.
        :return: JSON response from the API.
        """
        endpoint = f"/repos/{self.parent.owner}/{repo}/deployments/{deployment_id}/statuses"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        response = self.parent.make_request("GET", endpoint, params=params)
        return response

    def create_deployment_status(self, repo: str, deployment_id: int,
                                 state: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Create a deployment status for a given deployment.

        :param repo: Repository name.
        :param deployment_id: ID of the deployment.
        :param state: State of the deployment status.
            e.g., "error", "failure", "inactive", "in_progress", "queued", "pending", "success".
        :param target_url: (optional) URL to associate with this status.
        :param log_url: (optional) URL for the deployment logs.
        :param description: (optional) Short description of the status.
        :param environment: (optional) Name of the environment.
        :param environment_url: (optional) URL for accessing the environment.
        :param auto_inactive: (optional) Automatically set previous deployment
            statuses to inactive (default: True).
        :return: JSON response from the API.
        """
        endpoint = f"/repos/{self.parent.owner}/{repo}/deployments/{deployment_id}/statuses"
        data: Dict[str, Any] = {
            "state": state,
            "target_url": kwargs.get("target_url", ""),
            "log_url": kwargs.get("log_url", ""),
            "description": kwargs.get("description", ""),
            "environment": kwargs.get("environment", ""),
            "environment_url": kwargs.get("environment_url", ""),
            "auto_inactive": kwargs.get("auto_inactive", True)
        }
        response = self.parent.make_request("POST", endpoint, json=data)
        return response

    def get_deployment_status(self, repo: str, deployment_id: int,
                              status_id: int) -> Dict[str, Any]:
        """
        Get a specific deployment status by ID.

        :param repo: Repository name.
        :param deployment_id: ID of the deployment.
        :param status_id: ID of the deployment status.
        :return: JSON response from the API.
        """
        endpoint = f"/repos/{self.parent.owner}/{repo}/deployments/{deployment_id}/statuses/{status_id}"
        response = self.parent.make_request("GET", endpoint)
        return response

class Deployment:
    """
    Main module for managing deployments and related submodules.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

        # Initialize submodules
        self.branch_policies = DeploymentBranchPolicies(parent)
        self.deployments = Deployments(parent)
        self.environment = Environment(parent)
        self.protection_rules = ProtectionRules(parent)