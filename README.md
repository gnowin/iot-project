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
The Raspberry Pi Pico WH is the microcontroller used in the project. It has a micro-USB port that is used to give it power and to program it by uploading code. There are ground, power and GPIO pins so that electrical components can be connected and controlled by the microcontroller. This microcontroller can also connect to WIFI which makes it able to send and recieve messages wirelessly.
![pico](https://hackmd.io/_uploads/HJZ9uBdL0.jpg)


###    DHT11
A sensor that measures both humidity and temperature.
![dht11](https://hackmd.io/_uploads/SkgTuS_8C.jpg)


###    Piezo
A piezo can detect vibrations and make noises.
![piezo](https://hackmd.io/_uploads/rJIauS_UR.jpg)


###    RGB LED
An LED that can display a multitude of colors. It has one pin for power, and three pins that correspond to the intensity of the red, green and blue color channels to light up in different colors.
![LED](https://hackmd.io/_uploads/SyX1tH_UR.jpg)


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
![Wiring](https://hackmd.io/_uploads/r1gLpBuLA.png)

This is a simplified view of the wiring, showing what types of resistors are used and which pins the different components are connected to. This image is created in WokWi, and as there were no DHT11 component, a DHT22 sensor is shown instead. However, the amount of pins are the same for both sensors so the wiring is correct otherwise.


##    Platform

##    The code

##    Transmitting the data / connectivity

##    Presenting the data

##    Finalizing the design