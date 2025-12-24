from importlib.metadata import version

from .client import OddsblazeClient
from .settings import get_settings

__version__ = version("oddsblaze")

settings = get_settings()
client = OddsblazeClient(settings=settings)

__all__ = ["client", "settings"]
