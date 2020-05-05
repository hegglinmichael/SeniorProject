from nanpy import Stepper

motor = Stepper(100,4,5,100)
motor2 = Stepper(100,6,7,100)
while True:
	motor.step(60)
	motor2.step(60)
