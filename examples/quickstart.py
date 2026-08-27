from mobile_app_revenue_analyzer import MobileAppRevenueAnalyzerClient

client = MobileAppRevenueAnalyzerClient()
rows = client.run({'mode': 'search',
 'searchTerms': ['invoice maker'],
 'country': 'us',
 'maxSearchResults': 10})
print(rows[0] if rows else "No results")
