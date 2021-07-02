from coapthon.client.helperclient import HelperClient
import time, ast, threading


applications = {'farm': ("127.0.0.1", 5681), 'home': ("127.0.0.1", 5682), 'hospital': ("127.0.0.1", 5683)}
all_values = {app: {str(j): {} for j in range(10)} for app in applications}


def submitDict(path, values):
    topic = path.split("_")
    for key in list(values.keys()):
        all_values[topic[0]][topic[1]][key] = values[key]


def getFromPublishers():
    while True:
        for application in applications:
            client = HelperClient(server=applications[application])
            for i in range(10):
                path = application + "_" + str(i)
                response = client.get(path)
                submitDict(path, ast.literal_eval(response.payload))
            client.close()
        time.sleep(31)


def sendForSubscribers(host, port):
    client = HelperClient(server=(host, port))
    while True:
        response = client.post("/subscribe", str(all_values))
        time.sleep(31)


threading.Thread(target=getFromPublishers).start()
threading.Thread(target=sendForSubscribers, args=("127.0.0.1", 5684, )).start()
