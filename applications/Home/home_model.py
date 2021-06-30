class Home:

    def __init__(self):
        self.__parking = False
        self.__lights = [False for i in range(5)]
        self.__doorlock = False
        self.__temperature = 0.0
        self.__energy = 100

    @property
    def parking(self):
        return self.__parking

    def setParking(self, parking):
        self.__parking = parking

    @property
    def lights(self):
        return self.__lights

    def setLights(self, lights):
        self.__lights = lights

    @property
    def doorlock(self):
        return self.__doorlock

    def setDoorlock(self, doorlock):
        self.__doorlock = doorlock

    @property
    def temperature(self):
        return self.__temperature

    def setTemperature(self, temperature):
        self.__temperature = temperature

    @property
    def energy(self):
        return self.__energy

    def setEnergy(self, energy):
        self.__energy = energy
