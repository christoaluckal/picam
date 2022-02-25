import re
from picamera import PiCamera,array
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

def cam_stream(frame,reso):
    camera = PiCamera(resolution=reso,framerate=frame)
    stream = array.PiRGBArray(camera)
    while True:
        camera.capture(stream, 'rgb')
        frame = stream.array
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')