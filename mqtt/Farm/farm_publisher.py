from mqtt.Farm.farm_model import Farm
from mqtt.publisher import Publisher
import random
import time


class FarmPublisher(Publisher):

    def __init__(self):
        super().__init__()

    def _assignValues(self):
        farms = []
        for i in range(self._numberOfInstances):
            farm = Farm()
            farm.setHumidity(int(100*random.uniform(0, 100))/100)
            farm.setLight(int(100*random.uniform(0, 100))/100)
            farm.setMoisture(int(100*random.uniform(0, 100))/100)
            farm.setTemperature(int(100*random.uniform(0, 100))/100)
            farm.setEnergy(random.randint(0, 100))
            farms.append(farm)
        return farms

    def _publishMQTT(self, path):
        client = super()._publishMQTT(path)
        while True:
            farms = self._assignValues()
            for i in range(len(farms)):
                farm = farms[i]
                client.publish(path + str(i) + "/humidity", str(farm.humidity), qos = 1, retain=True)
                client.publish(path + str(i) + "/light", str(farm.light), qos = 1, retain=True)
                client.publish(path + str(i) + "/moisture", str(farm.moisture), qos = 1, retain=True)
                client.publish(path + str(i) + "/temperature", str(farm.temperature), qos = 1, retain=True)
                client.publish(path + str(i) + "/energy", str(farm.energy), qos = 1, retain=True)
            time.sleep(1000)
