# importing Flask and other modules
from flask import Flask, request, render_template,Response
import cam
import picamera
import picamera.array
import cv2
# Flask constructor
app = Flask(__name__, template_folder='.')
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def index():
   return render_template("index.html")


def gen():
   with picamera.PiCamera() as camera:
      camera.resolution = (640,480)
      camera.framerate = 24
      with picamera.array.PiRGBArray(camera,size=(640,480)) as output:
         while True:
            camera.capture(output, 'rgb')
            frame = output.array
            ret, jpeg = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\n'
                  b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
     return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
  
if __name__=='__main__':
   app.run()