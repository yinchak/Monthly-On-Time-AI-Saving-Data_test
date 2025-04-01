"""Monthly On-Time AI Saving Data integration."""
import logging
from homeassistant.core import HomeAssistant

DOMAIN = "monthly_on_time_ai"
_LOGGER = logging.getLogger(__name__)

def setup(hass: HomeAssistant, config):
    """Set up the component."""
    _LOGGER.error("Monthly On-Time AI is LOADING!")  # 用 error 確保出 log
    hass.helpers.discovery.load_platform("sensor", DOMAIN, {}, config)
    return True
