
# from opcua import Client


# client = Client("opc.tcp://127.0.0.1:49320")
# client.connect()


# tags = ["ns=2;s=Demo.Press5.Billet temperature","ns=2;s=Demo.Press5.Container temperature","ns=2;s=Demo.Press5.Plan number","ns=2;s=Demo.Press5.Material number","ns=2;s=Demo.Press5.Active plan","ns=2;s=Demo.Press5.Profile length","ns=2;s=Demo.Press5.Profile weight"]
# node_id = "ns=2;s=Demo.Press5."  # Replace "ns=2;s=MyVariable" with your actual Node ID


# for tag in tags:
#     identifier = tag.split('.')[2]
#     value = client.get_node(tag).get_value()

#     print(f"{identifier} : {value}")


# # value = variable.get_value()
# # print("Value of the variable:", node_id)

from opcua import Client
from opcua import ua

# Define a callback function to handle data change notifications
def datachange_notification(node, val, data):
    print("hello")
    print("Value of variable '{}' changed to: {}".format(node.get_browse_name().Name, val))

# Connect to the OPC UA server
client = Client("opc.tcp://127.0.0.1:49320")
try:
    client.connect()

except Exception as e:
    print("Error connecting to server:", e)
    exit()

# Create a subscription and specify the callback function
subscription = client.create_subscription(10000, datachange_notification)  # Set a longer period

# Get node objects for each tag
tags = ["ns=2;s=Demo.Press5.Billet temperature",
        "ns=2;s=Demo.Press5.Container temperature",
        "ns=2;s=Demo.Press5.Plan number",
        "ns=2;s=Demo.Press5.Material number",
        "ns=2;s=Demo.Press5.Active plan",
        "ns=2;s=Demo.Press5.Profile length",
        "ns=2;s=Demo.Press5.Profile weight"]

for tag in tags:
    try:
        node = client.get_node(tag)
        handle = subscription.subscribe_data_change(node)
        print(handle)
    except ua.UaError as e:
        print(f"Error getting node {tag}: {e}")

try:
    while True:
        pass
except KeyboardInterrupt:
    pass

# Disconnect from the server
finally:
    client.disconnect()
