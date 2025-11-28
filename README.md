
# MQTT Lab – Python + Paho

**Student ID:** 12011251

## Project Description
This lab demonstrates the use of MQTT protocol with Python using Paho library.  
It includes:
- Mosquitto MQTT Broker
- 3 Publishers:
  - Temperature
  - Humidity
  - People Counter
- 3 Subscribers, each listens to a specific topic
- All messages include Student ID
- Screenshots of results included

## How to Run
1. Start Mosquitto Broker:
   ```bash
   mosquitto
2.Run Publishers (each in a separate terminal) : 
python publishers/temp_pub.py
python publishers/humidity_pub.py
python publishers/people_pub.py
3.Run Subscribers (each in a separate terminal) : 
python subscribers/temp_sub.py
python subscribers/humidity_sub.py
python subscribers/people_sub.py
Screenshots : 
/Screenshots folder 
