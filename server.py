from flask import Flask, render_template, request, url_for, redirect
from model import functions

# Init server
app=Flask("app")

@app.route('/', methods=["POST", "GET"])
def main():
    if request.method=="POST":
        image = request.files['upload-image']
        image.save("./static/img/original.jpg")
        functions.detect("./static/img/original.jpg")
        return render_template('home.html',image_input="./static/img/original.jpg",image_output="./static/img/detection.jpg")
    else:
        return render_template('home.html',image_input="./static/img/blank.jpg", image_output="./static/img/blank.jpg")

# Run server
if __name__ == "__main__":
    app.run(debug=True)