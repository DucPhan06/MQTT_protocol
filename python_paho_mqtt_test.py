import paho.mqtt.client as mqtt
from config import MQTT_USERNAME, MQTT_PASSWORD, CAFILE, CERTFILE, KEYFILE

# Define topic
topic = "test"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(topic)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("Message received on topic " + msg.topic + ": " + msg.payload.decode())

# Initialize the MQTT client
mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

mqttc.username_pw_set(username=MQTT_USERNAME, password=MQTT_PASSWORD)
mqttc.tls_set(ca_certs=CAFILE, certfile=CERTFILE, keyfile=KEYFILE)

mqttc.on_connect = on_connect
mqttc.on_message = on_message


# Connect to the remote EC2 instance
mqttc.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT, 60)

# Publish a test message
# mqttc.publish("test", "Hello from Python!")

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
mqttc.loop_forever()