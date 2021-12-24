import paho.mqtt.client as mqtt
import time
from json import dumps, loads
from kafka import KafkaProducer


mqtt_client = mqtt.Client("shaparsa")
mqtt_client.username_pw_set('Hans', password='Test')
mqtt_client.connect(host='194.67.112.161', port=1883)


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: dumps(x).encode('utf-8'))

def on_message(client, userdata, message):
    msg_payload = loads(message.payload.decode('utf-8'))
    print("Received MQTT message: ", msg_payload)
    print(type(msg_payload))
    producer.send('v13', value=msg_payload)
#    print(dumps(msg_payload).encode('utf-8'))
    print("KAFKA: Just published to topic v13:", msg_payload)

mqtt_client.loop_start()
mqtt_client.subscribe("v13", 1)
mqtt_client.on_message = on_message
time.sleep(300)
mqtt_client.loop_stop()