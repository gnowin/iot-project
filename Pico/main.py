import time
from machine import Pin, PWM
import dht
from umqtt.simple import MQTTClient
import random
import math
import json

import secrets

temperatures = [17, 27]

# MQTT Client 
ClientID = f'raspberry-sub-{time.time_ns()}'
topic = "pico/mqtt"

def main():
    client = MQTTClient(ClientID, secrets.MQTT_SERVER, 1883)

    # On-board LED
    led = Pin("LED", Pin.OUT)

    # DHT11 sensor
    sensor = dht.DHT11(Pin(16))

    # Piezo
    buzzer = PWM(Pin(17))

    # RGB LED
    ledR = PWM(Pin(11), freq=300_00, duty_u16=0)
    #ledG = PWM(Pin(15), freq=300_00, duty_u16=0)
    ledB = PWM(Pin(14), freq=300_00, duty_u16=0)

    #Try to connect, reconnect
    # try:
    #     connect(client)
    # except OSError as e:
    #     reconnect(client)

    currentTemp = 0


    # Main loop
    while True:
        temp, hum = readSensor(sensor)

        if currentTemp > temp:
            beep(buzzer)
        elif currentTemp < temp:
            beep(buzzer)

        currentTemp = temp


        # temp += 1
        updateLed(temp, R=ledR, B=ledB)
        time.sleep(3)
        #send_data(client)


def connect(c):
    c.connect()
    print('Connected to MQTT Broker "%s"' % (secrets.MQTT_SERVER))

def reconnect(c):
    print('Failed to connect to MQTT broker, Reconnecting...')
    time.sleep(5)
    c.reconnect()

def send_data(c, led, msg):
    print('send message %s on topic %s' % (msg, topic))
    try: 
        c.publish(topic, json.dumps(msg), qos=0)
    except OSError as e:
        print(e)
    led.on()
    time.sleep(0.2)
    led.off()
    time.sleep(0.8)


def readSensor(s):
    try:
        s.measure()
        temperature = s.temperature()
        humidity = s.humidity()
        print("Temperature is {} degrees Celsius and Humidity is {}%".format(temperature, humidity))

        return temperature, humidity
    except Exception as error:
        print("Exception occurred", error)
    time.sleep(2)

def updateLed(temp, R, B):
        if(temp <= temperatures[0]):
            colorVal = 1
        elif(temp >= temperatures[1]):
            colorVal = 0
        else:
            colorVal = (temperatures[1] - temp) / (temperatures[1] - temperatures[0])

        R.duty_u16(int(2**16*(1 - colorVal)))
        B.duty_u16(int(2**16*colorVal))

def beep(buzzer):
    buzzer.duty_u16(1000)
    buzzer.freq(500)
    time.sleep(0.1)
    buzzer.duty_u16(0)

try:
    main()
except OSError as e:
    print(f"Error:{e}")

# # Runs forever
# while True:
#     led.on()              # Turn on LED
#     time.sleep(0.2)       # Delay for 0.2 seconds
#     led.off()             # Turn off LED
#     time.sleep(1.0)       # Delay for 1.0 seconds