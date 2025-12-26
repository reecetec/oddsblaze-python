# oddsblaze-python

Python SDK for the [OddsBlaze API](https://docs.oddsblaze.com/).

## Features

- **Pydantic models** for all API responses
- **Type hints** throughout
- **Automatic error handling** with custom exceptions
- **Configurable price formats** (american, decimal, fractional, etc.)

## Quick Start

```bash
uv add oddsblaze
```

```python
from oddsblaze import OddsblazeClient

client = OddsblazeClient()

# Get NFL odds from DraftKings
odds = client.get_odds("draftkings", "nfl")
for event in odds.events:
    print(f"{event.teams.away.name} @ {event.teams.home.name}")
```

See [Getting Started](getting-started.md) for setup and configuration.