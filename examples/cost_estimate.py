from mobile_app_revenue_analyzer import MobileAppRevenueAnalyzerClient

for count in (10, 100, 1000):
    print(count, MobileAppRevenueAnalyzerClient.estimate_cost(count), "USD estimated result charges")
