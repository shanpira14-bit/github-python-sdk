"""
Organization module to manage organization-related functionalities.
"""

from typing import Any, Dict, List

class ApiInsights:
    """
      ApiInsights module for interacting with GitHub Organization API Insights.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    # Code for ApiInsights methods would go here
    def get_route_stats_by_actor(self, actor_type: str, actor_id: str,
                                 **kwargs: Any) -> Any:
        """
        Retrieve route statistics for a specific actor within the organization.

        :param actor_type: The type of actor (e.g., 'installation', 'classic_pat',
          'fine_grained_pat', 'oauth_app', 'github_app_user_to_server').
        :param actor_id: The unique identifier of the actor.
        :param min_timestamp: (optional) The minimum timestamp to query for stats.
          This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.
        :param max_timestamp: (optional) The maximum timestamp to query for stats.
          This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.
        :param page: (optional) Page number of the results to fetch. Default is 1.
        :param per_page: (optional) Number of results per page. Default is 30
        :param direction: (optional) Direction of the results. Can be 'asc' or 'desc'.
        :param sort: (optional) The field to sort results by.
        :param api_route_substring: (optional) Providing a substring will filter results where
          the API route contains the substring. This is a case-insensitive search.
        :return: List of route statistics.
        """
        endpoint = f"/orgs/{self.parent.org}/insights/api/route-stats/{actor_type}/{actor_id}"
        params: Dict[str, Any] = {
            "min_timestamp": kwargs.get("min_timestamp"),
            "max_timestamp": kwargs.get("max_timestamp"),
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1),
            "direction": kwargs.get("direction", "asc"),
            "sort": kwargs.get("sort"),
            "api_route_substring": kwargs.get("api_route_substring")
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def get_subject_stats(self, **kwargs: Any) -> Any:
        """
        Get API request statistics for all subjects within an organization
          within a specified time frame.

        :param min_timestamp: (optional) The minimum timestamp to query for stats.
          This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.
        :param max_timestamp: (optional) The maximum timestamp to query for stats.
          This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.
        :param page: (optional) Page number of the results to fetch. Default is 1.
        :param per_page: (optional) Number of results per page. Default is 30
        :param direction: (optional) Direction of the results. Can be 'asc' or 'desc'.
        :param sort: (optional) The field to sort results by.
        :param subject_name_substring: (optional) Providing a substring will filter results where
          the subject name contains the substring. This is a case-insensitive search.
        :return: List of subject statistics.
        """
        endpoint = f"/orgs/{self.parent.org}/insights/api/subject-stats"
        params: Dict[str, Any] = {
            "min_timestamp": kwargs.get("min_timestamp"),
            "max_timestamp": kwargs.get("max_timestamp"),
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1),
            "direction": kwargs.get("direction", "asc"),
            "sort": kwargs.get("sort"),
            "subject_name_substring": kwargs.get("subject_name_substring")
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def get_summary_stats(self, **kwargs: Any) -> Any:
        """
        Get a summary of API request statistics for the organization
          within a specified time frame.
        :param min_timestamp: (optional) The minimum timestamp to query for stats.
          This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.
        :param max_timestamp: (optional) The maximum timestamp to query for stats.
          This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.
        :return: Summary of API request statistics.
        """
        endpoint = f"/orgs/{self.parent.org}/insights/api/summary-stats"
        params: Dict[str, Any] = {
            "min_timestamp": kwargs.get("min_timestamp"),
            "max_timestamp": kwargs.get("max_timestamp")
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def get_summary_stats_by_user(self, user_id: str,
                              **kwargs: Any) -> Any:
        """
        Get a summary of API request statistics for a specific user
          within the organization and a specified time frame.

        :param user_id: The unique identifier of the user.
        :param min_timestamp: (optional) The minimum timestamp to query for stats.
          This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.
        :param max_timestamp: (optional) The maximum timestamp to query for stats.
          This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.
        :return: Summary of API request statistics for the user.
        """
        endpoint = f"/orgs/{self.parent.org}/insights/api/summary-stats/users/{user_id}"
        params: Dict[str, Any] = {
            "min_timestamp": kwargs.get("min_timestamp"),
            "max_timestamp": kwargs.get("max_timestamp")
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def get_summary_stats_by_actor(self, actor_type: str, actor_id: str,
                              min_timestamp: str, **kwargs: Any) -> Any:
        """
        Get a summary of API request statistics for a specific actor
          within the organization and a specified time frame.

        :param actor_type: The type of actor (e.g., 'installation', 'classic_pat',
          'fine_grained_pat', 'oauth_app', 'github_app_user_to_server').
        :param actor_id: The unique identifier of the actor.
        :param min_timestamp: The minimum timestamp to query for stats.
          This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.
        :param max_timestamp: (optional) The maximum timestamp to query for stats.
          This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.
        :return: Summary of API request statistics for the actor.
        """
        endpoint = f"/orgs/{self.parent.org}/insights/api/summary-stats/{actor_type}/{actor_id}"
        params: Dict[str, Any] = {
            "min_timestamp": min_timestamp,
            "max_timestamp": kwargs.get("max_timestamp")
        }
        return self.parent.make_request("GET", endpoint, params=params)


    def get_time_stats(self, min_timestamp: str, timestamp_increment: str = "1h",
                       **kwargs: Any) -> Any:
        """
        Get API request statistics over time for the organization
          within a specified time frame.

        :param min_timestamp: The minimum timestamp to query for stats.
          This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.
        :param max_timestamp: (optional) The maximum timestamp to query for stats.
          This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.
        :param timestamp_increment: The time increment for the stats.
          Can be '5m', '10m', '1h', etc. Default is '1h'.
        :return: List of time-based statistics.
        """
        endpoint = f"/orgs/{self.parent.org}/insights/api/time-stats"
        params: Dict[str, Any] = {
            "min_timestamp": min_timestamp,
            "max_timestamp": kwargs.get("max_timestamp"),
            "timestamp_increment": timestamp_increment
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def get_time_stats_by_user(self, user_id: str, min_timestamp: str,
                               timestamp_increment: str = "1h",
                               **kwargs: Any) -> Any:
        """
        Get API request statistics over time for a specific user
          within the organization and a specified time frame.

        :param user_id: The unique identifier of the user.
        :param min_timestamp: The minimum timestamp to query for stats.
          This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.
        :param max_timestamp: (optional) The maximum timestamp to query for stats.
          This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.
        :param timestamp_increment: The time increment for the stats.
          Can be '5m', '10m', '1h', etc. Default is '1h'.
        :return: List of time-based statistics for the user.
        """
        endpoint = f"/orgs/{self.parent.org}/insights/api/time-stats/users/{user_id}"
        params: Dict[str, Any] = {
            "min_timestamp": min_timestamp,
            "max_timestamp": kwargs.get("max_timestamp"),
            "timestamp_increment": timestamp_increment
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def get_time_stats_by_actor(self, actor_type: str, actor_id: str,
                               min_timestamp: str,
                               timestamp_increment: str = "1h",
                               **kwargs: Any) -> Any:
        """
        Get API request statistics over time for a specific actor
          within the organization and a specified time frame.

        :param actor_type: The type of actor (e.g., 'installation', 'classic_pat',
          'fine_grained_pat', 'oauth_app', 'github_app_user_to_server').
        :param actor_id: The unique identifier of the actor.
        :param min_timestamp: The minimum timestamp to query for stats.
          This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.
        :param max_timestamp: (optional) The maximum timestamp to query for stats.
          This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.
        :param timestamp_increment: The time increment for the stats.
          Can be '5m', '10m', '1h', etc. Default is '1h'.
        :return: List of time-based statistics for the actor.
        """
        endpoint = f"/orgs/{self.parent.org}/insights/api/time-stats/{actor_type}/{actor_id}"
        params: Dict[str, Any] = {
            "min_timestamp": min_timestamp,
            "max_timestamp": kwargs.get("max_timestamp"),
            "timestamp_increment": timestamp_increment
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def get_user_stats(self, user_id: str, **kwargs: Any) -> Any:
        """
        Retrieve API request statistics for a specific user within the organization.

        :param user_id: The unique identifier of the user.
        :param min_timestamp: (optional) The minimum timestamp to query for stats.
          This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.
        :param max_timestamp: (optional) The maximum timestamp to query for stats.
          This is a timestamp in ISO 8601 format: YYYY-MM-DDTHH:MM:SSZ.
        :param page: (optional) Page number of the results to fetch. Default is 1.
        :param per_page: (optional) Number of results per page. Default is 30
        :param direction: (optional) Direction of the results. Can be 'asc' or 'desc'.
        :param sort: (optional) The field to sort results by.
        :param actor_name_substring: (optional) Providing a substring will filter results where
          the actor name contains the substring. This is a case-insensitive search.
        :return: List of user statistics.
        """
        endpoint = f"/orgs/{self.parent.org}/insights/api/user-stats/{user_id}"
        params: Dict[str, Any] = {
            "min_timestamp": kwargs.get("min_timestamp"),
            "max_timestamp": kwargs.get("max_timestamp"),
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1),
            "direction": kwargs.get("direction", "asc"),
            "sort": kwargs.get("sort"),
            "actor_name_substring": kwargs.get("actor_name_substring")
        }
        return self.parent.make_request("GET", endpoint, params=params)


class ArtifactMetadata:
    """
    ArtifactMetadata module for managing artifact metadata in an organization.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def create_artifact_deployment_record(self, name: str, digest: str, status: str,
                                          logical_environment: str, deployment_name: str,
                                          **kwargs: Any) -> Any:
        """
        Create or update deployment record for an artifact associated with an organization.

        :param name: The name of the artifact.
        :param digest: The digest of the artifact.
        :param version: (optional) The version of the artifact.
        :param status: The deployment status (e.g., 'deployed', 'decommissioned').
        :param logical_environment: The logical environment where the artifact is deployed
          (e.g., 'production', 'staging').
        :param physical_environment: (optional) The physical environment of the deployment
          (e.g., 'us-east-1', 'eu-west-1').
        :param cluster: (optional) The cluster where the artifact is deployed.
        :param deployment_name: The name of the deployment.
        :param tags: (optional) A list of tags associated with the deployment.
        :param runtime_risks: (optional) A list of runtime risks associated with the deployment.
          (e.g., ['vulnerability', 'misconfiguration']).
        :param github_repository: (optional) The GitHub repository associated with the deployment.
        :return: The created or updated deployment record.
        """
        endpoint = f"/orgs/{self.parent.org}/artifacts/metadata/deployment-record"
        data: Dict[str, Any] = {
            "name": name,
            "digest": digest,
            "version": kwargs.get("version"),
            "status": status,
            "logical_environment": logical_environment,
            "physical_environment": kwargs.get("physical_environment"),
            "cluster": kwargs.get("cluster"),
            "deployment_name": deployment_name,
            "tags": kwargs.get("tags"),
            "runtime_risks": kwargs.get("runtime_risks"),
            "github_repository": kwargs.get("github_repository")
        }
        return self.parent.make_request("POST", endpoint, json=data)

    def set_cluster_deployment_records(self, cluster: str, logical_environment: str,
                                       name: str, digest: str, deployment_name: str,
                                       **kwargs: Any) -> Any:
        """
        Set deployment records for a given cluster. If proposed records in the
        'deployments' field have identical 'cluster', 'logical_environment',
        'physical_environment', and 'deployment_name' values as existing records,
        the existing records will be updated. If no existing records match,
        new records will be created.

        :param cluster: The cluster where the artifacts are deployed.
        :param logical_environment: The logical environment of the deployments
          (e.g., 'production', 'staging').
        :param physical_environment: (optional) The physical environment of the deployments
          (e.g., 'us-east-1', 'eu-west-1').
        :param name: The name of the artifact.
        :param digest: The digest of the artifact.
        :param version: (optional) The version of the artifact.
        :param status: (optional) The deployment status (e.g., 'deployed', 'decommissioned').
        :param deployment_name: The name of the deployment.
        :param tags: (optional) A list of tags associated with the deployments.
        :param runtime_risks: (optional) A list of runtime risks associated with the deployments.
          (e.g., ['vulnerability', 'misconfiguration']).
        :param github_repository: (optional) The GitHub repository associated with the deployments.
        """
        endpoint = f"/orgs/{self.parent.org}/artifacts/metadata/deployment-record/cluster/{cluster}"
        data: Dict[str, Any] = {
            "logical_environment": logical_environment,
            "physical_environment": kwargs.get("physical_environment"),
            "deployments": [
                {
                    "name": name,
                    "digest": digest,
                    "version": kwargs.get("version"),
                    "status": kwargs.get("status"),
                    "deployment_name": deployment_name,
                    "tags": kwargs.get("tags"),
                    "runtime_risks": kwargs.get("runtime_risks"),
                    "github_repository": kwargs.get("github_repository")
                }
            ]
        }
        return self.parent.make_request("POST", endpoint, json=data)

    def create_artifact_metadata_storage_record(self, name: str, digest: str,
                                                registry_url: str, **kwargs: Any) -> Any:
        """
        Create metadata storage records for artifacts associated with an organization.

        :param name: The name of the artifact.
        :param digest: The digest of the artifact.
        :param version: (optional) The version of the artifact.
        :param artifact_url: (optional) The URL where the artifact is stored.
        :param path: (optional) The path of the artifact in the storage.
        :param registry_url: The URL of the registry where the artifact is stored.
        :param repository: (optional) The repository name within the registry.
        :param status: (optional) The storage status of the artifact. Default is 'active'
          (e.g., 'active', 'eol', 'deleted').
        :param github_repository: (optional) The GitHub repository associated with the artifact.
        :return: The created storage record.
        """
        endpoint = f"/orgs/{self.parent.org}/artifacts/metadata/storage-record"
        data: Dict[str, Any] = {
            "name": name,
            "digest": digest,
            "version": kwargs.get("version"),
            "artifact_url": kwargs.get("artifact_url"),
            "path": kwargs.get("path"),
            "registry_url": registry_url,
            "repository": kwargs.get("repository"),
            "status": kwargs.get("status", "active"),
            "github_repository": kwargs.get("github_repository")
        }
        return self.parent.make_request("POST", endpoint, json=data)

    def list_artifact_deployment_records(self, subject_digest: str) -> Any:
        """
        List deployment records for a specific artifact associated with an organization.

        :param subject_digest: The parameter should be set to the attestation's
          subject's SHA256 digest, in the form sha256:HEX_DIGEST.
        :return: List of deployment records.
        """
        endpoint = f"/orgs/{self.parent.org}/artifacts/{subject_digest}/metadata/deployment-records"
        return self.parent.make_request("GET", endpoint)

    def list_storage_records(self, subject_digest: str) -> Any:
        """
        List storage records for a specific artifact associated with an organization.

        :param subject_digest: The parameter should be set to the attestation's
          subject's SHA256 digest, in the form sha256:HEX_DIGEST.
        :return: List of storage records.
        """
        endpoint = f"/orgs/{self.parent.org}/artifacts/{subject_digest}/metadata/storage-records"
        return self.parent.make_request("GET", endpoint)


