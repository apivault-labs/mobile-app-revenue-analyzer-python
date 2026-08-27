import json
from mobile_app_revenue_analyzer import MobileAppRevenueAnalyzerClient

rows = MobileAppRevenueAnalyzerClient().run({'mode': 'search',
 'searchTerms': ['invoice maker'],
 'country': 'us',
 'maxSearchResults': 10})
with open("results.json", "w", encoding="utf-8") as handle:
    json.dump(rows, handle, ensure_ascii=False, indent=2)
