from vision.face_detection import FaceDetection


class FaceDetectionActor(object):

    def __init__(self, say):
        self.say = say

    def run(self, voice_command):
        FaceDetection.detect_faces(FaceDetection())