class ArtifactAttestation:
    """
    ArtifactAttestation module for managing artifact attestations in an organization.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def list_attestations_by_bulk_subjects(self, subject_digests: List[str],
                                           **kwargs: Any) -> Any:
        """
        List attestations for multiple artifact subjects associated with an organization.

        :param per_page: (optional) Number of results per page. Default is 30.
        :param before: (optional) A cursor for pagination to get results before a specific point.
        :param after: (optional) A cursor for pagination to get results after a specific point
        :param subject_digests: A list of subject digests. Each digest should be in the
          form sha256:HEX_DIGEST.
        :param predicate_type: (optional) Filter results by predicate type.
        :return: List of attestations.
        """
        endpoint = f"/orgs/{self.parent.org}/artifacts/attestations/bulk-subjects"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "before": kwargs.get("before"),
            "after": kwargs.get("after")
        }
        data: Dict[str, Any] = {
            "subject_digests": subject_digests,
            "predicate_type": kwargs.get("predicate_type")
        }
        return self.parent.make_request("POST", endpoint, params=params, json=data)

    def delete_attestation_by_subject(self, subject_digest: str) -> Any:
        """
        Delete an attestation for a specific artifact subject associated with an organization.

        :param subject_digest: The parameter should be set to the attestation's
          subject's SHA256 digest, in the form sha256:HEX_DIGEST.
        """
        endpoint = f"/orgs/{self.parent.org}/attestations/digest/{subject_digest}"
        self.parent.make_request("DELETE", endpoint)

    def list_attestations_repositories(self) -> Any:
        """
        List repositories with attestations for the organization.

        :param per_page: (optional) Number of results per page. Default is 30.
        :param before: (optional) A cursor for pagination to get results before a specific point.
        :param after: (optional) A cursor for pagination to get results after a specific point
        :param predicate_type: (optional) Filter results by predicate type.
          (e.g., 'provenance', 'sbom', 'custom').
        :return: List of repositories.
        """
        endpoint = f"/orgs/{self.parent.org}/attestations/repositories"
        return self.parent.make_request("GET", endpoint)

    def delete_attestation_by_id(self, attestation_id: str) -> Any:
        """
        Delete an attestation by its unique identifier for the organization.

        :param attestation_id: The unique identifier of the attestation.
        """
        endpoint = f"/orgs/{self.parent.org}/attestations/{attestation_id}"
        self.parent.make_request("DELETE", endpoint)

    def list_attestations(self, subject_digest: str,
                          **kwargs: Any) -> Any:
        """
        List attestations for a specific artifact subject associated with an organization.

        :param subject_digest: The parameter should be set to the attestation's
          subject's SHA256 digest, in the form sha256:HEX_DIGEST.
        :param per_page: (optional) Number of results per page. Default is 30.
        :param before: (optional) A cursor for pagination to get results before a specific point.
        :param after: (optional) A cursor for pagination to get results after a specific point
        :param predicate_type: (optional) Filter results by predicate type.
        :return: List of attestations.
        """
        endpoint = f"/orgs/{self.parent.org}/attestations/{subject_digest}"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "before": kwargs.get("before"),
            "after": kwargs.get("after"),
            "predicate_type": kwargs.get("predicate_type")
        }
        return self.parent.make_request("GET", endpoint, params=params)


class BlockingUsers:
    """
    BlockingUsers module for managing blocked users in an organization.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def list_blocked_users(self, **kwargs: Any) -> Any:
        """
        List users blocked from the organization.

        :param per_page: (optional) Number of results per page. Default is 30.
        :param page: (optional) Page number of the results to fetch. Default is 1.
        :return: List of blocked users.
        """
        endpoint = f"/orgs/{self.parent.org}/blocks"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def check_blocked_user(self, username: str) -> bool:
        """
        Check if a user is blocked from the organization.

        :param username: The username of the user to check.
        :return: True if the user is blocked, False otherwise.
        """
        endpoint = f"/orgs/{self.parent.org}/blocks/{username}"
        return self.parent.make_request("GET", endpoint)

    def block_user(self, username: str) -> Any:
        """
        Block a user from the organization.

        :param username: The username of the user to block.
        """
        endpoint = f"/orgs/{self.parent.org}/blocks/{username}"
        self.parent.make_request("PUT", endpoint)

    def unblock_user(self, username: str) -> Any:
        """
        Unblock a user from the organization.

        :param username: The username of the user to unblock.
        """
        endpoint = f"/orgs/{self.parent.org}/blocks/{username}"
        self.parent.make_request("DELETE", endpoint)


