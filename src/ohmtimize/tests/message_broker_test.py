import unittest
from unittest.mock import MagicMock, patch
import paho.mqtt.client as mqtt
from ohmtimize.message_broker import mqtt_client


class TestMQTTClient(unittest.TestCase):

    @patch('paho.mqtt.client.Client')
    def test_start_mqtt(self, mock_mqtt_client):
        # Arrange
        mock_client_instance = mock_mqtt_client.return_value
        mock_client_instance.connect.return_value = None
        mock_client_instance.subscribe.return_value = (mqtt.MQTT_ERR_SUCCESS, 1)

        # Act
        mqtt_client.start_mqtt()

        # Assert
        mock_mqtt_client.assert_called_once_with(client_id="07f079abe9714c73baaf295c62f69fa8", userdata=None, protocol=mqtt.MQTTv5)
        mock_client_instance.tls_set.assert_called_once()
        mock_client_instance.username_pw_set.assert_called_once_with("hivemq.pythonclient", "xNQV(q=k:47L9p#2?C6HGf")
        mock_client_instance.connect.assert_called_once_with("07f079abe9714c73baaf295c62f69fa8.s1.eu.hivemq.cloud", 8883)
        mock_client_instance.loop_forever.assert_called_once()

    def test_on_connect(self):
        # Arrange
        mock_client = MagicMock()
        userdata = {}
        flags = {}
        rc = 0

        # Act
        mqtt_client.on_connect(mock_client, userdata, flags, rc)

        # Assert
        mock_client.subscribe.assert_called_once_with("home")

    def test_on_message(self):
        # Arrange
        mock_client = MagicMock()
        userdata = {}
        mock_message = MagicMock()
        mock_message.topic = "home/test"
        mock_message.payload.decode.return_value = "test message"

        # Act
        mqtt_client.on_message(mock_client, userdata, mock_message)

        # Assert
        mock_message.payload.decode.assert_called_once()

    def test_on_subscribe(self):
        # Arrange
        mock_client = MagicMock()
        userdata = {}
        mid = 1
        granted_qos = [1]

        # Act
        mqtt_client.on_subscribe(mock_client, userdata, mid, granted_qos)

        # Assert
        # Check if the subscribe callback prints the correct mid and QoS
        with patch('builtins.print') as mocked_print:
            mqtt_client.on_subscribe(mock_client, userdata, mid, granted_qos)
            mocked_print.assert_called_once_with(f"Subscribed: {mid} {granted_qos}")

    def test_on_publish(self):
        # Arrange
        mock_client = MagicMock()
        userdata = {}
        mid = 1

        # Act
        with patch('builtins.print') as mocked_print:
            mqtt_client.on_publish(mock_client, userdata, mid)

        # Assert
        mocked_print.assert_called_once_with(f"mid: {mid}")

if __name__ == '__main__':
    unittest.main()
