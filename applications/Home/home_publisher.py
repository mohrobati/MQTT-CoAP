from applications.Home.home_model import Home
from applications.publisher import Publisher
import random
import time


class HomePublisher(Publisher):

    def __init__(self):
        super().__init__()

    def _assignValues(self):
        homes = []
        for i in range(self._numberOfInstances):
            home = Home()
            home.setParking(random.randint(0, 1) == 0)
            home.setLights([(random.randint(0, 1) == 0) for i in range(len(home.lights))])
            home.setDoorlock(random.randint(0, 1) == 0)
            home.setTemperature(int(100*random.uniform(0, 100))/100)
            home.setEnergy(random.randint(0, 100))
            homes.append(home)
        return homes

    def _publish(self, path):
        client = super()._publish(path)
        while True:
            homes = self._assignValues()
            for i in range(len(homes)):
                home = homes[i]
                client.publish(path + str(i) + "/parking", str(home.parking), qos = 1, retain=True)
                client.publish(path + str(i) + "/lights", str(home.lights), qos = 1, retain=True)
                client.publish(path + str(i) + "/doorlock", str(home.doorlock), qos = 1, retain=True)
                client.publish(path + str(i) + "/temperature", str(home.temperature), qos = 1, retain=True)
                client.publish(path + str(i) + "/energy", str(home.energy), qos = 1, retain=True)
            time.sleep(1000)
