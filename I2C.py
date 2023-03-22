from imu import MPU6050
from time import sleep
from machine import Pin, I2C
from hmc5883l import HMC5883L
from time import sleep


LED = machine.Pin(25, machine.Pin.OUT)
LED.value(1)

sleep(1)

LED(0)

i2c=machine.I2C(0,sda=machine.Pin(0), scl=machine.Pin(1))
print('Scanning I2C bus.')
devices = i2c.scan()
print(devices)

while True:
    #Sensor 1 full call code
    sensor = HMC5883L(scl=1, sda=0)
    x, y, z = sensor.read()
    print(sensor.format_result(x, y, z))
    sleep(0.2)

    #Sensor 2 full call code
    imu = MPU6050(i2c)
    ax=round(imu.accel.x,5)
    ay=round(imu.accel.y,5)
    az=round(imu.accel.z,5)
    gx=round(imu.gyro.x,5)
    gy=round(imu.gyro.y,5)
    gz=round(imu.gyro.z,5)
    tem=round(imu.temperature,2)
    print("ax",ax,"ay",ay,"az",az,"gx",gx,"gy",gy,"gz",gz,"Temperature",tem)


