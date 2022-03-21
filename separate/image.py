# importing Flask and other modules
from flask import Flask, request, render_template,Response,send_file,url_for,redirect
# import cam
import picamera
import picamera.array
import cv2
# Flask constructor
app = Flask(__name__, template_folder='.')
# camera = picamera.PiCamera()
def takeimage(shut,reso,iso_val):
   camera2 = picamera.PiCamera(resolution=reso)
   camera2.shutter_speed = shut
   camera2.iso = iso_val
   output = picamera.array.PiRGBArray(camera2)
   camera2.capture(output, 'bgr')
   frame = output.array
   #cv2.flip(frame,0)

   # APPLY FILTERS HERE
   # frame = cv2.GaussianBlur(frame,(5,5),cv2.BORDER_DEFAULT) 

   # ret, jpeg = cv2.imencode('.jpg', frame)
   cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
   cv2.imwrite('image.jpg',frame)
   camera2.close()

# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def index():
   if request.method == "GET":
      return render_template("image.html")
   elif request.method == "POST":
      reso = request.form.get("resolution")

      if reso=="640480":
            res = (640,480)
      elif reso=="1280720":
         res = (1280,720)
      else:
         res = (1920,1080)

      shut = int(request.form.get("shutter"))
      iso = int(request.form.get("iso"))
      takeimage(shut,res,iso)
      return send_file('image.jpg', as_attachment=True)
         

# def gen():
#    global camera
#    with picamera.array.PiRGBArray(camera) as output:
#       while True:
#          camera.capture(output, 'bgr',use_video_port=True)
#          frame = output.array
#          ret, jpeg = cv2.imencode('.jpg', frame)
#          cv2.cvtColor(jpeg,cv2.COLOR_BGR2RGB)
#          output.truncate(0)
#          yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')
            

# @app.route('/video_feed',methods=["GET","POST"])
# def video_feed():
#    # camera = picamera.Camera()
#    # camera.close()
#    return Response(gen(),
#                   mimetype='multipart/x-mixed-replace; boundary=frame')
  
if __name__=='__main__':
   default_port = 5000
   new_port = input('Port Number:')
   if new_port=='':
      new_port=default_port
   else:
      default_port = int(new_port)

   app.run(host='0.0.0.0',port=default_port)