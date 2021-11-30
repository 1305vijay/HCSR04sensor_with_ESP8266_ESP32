from machine import Pin
import hcsr04
from time import sleep
sensor=hcsr04.HCSR04(trigger_pin=0, echo_pin=4, echo_timeout_us=1000)
while True:
  distance=sensor.distnace_cm()
  print('distance is :', distance)
  sleep(1000)
