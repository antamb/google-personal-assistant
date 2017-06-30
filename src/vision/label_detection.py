from vision.vision_helpers import VisionHelper


class LabelDetection:

    def __init__(self):
        self._vision = VisionHelper()

    def detect_labels(self):
        image = self._vision.get_vision_image()
        labels = image.detect_labels()

        response = "Well, I see "

        if len(labels) < 1:
            response += " nothing"

        for label in labels:
            response += "a "
            response += label.description

        print("[LabelDetection][response]: " + response)
        return response

