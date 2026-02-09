"""
GitHub Modules for interacting with GitHub API.
"""
# --- Built-in modules --- #
import sys
import os
import logging
import base64
from typing import Any, Dict
from nacl import public, encoding
# --- Third-party modules --- #
import requests
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# --- Custom submodules --- #
from modules.actions import Actions
from modules.apps import Apps
from modules.billing import Billing
from modules.branch import Branch
from modules.collaborators import Collaborator
from modules.copilot import Copilot
from modules.dependabot import Dependabot
from modules.deployments import Deployment
from modules.git_database import GitDatabase
from modules.gitignore import GitIgnore
from modules.issues import Issue
from modules.organizations import Organization
from modules.packages import Packages
from modules.private_registries import PrivateRegistries
from modules.rate_limit import RateLimit
from modules.releases import Release
from modules.repositories import Repository
from modules.pull_requests import PullRequest
from modules.teams import Team

class GitHubModules:
    """
    Docstring for GitHubModules
    """
    def __init__(self, token: str, **kwargs: Any):
        """Initialize GitHubModules with authentication token and optional parameters.

        :param token: GitHub authentication token.
        :param org: Organization name for organization-level operations.
        :param owner: Owner name for owner-level operations.
        :param username: Username for user-level operations.
        :param log_level: (optional) Logging level (default is INFO).
        """
        self.base_url = "https://api.github.com"
        self.org = kwargs.get("org", "")
        self.owner = kwargs.get("owner", "")
        self.username = kwargs.get("username", "")
        self.headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}"
        }
        self.logger = logging.getLogger()
        log_level = kwargs.get("log_level", "INFO")
        self.logger.setLevel(getattr(logging, log_level) if isinstance(log_level, str) else log_level)

        # Optional: Add a handler if none exist (Lambda usually has one by default)
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - [%(levelname)s] - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

        self.modules()

    def make_request(self, method: str, endpoint: str, **kwargs: Any) -> Any:
        """
        Make an HTTP request to the GitHub API.

        :param method: HTTP method (GET, POST, DELETE, etc.).
        :param endpoint: API endpoint to call.
        :return: Parsed response (dict, list, str, bool, int, float, or None).
        """
        url = f"{self.base_url}{endpoint}"
        response = requests.request(method, url, headers=self.headers, timeout=10, **kwargs)
        self.logger.debug("Request URL: %s", url)
        self.logger.debug("Response Status: %s", response.status_code)
        self.logger.debug("Response Body: %s", response.text)

        return self._parse_response(response)

    def _parse_response(self, response: requests.Response) -> Dict[str, Any]:
        """
        Parse the HTTP response into appropriate Python types.

        :param response: The requests Response object.
        :return: Dict with status_code and parsed data.
        """
        result: Dict[str, Any] = {"status_code": response.status_code, "data": None}

        if not response.content:
            return result

        # JSON handles: dict, list, bool, int, float, None
        try:
            result["data"] = response.json()
        except requests.exceptions.JSONDecodeError:
            result["data"] = self._parse_text(response.text)

        return result

    def _parse_text(self, text: str) -> Any:
        """
        Parse plain text response into appropriate Python type.

        :param text: Raw text from response.
        :return: Parsed value (str, bool, int, float, or None).
        """
        text = text.strip()

        if not text:
            return None

        text_lower = text.lower()

        # Boolean mapping
        if text_lower in ("true", "false"):
            return text_lower == "true"

        # Null mapping
        if text_lower in ("null", "none"):
            return None

        # Numeric parsing
        for converter in (int, float):
            try:
                return converter(text)
            except ValueError:
                continue

        return text

    def encrypt_secret(self, public_key: str, secret_value: str) -> str:
        """
        Encrypt a secret value using the provided public key with LibSodium.

        :param public_key: Base64-encoded public key.
        :param secret_value: The secret value to encrypt.
        :return: Base64-encoded encrypted secret.
        """
        public_key_obj = public.PublicKey(base64.b64decode(public_key), encoding.RawEncoder)
        sealed_box = public.SealedBox(public_key_obj)
        encrypted = sealed_box.encrypt(secret_value.encode("utf-8"))
        return base64.b64encode(encrypted).decode("utf-8")

    def modules(self) -> None:
        """
        Initialize submodules for GitHub operations.
        """
        self.actions = Actions(self)
        self.apps = Apps(self)
        self.billing = Billing(self)
        self.branch = Branch(self)
        self.collaborator = Collaborator(self)
        self.copilot = Copilot(self)
        self.dependabot = Dependabot(self)
        self.deployment = Deployment(self)
        self.git_database = GitDatabase(self)
        self.gitignore = GitIgnore(self)
        self.issue = Issue(self)
        self.organization = Organization(self)
        self.packages = Packages(self)
        self.private_registries = PrivateRegistries(self)
        self.pull_request = PullRequest(self)
        self.rate_limit = RateLimit(self)
        self.release = Release(self)
        self.repository = Repository(self)
        self.team = Team(self)
