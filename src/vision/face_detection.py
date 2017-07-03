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
        print("[{}] NB FACES : {}".format(Constants.get_timestamp(), nb_faces))
        if nb_faces > 1:
            response += "{} people ".format(nb_faces)
        elif nb_faces == 1:
            response += "one person "
        else:
            response += "nobody"
            return response

        # Get emotions from faces
        emotions = [0] * 4
        for face in faces:
            print("[{}] [FaceDetection][emotion][JOY]: {}".format(Constants.get_timestamp(), face.emotions.joy))
            print("[{}] [FaceDetection][emotion][ANGER]: {}".format(Constants.get_timestamp(), face.emotions.anger))
            print("[{}] [FaceDetection][emotion][SORROW]: {}".format(Constants.get_timestamp(), face.emotions.sorrow))
            if face.emotions.joy.name in Constants.RATINGS:
                emotions[FaceDetection.JOY] += 1
            elif face.emotions.anger.name in Constants.RATINGS:
                emotions[FaceDetection.ANGER] += 1
            elif face.emotions.sorrow.name in Constants.RATINGS:
                emotions[FaceDetection.SORROW] += 1
            elif face.emotions.surprise.name in Constants.RATINGS:
                emotions[FaceDetection.SURPRISE] += 1
        response += FaceDetection.get_message_from_emotions(emotions, nb_faces)

        print("[{}] [FaceDetection][response]: {}".format(Constants.get_timestamp(), response))
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
        elif emotions[FaceDetection.ANGER] == 1 and nb_faces == 1:
            message += "who is angry"
            return message
        else:
            message += " and nobody is happy"
            return message

        # Detect sad emotion
        if emotions[FaceDetection.SORROW] > 1 and emotions[FaceDetection.JOY] != nb_faces:
            message += "however, {} of them are sad, please give them a hug for me".format(emotions[FaceDetection.JOY])
        return message
