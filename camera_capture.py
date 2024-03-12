from picamera2 import Picamera2
from time import sleep

picam2 = Picamera2()
config = picam2.create_preview_configuration()
picam2.configure(config)
image_sample = "data/image.jpg"

# Take picture
def capture_image():
    picam2.start()
    print("image processing")
    sleep(3)
    picam2.capture_file(image_sample)
    picam2.stop()
    print("success")