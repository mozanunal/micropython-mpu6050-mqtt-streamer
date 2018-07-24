# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import gc
import webrepl
import network

webrepl.start()
gc.collect()
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('xx', 'xx')
