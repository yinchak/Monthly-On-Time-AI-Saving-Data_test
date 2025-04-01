"""Initialize the Monthly On-Time AI Saving Data integration."""
import logging
from homeassistant.core import HomeAssistant

DOMAIN = "monthly_on_time_ai"
_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config):
    """Set up the component."""
    _LOGGER.warning("Monthly On-Time AI integration is LOADING!")
    hass.async_create_task(
        hass.helpers.discovery.async_load_platform("sensor", DOMAIN, {}, config)
    )
    return True
