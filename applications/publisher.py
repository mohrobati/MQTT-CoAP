import paho.mqtt.client as paho


class Publisher:

    def __init__(self):
        self._numberOfInstances = 10
        self._assignValues()

    def _assignValues(self):
        pass

    def _publish(self, path):
        def on_publish(client, userdata, mid):
            print("mid: " + str(mid))
        client = paho.Client()
        client.on_publish = on_publish
        client.connect("broker.mqttdashboard.com", 1883)
        client.loop_start()
        return client

    def startPublishLoop(self, path):
        self._publish(path)
