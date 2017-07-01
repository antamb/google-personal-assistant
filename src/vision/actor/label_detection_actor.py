from vision.label_detection import LabelDetection


class LabelDetectionActor(object):

    def __init__(self, say):
        self.say = say

    def run(self, command):
        response = LabelDetection.detect_labels(LabelDetection())
        self.say(response)
