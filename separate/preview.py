# importing Flask and other modules
from flask import Flask, request, render_template,Response,send_file,url_for,redirect
# import cam
import picamera
import picamera.array
import cv2
from time import sleep

reso = input("1:640x480\n2:1280x720\n3:1920x1080\n")
if reso==1:
    res = (640,480)
elif reso==2:
    res = (1280,720)
else:
    res = (1920,1080)

frame = 24
iso_val = int(input("ISO:\n"))
camera = picamera.PiCamera(resolution=res,framerate=frame)
camera.iso = iso_val
# sleep(2)

# Flask constructor
app = Flask(__name__, template_folder='.')

@app.route('/', methods =["GET", "POST"])
def video():
    return render_template('video.html')
    
def gen(camera):
   with picamera.array.PiRGBArray(camera) as output:
      while True:
         camera.capture(output, 'bgr',use_video_port=True)
         frame = output.array
         ret, jpeg = cv2.imencode('.jpg', frame)
         cv2.cvtColor(jpeg,cv2.COLOR_BGR2RGB)
         output.truncate(0)
         yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')
            
@app.route('/video_feed',methods=["GET","POST"])
def video_feed():
   # camera = picamera.Camera()
   # camera.close()
   global camera
   return Response(gen(camera),
                  mimetype='multipart/x-mixed-replace; boundary=frame')
  
if __name__=='__main__':
    default_port = 5000
    try:  
        new_port = input('Port Number:')
    except SyntaxError:
        new_port = None

    if new_port is None:
        default_port=5000
    else:
        default_port = int(new_port)

    app.run(host='0.0.0.0',port=default_port)