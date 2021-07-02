from coap.Farm.farm_model import Farm
from coapthon.resources.resource import Resource
import random
import threading
import time


class FarmPublisher(Resource):

    def __init__(self, name="FarmPublisher", coap_server=None):
        super(FarmPublisher, self).__init__(name, coap_server, visible=True,
                                            observable=True, allow_children=True)
        self.payload = str(self._assignValues())
        threading.Thread(target=self.__updateValues).start()

    def _assignValues(self):
        farm = Farm()
        farm.setHumidity(int(100*random.uniform(0, 100))/100)
        farm.setLight(int(100*random.uniform(0, 100))/100)
        farm.setMoisture(int(100*random.uniform(0, 100))/100)
        farm.setTemperature(int(100*random.uniform(0, 100))/100)
        farm.setEnergy(random.randint(0, 100))
        return farm

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
        res = FarmPublisher()
        res.location_query = request.uri_query
        res.payload = request.payload
        return res

    def render_DELETE(self, request):
        return True

    #
    # def _publishMQTT(self, path):
    #     client = super()._publishMQTT(path)
    #     while True:
    #         farms = self._assignValues()
    #         for i in range(len(farms)):
    #             farm = farms[i]
    #             client.publish(path + str(i) + "/humidity", str(farm.humidity), qos = 1, retain=True)
    #             client.publish(path + str(i) + "/light", str(farm.light), qos = 1, retain=True)
    #             client.publish(path + str(i) + "/moisture", str(farm.moisture), qos = 1, retain=True)
    #             client.publish(path + str(i) + "/temperature", str(farm.temperature), qos = 1, retain=True)
    #             client.publish(path + str(i) + "/energy", str(farm.energy), qos = 1, retain=True)
    #         time.sleep(1000)
