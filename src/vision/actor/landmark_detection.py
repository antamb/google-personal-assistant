from vision.landmark_detection import LandMarkDetection


class LandMarkDetectionActor(object):

    def __init__(self, say):
        self.say = say

    def run(self, command):
        response = LandMarkDetection.detect_landmark(LandMarkDetection())
        self.say(response)
