import os
import os.path
import tempfile

from time import sleep
from picamera import PiCamera

class CameraUtils:

    IMAGE_DIR = "~/Pictures/screenshots/"

    @staticmethod
    def take_screenshot():
        file = os.path.join(CameraUtils.IMAGE_DIR + "screenshot.jpg")
        camera = PiCamera()
        camera.start_preview()
        sleep(2)
        camera.capture(file)
        camera.stop_preview()



