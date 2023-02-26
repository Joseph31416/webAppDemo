from flask import Flask, request, render_template, flash, redirect, url_for
import os
from PIL import Image
import numpy as np
import requests
from env import HOST


app = Flask(__name__)
UPLOAD_FOLDER = "./static/images"
ALLOWED_EXTENSIONS = {"jpeg", "jpg", "png"}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
URL = f'http://{HOST}/predict'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def pad_image(img):
    new_arr = []
    for row in img:
        diff = 28 - len(row)
        left = diff // 2
        right = diff - left
        new_arr.append(np.pad(row, (left, right), constant_values=(255, 255)))
    while len(new_arr) < 28:
        new_arr.append(np.ones(28) * 255.0)
        new_arr = [np.ones(28) * 255.0] + new_arr
    if len(new_arr) > 28:
        new_arr.pop(-1)
    return np.array(new_arr)


def invert(img):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i][j] = 255 - img[i][j]
    return img


def preprocess(img):
    scale_ratio = min(28 / img.size[0], 28 / img.size[1])
    new_width = int(img.size[0] * scale_ratio)
    new_height = int(img.size[1] * scale_ratio)
    img = img.resize((new_width, new_height))
    img_np = np.array(img)
    img_np = pad_image(img_np)
    img_np = invert(img_np)
    img_np = img_np / 255.0
    img_np = img_np[:, :, np.newaxis]
    return img_np.tolist()


def get_result(src):
    img = Image.open(src).convert("L")
    img = preprocess(img)
    json = {"test": img}
    response = requests.post(URL, json=json).json() # modify URL
    response["pred_probability"] = int(response["pred_probability"] * 100)
    return response


@app.route("/", methods=["GET", "POST"])
def root():
    if request.method == "GET":
        return render_template("home.html")
    else:
        key = "test_image"
        if key not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files[key]
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = "test_image.jpeg"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for("result"))
        return render_template("home.html")


@app.route("/result", methods=["GET", "POST"])
def result():
    src = os.path.join(app.config['UPLOAD_FOLDER'], "test_image.jpeg")
    result = get_result(src)
    return render_template("result.html", src=src, result=result)


if __name__ == "__main__":
    app.run()
