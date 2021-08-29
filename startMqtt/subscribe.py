import json
import random

from paho.mqtt import client as mqtt_client


class DeviceMqttClient(object):
    def __init__(self, broker, port, device_info):
        self.broker = broker
        self.port = port
        self.keepalive = 235
        self.client_id = device_info["device_id"]
        self.device_id = device_info["device_id"]
        self.client = self.connect_mqtt()
        self.topic = "/python/mqtt1"
        self.reply_topic = "/python/mqtt1/reply"

    def connect_mqtt(self) -> mqtt_client:
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)

        client = mqtt_client.Client(self.client_id)
        client.on_connect = on_connect
        client.connect(self.broker, self.port, self.keepalive)
        return client

    def on_message(self, client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        param = "I received the message"
        if msg.topic == self.topic:
            msg_obj_num = json.loads(msg.payload.decode())["message"]
            print("send reply of message {}".format(msg_obj_num))
            self.client.publish(self.reply_topic, payload=param, qos=1)

    def subscribe(self):
        # 订阅所有主题
        self.client.subscribe(self.topic)
        self.client.on_message = self.on_message

    def run(self):
        self.subscribe()
        self.client.loop_forever()


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port, keepalive)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        param = "I received the message"
        if msg.topic == topic:
            msg_obj_num = json.loads(msg.payload.decode())["message"]
            print("send reply of message {}".format(msg_obj_num))
            client.publish(reply_topic, payload=param, qos=1)

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    # run()
    broker = 'broker.emqx.io'
    port = 1883
    device_info = {"device_id": "123123123123123"}
    start_client = DeviceMqttClient(broker, port, device_info)
    start_client.run()
