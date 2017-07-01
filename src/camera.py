import os
import os.path
from picamera import PiCamera

from time import sleep


class CameraUtils:

    IMAGE_DIR = "~/Pictures/screenshots/"

    @staticmethod
    def take_screenshot():
        file = os.path.join(CameraUtils.IMAGE_DIR, "screenshot.jpg")
        camera = PiCamera()
        try:
            print("Give me your best smile")
            camera.start_preview()
            sleep(2)
            camera.capture(file)
            camera.stop_preview()
        finally:
            print("Ok now you can relax")
            camera.close()
