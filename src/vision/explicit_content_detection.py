from vision.vision_helpers import VisionHelper


class ExplicitContentDetection:

    def __init__(self):
        self._vision = VisionHelper()

    def detect_explicit_content(self):
        image = self._vision.get_vision_image()
        explicit_content = image.detect_safe_search()

        from constants import Constants
        if explicit_content.adult.name in Constants.RATINGS:
            print(explicit_content.adult.name)
            response = "I see some adult content, please, make sure that there is no under-age people in the room"
        elif explicit_content.medical.name in Constants.RATINGS:
            print(explicit_content.medical.name)
            response = "I see medical stuff"
        elif explicit_content.violence.name in Constants.RATINGS:
            print(explicit_content.violence.name)
            response = "What I see is violent, do you need me to call 911 ?"
        else:
            response = "I see nothing special"

        print("[ExplicitContentDetection][response]: " + response)
        return response
