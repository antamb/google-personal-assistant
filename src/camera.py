import os
import os.path
from picamera import PiCamera

from time import sleep


class CameraUtils:

    IMAGE_DIR = "/home/pi/Pictures/screenshots/"

    @staticmethod
    def take_screenshot():
        file = os.path.join(CameraUtils.IMAGE_DIR, "screenshot.jpg")
        camera = PiCamera()
        try:
            print("Give me your best smile")
            camera.start_preview()
            sleep(1)
            camera.capture(file)
            camera.stop_preview()
        finally:
            camera.close()

        print("Ok now you can relax")
        return file
