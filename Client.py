import time
from counterfit_connection import CounterFitConnection
from counterfit_shims_grove.grove_light_sensor_v1_2 import GroveLightSensor
from counterfit_shims_grove.grove_led import GroveLed
import paho.mqtt.client as mqtt
import json

CounterFitConnection.init('127.0.0.1',1234)

light_sensor = GroveLightSensor(0)

id = '11'

client_telemetry_topic = id + '/telemetry'
client_name = id + 'nightlight_client'

mqtt_client = mqtt.Client(client_name)
mqtt_client.connect('test.mosquitto.org')

mqtt_client.loop_start()

print("MQTT connected!")

while True:
    light = light_sensor.light
    telemetery = json.dumps({'light':light})

    print('Sending telemetry',telemetery)

    mqtt_client.publish(client_telemetry_topic,telemetery)

    time.sleep(5)