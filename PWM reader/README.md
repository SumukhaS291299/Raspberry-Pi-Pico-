# PWM Reader Micro-Python


## Usage

# IMPORTANT USE this ONLY IF YOU KNOW THE FREAQUENCY OF THE PWM SIGNAL

```
readDuty(GPIO_PIN,pulse_level=1)
```

### GPIO_PIN from where you want to read the values.
### pulse_level The timeperiod of signal HIGH(1) or LOW(0), default value (1) will read timeperiod of signal HIGH
### Returns Pulse Width measuring high/low in PWM signal in microsecond


```
readDutyAsPercentage(GPIO_PIN,freaquency,pulse_level=1)
```

### GPIO_PIN from where you want to read the values.
### freaquency of the PWM signal
### pulse_level The timeperiod of signal HIGH(1) or LOW(0), default value (1) will read timeperiod of signal HIGH
### Returns Pulse Width measuring high/low in PWM signal in microsecond


# Example

```
import machine
from machine import Pin,time_pulse_us

# IMPORTANT USE this ONLY IF YOU KNOW THE FREAQUENCY OF THE PWM SIGNAL

def readDuty(GPIO_PIN,pulse_level=1):
    ReadPWMPin = Pin(GPIO_PIN,Pin.IN)
    return time_pulse_us(ReadPWMPin,pulse_level)

def readDutyAsPercentage(GPIO_PIN,freaquency,pulse_level=1):
    ReadPWMPin = Pin(GPIO_PIN,Pin.IN)
    Time_period = 1/freaquency
    Curr_PWM = time_pulse_us(ReadPWMPin,pulse_level)
    Curr_PWM = Curr_PWM / 1000000
    Percentage = (Curr_PWM/Time_period) * 100
    return Percentage

pwm = machine.Pin(0)
pwmout = machine.PWM(pwm)

pwmout.freq(50)

for D in range(8192,32768,50):
    pwmout.duty_u16(D)
    pwm = machine.Pin(1)
    P = readDutyAsPercentage(1,50)
    print("Percent:",P)


```
