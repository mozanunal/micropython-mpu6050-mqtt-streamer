

from machine import I2C, Pin
import mpu6050
from umqtt.simple import MQTTClient
import time, json

i2c = I2C(scl=Pin(5), sda=Pin(4))
accelerometer = mpu6050.accel(i2c)
c = MQTTClient("asdsdsadsadadsdsa", "iot.eclipse.org")
c.connect()

def run():
	while True:
	    c.publish( b"micropython/test/mpu6050", json.dumps(accelerometer.get_values()) )
	    time.sleep_ms(45)
