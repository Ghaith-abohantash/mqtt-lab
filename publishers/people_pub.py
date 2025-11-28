import paho.mqtt.client as mqtt
import time
import random

student_id = "YourStudentID"

client = mqtt.Client()
client.connect("localhost", 1883, 60)

while True:
    people = random.randint(0, 15)
    message = f"People Count: {people} | ID: {12011251}"
    client.publish("people/topic", message)
    print("Published:", message)
    time.sleep(3)