class CustomProperties:
    """
    CustomProperties module for managing organization custom properties.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def get_all_custom_properties(self) -> Any:
        """
        Retrieve all custom properties for the organization.

        :return: Dictionary of all custom properties.
        """
        endpoint = f"/orgs/{self.parent.org}/properties/schema"
        return self.parent.make_request("GET", endpoint)

    def create_or_update_custom_properties(self, property_name: str, value_type: str,
                                         **kwargs: Any) -> Any:
        """
        Create or update a custom

        :param property_name: The name of the custom property.
        :param url: (optional) The URL associated with the custom property.
        :param source_type: (optional) The source type of the custom property.
        :param value_type: The value type of the custom property (e.g., 'string',
          'number', 'boolean', 'array', 'object').
        :param required: (optional) Whether the custom property is required. Default is False.
        :param description: (optional) A description of the custom property.
        :param allowed_values: (optional) A list of allowed values for the custom property.
        :param values_editable_by: (optional) Who can edit the values of the custom property
          (e.g., 'org_actors', 'org_and_repo_actors', 'none').
        :param sample_data: List of dictionaries in the format:
          [
            {
              "property_name":"environment",
              "value_type":"single_select",
              "required":true,
              "default_value":"production",
              "description":"Prod or dev environment",
              "allowed_values":[
                "production",
                "development"
                ],
              "values_editable_by":"org_actors"
            }, {
              "property_name":"service",
              "value_type":"string"
            },{
              "property_name":"team",
              "value_type":"string",
              "description":"Team owning the repository"
            }
          ]
        :return: The created or updated custom property.
        """
        endpoint = f"/orgs/{self.parent.org}/properties/schema"
        data: List[Dict[str, Any]] = kwargs.get("sample_data", [
            {
                "property_name": property_name,
                "url": kwargs.get("url"),
                "source_type": kwargs.get("source_type"),
                "value_type": value_type,
                "required": kwargs.get("required", False),
                "description": kwargs.get("description"),
                "allowed_values": kwargs.get("allowed_values"),
                "values_editable_by": kwargs.get("values_editable_by")
            }
        ])
        return self.parent.make_request("PATCH", endpoint, json=data)

    def get_custom_property(self, property_name: str) -> Any:
        """
        Retrieve a specific custom property for the organization.

        :param property_name: The name of the custom property.
        :return: The custom property details.
        """
        endpoint = f"/orgs/{self.parent.org}/properties/schema/{property_name}"
        return self.parent.make_request("GET", endpoint)

    def create_or_update_custom_property(self, property_name: str, value_type: str,
                                         **kwargs: Any) -> Any:
        """
        Create or update the value of a custom property for the organization.

        :param property_name: The name of the custom property.
        :param value_type: The value type of the custom property (e.g., 'string',
          'number', 'boolean', 'array', 'object').
        :param required: (optional) Whether the custom property is required. Default is False.
        :param description: (optional) A description of the custom property.
        :param allowed_values: (optional) A list of allowed values for the custom property.
        :param values_editable_by: (optional) Who can edit the values of the custom property
          (e.g., 'org_actors', 'org_and_repo_actors', 'none').
        :return: The created or updated custom property value.
        """
        endpoint = f"/orgs/{self.parent.org}/properties/{property_name}"
        data: Dict[str, Any] = {
            "value_type": value_type,
            "required": kwargs.get("required", False),
            "default_value": kwargs.get("default_value"),
            "description": kwargs.get("description"),
            "allowed_values": kwargs.get("allowed_values"),
            "values_editable_by": kwargs.get("values_editable_by")
        }
        return self.parent.make_request("PUT", endpoint, json=data)

    def remove_custom_property(self, property_name: str) -> Any:
        """
        Remove a custom property from the organization.

        :param property_name: The name of the custom property to remove.
        """
        endpoint = f"/orgs/{self.parent.org}/properties/schema/{property_name}"
        self.parent.make_request("DELETE", endpoint)

    def list_custom_properties_for_repositories(self,
                                                      **kwargs: Any) -> Any:
        """
        List custom properties for repositories within the organization.

        :param per_page: (optional) Number of results per page. Default is 30.
        :param page: (optional) Page number of the results to fetch. Default is 1.
        :param repository_query: (optional) A search query to filter repositories
          by name or other attributes.
        :return: List of custom properties for organization repositories.
        """
        endpoint = f"/orgs/{self.parent.org}/properties/values"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1),
            "repository_query": kwargs.get("repository_query")
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def create_or_update_custom_property_values_for_repositories(self,
                                      repository_names: List[str],
                                      property_name: str,
                                      value: Any, **kwargs: Any) -> Any:
        """
        Create or update custom property values for repositories within the organization.

        :param repository_names: A list of repository names to set the custom property value for.
        :param property_name: The name of the custom property.
        :param value: The value to set for the custom property.

        sample data:
          [
            {
              "property_name":"environment",
              "value":"production"
            },{
              "property_name":"service",
              "value":"web"
            },{
              "property_name":"team",
              "value":"octocat"
            }
          ]
        :return: None
        """

        endpoint = f"/orgs/{self.parent.org}/properties/values"
        data: Dict[str, Any] = {
          "repository_names": repository_names,
          "properties": kwargs.get("data", {
              "property_name": property_name,
              "value": value
          })
        }
        self.parent.make_request("PUT", endpoint, json=data)


class IssueTypes:
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def list_issue_types(self) -> Any:
        """
        List issue types for the organization.

        :return: List of issue types.
        """
        endpoint = f"/orgs/{self.parent.org}/issue-types"
        return self.parent.make_request("GET", endpoint)

    def create_issue_type(self, name: str, description: str, is_enabled: bool,
                          **kwargs: Any) -> Any:
        """
        Create a new issue type for the organization.

        :param name: The name of the issue type.
        :param is_enabled: Whether the issue type is enabled.
        :param description: A description of the issue type.
        :param color: (optional) The color associated with the issue type.
        :return: The created issue type.
        """
        endpoint = f"/orgs/{self.parent.org}/issue-types"
        data: Dict[str, Any] = {
            "name": name,
            "is_enabled": is_enabled,
            "description": description,
            "color": kwargs.get("color")
        }
        return self.parent.make_request("POST", endpoint, json=data)

    def update_issue_type(self, issue_type_id: str, **kwargs: Any) -> Any:
        """
        Update an existing issue type for the organization.

        :param issue_type_id: The unique identifier of the issue type.
        :param name: (optional) The new name of the issue type.
        :param is_enabled: (optional) Whether the issue type is enabled.
        :param description: (optional) A new description of the issue type.
        :param color: (optional) The new color associated with the issue type.
        :return: The updated issue type.
        """
        endpoint = f"/orgs/{self.parent.org}/issue-types/{issue_type_id}"
        data: Dict[str, Any] = {
            "name": kwargs.get("name"),
            "is_enabled": kwargs.get("is_enabled"),
            "description": kwargs.get("description"),
            "color": kwargs.get("color")
        }
        return self.parent.make_request("PUT", endpoint, json=data)

    def delete_issue_type(self, issue_type_id: str) -> Any:
        """
        Delete an issue type from the organization.

        :param issue_type_id: The unique identifier of the issue type to delete.
        """
        endpoint = f"/orgs/{self.parent.org}/issue-types/{issue_type_id}"
        self.parent.make_request("DELETE", endpoint)


class Members:
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def list_failed_invitations(self, **kwargs: Any) -> Any:
        """
        List failed organization invitations.

        :param per_page: (optional) Number of results per page. Default is 30.
        :param page: (optional) Page number of the results to fetch. Default is 1.
        :return: List of failed organization invitations.
        """
        endpoint = f"/orgs/{self.parent.org}/failed_invitations"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def list_pending_invitations(self, **kwargs: Any) -> Any:
        """
        List pending organization invitations.

        :param per_page: (optional) Number of results per page. Default is 30.
        :param page: (optional) Page number of the results to fetch. Default is 1.
        :param role: (optional) Filter invitations by role.
        :param invitation_source: (optional) Filter invitations by invitation source.
        :return: List of pending organization invitations.
        """
        endpoint = f"/orgs/{self.parent.org}/invitations"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1),
            "role": kwargs.get("role"),
            "invitation_source": kwargs.get("invitation_source")
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def create_invitation(self, email: str,
                                       **kwargs: Any) -> Any:
        """
        Create an organization invitation.

        :param email: The email address of the user to invite.
        :param invitee_id: (optional) The unique identifier of the user to invite.
        :param role: (optional) The role for the invited user.
          can be 'admin', 'direct_member', 'billing_manager', or 'reinstate'.
        :param team_ids: (optional) A list of team IDs to add the user to.
        :return: The created organization invitation.
        """
        endpoint = f"/orgs/{self.parent.org}/invitations"
        data: Dict[str, Any] = {
            "email": email,
            "role": kwargs.get("role", "direct_member"),
            "team_ids": kwargs.get("team_ids")
        }
        if kwargs.get("invitee_id") and not kwargs.get("email"):
            data["invitee_id"] = kwargs.get("invitee_id")

        return self.parent.make_request("POST", endpoint, json=data)

    def cancel_invitation(self, invitation_id: str) -> Any:
        """
        Cancel an organization invitation.

        :param invitation_id: The unique identifier of the invitation to cancel.
        """
        endpoint = f"/orgs/{self.parent.org}/invitations/{invitation_id}"
        self.parent.make_request("DELETE", endpoint)

    def list_invitation_teams(self, invitation_id: str,
                                           **kwargs: Any) -> Any:
        """
        List teams associated with an organization invitation.

        :param invitation_id: The unique identifier of the invitation.
        :return: List of teams associated with the invitation.
        """
        endpoint = f"/orgs/{self.parent.org}/invitations/{invitation_id}/teams"
        params: Dict[str, Any] = {
          "per_page": kwargs.get("per_page", 30),
          "page": kwargs.get("page", 1)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def list_members(self, **kwargs: Any) -> Any:
        """
        List members of the organization.

        :param filter: (optional) Filter members by type. Can be 'all', '2fa_disabled',
          or '2fa_insecure'. Default is 'all'.
        :param per_page: (optional) Number of results per page. Default is 30.
        :param page: (optional) Page number of the results to fetch. Default is 1.
        :param role: (optional) Filter members by role.
        :return: List of organization members.
        """
        endpoint = f"/orgs/{self.parent.org}/members"
        params: Dict[str, Any] = {
            "filter": kwargs.get("filter", "all"),
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1),
            "role": kwargs.get("role")
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def check_membership(self, username: str) -> bool:
        """
        Check if a user is a member of the organization.

        :param username: The username of the user to check.
        :return: True if the user is a member, False otherwise.
        """
        endpoint = f"/orgs/{self.parent.org}/members/{username}"
        return self.parent.make_request("GET", endpoint)

    def remove_member(self, username: str) -> Any:
        """
        Remove a member from the organization.

        :param username: The username of the member to remove.
        """
        endpoint = f"/orgs/{self.parent.org}/members/{username}"
        self.parent.make_request("DELETE", endpoint)

    def get_membership(self, username: str) -> Any:
        """
        Get membership details for a user in the organization.

        :param username: The username of the user.
        :return: Membership details of the user.
        """
        endpoint = f"/orgs/{self.parent.org}/memberships/{username}"
        return self.parent.make_request("GET", endpoint)

    def set_membership(self, username: str,
                                    role: str) -> Any:
        """
        Set the membership role for a user in the organization.

        :param username: The username of the user.
        :param role: The role to assign to the user. Can be 'admin' or 'member'.
        :return: Updated membership details of the user.
        """
        endpoint = f"/orgs/{self.parent.org}/memberships/{username}"
        data: Dict[str, Any] = {
            "role": role
        }
        return self.parent.make_request("PUT", endpoint, json=data)

    def remove_membership(self, username: str) -> Any:
        """
        Remove a user's membership from the organization.

        :param username: The username of the user.
        """
        endpoint = f"/orgs/{self.parent.org}/memberships/{username}"
        self.parent.make_request("DELETE", endpoint)

    def list_public_members(self, **kwargs: Any) -> Any:
        """
        List public members of the organization.

        :param per_page: (optional) Number of results per page. Default is 30.
        :param page: (optional) Page number of the results to fetch. Default is 1.
        :return: List of public organization members.
        """
        endpoint = f"/orgs/{self.parent.org}/public_members"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def check_public_membership(self, username: str) -> bool:
        """
        Check if a user is a public member of the organization.

        :param username: The username of the user to check.
        :return: True if the user is a public member, False otherwise.
        """
        endpoint = f"/orgs/{self.parent.org}/public_members/{username}"
        return self.parent.make_request("GET", endpoint)

    def set_public_membership_for_authenticated_user(self) -> Any:
        """
        Set the authenticated user as a public member of the organization.
        """
        endpoint = f"/orgs/{self.parent.org}/public_members/{self.parent.username}"
        self.parent.make_request("PUT", endpoint)

    def remove_public_membership_for_authenticated_user(self) -> Any:
        """
        Remove the authenticated user from public members of the organization.
        """
        endpoint = f"/orgs/{self.parent.org}/public_members/{self.parent.username}"
        self.parent.make_request("DELETE", endpoint)

    def list_memberships_for_authenticated_user(self,
                                                  **kwargs: Any) -> Any:
        """
        List organization memberships for the authenticated user.

        :param per_page: (optional) Number of results per page. Default is 30.
        :param page: (optional) Page number of the results to fetch. Default is 1.
        :return: List of organization memberships for the authenticated user.
        """
        endpoint = "/user/memberships/orgs"
        params: Dict[str, Any] = {
            "state": kwargs.get("state"),
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def get_membership_for_authenticated_user(self,
                                                  org: str) -> Any:
        """
        Get membership details for the authenticated user in a specific organization.

        :param org: The name of the organization.
        :return: Membership details of the authenticated user in the organization.
        """
        endpoint = f"/user/memberships/orgs/{org}"
        return self.parent.make_request("GET", endpoint)

    def update_membership_for_authenticated_user(self,
                                                  org: str,
                                                  state: str) -> Any:
        """
        Update the membership state for the authenticated user in a specific organization.

        :param org: The name of the organization.
        :param state: The state to set for the membership. Can be 'active' or 'pending'.
        :return: Updated membership details of the authenticated user in the organization.
        """
        endpoint = f"/user/memberships/orgs/{org}"
        data: Dict[str, Any] = {
            "state": state
        }
        return self.parent.make_request("PATCH", endpoint, json=data)


class OrganizationRoles:
    """
    OrganizationRoles module for managing organization roles in an organization.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def get_all_roles(self) -> Any:
        """
        Retrieve all organization roles.

        :return: List of organization roles.
        """
        endpoint = f"/orgs/{self.parent.org}/organization-roles"
        return self.parent.make_request("GET", endpoint)

    def remove_all_roles_for_team(self,
                                      team_slug: str) -> Any:
        """
        Remove all organization roles assigned to a specific team.

        :param team_slug: The unique identifier of the team.
        """
        endpoint = f"/orgs/{self.parent.org}/organization-roles/team/{team_slug}"
        self.parent.make_request("DELETE", endpoint)

    def assign_role_to_team(self,
                                      team_slug: str,
                                      role_id: str) -> Any:
        """
        Assign an organization role to a specific team.

        :param team_slug: The unique identifier of the team.
        :param role_id: The unique identifier of the organization role to assign.
        """
        endpoint = f"/orgs/{self.parent.org}/organization-roles/teams/{team_slug}/{role_id}"
        self.parent.make_request("PUT", endpoint)

    def remove_role_from_team(self,
                                      team_slug: str,
                                      role_id: str) -> Any:
        """
        Remove an organization role from a specific team.

        :param team_slug: The unique identifier of the team.
        :param role_id: The unique identifier of the organization role to remove.
        """
        endpoint = f"/orgs/{self.parent.org}/organization-roles/teams/{team_slug}/{role_id}"
        self.parent.make_request("DELETE", endpoint)

    def remove_all_roles_for_user(self,
                                      username: str) -> Any:
        """
        Remove all organization roles assigned to a specific user.

        :param username: The username of the user.
        """
        endpoint = f"/orgs/{self.parent.org}/organization-roles/user/{username}"
        self.parent.make_request("DELETE", endpoint)

    def assign_role_to_user(self,
                                      username: str,
                                      role_id: str) -> Any:
        """
        Assign an organization role to a specific user.

        :param username: The username of the user.
        :param role_id: The unique identifier of the organization role to assign.
        """
        endpoint = f"/orgs/{self.parent.org}/organization-roles/user/{username}/{role_id}"
        self.parent.make_request("PUT", endpoint)

    def remove_role_from_user(self,
                                      username: str,
                                      role_id: str) -> Any:
        """
        Remove an organization role from a specific user.

        :param username: The username of the user.
        :param role_id: The unique identifier of the organization role to remove.
        """
        endpoint = f"/orgs/{self.parent.org}/organization-roles/user/{username}/{role_id}"
        self.parent.make_request("DELETE", endpoint)

    def get_role(self, role_id: str) -> Any:
        """
        Retrieve details of a specific organization role.

        :param role_id: The unique identifier of the organization role.
        :return: Details of the organization role.
        """
        endpoint = f"/orgs/{self.parent.org}/organization-roles/{role_id}"
        return self.parent.make_request("GET", endpoint)

    def list_teams_assigned_to_role(self,
                                      role_id: str,
                                      **kwargs: Any) -> Any:
        """
        List teams assigned to a specific organization role.

        :param role_id: The unique identifier of the organization role.
        :param per_page: (optional) Number of results per page. Default is 30.
        :param page: (optional) Page number of the results to fetch. Default is 1.
        :return: List of teams assigned to the organization role.
        """
        endpoint = f"/orgs/{self.parent.org}/organization-roles/{role_id}/teams"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def list_users_assigned_to_role(self,
                                      role_id: str,
                                      **kwargs: Any) -> Any:
        """
        List users assigned to a specific organization role.

        :param role_id: The unique identifier of the organization role.
        :param per_page: (optional) Number of results per page. Default is 30.
        :param page: (optional) Page number of the results to fetch. Default is 1.
        :return: List of users assigned to the organization role.
        """
        endpoint = f"/orgs/{self.parent.org}/organization-roles/{role_id}/users"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self.parent.make_request("GET", endpoint, params=params)


