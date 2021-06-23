# python3.6
import random

from paho.mqtt import client as mqtt_client

broker = 'la.hisui.tech'
port = 1883
topic = "/RFID/schoolcard_8266"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'


# def connect_mqtt() -> mqtt_client:
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
    def on_message(client, userdata, msg):
        received_msg = msg.payload.decode()
        print(f"Received `{received_msg}` from `{msg.topic}` topic")
        return received_msg

    client.subscribe(topic)
    client.on_message = on_message



def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


#if __name__ == '__main__':
#    run()
