from machine import Pin, PWM
import utime
import time
print("Starting")
motor = PWM(Pin(7))
motor.freq(50)
motor.duty_u16(65000)
utime.sleep_ms(2000)
x = input("Press anything")
motor.duty_u16(2600)
time.sleep(5)
print("Callibrated!!")
while True:
    for duty in range(260,550):
		motor.duty_u16(duty*10)
		print(duty*10)
		utime.sleep_ms(50)
