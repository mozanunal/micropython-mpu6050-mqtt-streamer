# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
# esp.osdebug(None)
import gc
import network

gc.collect()
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('XX', 'XX')
print(wlan.ifconfig())