class Organizations:
    """
    Organizations module for managing organizations.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def list_organizations(self, **kwargs: Any) -> Any:
        """
        List organizations.

        :param since: (optional) The organization ID to start the list from.
        :param per_page: (optional) Number of results per page. Default is 30.
        :return: List of organizations.
        """
        endpoint = "/organizations"
        params: Dict[str, Any] = {
            "since": kwargs.get("since"),
            "per_page": kwargs.get("per_page", 30)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def get_organization(self) -> Any:
        """
        Get details of a specific organization.

        :return: Details of the organization.
        """
        endpoint = f"/orgs/{self.parent.org}"
        return self.parent.make_request("GET", endpoint)

    def update_organization(self, **kwargs: Any) -> Any:
        """
        Update details of a specific organization.

        :param org: The name of the organization.
        :param billing_email: (optional) The billing email address for the organization.
        :param company: (optional) The company name for the organization.
        :param email: (optional) The email address for the organization.
        :param location: (optional) The location of the organization.
        :param name: (optional) The display name of the organization.
        :param description: (optional) A description of the organization.
        :param has_organization_projects: (optional) Whether the organization has
          organization projects enabled.
        :param has_repository_projects: (optional) Whether the organization has
          repository projects enabled.
        :param default_repository_permission: (optional) The default permission level
          for repositories in the organization. Can be 'read', 'write', 'admin', or 'none'.
        :param members_can_create_repositories: (optional) Whether members can create
          repositories in the organization.
        :param members_can_create_internal_repositories: (optional) Whether members can
          create internal repositories in the organization.
        :param members_can_create_private_repositories: (optional) Whether members can
          create private repositories in the organization.
        :param members_can_create_public_repositories: (optional) Whether members can
          create public repositories in the organization.
        :param members_allowed_repository_creation_type: (optional) The types of
          repositories members are allowed to create. Can be 'all', 'private', or 'none'.
        :param members_can_create_pages: (optional) Whether members can create GitHub Pages sites
          in the organization.
        :param members_can_create_public_pages: (optional) Whether members can create public
          GitHub Pages sites in the organization.
        :param members_can_create_private_pages: (optional) Whether members can create private
          GitHub Pages sites in the organization.
        :param members_can_fork_private_repositories: (optional) Whether members can fork
          private repositories in the organization.
        :param web_commit_signoff_required: (optional) Whether web-based commits to
          repositories in the organization require sign-off.
        :param blog: (optional) The blog URL for the organization.
        :param secret_scanning_push_protection_custom_link_enabled: (optional) Whether
          a custom link is enabled for secret scanning push protection.
        :param secret_scanning_push_protection_custom_link: (optional) The custom link
          for secret scanning push protection.
        :param deploy_keys_enabled_for_repositories: (optional) Whether deploy keys
          are enabled for repositories in the organization.
        :return: Updated details of the organization.
        """
        endpoint = f"/orgs/{self.parent.org}"
        data: Dict[str, Any] = {
            "billing_email": kwargs.get("billing_email"),
            "company": kwargs.get("company"),
            "email": kwargs.get("email"),
            "location": kwargs.get("location"),
            "name": kwargs.get("name"),
            "description": kwargs.get("description"),
            "has_organization_projects": kwargs.get("has_organization_projects"),
            "has_repository_projects": kwargs.get("has_repository_projects"),
            "default_repository_permission": kwargs.get("default_repository_permission", "read"),
            "members_can_create_repositories": kwargs.get("members_can_create_repositories", True),
            "members_can_create_internal_repositories": kwargs.get("members_can_create_internal_repositories", True),
            "members_can_create_private_repositories": kwargs.get("members_can_create_private_repositories", True),
            "members_can_create_public_repositories": kwargs.get("members_can_create_public_repositories", False),
            "members_allowed_repository_creation_type": kwargs.get("members_allowed_repository_creation_type", "private"),
            "members_can_create_pages": kwargs.get("members_can_create_pages", True),
            "members_can_create_public_pages": kwargs.get("members_can_create_public_pages", True),
            "members_can_create_private_pages": kwargs.get("members_can_create_private_pages", False),
            "members_can_fork_private_repositories": kwargs.get("members_can_fork_private_repositories", False),
            "web_commit_signoff_required": kwargs.get("web_commit_signoff_required", False),
            "blog": kwargs.get("blog"),
            "secret_scanning_push_protection_custom_link_enabled": kwargs.get("secret_scanning_push_protection_custom_link_enabled", False),
            "secret_scanning_push_protection_custom_link": kwargs.get("secret_scanning_push_protection_custom_link"),
            "deploy_keys_enabled_for_repositories": kwargs.get("deploy_keys_enabled_for_repositories", True)
        }
        return self.parent.make_request("PATCH", endpoint, json=data)

    def list_app_installations(self, **kwargs: Any) -> Any:
        """
        List app installations for a specific organization.

        :param per_page: (optional) Number of results per page. Default is 30.
        :param page: (optional) Page number of the results to fetch. Default is 1.
        :return: List of app installations.
        """
        endpoint = f"/orgs/{self.parent.org}/installations"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def get_immutable_release_settings(self) -> Any:
        """
        Get immutable release settings for a specific organization.

        :return: Immutable release settings of the organization.
        """
        endpoint = f"/orgs/{self.parent.org}/settings/immutable-releases"
        return self.parent.make_request("GET", endpoint)

    def set_immutable_release_settings(self, enforced_repositories: bool,
                                       **kwargs: Any) -> Any:
        """
        Set immutable release settings for a specific organization.

        :enforced_repositories: Whether to enforce immutable releases for all repositories.
          can be 'all', 'none', or 'selected'.
        :param selected_repositories_ids: (optional) List of repository IDs to enforce
          immutable releases on when 'enforced_repositories' is set to 'selected'.
        :return: Updated immutable release settings of the organization.
        """
        endpoint = f"/orgs/{self.parent.org}/settings/immutable-releases"
        data: Dict[str, Any] = {
            "enforced_repositories": enforced_repositories,
        }
        if kwargs.get("enforced_repositories") == "selected":
            data["selected_repositories_ids"] = kwargs.get("selected_repositories_ids", [])

        return self.parent.make_request("PUT", endpoint, json=data)

    def list_selected_repositories_for_immutable_releases_enforcement(self,
                                                            **kwargs: Any) -> Any:
        """
        List selected repositories for immutable releases enforcement in a specific organization.

        :param per_page: (optional) Number of results per page. Default is 30.
        :param page: (optional) Page number of the results to fetch. Default is 1.
        :return: List of selected repositories for immutable releases enforcement.
        """
        endpoint = f"/orgs/{self.parent.org}/settings/immutable-releases/repositories"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def set_selected_repositories_for_immutable_releases_enforcement(self,
                                              selected_repository_ids: List[int]) -> Any:
        """
        Set selected repositories for immutable releases enforcement in a specific organization.

        :param selected_repository_ids: List of repository IDs to enforce immutable releases on.
        """
        endpoint = f"/orgs/{self.parent.org}/settings/immutable-releases/repositories"
        data: Dict[str, Any] = {
            "selected_repository_ids": selected_repository_ids
        }
        self.parent.make_request("PUT", endpoint, json=data)

    def enable_selected_repositories_for_immutable_releases(self,
                                              repository_id: str) -> Any:
        """
        Enable selected repositories for immutable releases enforcement in a specific organization.

        :param repository_id: Repository ID to enable immutable releases on.
        """
        endpoint = f"/orgs/{self.parent.org}/settings/immutable-releases/repositories/{repository_id}"
        self.parent.make_request("POST", endpoint)

    def disable_selected_repositories_for_immutable_releases(self,
                                              repository_id: str) -> Any:
        """
        Disable selected repositories for immutable releases enforcement in a specific organization.

        :param repository_id: Repository ID to disable immutable releases on.
        """
        endpoint = f"/orgs/{self.parent.org}/settings/immutable-releases/repositories/{repository_id}"
        self.parent.make_request("DELETE", endpoint)

    def list_organizations_for_authenticated_user(self,
                                                  **kwargs: Any) -> Any:
        """
        List organizations for the authenticated user.

        :param per_page: (optional) Number of results per page. Default is 30.
        :param page: (optional) Page number of the results to fetch. Default is 1.
        :return: List of organizations for the authenticated user.
        """
        endpoint = "/user/orgs"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def list_organizations_for_user(self, username: str, **kwargs: Any) -> Any:
        """
        List organizations for a specific user.

        :param username: The username of the user.
        :param per_page: (optional) Number of results per page. Default is 30.
        :param page: (optional) Page number of the results to fetch. Default is 1.
        :return: List of organizations for the specified user.
        """
        endpoint = f"/users/{username}/orgs"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self.parent.make_request("GET", endpoint, params=params)

class PersonalAccessTokens:
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def list_request_to_access_fine_grained_personal_access_tokens(self,
                                                            **kwargs: Any) -> Any:
        """
        List requests to access fine-grained personal access tokens for the organization.

        :param per_page: (optional) Number of results per page. Default is 30.
        :param page: (optional) Page number of the results to fetch. Default is 1.
        :return: List of requests to access fine-grained personal access tokens.
        """
        endpoint = f"/orgs/{self.parent.org}/personal-access-tokens-requests"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1),
            "sort": kwargs.get("sort"),
            "direction": kwargs.get("direction"),
            "owner": kwargs.get("owner"),
            "repository": kwargs.get("repository"),
            "permission": kwargs.get("permission"),
            "last_used_before": kwargs.get("last_used_before"),
            "last_used_after": kwargs.get("last_used_after"),
            "token_id": kwargs.get("token_id")
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def review_requests_to_access_fine_grained_personal_access_tokens(self,
                                                            pat_request_ids: List[str],
                                                            action: str,
                                                            **kwargs: Any) -> Any:
        """
        Approves or denies multiple pending requests to access organization resources
          via a fine-grained personal access token.

        :param request_id: List of personal access token request IDs to review.
        :param action: The action to take on the request. Can be 'approve' or 'deny'.
        :param reason: (optional) The reason for approving or  denying the request.
        :return: The reviewed request details.
        """
        endpoint = f"/orgs/{self.parent.org}/personal-access-tokens-requests"
        data: Dict[str, Any] = {
            "pat_request_ids": pat_request_ids,
            "action": action,
            "reason": kwargs.get("reason")
        }
        return self.parent.make_request("POST", endpoint, json=data)

    def review_request_to_access_fine_grained_personal_access_token(self,
                                                            pat_request_id: str,
                                                            action: str,
                                                            **kwargs: Any) -> Any:
        """
        Approves or denies a pending request to access organization resources
          via a fine-grained personal access token.

        :param request_id: The personal access token request ID to review.
        :param action: The action to take on the request. Can be 'approve' or 'deny'.
        :param reason: (optional) The reason for approving or  denying the request.
        :return: The reviewed request details.
        """
        endpoint = f"/orgs/{self.parent.org}/personal-access-tokens-requests/{pat_request_id}"
        data: Dict[str, Any] = {
            "action": action,
            "reason": kwargs.get("reason")
        }
        return self.parent.make_request("POST", endpoint, json=data)

    def list_repositories_requested_to_access_fine_grained_personal_access_token(self,
                                                            pat_request_id: str,
                                                            **kwargs: Any) -> Any:
        """
        List repositories requested to access via a fine-grained personal access token.

        :param pat_request_id: The personal access token request ID.
        :param per_page: (optional) Number of results per page. Default is 30.
        :param page: (optional) Page number of the results to fetch. Default is 1.
        :return: List of repositories requested to access via the personal access token.
        """
        endpoint = f"/orgs/{self.parent.org}/personal-access-tokens-requests/{pat_request_id}/repositories"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def list_fine_grained_personal_access_tokens(self, **kwargs: Any) -> Any:
        """
        List fine-grained personal access tokens for the organization.

        :param per_page: (optional) Number of results per page. Default is 30.
        :param page: (optional) Page number of the results to fetch. Default is 1.
        :param sort: (optional) The field to sort results by.
        :param direction: (optional) The direction to sort results. Can be 'asc' or 'desc'.
        :param owner: (optional) Filter tokens by owner username.
        :param repository: (optional) Filter tokens by repository name.
        :param permission: (optional) Filter tokens by permission level.
        :param last_used_before: (optional) Filter tokens last used before this date.
        :param last_used_after: (optional) Filter tokens last used after this date.
        :param token_id: (optional) Filter tokens by token ID.
        :return: List of fine-grained personal access tokens.
        """
        endpoint = f"/orgs/{self.parent.org}/personal-access-tokens"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1),
            "sort": kwargs.get("sort"),
            "direction": kwargs.get("direction"),
            "owner": kwargs.get("owner"),
            "repository": kwargs.get("repository"),
            "permission": kwargs.get("permission"),
            "last_used_before": kwargs.get("last_used_before"),
            "last_used_after": kwargs.get("last_used_after"),
            "token_id": kwargs.get("token_id")
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def update_access_to_org_via_fine_grained_personal_access_token(self,
                                                            pat_ids: List[str],
                                                            action: str) -> Any:
        """
        Update access for multiple fine-grained personal access tokens in the organization.

        :param pat_ids: List of personal access token IDs.
        :param action: The action to take on the tokens. Can be 'revoke'.
        :return: Updated personal access token details.
        """
        endpoint = f"/orgs/{self.parent.org}/personal-access-tokens"
        data: Dict[str, Any] = {
            "pat_ids": pat_ids,
            "action": action
        }
        return self.parent.make_request("PATCH", endpoint, json=data)

    def update_access_for_fine_grained_personal_access_token(self,
                                                            pat_id: str,
                                                            action: str) -> Any:
        """
        Update access for a fine-grained personal access token in the organization.

        :param pat_id: The personal access token ID.
        :param action: The action to take on the token. Can be 'revoke'.
        :return: Updated personal access token details.
        """
        endpoint = f"/orgs/{self.parent.org}/personal-access-tokens/{pat_id}"
        data: Dict[str, Any] = {
            "action": action
        }
        return self.parent.make_request("PATCH", endpoint, json=data)

    def list_repositories_fine_grained_token_has_access(self, pat_id: str,
                                                            **kwargs: Any) -> Any:
        """
        List repositories a fine-grained personal access token has access to in the organization.

        :param pat_id: The personal access token ID.
        :param per_page: (optional) Number of results per page. Default is 30.
        :param page: (optional) Page number of the results to fetch. Default is 1.
        :return: List of repositories the personal access token has access to.
        """
        endpoint = f"/orgs/{self.parent.org}/personal-access-tokens/{pat_id}/repositories"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self.parent.make_request("GET", endpoint, params=params)

class RuleSuites:
    """
    RuleSuites module for managing rule suites in an organization.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def list_rule_suites(self, **kwargs: Any) -> Any:
        """
        List rule suites for the organization.

        :param ref: (optional) The git reference for filtering rule suites.
        :param repository_name: (optional) The name of the repository to filter rule suites.
        :param time_period: (optional) The time period for filtering rule suites.
          can be 'hour', 'day', 'week', or 'month'. Default is 'day'.
        :param actor_name: (optional) The name of the actor for filtering rule suites.
        :param rule_suite_result: (optional) The result status for filtering rule suites.
          can be 'pass', 'fail', 'bypass', 'all'. Default is 'all'.
        :param per_page: (optional) Number of results per page. Default is 30.
        :param page: (optional) Page number of the results to fetch. Default is 1.
        :return: List of rule suites for the organization.
        """
        endpoint = f"/orgs/{self.parent.org}/rulesets/rule-suites"
        params: Dict[str, Any] = {
            "ref": kwargs.get("ref"),
            "repository_name": kwargs.get("repository_name"),
            "time_period": kwargs.get("time_period", "day"),
            "actor_name": kwargs.get("actor_name"),
            "rule_suite_result": kwargs.get("rule_suite_result", "all"),
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def get_rule_suite(self, rule_suite_id: str) -> Any:
        """
        Get details of a specific rule suite.

        :param rule_suite_id: The unique identifier of the rule suite.
        :return: Details of the rule suite.
        """
        endpoint = f"/orgs/{self.parent.org}/rulesets/rule-suites/{rule_suite_id}"
        return self.parent.make_request("GET", endpoint)

class Rules:
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def get_all_repository_rulesets(self, **kwargs: Any) -> Any:
        """
        Get all repository rulesets for the organization.

        :param per_page: (optional) Number of results per page. Default is 30.
        :param page: (optional) Page number of the results to fetch. Default is 1.
        :param targets: (optional) Filter rulesets by target type.
        :return: List of repository rulesets.
        """
        endpoint = f"/orgs/{self.parent.org}/rulesets"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1),
            "targets": kwargs.get("targets")
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def create_repository_ruleset(self, ruleset: Dict[str, Any]) -> Any:
        """
        Create a new repository ruleset for the organization.

        :param ruleset: The ruleset configuration dictionary. For the complete schema
          and available options, see the GitHub API documentation:
          https://docs.github.com/en/rest/orgs/rules#create-an-organization-repository-ruleset
        :return: Details of the created repository ruleset.
        """
        endpoint = f"/orgs/{self.parent.org}/rulesets"
        return self.parent.make_request("POST", endpoint, json=ruleset)

    def get_repository_ruleset(self, ruleset_id: str) -> Any:
        """
        Get a repository ruleset for an organization.

        :param ruleset_id: The unique identifier of the repository ruleset.
        :return: Details of the repository ruleset.
        """
        endpoint = f"/orgs/{self.parent.org}/rulesets/{ruleset_id}"
        return self.parent.make_request("GET", endpoint)

    def update_repository_ruleset(self, ruleset_id: str, ruleset: Dict[str, Any]) -> Any:
        """
        Update a repository ruleset for an organization.

        :param ruleset_id: The unique identifier of the repository ruleset.
        :param ruleset: The updated ruleset configuration dictionary. For the complete schema
          and available options, see the GitHub API documentation:
          https://docs.github.com/en/rest/orgs/rules#update-an-organization-repository-ruleset
        :return: Details of the updated repository ruleset.
        """
        endpoint = f"/orgs/{self.parent.org}/rulesets/{ruleset_id}"
        return self.parent.make_request("PUT", endpoint, json=ruleset)

    def delete_repository_ruleset(self, ruleset_id: str) -> Any:
        """
        Delete a repository ruleset for an organization.

        :param ruleset_id: The unique identifier of the repository ruleset.
        """
        endpoint = f"/orgs/{self.parent.org}/rulesets/{ruleset_id}"
        return self.parent.make_request("DELETE", endpoint)

    def get_ruleset_history(self, ruleset_id: str, **kwargs: Any) -> Any:
        """
        Get the history of a repository ruleset for an organization.

        :param ruleset_id: The unique identifier of the repository ruleset.
        :param per_page: (optional) Number of results per page. Default is 30.
        :param page: (optional) Page number of the results to fetch. Default is 1.
        :return: History of the repository ruleset.
        """
        endpoint = f"/orgs/{self.parent.org}/rulesets/{ruleset_id}/history"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def get_ruleset_version(self, ruleset_id: str, version_id: str) -> Any:
        """
        Get a specific version of a repository ruleset for an organization.

        :param ruleset_id: The unique identifier of the repository ruleset.
        :param version_id: The unique identifier of the ruleset version.
        :return: Details of the specific version of the repository ruleset.
        """
        endpoint = f"/orgs/{self.parent.org}/rulesets/{ruleset_id}/history/{version_id}"
        return self.parent.make_request("GET", endpoint)


