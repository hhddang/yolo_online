1. Structure

yolo_online----images  Store images to test website

    |----------model------coco.names  List of objects'name that model is trained for dectecting
    |            |--------functions.py  Call YOLO and detect image
    |            |--------yolov3.cfg  Configuration of YOLO model
    |            |--------yolov3.weights  YOLO model
    |---------static------css  Store .css files
    |           |--------js  Store .js file
    |           |--------img------blank.jpg  Default image to show when starting server
    |                     |-------original.jpg  Save image uploaded by user
    |                     |-------detection.jpg  Save image after detecting objects
    |-------templates Store .html files
    |-------server.py  Run this file to start server
    |-------requirements.txt


2.How it works?

After accessing to the website, users can upload 1 image and our models will detect objects appear.
When no image is uploaded, the default one is blank.jpg - a white background photo.
If an image is uploaded,
First, the image will be saved as ./static/img/original.jpg.
Then a function named model.functions.detect() will be called and detect objects in the image. 
The detected image will be stored as ./static/img/detection.jpg.
Finally, reset the website and show original.jpg and detection.jpg instead of blank.jpg.


3.Run website

Run server: python server.py
On website, upload a photo then click arrow button. You can upload either your own photo or photo in images folder.
Take a look at output.
<!> Note: The images from 2 models are linked together due to some code is not finished yet :3

Love ya!
