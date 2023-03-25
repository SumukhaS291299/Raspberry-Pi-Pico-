from machine import Pin,time_pulse_us

# IMPORTANT USE this ONLY IF YOU KNOW THE FREAQUENCY OF THE PWM SIGNAL

def readDuty(GPIO_PIN,pulse_level=1):
    ReadPWMPin = Pin(GPIO_PIN,Pin.IN)
    return time_pulse_us(ReadPWMPin,pulse_level)

def readDutyAsPercentage(GPIO_PIN,freaquency,pulse_level=1):
    ReadPWMPin = Pin(GPIO_PIN,Pin.IN)
    Time_period = 1/freaquency
    Curr_PWM = time_pulse_us(ReadPWMPin,pulse_level)
    Curr_PWM = Curr_PWM / 1000000    #Change microseconds to seconds
    Percentage = (Curr_PWM/Time_period) * 100
    return Percentage