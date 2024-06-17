import time
from machine import Pin, PWM
import dht
from umqtt.simple import MQTTClient
import random
import json

import secrets

# Set the OUTPUT pin to on-board LED
led = Pin("LED", Pin.OUT)

ledR = Pin(2, Pin.OUT)
ledG = Pin(11, Pin.OUT)
ledB = Pin(15, Pin.OUT)

tempSensor = dht.DHT11(Pin(16))
buzzer = PWM(Pin(17))

# MQTT Client 
ClientID = f'raspberry-sub-{time.time_ns()}'
topic = "pico/mqtt"
#msg = b'{"msg":"hello"}'

def main():
    client = MQTTClient(ClientID, secrets.MQTT_SERVER, 1883)

    # Try to connect, reconnect
    # try:
    #     connect(client)
    # except OSError as e:
    #     reconnect(client)

    # Main loop
    while True:
        time.sleep(1)
        getTemperature()
        beep()
        colortest()
        #send_data(client)

def connect(c):
    c.connect()
    print('Connected to MQTT Broker "%s"' % (secrets.MQTT_SERVER))

def reconnect(c):
    print('Failed to connect to MQTT broker, Reconnecting...')
    time.sleep(5)
    c.reconnect()

def send_data(c):

    msg = {
                "test1": random.randrange(0, 25)
           }

    print('send message %s on topic %s' % (msg, topic))
    try: 
        c.publish(topic, json.dumps(msg), qos=0)
    except OSError as e:
        print(e)
    led.on()
    time.sleep(0.2)
    led.off()
    time.sleep(0.8)


def getTemperature():
    try:
        tempSensor.measure()
        temperature = tempSensor.temperature()
        humidity = tempSensor.humidity()
        print("Temperature is {} degrees Celsius and Humidity is {}%".format(temperature, humidity))
    except Exception as error:
        print("Exception occurred", error)
    time.sleep(2)

def beep():
    buzzer.duty_u16(1000)
    buzzer.freq(500)
    time.sleep(0.3)
    buzzer.duty_u16(0)

def colortest():
    ledR.value(1.0)
    ledG.value(0.0)
    ledB.value(0.0)
    time.sleep(0.5)
    ledR.value(0.0)
    ledG.value(1.0)
    ledB.value(0.0)
    time.sleep(0.5)
    ledR.value(0.0)
    ledG.value(0.0)
    ledB.value(1.0)
    time.sleep(0.5)

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