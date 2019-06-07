

from machine import I2C, Pin
import mpu6050
from umqtt.simple import MQTTClient
import time
import json
import urandom

time.sleep_ms(1000)

i2c = I2C(scl=Pin(5), sda=Pin(4))
mpu = mpu6050.accel(i2c)
c = MQTTClient(str(urandom.getrandbits(32)), "broker.mqttdashboard.com")
c.connect()


while True:
    values = mpu.get_values()
    c.publish(b"micropython/test/mpu6050",
            json.dumps(values))
    print(values)
    time.sleep_ms(20)
