# picam

## Requirements
1.  Python OpenCV
2.  Flask
3.  PiCamera

## Steps

1. To run the more customizable streams cd into the `separate` directory: `cd separate/`
2. To click images run the `image.py` server. You'll be prompted to enter the port number. You can simply press Enter and it will choose the default port (5000) or you can input the port you want to use. **Just ensure that the port is valid**.
3. To see a preview run the `preview.py` server. You'll be prompted to first enter 1:640x480, 2:1280x720 or 3:1920x1080. Then you can input the ISO value. Stick to the known [values](https://picamera.readthedocs.io/en/release-1.10/api_camera.html#picamera.camera.PiCamera.iso) (100,200,320,400,500,640,800). Finally, input the port number. Same as above.

### TODO
1. The preview code relies on a response generated by a sibling thread. Before the sibling thread begins, the camera parameters must be set (CLI inputs). This is tedious. Hence, a way to actually change values on the fly (Request-Response, JSONs, etc.) may need to be developed.

