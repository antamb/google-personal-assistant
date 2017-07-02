import os
import os.path
import subprocess

from picamera import PiCamera

from time import sleep

from pip import logger
from pip.utils import logging

logger = logging.getLogger('CameraUtils')


class CameraUtils:
    IMAGE_DIR = "/home/pi/Pictures/screenshots/"

    @staticmethod
    def take_screenshot():
        file = os.path.join(CameraUtils.IMAGE_DIR, "screenshot.jpg")
        camera = PiCamera()
        try:
            logger.info("About to take a picture")
            camera.start_preview()
            sleep(1)
            camera.capture(file)
            camera.stop_preview()
        finally:
            camera.close()

        logger.info("Done taking picture")
        return file

    @staticmethod
    def take_video():
        file = os.path.join(CameraUtils.IMAGE_DIR, "video.h264")
        camera = PiCamera()
        try:
            logger.info("About to take a video")
            camera.start_recording(file)
            sleep(10)
            camera.stop_recording()
            subprocess.check_output(['MP4Box', '-add {}.h264 {}.mp4'.format(file, file.replace("h264", "mp4"))])
        finally:
            camera.close()

        logger.info("Done taking video")
        return file
