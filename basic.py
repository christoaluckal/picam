from picamera import PiCamera
from time import sleep

camera = PiCamera()
for i in range(100,801,100):
    camera.iso = i
    camera.start_preview()
    sleep(1)
    camera.stop_preview()