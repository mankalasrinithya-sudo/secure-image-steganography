# Secure Image Steganography Tool

## Overview

This project is a Flask-based web application that hides secret text messages inside images using Least Significant Bit (LSB) steganography.

The hidden message can later be extracted securely from the encoded image.

---

## Features

* Hide secret messages inside images
* Extract hidden messages
* Flask web application
* User-friendly interface
* PNG image support
* Secure communication concept

---

## Technologies Used

* Python
* Flask
* Pillow
* HTML/CSS

---

## Project Structure

Steganography Tool/
│
├── app.py
├── encoder.py
├── decoder.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── uploads/
├── encoded/
└── screenshots/

---

## Installation

Install required libraries:

pip install flask pillow

---

## Run the Project

python app.py

Open browser:

http://127.0.0.1:5000

---

## How It Works

1. User uploads an image
2. User enters secret message
3. Message is converted to binary
4. Binary data is hidden in image pixels using LSB
5. Encoded image is generated
6. Receiver uploads encoded image
7. Original hidden message is extracted

---

## Future Improvements

* Password protection
* AES encryption
* Audio steganography
* Cloud deployment

---

## Author

Internship Project - Secure Communication using Steganography
