from vision.video_label_detection import VideoIntelligence


class VideoIntelligenceActor(object):

    def __init__(self, say):
        self.say = say

    def run(self, command):
        response = VideoIntelligence.get_labels()
        self.say(response)
