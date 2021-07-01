class Store:

    def __init__(self, applications, initPath):
        self.__applications = applications
        self.__values = {app: {str(j): {} for j in range(10)} for app in applications}
        self.__initPath = initPath

    def getValues(self, topic):
        if topic == "/":
            return self.__values
        else:
            parts = topic.split("/")
            if len(parts) == 2:
                return self.__values[parts[0]][parts[1]]
            elif len(parts) == 3:
                return self.__values[parts[0]][parts[1]][parts[2]]

    def submitValues(self, values):
        topic = values[0].replace(self.__initPath, "").split("/")
        self.__values[topic[0]][topic[1]][topic[2]] = values[1].decode()

