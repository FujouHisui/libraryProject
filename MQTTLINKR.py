
# python3.6
import random

from paho.mqtt import client as mqtt_client

broker = 'la.hisui.tech'
port = 1883
topic = "/RFID/schoolcard_8266"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'



def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def subscribe(client: mqtt_client):
    def on_message(msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message

def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


def legit_data(data):
    data_type = data[0]
    data_new = data[1:]
    if data_type == "P" or data_type == "B":
        if data_new.isdigit():
            return data_type, data_new
        else:
            return -1
    else:
        return -1


if __name__ == '__main__':
    print(legit_data("P341243")[1])
