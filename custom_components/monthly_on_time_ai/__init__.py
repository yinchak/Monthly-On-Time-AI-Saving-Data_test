"""Initialize the Monthly On-Time AI Saving Data integration."""
from homeassistant.core import HomeAssistant

DOMAIN = "monthly_on_time_ai"

async def async_setup(hass: HomeAssistant, config):
    """Set up the component."""
    hass.data.setdefault(DOMAIN, {})
    # 直接啟動 sensor platform
    hass.async_create_task(
        hass.helpers.discovery.async_load_platform("sensor", DOMAIN, {}, config)
    )
    return True
