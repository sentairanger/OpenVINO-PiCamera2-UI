from flask import Flask, render_template, request
from camera_capture import capture_image
from classification_image import classify_image
from detection_text import *
from detection_vehicle import *
from werkzeug.utils import secure_filename


app = Flask(__name__)

# Define the directory
upload_folder = "static/images"
app.config['UPLOAD'] = upload_folder

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/capture")
def capture():
    capture_image()
    return render_template("index.html")

@app.route("/classify")
def classify():
    image_class = str(classify_image())
    return image_class


@app.route("/vehicle")
def vehicle():
    plt_show(convert_result_vehicle(compiled_model_re, image_show(), resize_image_vehicle(), box_car()))
    return render_template("index.html")

@app.route("/detect")
def detect():
    show_image(convert_result_text(image_show(), resize_image_text(), box_detect(), conf_labels=False))
    return render_template("index.html")

# Upload and display the image from the upload directory
@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files['img']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD'], filename))
        img = os.path.join(app.config['UPLOAD'], filename)
        return render_template('index.html', img=img)
    return render_template("index.html")

# Run the app 
if __name__ == "__main__":
    app.run(host="0.0.0.0")