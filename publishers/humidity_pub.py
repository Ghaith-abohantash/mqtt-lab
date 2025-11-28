import paho.mqtt.client as mqtt
import time
import random

student_id = "YourStudentID"

client = mqtt.Client()
client.connect("localhost", 1883, 60)

while True:
    hum = random.randint(40, 90)
    message = f"Humidity: {hum}% | ID: {12011251}"
    client.publish("humidity/topic", message)
    print("Published:", message)
    time.sleep(3)
