import paho.mqtt.client as mqtt
import time
import random

student_id = "YourStudentID"

client = mqtt.Client()
client.connect("localhost", 1883, 60)

while True:
    temp = random.randint(20, 35)
    message = f"Temperature: {temp} C | ID: {12011251}"
    client.publish("temp/topic", message)
    print("Published:", message)
    time.sleep(3)
