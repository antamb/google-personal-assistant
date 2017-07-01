from vision.image_attributes import ImageAttributesDetection


class ImageAttributesDetectionActor(object):

    def __init__(self, say):
        self.say = say

    def run(self, command):
        response = ImageAttributesDetection.detect_attributes(ImageAttributesDetection())
        self.say(response)
