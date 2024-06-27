#     Temperature and Humidity Sensor
Albin Johansson / aa227sz

In this project I have created an IoT system that gathers, stores and displays temperature and humidity data. The system consists of a microcontroller with the sensor, MQTT-broker and a TIG-stack. The microcontroller is used to collect data and send data to the MQTT-broker. It also has an RGB LED to display current temperature, and a Piezo to alert of temperature changes. The data sent to the MQTT-broker is then collected, stored and then finally visualized on a dashboard, which is all done through a TIG-stack.

This project should take approximately 2-8 hours to finish depending on your familiarity with microcontrollers and Docker. 
##     Objective
I chose this project as I thought it would be interesting to be able to gather data on the temperatures and humidity levels throughout the day in my apartment. This meant I could see for example how much of a difference an open window has on the temperature, or what the conditions are like while I sleep.

For this project I also decided to host the server side myself. This is because I already had plans to make a home server and wanted to make use of it right away. Through this I could also use Docker for the first time and gain some new knowledge.

##    Material
Below is a table of the main components used in the project.

| Component            | Link                                                                        | Price   |
| -------------------- | --------------------------------------------------------------------------- | ------- |
| Raspberry Pi Pico WH | [Electrokit](https://www.electrokit.com/raspberry-pi-pico-wh)               | 109 SEK |
| DHT11                | [Electrokit](https://www.electrokit.com/temp/fuktsensor-dht11)              | 39 SEK  |
| Piezo                | [Electrokit](https://www.electrokit.com/piezoelement-12x5.5mm)              | 15 SEK  |
| RGB LED              | [Electrokit](https://www.electrokit.com/led-rgb-5mm-adresserbar-ws2812d-f5) | 5 SEK   |

In addition, you need a breadboard, resistors, jumper wires and a USB-A to micro USB cable. These can all be bought at Electrokit. An example of what resistors and wires needed and how they can be connected will be provided later on.

###    Raspberry Pi Pico WH
The Raspberry Pi Pico WH is the microcontroller used in the project. It has a micro-USB port that is used to give it power and to program it by uploading code. There are ground, power and GPIO pins so that electrical components can be connected and controlled by the microcontroller. This microcontroller can also connect to WiFi which makes it able to send and recieve messages wirelessly.

<img src="https://github.com/gnowin/iot-project/assets/100692493/f471fdd4-94a1-4c5e-bd69-ecc444c994b7" alt="pico" style="width:50%;"/>


###    DHT11
A sensor that measures both humidity and temperature.

<img src="https://github.com/gnowin/iot-project/assets/100692493/8af396f4-aee0-4e85-ad96-587265f504fc" alt="dht11" style="width:50%;"/>


###    Piezo
A piezo can detect vibrations and make noises.

<img src="https://github.com/gnowin/iot-project/assets/100692493/4f787bc6-96eb-4d2e-aee0-624b47ec20e8" alt="piezo" style="width:50%;"/>


###    RGB LED
An LED that can display a multitude of colors. It has one pin for power, and three pins that correspond to the intensity of the red, green and blue color channels to light up in different colors.

<img src="https://github.com/gnowin/iot-project/assets/100692493/275643b6-6dea-4d1e-8785-101b64a72f7f" alt="rgbled" style="width:50%;"/>


##    Computer setup
Here I will explain my computer setup for this project. The tools I used are:
* Visual Studio Code
* Node.js
* Pymakr extension
* Micropython firmware (for microcontroller)

### Visual Studio Code
The IDE I used for this project is Visual Studio Code, which can be downloaded [here](https://code.visualstudio.com/).

### Pymakr
To interact with the microcontroller I used Pymakr. It is a Visual Studio Code extension you can download by searching on it in the extensions tab in the application. A guide to getting started can be read [here](https://github.com/sg-wireless/pymakr-vsc/blob/HEAD/GET_STARTED.md).

### Node.js
To make Pymakr work, you need to install Node.js. You can download it from their [website](https://nodejs.org/en).

### Micropython firmware
To use Raspberry Pi Pico WH and upload micropython files from your computer, you need to update its firmware. The micropython firmware can be downloaded from [this](https://micropython.org/download/RPI_PICO_W/) website. Follow the installation instructions.

##    Putting everything together

<img src="https://github.com/gnowin/iot-project/assets/100692493/c6f84446-b17f-45d3-b00c-db5fa1ac49fd" alt="wiring_diagram" style="width:50%;"/>

This is a simplified view of the wiring, showing what types of resistors are used and which pins the different components are connected to. This image is created in WokWi, and as there were no DHT11 component, a DHT22 sensor is shown instead. However, the amount of pins are the same for both sensors so the wiring is correct otherwise.


##    Platform
I had an old laptop laying around that I wanted to turn into a server, so early on I made the choice to self-host the server side of the project. I also wanted to try out Docker for the first time.

On my laptop I installed Ubuntu Server, but as I set this up with docker it sohuld work on most operating systems. Before deploying it on my Ubuntu Server I worked on it on my Windows 10 computer.

The server's stack consists of the following:
* Eclipse Mosquitto: MQTT Broker
* Telegraf: Gathers data from MQTT Broker and sends it to database
* InfluxDB: Time-series database
* Grafana: Connects to the InfluxDB database. Grafana provides a multitude of visualization options to display data, e.g. different graphs.

##    The code
In the boot file, there is code that attempts to connect to a WiFi network through the [network](https://docs.micropython.org/en/latest/library/network.html) library, and then tests the connection by using the [socket](https://docs.micropython.org/en/latest/library/socket.html) library. The WiFi network credentials are stored in a secrets file. These libraries are built-in modules within micropython. I will not go through the details of these functions, but they are called through two different error exception handlings.

```python
# WiFi Connection
try:
    ip = connect()
except KeyboardInterrupt:
    print("Keyboard interrupt")

# HTTP request
try:
    http_get()
except (Exception, KeyboardInterrupt) as err:
    print("No Internet", err)
```

The majority of the code is in the main file. It consists of some initilizations and a loop for the microcontrollers logic. To connect and send data to the MQTT Broker, [umqtt_simple](https://github.com/micropython/micropython-lib/blob/master/micropython/umqtt.simple/umqtt/simple.py) library is used. A MQTT client object is created

```python
client = MQTTClient(ClientID, secrets.MQTT_SERVER, 1883)
```

and then later attempts to connect to the broker. If it doesn't succeed in connecting, it tries to reconnect until it does.

```python
#Try to connect, reconnect
try:
    connect(client)
except OSError as e:
    reconnect(client)
```

Also before the main loop, objects that define what pin and how to interact with the different components on the board are initiated.

```python
# On-board LED
led = Pin("LED", Pin.OUT)

# DHT11 sensor
sensor = dht.DHT11(Pin(16))

# Piezo
buzzer = PWM(Pin(17))

# RGB LED (only red and blue)
ledR = PWM(Pin(11), freq=300_00, duty_u16=0)
ledB = PWM(Pin(14), freq=300_00, duty_u16=0)
```

If the MQTT connection is successful, the main loop is initiated and will never leave the loop unless the microcontroller is restarted. The main loop does the following:
1. Reads temperature and humidity from sensor.
2. Compares last temperature with current, and makes piezo do a sound if changed. Lower frequency for a lowered value, higher frequency for higher value.
3. Updates RGB LED color. It is more blue on lower temperatures and more red on higher.
4. Sends data in a json format and blinks the onboard LED.
5. Sleeps/waits for 60 seconds to continue with the next loop.

##    Transmitting the data / connectivity
As explained in the previous section, a wireless connection is established on the microcontroller with a WiFi protocol with the built-in [network](https://docs.micropython.org/en/latest/library/network.html) library.

```python
def connect():
    wlan = network.WLAN(network.STA_IF)         # Put modem on Station mode
    if not wlan.isconnected():                  # Check if already connected
        print('connecting to network...')
        wlan.active(True)                       # Activate network interface

        # set power mode to get WiFi power-saving off (if needed)
        wlan.config(pm = 0xa11140)
        wlan.connect(secrets.WIFI_SSID, secrets.WIFI_PASS)  # Your WiFi Credential
        print('Waiting for connection...', end='')
        
        # Check if it is connected otherwise wait
        while not wlan.isconnected() and wlan.status() >= 0:
            print('.', end='')
            sleep(1)
            
    # Print the IP assigned by router
    ip = wlan.ifconfig()[0]
    print('\nConnected on {}'.format(ip))
    return ip
```

Through the [json](https://docs.micropython.org/en/latest/library/json.html) library, a dictionary of the data is converted to json and then sent with the publish function with help from the [umqtt_simple](https://github.com/micropython/micropython-lib/blob/master/micropython/umqtt.simple/umqtt/simple.py) client object. The library uses the MQTT transport protocol. The data is sent every minute.

```python
# Prepare message data
msg = {
    "temperature": temp,
    "humidity": hum
}

# Send data
send_data(client, led, msg)
```

```python
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
```

##    Presenting the data
Using Grafana I have built a dashboard to visualize my data.

<img src="https://github.com/gnowin/iot-project/assets/100692493/c6a61c10-213c-4201-b367-4bcdf54784b3" alt="grafanapc" style="width:100%;"/>

<img src="https://github.com/gnowin/iot-project/assets/100692493/7e5d7b7c-5ef8-43d7-af50-cde740674a59" alt="grafanamobile" style="width:50%;"/>

<img src="https://github.com/gnowin/iot-project/assets/100692493/4f1c7405-3e84-447b-b7ab-244811bb9f92" alt="grafanamobile2" style="width:50%;"/>




##    Finalizing the design
<img src="https://github.com/gnowin/iot-project/assets/100692493/7fb8958b-f80d-49b3-96c1-c5bd53c4067d" alt="finalresult" style="width:100%;"/>

