import threading
import multiprocessing
import paho.mqtt.client as mqtt
import time
import random

HOST = "broker.emqx.io"
PORT = 1883


class MqttTest(object):
    def __init__(self, client_id):
        self.client_id = client_id
        self.client = mqtt.Client(self.client_id)
        self.start_client()

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        client.subscribe("data/receive", 1)  # 订阅消息

    def on_message(self, client, userdata, msg):
        print("主题:" + msg.topic + " 消息:" + str(msg.payload.decode('utf-8')))

    def on_subscribe(self, client, userdata, mid, granted_qos):
        print("On Subscribed: qos = %d" % granted_qos)

    def on_disconnect(self, client, userdata, rc):
        if rc != 0:
            print("Unexpected disconnection %s" % rc)

    def start_client(self):
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_subscribe = self.on_subscribe
        self.client.on_disconnect = self.on_disconnect
        self.client.connect(HOST, PORT, 60)


def test_a(device: MqttTest):
    while True:
        device.client.loop_start()
        print("start")
        time.sleep(2)
        device.client.loop_stop()
        print("end")


def test_b():
    for i in range(10):
        client_id = str(random.randint(1, 9999))
        print(client_id)
        device = MqttTest(client_id)
        test_thread = threading.Thread(target=test_a, args=(device, ))
        test_thread.start()


if __name__ == "__main__":
    for i in range(1):
        test_process = multiprocessing.Process(target=test_b)
        test_process.start()
        test_process.join()
    # start_test = MqttTest("123")
    # start_test.client.loop_forever()
