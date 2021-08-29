import paho.mqtt.client as mqtt
import json
import time
import requests
import sys

HOST = "broker.emqx.io"
PORT = 1883
client_id = "1083421xxxxx"  # 没有就不写，此处部分内容用xxx代替原内容，下同


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("data/receive", 1)         # 订阅消息


def on_message(client, userdata, msg):
    print("主题:"+msg.topic+" 消息:"+str(msg.payload.decode('utf-8')))


def on_subscribe(client, userdata, mid, granted_qos):
    print("On Subscribed: qos = %d" % granted_qos)


def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection %s" % rc)


data = {
    "type": 2,
    "timestamp": time.time(),
    "messageId": "9fcda359-89f5-4933-xxxx",
    "command": "xx/recommend",
    "data": {
        "openId": "xxxx",
        "appId": "xxxx",
        "recommendType": "temRecommend"
    }
}


class TestClient(object):
    def __init__(self, security_host, device_info):
        self.security_host = security_host
        self.device_info = device_info
        self.user_name = None
        self.password = None
        self.mqtt_host = None
        self.mqtt_port = None

    def get_mqtt_host_jwt(self):
        response = requests.post(url=self.security_host, json=self.device_info)
        if response.status_code != 200:
            print("get_jwt_error")
            sys.exit()
        response_info = json.loads(response.text)
        self.mqtt_host = response_info.get("host", "")
        self.mqtt_port = response_info.get("port", "")
        self.password = response_info.get("jwt", "")

    def run(self):
        param = json.dumps(data)
        client = mqtt.Client(client_id)
        # client.tls_set()
        client.username_pw_set(self.user_name, self.password)
        client.on_connect = on_connect
        client.on_message = on_message
        client.on_subscribe = on_subscribe
        client.on_disconnect = on_disconnect
        client.connect(HOST, PORT, 60)
        client.publish("data/send", payload=param, qos=1)  # 发送消息
        client.loop_forever()


if __name__ == "__main__":
    param = json.dumps(data)
    client = mqtt.Client(client_id)
    client.username_pw_set("xxxxxx", "xxxxxx")
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_subscribe = on_subscribe
    client.on_disconnect = on_disconnect
    client.connect(HOST, PORT, 60)
    client.publish("data/send", payload=param, qos=1)     # 发送消息
    client.loop_forever()

