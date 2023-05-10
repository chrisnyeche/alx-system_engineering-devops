#!venv/bin/python
"""
Get all dashboards returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DashboardsApi(api_client)
    response = api_instance.list_dashboards(
        filter_shared=False,
    )

    print(response)

# DD_SITE="datadoghq.com" DD_API_KEY="" DD_APP_KEY="" python3 get_dashboards.py
