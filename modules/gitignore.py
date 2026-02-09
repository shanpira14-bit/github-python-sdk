"""
GitIgnore module for interacting with GitHub .gitignore templates API.
"""
from typing import Any, Dict, List

class GitIgnore:
    """
    GitIgnore module for interacting with GitHub .gitignore templates API.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent
        self.get_all_gitignore_templates = self._get_all_gitignore_templates
        self.get_gitignore_template = self._get_gitignore_template

    def _get_all_gitignore_templates(self) -> List[str]:
        """
        Retrieve all available .gitignore templates from GitHub.

        :return: List of .gitignore template names.
        """
        endpoint = "/gitignore/templates"
        return self.parent.make_request("GET", endpoint)

    def _get_gitignore_template(self, name: str) -> Dict[str, Any]:
        """
        Retrieve a specific .gitignore template by name from GitHub.

        :param name: The name of the .gitignore template.
        :return: The .gitignore template content and metadata.
        """
        endpoint = f"/gitignore/templates/{name}"
        return self.parent.make_request("GET", endpoint)
