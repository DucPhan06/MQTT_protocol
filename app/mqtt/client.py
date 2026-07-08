import paho.mqtt.client as mqtt
from app.core.mqtt_config import (
    MQTT_USERNAME,
    MQTT_PASSWORD,
    MQTT_BROKER_HOST,
    MQTT_BROKER_PORT,
    CAFILE,
    CERTFILE,
    KEYFILE,
)

class MQTTManager:
    def __init__(self, id: str, topic: str = "news/v1/#", on_client_connect = None):
        self.id = id
        self.topic = topic
        self.client = self.create_client()
        self.connected = False
        self.on_client_connect = on_client_connect

    def create_client(self):
        client = mqtt.Client( mqtt.CallbackAPIVersion.VERSION2, client_id=self.id)

        client.username_pw_set(username=MQTT_USERNAME, password=MQTT_PASSWORD)
        client.tls_set(ca_certs=CAFILE, certfile=CERTFILE, keyfile=KEYFILE)

        client.on_connect = self.on_connect
        client.on_message = self.on_message

        return client

    def on_connect(self, client, userdata, flags, reason_code, properties):
        print(f"Connected with result code {reason_code}")
        self.subscribe(self.topic)
        self.connected = True

        if self.on_client_connect:
            self.on_client_connect(self.id)

    def on_message(self, client, userdata, msg):
        print("Message received on topic " + msg.topic + ": " + msg.payload.decode())

    def connect(self):
        self.client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT, 60)
        self.client.loop_start()

    def publish(self, topic: str, msg: str, qos: int = 0, retain: bool = False):
        if not self.connected:
            print("Error: client is not connected.\n")
            return

        self.client.publish(topic, msg, qos=qos, retain=retain)
    
    def subscribe(self, topic: str):
        self.client.subscribe(topic)

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()
        self.connected = False