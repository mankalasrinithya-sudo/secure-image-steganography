from flask import Flask, render_template, request
import os

from encoder import encode_image
from decoder import decode_image

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
ENCODED_FOLDER = "encoded"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(ENCODED_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/encode", methods=["POST"])
def encode():

    image = request.files["image"]
    message = request.form["message"]

    image_path = os.path.join(
        UPLOAD_FOLDER,
        image.filename
    )

    image.save(image_path)

    output_path = os.path.join(
        ENCODED_FOLDER,
        "encoded_" + image.filename
    )

    encode_image(
        image_path,
        message,
        output_path
    )

    return f"""
    Message hidden successfully.<br><br>
    Encoded image saved as:<br>
    {output_path}
    """

@app.route("/decode", methods=["POST"])
def decode():

    image = request.files["image"]

    image_path = os.path.join(
        UPLOAD_FOLDER,
        image.filename
    )

    image.save(image_path)

    message = decode_image(image_path)

    return f"""
    Hidden Message:<br><br>
    {message}
    """

if __name__ == "__main__":
    app.run(debug=True)