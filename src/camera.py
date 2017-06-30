import os
import os.path
import tempfile

from time import sleep
from picamera import PiCamera

class CameraUtils:

    @staticmethod
    def take_screenshot():
        file = os.path.join(tempfile.gettempdir() + "screenshot.jpg")
        camera = PiCamera()
        camera.start_preview()
        sleep(5)
        camera.capture(file)
        camera.stop_preview()



