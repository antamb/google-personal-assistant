from vision.vision_helpers import VisionHelper
from constants import Constants

class ExplicitContentDetection:

    def __init__(self):
        self._vision = VisionHelper()

    def detect_explicit_content(self):
        image = self._vision.get_vision_image()
        explicit_content = image.detect_safe_search()

        print("ADULT: {}\n MEDICAL: {}\n VIOLENCE: {}\n ".format(explicit_content.adult,
                                                                 explicit_content.medical,
                                                                 explicit_content.violence))

        if explicit_content.adult.name in Constants.RATINGS:
            response = "I see some adult content, please, make sure that there is no under-age people in the room"
        elif explicit_content.medical.name in Constants.RATINGS:
            response = "I see medical stuff"
        elif explicit_content.violence.name in Constants.RATINGS:
            response = "What I see is violent, do you need me to call 911 ?"
        else:
            response = "I see nothing special"

        print("[ExplicitContentDetection][response]: " + response)
        return response
