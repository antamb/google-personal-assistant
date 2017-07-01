import os
import os.path
import picamera

from time import sleep


class CameraUtils:
    
    IMAGE_DIR = "/Pictures/screenshots/"

    @staticmethod
    def take_screenshot():
        file = os.path.join(CameraUtils.IMAGE_DIR, "screenshot.jpg")
        with picamera.PiCamera as camera:
            print("Give me your best smile")
            camera.start_preview()
            sleep(2)
            camera.capture(file)
            camera.stop_preview()
            print("Ok now you can relax")
