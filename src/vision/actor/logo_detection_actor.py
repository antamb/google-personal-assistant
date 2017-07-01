from vision.logo_detection import LogoDetection


class LogoDetectionActor(object):

    def __init__(self, say):
        self.say = say

    def run(self, command):
        response = LogoDetection.detect_logos(LogoDetection())
        self.say(response)
