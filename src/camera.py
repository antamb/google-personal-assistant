import os
import os.path
import subprocess

from picamera import PiCamera

from time import sleep
from constants import Constants


class CameraUtils:
    IMAGE_DIR = "/home/pi/Pictures/screenshots/"

    @staticmethod
    def take_screenshot():
        file = os.path.join(CameraUtils.IMAGE_DIR, "screenshot.jpg")
        camera = PiCamera()
        try:
            print("[{}] About to take a picture".format(Constants.get_timestamp()))
            camera.start_preview()
            sleep(1)
            camera.capture(file)
            camera.stop_preview()
        finally:
            camera.close()

        print("[{}] Done taking picture".format(Constants.get_timestamp()))
        return file

    @staticmethod
    def take_video():
        file = os.path.join(CameraUtils.IMAGE_DIR, "video.h264")
        camera = PiCamera()
        converted_file = file.replace("h264", "mp4")
        try:
            print("[{}] About to take a video".format(Constants.get_timestamp()))
            camera.start_recording(file)
            sleep(10)
            camera.stop_recording()
            subprocess.check_output(['MP4Box', '-add', '{}'.format(file), '{}'.format(converted_file)])
        finally:
            camera.close()

        print("[{}] Done taking video: {}".format(Constants.get_timestamp(), converted_file))
        return converted_file
