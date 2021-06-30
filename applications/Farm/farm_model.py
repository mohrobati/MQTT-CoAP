class Farm:

    def __init__(self):
        self.__humidity = 0.0
        self.__light = 0.0
        self.__moisture = 0.0
        self.__temperature = 0.0
        self.__energy = 100

    @property
    def humidity(self):
        return self.__humidity

    def setHumidity(self, humidity):
        self.__humidity = humidity

    @property
    def light(self):
        return self.__light

    def setLight(self, light):
        self.__light = light

    @property
    def moisture(self):
        return self.__moisture

    def setMoisture(self, moisture):
        self.__moisture = moisture

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
