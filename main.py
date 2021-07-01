from applications.Hospital.hospital_publisher import HospitalPublisher
from applications.Home.home_publisher import HomePublisher
from applications.Farm.farm_publisher import FarmPublisher


pub1 = HospitalPublisher()
pub1.startPublishLoop("IoT_9631028_MQTT/hospital/")

# pub2 = HomePublisher()
# pub2.startPublishLoop("IoT_9631028_MQTT/home/")

# pub3 = FarmPublisher()
# pub3.startPublishLoop("IoT_9631028_MQTT/farm/")
