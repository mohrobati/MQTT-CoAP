from mqtt.Hospital.hospital_model import Hospital
from mqtt.publisher import Publisher
import random
import time


class HospitalPublisher(Publisher):

    def __init__(self):
        super().__init__()

    def _assignValues(self):
        hospitals = []
        for i in range(self._numberOfInstances):
            hospital = Hospital()
            hospital.setBloodPressure((random.randint(5, 20), random.randint(5, 10)))
            hospital.setFever(int(100*random.uniform(0, 100))/100)
            hospital.setHeartbeat(int(100*random.uniform(0, 100))/100)
            hospital.setOxygen(int(100*random.uniform(0, 100))/100)
            hospital.setEnergy(random.randint(0, 100))
            hospitals.append(hospital)
        return hospitals

    def _publishMQTT(self, path):
        client = super()._publishMQTT(path)
        while True:
            hospitals = self._assignValues()
            for i in range(len(hospitals)):
                hospital = hospitals[i]
                client.publish(path + str(i) + "/bloodPressure", str(hospital.bloodPressure), qos = 2, retain=True)
                client.publish(path + str(i) + "/fever", str(hospital.fever), qos = 2, retain=True)
                client.publish(path + str(i) + "/heartbeat", str(hospital.heartbeat), qos = 2, retain=True)
                client.publish(path + str(i) + "/oxygen", str(hospital.oxygen), qos = 2, retain=True)
                client.publish(path + str(i) + "/energy", str(hospital.energy), qos = 2, retain=True)
            time.sleep(30)
