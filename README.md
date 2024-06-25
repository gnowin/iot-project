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
| LED RGB              | [Electrokit](https://www.electrokit.com/led-rgb-5mm-adresserbar-ws2812d-f5) | 5 SEK   |

In addition, you need a breadboard, resistors, jumper wires and a USB-A to micro USB cable. These can all be bought at Electrokit. An example of what resistors and wires needed and how they can be connected will be provided later on.

###    Raspberry Pi Pico WH

###    DHT11

###    Piezo

###    LED RGB

##    Computer setup

##    Puttin everything together

##    Platform

##    The code

##    Transmitting the data / connectivity

##    Presenting the data

##    Finalizing the design