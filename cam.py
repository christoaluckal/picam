import re
from picamera import PiCamera
from time import sleep

def image(shut,reso,iso_val):
    camera = PiCamera(resolution=reso)
    camera.shutter_speed = shut
    camera.iso = iso_val
    camera.capture('image.jpg')
    # camera.start_preview()
    # sleep(10)
    # camera.stop_preview()
    camera.close()
    return

def preview(frame,shut,reso,iso_val):
    camera = PiCamera(resolution=reso,framerate=frame)
    camera.shutter_speed = shut
    camera.iso = iso_val
    camera.start_preview()
    sleep(10)
    camera.stop_preview()
    camera.close()
    return