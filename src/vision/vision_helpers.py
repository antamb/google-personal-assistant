import io
from camera import CameraUtils
from google.cloud import vision


class VisionHelper:
    def __init__(self):
        self._client = vision.Client()

    def get_vision_image(self, web_annotations=False):
        if web_annotations:
            file = "/home/pi/Pictures/337px-Rosaparks.jpg"
        else:
            file = CameraUtils.take_screenshot()
        with io.open(file, 'rb') as image_file:
            content = image_file.read()
            image = self._client.image(content=content)
            return image


