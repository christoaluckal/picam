# importing Flask and other modules
from flask import Flask, request, render_template,Response,send_file,url_for,redirect
# import cam
import picamera
import picamera.array
import cv2
# Flask constructor
app = Flask(__name__, template_folder='.')
camera = picamera.PiCamera()

def takeimage(shut,reso,iso_val):
    camera = picamera.PiCamera(resolution=reso)
    camera.shutter_speed = shut
    camera.iso = iso_val
    camera.capture('image.jpg')
    # camera.start_preview()
    # sleep(10)
    # camera.stop_preview()
    camera.close()
    return

# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def index():
   global camera
   camera.close()
   if request.method == "GET":
      return render_template("landing.html")
   elif request.method == "POST":
      mode = request.form['submit_button']
      if mode == "preview":
         camera = picamera.PiCamera(resolution=(640,480),framerate=24)
         return render_template("video.html")
      if mode == "image":
         return redirect(url_for('image'))
         
      # return render_template("index.html")

@app.route('/image',methods=["GET","POST"])
def image():
   global camera
   camera.close()
   if request.method == "GET":
      return render_template("image.html")
   elif request.method == "POST":
      shut = int(request.form.get("shutter"))
      reso = request.form.get("resolution")
      iso = int(request.form.get("iso"))
      mode = request.form.get("type")
      if reso=="640480":
         resolution = (640,480)
      elif reso=="1280720":
         resolution = (1280,720)
      else:
         resolution = (1920,1080)
      takeimage(shut,resolution,iso)
      return send_file('image.jpg', as_attachment=True)

def gen():
   global camera
   camera.resolution = (640,480)
   # camera.framerate = 60 
   with picamera.array.PiRGBArray(camera,size=(640,480)) as output:
      while True:
         camera.capture(output, 'bgr',use_video_port=True)
         frame = output.array
         #cv2.flip(frame,0)
         ret, jpeg = cv2.imencode('.jpg', frame)
         cv2.cvtColor(jpeg,cv2.COLOR_BGR2RGB)
         jpeg = cv2.flip(jpeg,1)
         output.truncate(0)
         yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')
            

@app.route('/video_feed')
def video_feed():
     return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
  
if __name__=='__main__':
   app.run(host='0.0.0.0')