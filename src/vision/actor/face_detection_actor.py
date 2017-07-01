from vision.face_detection import FaceDetection


class FaceDetectionActor(object):

    def __init__(self, say):
        self.say = say

    def run(self):
        response = FaceDetection.detect_faces(FaceDetection())
        self.say(response)
