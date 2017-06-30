from vision.vision_helpers import VisionHelper


class LandMarkDetection:

    def __init__(self):
        self._vision = VisionHelper()

    def detect_landmark(self):
        image = self._vision.get_vision_image()
        landmarks = image.detect_landmarks()

        nb_landmark = len(landmarks)
        if nb_landmark > 1:
            response = "I detected {} landmark".format(len(landmarks))
        elif nb_landmark < 1:
            response = "I didn't detect any landmark"
            return response

        for landmark in landmarks:
            response += landmark.description
            response += ", "

        print("[LandMarkDetection][response]: " + response)
        return response
