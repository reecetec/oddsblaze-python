# Getting Started

## Installation

Install oddsblaze using uv:

```bash
uv add oddsblaze
```

Or with pip:

```bash
pip install oddsblaze
```

## Configuration

You need an API key from [oddsblaze.com](https://www.oddsblaze.com/).

Set your API key using one of these methods (checked in order):

=== "Environment Variable"

    ```bash
    export ODDSBLAZE_API_KEY=your_key
    ```

=== ".env File"

    Create a `.env` file in your project root:

    ```
    ODDSBLAZE_API_KEY=your_key
    ```

=== "Global Config"

    Create a file at `~/.oddsblaze`:

    ```
    ODDSBLAZE_API_KEY=your_key
    ```

### Price Format

You can configure the default price format:

```bash
export ODDSBLAZE_PRICE_FORMAT=decimal  # american (default), decimal, fractional, probability
```

Or set it per-request:

```python
from oddsblaze import OddsblazeClient, PriceFormat

client = OddsblazeClient()
odds = client.get_odds("draftkings", "nfl", price=PriceFormat.DECIMAL)
```

## Basic Usage

```python
from oddsblaze import OddsblazeClient

client = OddsblazeClient()

# Get NFL odds from DraftKings
odds = client.get_odds("draftkings", "nfl")

for event in odds.events:
    print(f"{event.teams.away.name} @ {event.teams.home.name}")
    for odd in event.odds:
        print(f"  {odd.name}: {odd.price}")
```

## Error Handling

The SDK raises specific exceptions for API errors:

```python
from oddsblaze import (
    OddsblazeClient,
    OddsblazeError,
    AuthenticationError,
    InvalidMarketError,
    EventNotFoundError,
    PlayerNotFoundError,
)

client = OddsblazeClient()

try:
    result = client.grade_bet("invalid-id")
except EventNotFoundError:
    print("Event not found")
except OddsblazeError as e:
    print(f"API error: {e.message}")
```
