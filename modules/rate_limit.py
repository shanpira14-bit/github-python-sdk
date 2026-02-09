"""
Module for rate limiting functionality.
"""
from typing import Any

class RateLimit:
    """
    Module for rate limiting functionality.
    """
    def __init__(self, parent: Any) -> None:
        self.parent = parent
        self.get_rate_limit = self._get_rate_limit

    def _get_rate_limit(self) -> Any:
        """
        Retrieve the current rate limit status from GitHub.

        :return: A dictionary containing rate limit information.
        """
        endpoint = "/rate_limit"
        return self.parent.make_request("GET", endpoint)