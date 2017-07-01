from vision.explicit_content_detection import ExplicitContentDetection


class ExplicitContentDetectionActor(object):

    def __init__(self, say):
        self.say = say

    def run(self, command):
        response = ExplicitContentDetection.detect_explicit_content(ExplicitContentDetection())
        self.say(response)
