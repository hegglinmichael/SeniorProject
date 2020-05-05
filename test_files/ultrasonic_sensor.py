from nanpy import ArduinoApi
from nanpy import SerialManager
from nanpy import Ultrasonic
from time import sleep

# setup
trigPin = 0
echoPin = 10

connection = SerialManager()
a = ArduinoApi(connection=connection)

ultrasonic = Ultrasonic(echoPin, trigPin, False, connection=connection)

def loop():
    distance = ultrasonic.get_distance()
    print("distance is: ")
    print(distance)
    sleep(0.02)

while loop:
    loop()
