from app.core.config import require_env
from pathlib import Path


MQTT_USERNAME = require_env("MQTT_USERNAME")
MQTT_PASSWORD = require_env("MQTT_PASSWORD")

CAFILE = Path(require_env("CAFILE"))
CERTFILE = Path(require_env("CERTFILE"))
KEYFILE = Path(require_env("KEYFILE"))

MQTT_BROKER_HOST = require_env("MQTT_BROKER_HOST")
MQTT_BROKER_PORT = int(require_env("MQTT_BROKER_PORT"))

NEWS_FETCH_TIMER = 15