"""Sensor platform for Monthly On-Time AI Saving Data."""
import json
import os
import logging
from homeassistant.components.sensor import SensorEntity
from homeassistant.core import HomeAssistant

DOMAIN = "monthly_on_time_ai"
DATA_FILE = "ai_saving_data.json"
_LOGGER = logging.getLogger(__name__)

def setup_platform(hass: HomeAssistant, config, add_entities, discovery_info=None):
    """Set up the sensor platform."""
    _LOGGER.error("Monthly On-Time AI sensor platform is STARTING!")
    file_path = os.path.join(os.path.dirname(__file__), DATA_FILE)
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
        _LOGGER.error("Loaded ai_saving_data.json successfully!")
    except Exception as e:
        _LOGGER.error(f"Failed to load {DATA_FILE}: {e}")
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
    add_entities(sensors)
    _LOGGER.error("Monthly On-Time AI sensors ADDED!")

class AISavingSensor(SensorEntity):
    """Representation of an AI Saving Sensor."""

    def __init__(self, data, unique_id, name, key, day=None):
        self._data = data
        self._unique_id = f"monthly_on_time_ai_{unique_id}"
        self._name = name
        self._key = key
        self._day = day
        if self._day:
            for entry in self._data[self._key]:
                if entry["Day"] == self._day:
                    self._state = entry["OnTime"]
                    break
        else:
            self._state = self._data[self._key]
        _LOGGER.error(f"Created sensor: {self._name} with value {self._state}")

    @property
    def name(self):
        return self._name

    @property
    def unique_id(self):
        return self._unique_id

    @property
    def state(self):
        return self._state