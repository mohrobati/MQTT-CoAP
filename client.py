from coapthon.client.helperclient import HelperClient

host = "127.0.0.1"
port = 5683
path = "farm_1"

client = HelperClient(server=(host, port))
response = client.get(path)
# print(response.payload)
print(response.pretty_print())
client.stop()