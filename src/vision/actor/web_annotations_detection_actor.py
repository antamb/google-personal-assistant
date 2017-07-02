from vision.web_detection import WebAnnotationsDetection


class WebAnnotationsDetectionActor(object):

    def __init__(self, say):
        self.say = say

    def run(self, command):
        response = WebAnnotationsDetection.detect_web_annotations(WebAnnotationsDetection())
        self.say(response)
