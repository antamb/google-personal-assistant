from constants import Constants
from vision.vision_helpers import VisionHelper


class FaceDetection:
    JOY = 0
    ANGER = 1
    SORROW = 2
    SURPRISE = 3

    def __init__(self):
        self._vision = VisionHelper()

    def detect_faces(self):
        image = self._vision.get_vision_image()
        faces = image.detect_faces()

        response = "I see "
        nb_faces = len(faces)
        if nb_faces > 1:
            response + "{} people ".format(nb_faces)
        elif nb_faces == 1:
            response += "one person "
        else:
            return response + "nobody "

        # Get emotions from faces
        response += "and "
        emotions = [0] * 4
        for face in faces:
            if face.emotions.joy in Constants.RATINGS:
                emotions[FaceDetection.JOY] += 1
            elif face.emotions.anger in Constants.RATINGS:
                emotions[FaceDetection.ANGER] += 1
            elif face.emotions.sorrow in Constants.RATINGS:
                emotions[FaceDetection.SORROW] += 1
            elif face.emotions.surprise in Constants.RATINGS:
                emotions[FaceDetection.SURPRISE] += 1
        response += response + FaceDetection.get_message_from_emotions(emotions)

        print("[FaceDetection][response]: " + response)
        return response

    @staticmethod
    def get_message_from_emotions(emotions):
        # Detect joy emotion
        if emotions[FaceDetection.JOY] > 1:
            return "there is {} that are happy".format(emotions[FaceDetection.JOY])
        elif emotions[FaceDetection.JOY] == 1:
            return "there is one who is happy"
        else:
            return "nobody is happy"

        # Detect sad emotion
        if emotions[FaceDetection.SORROW] > 1:
            return "there is {} sad people, please give them a hug for me".format(emotions[FaceDetection.JOY])
        elif emotions[FaceDetection.SORROW] == 1:
            return "there is one person who is sad, please him a hug for me"
        else:
            return "nobody is sad, that good cause I hate seeing people sad"
