'''
simulate a smart cooler which is equipped with a humidity 
sensor and a temperature sensor. If either the humidity or the 
temperature is abnormal, it should raise a warning by lighting a led.
temperature range:0-5degree,humidity range:20-60%
'''
import time
from counterfit_connection import CounterFitConnection
from counterfit_shims_grove.grove_light_sensor_v1_2 import GroveLightSensor
from counterfit_shims_grove.grove_led import GroveLed
# 在grove_light_sensor_v1_2包里增加了两个类
from counterfit_shims_grove.grove_light_sensor_v1_2 import GroveHumiditySensor
from counterfit_shims_grove.grove_light_sensor_v1_2 import GroveTemperatureSensor

# 连接counterfit
CounterFitConnection.init('127.0.0.1',1234)

# 定义led
led = GroveLed(2)

# 定义湿度和温度传感器
humidity_sensor = GroveHumiditySensor(3)
temperature_sensor = GroveTemperatureSensor(4)

while True:
    # 获取counterfit上的sensor的值
    humidity_value = humidity_sensor.humidity
    temperature_value = temperature_sensor.temperature
    print("humidity level is %.2f%% and temperature level is %.2f" % (humidity_value,temperature_value))

    # 如果湿度小于20%或大于60%，温度小于0或大于5度，即为异常情况
    if(((humidity_value < 20) or (humidity_value > 60)) or ((temperature_value < 0) or (temperature_value > 5))):
        print('The humidity or the temperature is abnormal!!Turning LED on')
        led.on()
    else:
        print('Turning LED off')
        led.off()

    time.sleep(3)