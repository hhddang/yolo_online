<b>1. Structure</b>

<img width="1200" alt="abc" src="https://user-images.githubusercontent.com/96240899/173215430-32afcf5b-454b-480d-962d-d57278f2d7bd.png">


<b>2. How it works?</b>

After accessing to the website, users can upload 1 image and our models will detect objects appear. <br>
When no image is uploaded, the default one is blank.jpg - a white background photo. <br>
If an image is uploaded, <br>
First, the image will be saved as ./static/img/original.jpg. <br>
Then a function named model.functions.detect() will be called and detect objects in the image.  <br>
The detected image will be stored as ./static/img/detection.jpg. <br>
Finally, reset the website and show original.jpg and detection.jpg instead of blank.jpg. <br>


<b>3. Run website</b>

Run server: python server.py. <br>
On website, upload a photo then click arrow button. You can upload either your own photo or photo in images folder. <br>
Take a look at output. <br>
<!> Note: The images from 2 models are linked together due to some code is not finished yet :3 <br>

Love ya!
