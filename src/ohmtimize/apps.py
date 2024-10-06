from django.apps import AppConfig

from ohmtimize.message_broker import mqtt_client

class OhmtimizeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ohmtimize'

    def ready(self):
        mqtt_client.start_mqtt()
