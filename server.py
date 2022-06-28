from flask import Flask, render_template, request, redirect
from model.yolo_coco import functions as f1
from model.yolo_sea_creature import functions as f2

# Init server
app=Flask("app")

@app.route('/', methods=["GET"])
def home():
    return redirect('/yolo-coco')

@app.route('/yolo-coco', methods=["POST", "GET"])
def yolo_coco():
    if request.method=="POST":
        image = request.files['upload-image']
        image.save("./static/img/original.jpg")
        f1.detect("./static/img/original.jpg")
        return render_template('yolo_coco.html',image_input="../static/img/original.jpg",image_output="../static/img/detection.jpg")
    else:
        return render_template('yolo_coco.html',image_input="../static/img/blank.jpg", image_output="../static/img/blank.jpg")

@app.route('/yolo-sea-creature', methods=["POST", "GET"])
def yolo_sea_creature():
    if request.method=="POST":
        image = request.files['upload-image']
        image.save("./static/img/original.jpg")
        f2.detect("./static/img/original.jpg")
        return render_template('yolo_sea_creature.html',image_input="./static/img/original.jpg",image_output="./static/img/detection.jpg")
    else:
        return render_template('yolo_sea_creature.html',image_input="./static/img/blank.jpg", image_output="./static/img/blank.jpg")

# Run server
if __name__ == "__main__":
    app.run(debug=True)