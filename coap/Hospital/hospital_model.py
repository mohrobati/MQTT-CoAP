class Hospital:

    def __init__(self):
        self.__bloodPressure = (12, 8)
        self.__fever = 0.0
        self.__heartbeat = 0.0
        self.__oxygen = 0.0
        self.__energy = 100

    @property
    def bloodPressure(self):
        return self.__bloodPressure

    def setBloodPressure(self, bloodPressure):
        self.__bloodPressure = bloodPressure

    @property
    def fever(self):
        return self.__fever

    def setFever(self, fever):
        self.__fever = fever

    @property
    def heartbeat(self):
        return self.__heartbeat

    def setHeartbeat(self, heartbeat):
        self.__heartbeat = heartbeat

    @property
    def oxygen(self):
        return self.__oxygen

    def setOxygen(self, oxygen):
        self.__oxygen = oxygen

    @property
    def energy(self):
        return self.__energy

    def setEnergy(self, energy):
        self.__energy = energy

    def __str__(self):
        return str({
            "bloodPressure": self.__bloodPressure,
            "fever": self.__fever,
            "heartbeat": self.__heartbeat,
            "oxygen": self.__oxygen,
            "energy": self.__energy
        })
