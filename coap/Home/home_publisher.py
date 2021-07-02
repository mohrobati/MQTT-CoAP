from coap.Home.home_model import Home
from coapthon.resources.resource import Resource
import random
import threading
import time


class HomePublisher(Resource):

    def __init__(self, name="HomePublisher", coap_server=None):
        super(HomePublisher, self).__init__(name, coap_server, visible=True,
                                            observable=True, allow_children=True)
        self.payload = str(self._assignValues())
        threading.Thread(target=self.__updateValues).start()

    def _assignValues(self):
        home = Home()
        home.setParking(random.randint(0, 1) == 0)
        home.setLights([(random.randint(0, 1) == 0) for i in range(len(home.lights))])
        home.setDoorlock(random.randint(0, 1) == 0)
        home.setTemperature(int(100*random.uniform(0, 100))/100)
        home.setEnergy(random.randint(0, 100))
        return home

    def __updateValues(self):
        while True:
            self.payload = str(self._assignValues())
            time.sleep(30)

    def render_GET(self, request):
        return self

    def render_PUT(self, request):
        self.payload = request.payload
        return self

    def render_POST(self, request):
        res = HomePublisher()
        res.location_query = request.uri_query
        res.payload = request.payload
        return res

    def render_DELETE(self, request):
        return True


    #
    # def _publishMQTT(self, path):
    #     client = super()._publishMQTT(path)
    #     while True:
    #         homes = self._assignValues()
    #         for i in range(len(homes)):
    #             home = homes[i]
    #             client.publish(path + str(i) + "/parking", str(home.parking), qos = 1, retain=True)
    #             client.publish(path + str(i) + "/lights", str(home.lights), qos = 1, retain=True)
    #             client.publish(path + str(i) + "/doorlock", str(home.doorlock), qos = 1, retain=True)
    #             client.publish(path + str(i) + "/temperature", str(home.temperature), qos = 1, retain=True)
    #             client.publish(path + str(i) + "/energy", str(home.energy), qos = 1, retain=True)
    #         time.sleep(1000)
