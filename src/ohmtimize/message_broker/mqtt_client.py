import paho.mqtt.client as mqtt
import ssl

# Define your MQTT broker details
MQTT_BROKER = '07f079abe9714c73baaf295c62f69fa8.s1.eu.hivemq.cloud'
MQTT_PORT = 8883
MQTT_KEEPALIVE = 60  # seconds
MQTT_USERNAME: str = 'hivemq.pythonclient'    # Replace with your username
MQTT_PASSWORD: str = 'xNQV(q=k:47L9p#2?C6HGf'      # Replace with your password

# Define the topic you want to subscribe to
TOPIC = 'home'

# Define the MQTT client callbacks
def on_connect(client: mqtt.Client, userdata: dict, flags: dict, rc: int, properties=None) -> None:
    print(f"Connected with result code {rc}")
    client.subscribe(TOPIC)

def on_message(client: mqtt.Client, userdata: dict, msg: mqtt.MQTTMessage) -> None:
    print(f"Message received: {msg.topic} {msg.payload.decode()}")  # Decode bytes to string

def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))

# print which topic was subscribed to
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

# Initialize the MQTT client
def start_mqtt() -> None:

    client = mqtt.Client(client_id="07f079abe9714c73baaf295c62f69fa8", userdata=None, protocol=mqtt.MQTTv5)
    client.on_connect = on_connect

    # enable TLS for secure connection
    client.tls_set(tls_version=ssl.PROTOCOL_TLS)
    # set username and password
    client.username_pw_set("hivemq.pythonclient", "xNQV(q=k:47L9p#2?C6HGf")
    # connect to HiveMQ Cloud on port 8883 (default for MQTT)
    client.connect("07f079abe9714c73baaf295c62f69fa8.s1.eu.hivemq.cloud", 8883)

    # setting callbacks, use separate functions like above for better visibility
    client.on_subscribe = on_subscribe
    client.on_message = on_message
    client.on_publish = on_publish
    client.on_connect = on_connect

    # subscribe to all topics of encyclopedia by using the wildcard "#"
    client.subscribe("home/#", qos=1)

    # a single publish, this can also be done in loops, etc.

    # loop_forever for simplicity, here you need to stop the loop manually
    # you can also use loop_start and loop_stop
    client.loop_forever()
