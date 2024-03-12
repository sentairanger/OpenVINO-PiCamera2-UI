# OpenVINO-PiCamera2-UI
This is a Flask based UI that allows the user to take images with the Pi Camera module, and use OpenVINO's pretrained models to classify images, detect text or detect a vehicle.

## Getting Started

Here are the things you will need to get started:
* Raspberry Pi 4 or 3B+. Pi 5 will be tested in the future
* Intel NCS2 (only found on places like eBay)
* Raspberry Pi Camera Module (Any Module will Work)
* Raspberry Pi OS Bullseye 64-bit (Will test with Bookworm)
* Raspberry Pi Camera Module Mount is recommended
* OpenVINO (Follow this [gist](https://gist.github.com/sentairanger/caf11a2432ceebd715c6b33c224f4960) for more details)
* `picamera2` Python module

## Components of the Application

The application is divided into several parts:

* `app.py`: This is the main code logic and is required to run the application.
* `classification_image.py`: This is used for the image classification portion.
* `detection_text.py`: This is used for text detection.
* `detection_vehicle.py`: This is used to detect and recognize vehicles
* `models_input.py`: This initializes the models for vehicle detection and recognition, text detection and image classification.
* `camera_capture.py`: This is used to capture an image with the Pi Camera module.

## Running for the First Time

Make sure to have OpenVINO installed, have the camera module installed and be sure to insert the Intel NCS2 into a USB port before running the application. After that run the application with `python3 app.py`. Then go to `0.0.0.0:5000/` and then you should see the UI as shown below. Then you can click the buttons to capture images, classify images, detect text or detect vehicles.

![image](https://github.com/sentairanger/OpenVINO-PiCamera2-UI/blob/main/openvino.png)

## Youtube Demo

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/ta1XP9TISrc/0.jpg)](https://www.youtube.com/watch?v=ta1XP9TISrc)
