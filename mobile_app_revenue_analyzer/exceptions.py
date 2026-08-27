"""Public exception hierarchy for the Mobile App Revenue & Competitor Analyzer SDK."""

class MobileAppRevenueAnalyzerError(Exception):
    """Base SDK error."""

class AuthenticationError(MobileAppRevenueAnalyzerError):
    """The Apify token is missing or rejected."""

class ActorRunError(MobileAppRevenueAnalyzerError):
    """The Actor run or Dataset request failed."""

class ActorTimeoutError(MobileAppRevenueAnalyzerError):
    """The client stopped waiting before the Actor completed."""
