"""
Billing and Auditing Submodule
"""

from typing import Any, Dict

class Budgets:
    """
    Handles budget management functionalities.
    """
    def __init__(self, parent: Any):
        """
        :param parent: An object with an 'org' attribute (organization identifier) 
            and a 'make_request' method.
        """
        self.parent = parent

    def get_all_org_budgets(self):
        """
        Retrieves all budgets for the organization.

        :return: List of budgets.
        """
        endpoint = f"/organizations/{self.parent.org}/settings/billing/budgets"
        return self.parent.make_request("GET", endpoint)

    def get_budget_id(self, budget_id: str) -> Dict[str, Any]:
        """
        Retrieves a specific budget by ID.

        :param budget_id: The ID of the budget to retrieve.
        :return: Budget details.
        """
        endpoint = f"/organizations/{self.parent.org}/settings/billing/budgets/{budget_id}"
        return self.parent.make_request("GET", endpoint)

    def update_budget(self, budget_id: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Updates a specific budget by ID.

        :param budget_id: The ID of the budget to update.
        :param budget_amount: New budget amount.
        :param prevent_further_usage: Boolean to prevent further usage.
        :param will_alert: Boolean to enable/disable alerts.
        :param alert_recipients: List of alert recipient emails.
        :param budget_scope: Scope of the budget.
            e.g., "enterprise", "organization", "repository", "cost_center"
        :param budget_entity_name: Name of the budget entity.
        :param budget_type: Type of the budget.
            e.g., "ProductPricing", "SkuPricing"
        :param budget_product_sku: Product SKU associated with the budget.

        :return: Updated budget details.
        """
        endpoint = f"/organizations/{self.parent.org}/settings/billing/budgets/{budget_id}"
        data: dict[str, Any] = {
            "budget_amount": kwargs.get("budget_amount", 0),
            "prevent_further_usage": kwargs.get("prevent_further_usage", True),
            "budget_alerting": {
                "will_alert": kwargs.get("will_alert", True),
                "alert_recipients": kwargs.get("alert_recipients", [])},
            "budget_scope": kwargs.get("budget_scope", ""),
            "budget_entity_name": kwargs.get("budget_entity_name", ""),
            "budget_type": kwargs.get("budget_type", ""),
            "budget_product_sku": kwargs.get("budget_product_sku", "")
        }
        return self.parent.make_request("PATCH", endpoint, json=data)

    def delete_budget(self, budget_id: str) -> Dict[str, Any]:
        """
        Deletes a specific budget by ID.

        :param budget_id: The ID of the budget to delete.
        :return: Deletion confirmation.
        """
        endpoint = f"/organizations/{self.parent.org}/settings/billing/budgets/{budget_id}"
        return self.parent.make_request("DELETE", endpoint)

class Usage:

    """
    Handles usage auditing functionalities.
    """
    def __init__(self, parent: Any):
        self.parent = parent

    def get_billing_premium_request_usage(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Gets a report of premium request usage for an organization.

        :param year: Filter by year.
        :param month: Filter by month.
        :param day: Filter by day.
        :param user: Filter by user ID.
        :param model: Filter by model name.
        :param product: Filter by product name.
        :return: Billing premium request usage data.
        """
        endpoint = f"/organizations/{self.parent.org}/settings/billing/premium_request/usage"
        params = {
            "year": kwargs.get("year", None),
            "month": kwargs.get("month", None),
            "day": kwargs.get("day", None),
            "user": kwargs.get("user", None),
            "model": kwargs.get("model", None),
            "product": kwargs.get("product", None),
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def get_org_billing_usage_report(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Gets a billing usage report for an organization.

        :param year: Filter by year.
        :param month: Filter by month.
        :param day: Filter by day.
        :param user: Filter by user ID.
        :param product: Filter by product name.
        :return: Organization billing usage report data.
        """
        endpoint = f"/organizations/{self.parent.org}/settings/billing/usage"
        params = {
            "year": kwargs.get("year", None),
            "month": kwargs.get("month", None),
            "day": kwargs.get("day", None)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def get_org_billing_usage_summary(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Gets a summary of billing usage for an organization.

        :param year: Filter by year.
        :param month: Filter by month.
        :param day: Filter by day.
        :param repository: Filter by repository name.
        :param product: Filter by product name.
        :param sku: Filter by SKU name.
        :return: Organization billing usage summary data.
        """
        endpoint = f"/organizations/{self.parent.org}/settings/billing/usage/summary"
        params = {
            "year": kwargs.get("year", None),
            "month": kwargs.get("month", None),
            "day": kwargs.get("day", None),
            "repository": kwargs.get("repository", None),
            "product": kwargs.get("product", None),
            "sku": kwargs.get("sku", None),
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def get_user_billing_usage_report(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Gets a billing usage report for a specific user.

        :param year: Filter by year.
        :param month: Filter by month.
        :param day: Filter by day.
        :return: User billing usage report data.
        """
        endpoint = f"/users/{self.parent.username}/settings/billing/usage"
        params = {
            "year": kwargs.get("year", None),
            "month": kwargs.get("month", None),
            "day": kwargs.get("day", None)
        }
        return self.parent.make_request("GET", endpoint, params=params)

    def get_user_billing_usage_summary(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Gets a summary of billing usage for a specific user.

        :param year: Filter by year.
        :param month: Filter by month.
        :param day: Filter by day.
        :param repository: Filter by repository name.
        :param product: Filter by product name.
        :param sku: Filter by SKU name.
        :return: User billing usage summary data.
        """
        endpoint = f"/users/{self.parent.username}/settings/billing/usage/summary"
        params = {
            "year": kwargs.get("year", None),
            "month": kwargs.get("month", None),
            "day": kwargs.get("day", None),
            "repository": kwargs.get("repository", None),
            "product": kwargs.get("product", None),
            "sku": kwargs.get("sku", None),
        }
        return self.parent.make_request("GET", endpoint, params=params)

class Billing:
    """
    Handles billing and auditing functionalities.
    """
    def __init__(self, parent: Any):
        self.parent = parent

        # Initialize submodules
        self.budgets = Budgets(parent)
        self.usage = Usage(parent)