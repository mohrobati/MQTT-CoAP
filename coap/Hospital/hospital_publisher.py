from coap.Hospital.hospital_model import Hospital
from coapthon.resources.resource import Resource
import random
import threading
import time


class HospitalPublisher(Resource):

    def __init__(self, name="HospitalPublisher", coap_server=None):
        super(HospitalPublisher, self).__init__(name, coap_server, visible=True,
                                            observable=True, allow_children=True)
        self.payload = str(self._assignValues())
        threading.Thread(target=self.__updateValues).start()

    def _assignValues(self):
        hospital = Hospital()
        hospital.setBloodPressure((random.randint(5, 20), random.randint(5, 10)))
        hospital.setFever(int(100*random.uniform(0, 100))/100)
        hospital.setHeartbeat(int(100*random.uniform(0, 100))/100)
        hospital.setOxygen(int(100*random.uniform(0, 100))/100)
        hospital.setEnergy(random.randint(0, 100))
        return hospital

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
        res = HospitalPublisher()
        res.location_query = request.uri_query
        res.payload = request.payload
        return res

    def render_DELETE(self, request):
        return True

    # def _publishMQTT(self, path):
    #     client = super()._publishMQTT(path)
    #     while True:
    #         hospitals = self._assignValues()
    #         for i in range(len(hospitals)):
    #             hospital = hospitals[i]
    #             client.publish(path + str(i) + "/bloodPressure", str(hospital.bloodPressure), qos = 2, retain=True)
    #             client.publish(path + str(i) + "/fever", str(hospital.fever), qos = 2, retain=True)
    #             client.publish(path + str(i) + "/heartbeat", str(hospital.heartbeat), qos = 2, retain=True)
    #             client.publish(path + str(i) + "/oxygen", str(hospital.oxygen), qos = 2, retain=True)
    #             client.publish(path + str(i) + "/energy", str(hospital.energy), qos = 2, retain=True)
    #         time.sleep(30)
