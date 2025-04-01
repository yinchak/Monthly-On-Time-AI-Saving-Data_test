"""Sensor platform for Monthly On-Time AI Saving Data."""
import json
import os
from homeassistant.components.sensor import SensorEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

DOMAIN = "monthly_on_time_ai"
DATA_FILE = "ai_saving_data.json"

async def async_setup_platform(
    hass: HomeAssistant,
    config,
    async_add_entities: AddEntitiesCallback,
    discovery_info=None
):
    """Set up the sensor platform."""
    # 改用相對路徑搵文件
    file_path = os.path.join(os.path.dirname(__file__), DATA_FILE)
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
    except Exception as e:
        hass.components.logger.error(f"Error loading {DATA_FILE}: {e}")
        return

    sensors = [
        AISavingSensor(data, "ai_saving_total", "AI Saving Total", "AISaving"),
        AISavingSensor(data, "monthly_on_time", "Monthly On-Time", "MonthlyOnTime"),
        AISavingSensor(data, "monthly_on_time_ai", "Monthly On-Time AI", "MonthlyOnTimeAI")
    ]

    for day_data in data["MonthlyOnTimeDetail"]:
        sensors.append(
            AISavingSensor(
                data,
                f"on_time_{day_data['Day']}",
                f"On-Time {day_data['Day']}",
                "MonthlyOnTimeDetail",
                day_data["Day"]
            )
        )
    for day_data in data["MonthlyOnTimeAIDetail"]:
        sensors.append(
            AISavingSensor(
                data,
                f"on_time_ai_{day_data['Day']}",
                f"On-Time AI {day_data['Day']}",
                "MonthlyOnTimeAIDetail",
                day_data["Day"]
            )
        )

    async_add_entities(sensors)

class AISavingSensor(SensorEntity):
    """Representation of an AI Saving Sensor."""

    def __init__(self, data, unique_id, name, key, day=None):
        """Initialize the sensor."""
        self._data = data
        self._unique_id = f"monthly_on_time_ai_{unique_id}"
        self._name = name
        self._key = key
        self._day = day
        self._state = None
        self.update()  # 一開始就更新狀態

    @property
    def name(self):
        return self._name

    @property
    def unique_id(self):
        return self._unique_id

    @property
    def state(self):
        return self._state

    def update(self):
        """Update the sensor state."""
        try:
            if self._day:
                for entry in self._data[self._key]:
                    if entry["Day"] == self._day:
                        self._state = entry["OnTime"]
                        break
            else:
                self._state = self._data[self._key]
        except Exception as e:
            self.hass.components.logger.error(f"Error updating {self._name}: {e}")