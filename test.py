import sys
import time
from opcua import Client

url = "opc.tcp://127.0.0.1:49320"

try:
    client = Client(url)
    client.connect()
    print("Connected to opcua server")
except Exception as err:
    print('err',err)
    sys.exit(1)


class SubHandler(object):
    def datachange_notification(self, node, val, data):
        print("Received values:",val)


billet_temp = "ns=2;s=Demo.Press5.Billet temperature"
container_temp = "ns=2;s=Demo.Press5.Container temperature"
plan_num = "ns=2;s=Demo.Press5.Plan number"
material_num = "ns=2;s=Demo.Press5.Material number"
active_plan = "ns=2;s=Demo.Press5.Active Plan"
prof_length = "ns=2;s=Demo.Press5.Profile length"
prof_weight = "ns=2;s=Demo.Press5.Profile weight"

tags = [billet_temp, container_temp, plan_num, material_num, active_plan, prof_length, prof_weight]
handler = SubHandler()
sub = client.create_subscription(500, handler)

if __name__ == '__main__':
    for tag in tags:
        my_node = client.get_node(tag)
        handle = sub.subscribe_data_change(my_node)

    #subscription handler
    #subscription
    #nodes of interest
