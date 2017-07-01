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
            response += "nobody"
            return response

        # Get emotions from faces
        emotions = [0] * 4
        for face in faces:
            print("[FaceDetection][emotion][JOY]: {}".format(face.emotions.joy))
            print("[FaceDetection][emotion][ANGER]: {}".format(face.emotions.anger))
            print("[FaceDetection][emotion][SORROW]: {}".format(face.emotions.sorrow))
            if face.emotions.joy in Constants.RATINGS:
                emotions[FaceDetection.JOY] += 1
            elif face.emotions.anger in Constants.RATINGS:
                emotions[FaceDetection.ANGER] += 1
            elif face.emotions.sorrow in Constants.RATINGS:
                emotions[FaceDetection.SORROW] += 1
            elif face.emotions.surprise in Constants.RATINGS:
                emotions[FaceDetection.SURPRISE] += 1
        response += FaceDetection.get_message_from_emotions(emotions, nb_faces)

        print("[FaceDetection][response]: " + response)
        return response

    @staticmethod
    def get_message_from_emotions(emotions, nb_faces):
        message = ""
        # Detect joy emotion
        if emotions[FaceDetection.JOY] > 1 and emotions[FaceDetection.JOY] != nb_faces:
            message += "and {} of them are happy.".format(emotions[FaceDetection.JOY])
        elif emotions[FaceDetection.JOY] == 1 and nb_faces == 1:
            message += "who is happy."
        elif emotions[FaceDetection.JOY] == nb_faces:
            message += "and they are all happy, well that good cause I hate seeing people sad"
            return message
        elif emotions[FaceDetection.JOY] < 1 and nb_faces == 1:
            message += "who is not happy"
            return message
        else:
            message += "nobody is happy"
            return message

        # Detect sad emotion
        if emotions[FaceDetection.SORROW] > 1 and emotions[FaceDetection.JOY] != nb_faces:
            message += "however, {} of them are sad, please give them a hug for me".format(emotions[FaceDetection.JOY])
        return message
