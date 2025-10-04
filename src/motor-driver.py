
import time
from machine import Pin, I2C
from picobricks import MotorDriver

i2c = I2C(0, scl=Pin(5), sda=Pin(4))
motor = MotorDriver(i2c)

motor.servo(1,180)


# motor.dc(which, speed, direction)
motor.dc(1,150,0)
time.sleep(10)
motor.dc(1,0,0)
