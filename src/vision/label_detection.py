from vision.vision_helpers import VisionHelper


class LabelDetection:

    def __init__(self):
        self._vision = VisionHelper()

    def detect_labels(self):
        image = self._vision.get_vision_image()
        labels = image.detect_labels()

        response = "Well, I detected "

        nb_labels = len(labels)
        if nb_labels < 1:
            response += " nothing"
        elif nb_labels == 1:
            response += "one label:"
        else:
            label_list = []
            response += "few labels:"
            for label in labels:
                label_list.append(label.description)
            response += " ".join(label_list)

        print("[LabelDetection][response]: " + response)
        return response

