# Mobile App Revenue & Competitor Analyzer — Python SDK

Python client for the [Mobile App Revenue & Competitor Analyzer Apify Actor](https://apify.com/apivault_labs/app-revenue-analyzer). Send public Actor inputs, wait for the hosted run, and receive clean Dataset rows without maintaining scraping infrastructure.

[![Apify Actor](https://img.shields.io/badge/Apify-Actor-blue)](https://apify.com/apivault_labs/app-revenue-analyzer)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## Results

- App revenue and download estimates
- Search and direct-app analysis
- Chart, update and in-app-purchase signals
- Developer portfolio and competitors

The Actor uses public marketplace signals and returns estimates or ranges where a platform does not publish exact figures.

## Install

```bash
pip install git+https://github.com/apivault-labs/mobile-app-revenue-analyzer-python.git
```

Create an Apify token at [Console → Integrations](https://console.apify.com/account/integrations), then:

```python
from mobile_app_revenue_analyzer import MobileAppRevenueAnalyzerClient

client = MobileAppRevenueAnalyzerClient(api_token="apify_api_xxxxxx")
rows = client.run({'mode': 'search',
 'searchTerms': ['invoice maker'],
 'country': 'us',
 'maxSearchResults': 10})
print(rows[0] if rows else "No results")
```

You can set `APIFY_API_TOKEN` instead of passing the token in code.

## Public input options

| Field | Type | Default | Description |
|---|---|---|---|
| `mode` | `string` | `analyze` | analyze = full reports for given apps. search = find top apps for keywords with estimates (ASO research). |
| `searchTerms` | `array` | `—` | App-store keywords to search, e.g. 'meditation', 'budget tracker'. |
| `maxSearchResults` | `integer` | `25` | How many top results to return per keyword (1-50). |
| `maxConcurrency` | `integer` | `10` | How many apps are processed in parallel (analyze mode). Higher = faster bulk runs. |
| `targets` | `array` | `—` | Each item can be an App Store URL (apps.apple.com/.../id123456), a numeric App Store app ID, or a Google Play package name (v1: Play inputs return a free pointer to the iOS twin). |
| `country` | `string` | `us` | Two-letter App Store country code (us, gb, de, ...). Affects ratings, charts and pricing. |

The complete, versioned schema is also available on the [Actor page](https://apify.com/apivault_labs/app-revenue-analyzer).

## Pricing

Pay per delivered result through Apify, starting around **$1/1,000 results** on paid tiers. Free-plan pricing and platform usage can differ; check the Actor page before large runs.

## Examples

- `examples/quickstart.py` — first run
- `examples/bulk_analysis.py` — expand a target list
- `examples/export_csv.py` — save flat result fields
- `examples/save_json.py` — preserve nested output
- `examples/cost_estimate.py` — estimate result-event charges
- `examples/environment_token.py` — keep credentials out of code

## Architecture and privacy

This repository is intentionally a thin API client. Collection, retries, analysis and billing run inside the hosted Apify Actor. No private implementation, credentials, scoring weights or infrastructure configuration are included.

## License

MIT. The hosted Actor is a separate paid service governed by Apify terms.
