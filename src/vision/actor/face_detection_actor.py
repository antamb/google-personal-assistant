from vision.face_detection import FaceDetection


class FaceDetectionActor(object):

    def __init__(self, say):
        self.say = say

    def run(self, voice_command):
        response = FaceDetection.detect_faces(FaceDetection())
        self.say(response)
