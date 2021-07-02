from coapthon.server.coap import CoAP
from coap.Farm.farm_publisher import FarmPublisher
from coap.Home.home_publisher import HomePublisher
from coap.Hospital.hospital_publisher import HospitalPublisher


class CoAPServer(CoAP):
    def __init__(self, host, port, application):
        CoAP.__init__(self, (host, port))
        for i in range(10):
            topic = application + '_' + str(i)
            if application == 'farm':
                self.add_resource(topic, FarmPublisher())
            if application == 'home':
                self.add_resource(topic, HomePublisher())
            if application == 'hospital':
                self.add_resource(topic, HospitalPublisher())


server = CoAPServer("0.0.0.0", 5683, 'hospital')
try:
    server.listen(10)
except KeyboardInterrupt:
    print("Server Shutdown")
    server.close()
    print("Exiting...")
