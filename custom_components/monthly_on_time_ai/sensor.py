"""Sensor platform for Monthly On-Time AI Saving Data."""
from homeassistant.components.sensor import SensorEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

DOMAIN = "monthly_on_time_ai"

async def async_setup_platform(
    hass: HomeAssistant,
    config,
    async_add_entities: AddEntitiesCallback,
    discovery_info=None
):
    """Set up the sensor platform."""
    # 先用硬碼數據，確保 sensor 出咗
    sensors = [
        AISavingSensor("ai_saving_total", "AI Saving Total", 3384),
        AISavingSensor("monthly_on_time", "Monthly On-Time", 33270),
        AISavingSensor("monthly_on_time_ai", "Monthly On-Time AI", 29886),
        AISavingSensor("on_time_02_01", "On-Time 02-01", 1395),
        AISavingSensor("on_time_ai_02_01", "On-Time AI 02-01", 1394)
    ]
    async_add_entities(sensors)

class AISavingSensor(SensorEntity):
    """Representation of an AI Saving Sensor."""

    def __init__(self, unique_id, name, value):
        """Initialize the sensor."""
        self._unique_id = f"monthly_on_time_ai_{unique_id}"
        self._name = name
        self._state = value

    @property
    def name(self):
        return self._name

    @property
    def unique_id(self):
        return self._unique_id

    @property
    def state(self):
        return self._state