<b>1. Structure</b>

<img width="1200" alt="abc" src="https://user-images.githubusercontent.com/96240899/173215430-32afcf5b-454b-480d-962d-d57278f2d7bd.png">


<b>2. How it works?</b>

After accessing to the website, users can upload 1 image and our models will detect objects appear.
When no image is uploaded, the default one is blank.jpg - a white background photo.
If an image is uploaded,
First, the image will be saved as ./static/img/original.jpg.
Then a function named model.functions.detect() will be called and detect objects in the image. 
The detected image will be stored as ./static/img/detection.jpg.
Finally, reset the website and show original.jpg and detection.jpg instead of blank.jpg.


<b>3. Run website</b>

Run server: python server.py
On website, upload a photo then click arrow button. You can upload either your own photo or photo in images folder.
Take a look at output.
<!> Note: The images from 2 models are linked together due to some code is not finished yet :3

Love ya!
