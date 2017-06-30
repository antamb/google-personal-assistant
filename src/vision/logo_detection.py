from vision.vision_helpers import VisionHelper


class LogoDetection:

    def __init__(self):
        self._vision = VisionHelper()

    def detect_logos(self):
        image = self._vision.get_vision_image()
        logos = image.detect_logos()
        response = "I see "

        if len(logos) < 1:
            response += " nothing"
        elif len(logos) == 1:
            response += "logo "
        else:
            response += "logos "

        response += "of "
        for logo in logos:
            response += logo.description
            response += ", "

        print("[LogoDetection][response]: " + response)
        return response
