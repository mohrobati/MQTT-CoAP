from .data_store import Store
import paho.mqtt.client as paho


class Subscriber:

    def __init__(self, applications, initPath):
        self.__applications = applications
        self.__initPath = initPath
        self.__store = Store(self.__applications, initPath)

    def getStore(self):
        return self.__store

    def runSubscriber(self):
        def on_subscribe(client, userdata, mid, granted_qos):
            print("Subscribed: " + str(mid) + " " + str(granted_qos))

        def on_message(client, userdata, msg):
            self.__store.submitValues([msg.topic, msg.payload])

        client = paho.Client()
        client.on_subscribe = on_subscribe
        client.on_message = on_message
        client.connect("broker.mqttdashboard.com", 1883)
        for app in self.__applications:
            client.subscribe(self.__initPath + app + "/#", qos=1)

        client.loop_forever()
