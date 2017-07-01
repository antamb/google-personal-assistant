from vision.vision_helpers import VisionHelper


class LandMarkDetection:

    def __init__(self):
        self._vision = VisionHelper()

    def detect_landmark(self):
        image = self._vision.get_vision_image()
        landmarks = image.detect_landmarks()

        response = ""
        nb_landmark = len(landmarks)
        if nb_landmark > 1:
            response = "I detected {} landmarks: ".format(nb_landmark)
        elif nb_landmark == 1:
            response = "I detected one landmark: "
        elif nb_landmark < 1:
            response = "I didn't detect any landmark"
            return response

        landmark_list = []
        for landmark in landmarks:
            landmark_list.append(landmark.description)
            response += ", ".join(landmark_list)

        print("[LandMarkDetection][response]: " + response)
        return response
