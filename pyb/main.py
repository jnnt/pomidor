import time
from pyb import (
    USB_VCP,
    Servo
)

SLEEP = 0.1

UP = -90
DOWN = 0
SPEED = 1000

servo = Servo(1)
servo.angle(30)

p = USB_VCP()

while True:
    if p.any():
        command = p.readline().strip()
        if command == b'up':
            servo.angle(UP, SPEED)
            p.write(b'up-ok\n')
        elif command == b'down':
            servo.angle(DOWN, SPEED)
            p.write(b'down-ok\n')
        else:
            p.write(command + b'\n')
            p.write(b'err\n')

    time.sleep(SLEEP)
