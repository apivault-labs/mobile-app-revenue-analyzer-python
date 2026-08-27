from mobile_app_revenue_analyzer import MobileAppRevenueAnalyzerClient

client = MobileAppRevenueAnalyzerClient()
payload = {'mode': 'search',
 'searchTerms': ['invoice maker'],
 'country': 'us',
 'maxSearchResults': 10}
# Add more targets or queries to the list fields supported by this Actor.
rows = client.run(payload)
print(f"Received {len(rows)} rows")