class Webhooks: #TODO: Implement Webhooks methods
    def __init__(self, parent: Any) -> None:
        self.parent = parent

    def list_webhooks(self, **kwargs: Any) -> Any:
        """
        List webhooks for the organization.

        :param per_page: (optional) Number of results per page. Default is 30.
        :param page: (optional) Page number of the results to fetch. Default is 1.
        :return: List of webhooks for the organization.
        """
        endpoint = f"/orgs/{self.parent.org}/hooks"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "page": kwargs.get("page", 1)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def create_webhook(self, **kwargs: Any) -> Any:
        """
        Create a new webhook for the organization.

        :param url: The URL to which the payloads will be delivered.
        :param content_type: (optional) The content type for the payloads. Default is 'json'.
        :param secret: (optional) The secret key to secure the webhook.
        :param insecure_ssl: (optional) Whether to disable SSL verification. Default is '0
        :param events: (optional) List of events that trigger the webhook.
          can be any of the supported webhook events. Default is ['push'].
          https://docs.github.com/en/webhooks/webhook-events-and-payloads
        :param active: (optional) Whether the webhook is active. Default is True.
        :return: Details of the created webhook.
        """
        endpoint = f"/orgs/{self.parent.org}/hooks"
        data: Dict[str, Any] = {
            "name": "web",
            "config": {
                "url": kwargs.get("url"),
                "content_type": kwargs.get("content_type", "json"),
                "secret": kwargs.get("secret"),
                "insecure_ssl": kwargs.get("insecure_ssl", "0")
            },
            "events": kwargs.get("events", ["push"]),
            "active": kwargs.get("active", True)
        }
        return self.parent.make_request("POST", endpoint, json=data)

    def get_webhook(self, hook_id: str) -> Any:
        """
        Get details of a specific webhook for the organization.

        :param hook_id: The unique identifier of the webhook.
        :return: Details of the webhook.
        """
        endpoint = f"/orgs/{self.parent.org}/hooks/{hook_id}"
        return self.parent.make_request("GET", endpoint)

    def update_webhook(self, hook_id: str, **kwargs: Any) -> Any:
        """
        Update a specific webhook for the organization.

        :param hook_id: The unique identifier of the webhook.
        :param url: (optional) The URL to which the payloads will be delivered.
        :param content_type: (optional) The content type for the payloads.
        :param secret: (optional) The secret key to secure the webhook.
        :param insecure_ssl: (optional) Whether to disable SSL verification.
        :param events: (optional) List of events that trigger the webhook.
          can be any of the supported webhook events.
          https://docs.github.com/en/webhooks/webhook-events-and-payloads
        :param active: (optional) Whether the webhook is active.
        :return: Details of the updated webhook.
        """
        endpoint = f"/orgs/{self.parent.org}/hooks/{hook_id}"
        data: Dict[str, Any] = {
            "config": {
                "url": kwargs.get("url"),
                "content_type": kwargs.get("content_type"),
                "secret": kwargs.get("secret"),
                "insecure_ssl": kwargs.get("insecure_ssl")
            },
            "events": kwargs.get("events"),
            "active": kwargs.get("active")
        }
        return self.parent.make_request("PATCH", endpoint, json=data)

    def delete_webhook(self, hook_id: str) -> Any:
        """
        Delete a specific webhook for the organization.

        :param hook_id: The unique identifier of the webhook.
        """
        endpoint = f"/orgs/{self.parent.org}/hooks/{hook_id}"
        return self.parent.make_request("DELETE", endpoint)

    def get_webhook_config(self, hook_id: str) -> Any:
        """
        Get the configuration of a specific webhook for the organization.

        :param hook_id: The unique identifier of the webhook.
        :return: Configuration details of the webhook.
        """
        endpoint = f"/orgs/{self.parent.org}/hooks/{hook_id}/config"
        return self.parent.make_request("GET", endpoint)

    def update_webhook_config(self, hook_id: str, **kwargs: Any) -> Any:
        """
        Update the configuration of a specific webhook for the organization.

        :param hook_id: The unique identifier of the webhook.
        :param url: (optional) The URL to which the payloads will be delivered.
        :param content_type: (optional) The content type for the payloads.
        :param secret: (optional) The secret key to secure the webhook.
        :param insecure_ssl: (optional) Whether to disable SSL verification.
        :return: Updated configuration details of the webhook.
        """
        endpoint = f"/orgs/{self.parent.org}/hooks/{hook_id}/config"
        data: Dict[str, Any] = {
            "url": kwargs.get("url"),
            "content_type": kwargs.get("content_type"),
            "secret": kwargs.get("secret"),
            "insecure_ssl": kwargs.get("insecure_ssl")
        }
        return self.parent.make_request("PATCH", endpoint, json=data)

    def list_webhook_deliveries(self, hook_id: str,
                              **kwargs: Any) -> Any:
        """
        List deliveries for a specific webhook in the organization.

        :param hook_id: The unique identifier of the webhook.
        :param per_page: (optional) Number of results per page. Default is 30.
        :param cursor: (optional) Cursor for pagination.
        :return: List of webhook deliveries.
        """
        endpoint = f"/orgs/{self.parent.org}/hooks/{hook_id}/deliveries"
        params: Dict[str, Any] = {
            "per_page": kwargs.get("per_page", 30),
            "cursor": kwargs.get("cursor")
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def redeliver_webhook_delivery(self, hook_id: str,
                                 delivery_id: str) -> Any:
        """
        Redeliver a specific webhook delivery for the organization.

        :param hook_id: The unique identifier of the webhook.
        :param delivery_id: The unique identifier of the webhook delivery.
        :return: Details of the redelivered webhook delivery.
        """
        endpoint = f"/orgs/{self.parent.org}/hooks/{hook_id}/deliveries/{delivery_id}/attempts"
        return self.parent.make_request("POST", endpoint)

    def ping_webhook(self, hook_id: str) -> Any:
        """
        Ping a specific webhook for the organization.

        :param hook_id: The unique identifier of the webhook.
        :return: Details of the pinged webhook.
        """
        endpoint = f"/orgs/{self.parent.org}/hooks/{hook_id}/pings"
        return self.parent.make_request("POST", endpoint)

class Organization:
    """
    Organization module to manage organization-related functionalities.
    """
    def __init__(self, parent: Any) -> None:

        # Initialize sub-modules
        self.api_insights = ApiInsights(parent)
        self.artifact_metadata = ArtifactMetadata(parent)
        self.artifact_attestation = ArtifactAttestation(parent)
        self.blocking_users = BlockingUsers(parent)
        self.custom_properties = CustomProperties(parent)
        self.issue_types = IssueTypes(parent)
        self.members = Members(parent)
        self.organization_roles = OrganizationRoles(parent)
        self.organizations = Organizations(parent)
        self.personal_access_tokens = PersonalAccessTokens(parent)
        self.rule_suites = RuleSuites(parent)
        self.rules = Rules(parent)
        self.webhooks = Webhooks(parent)
