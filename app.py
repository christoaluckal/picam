# importing Flask and other modules
from flask import Flask, request, render_template 
import cam
# Flask constructor
app = Flask(__name__, template_folder='.')
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def index():
   if request.method == "POST":
      frame = int(request.form.get("framerate"))
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
      if mode == "preview":
         cam.preview(frame,shut,resolution,iso)
      else:
         cam.image(shut,resolution,iso)
   return render_template("index.html")
  
if __name__=='__main__':
   app.run()