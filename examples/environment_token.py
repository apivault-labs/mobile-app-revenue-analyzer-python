import os
from mobile_app_revenue_analyzer import MobileAppRevenueAnalyzerClient

if not os.environ.get("APIFY_API_TOKEN"):
    raise SystemExit("Set APIFY_API_TOKEN before running this example")
client = MobileAppRevenueAnalyzerClient()
print(client.run_one({'mode': 'search',
 'searchTerms': ['invoice maker'],
 'country': 'us',
 'maxSearchResults': 10}))
