from vision.vision_helpers import VisionHelper


class LogoDetection:

    def __init__(self):
        self._vision = VisionHelper()

    def detect_logos(self):
        image = self._vision.get_vision_image()
        logos = image.detect_logos()

        nb_logos = len(logos)
        response = "I see "
        if nb_logos < 1:
            response += " nothing"
            return response
        elif nb_logos == 1:
            response += "the logo of"
        else:
            response += "many logos: "

        if nb_logos >= 1:
            logo_list = {}
            for logo in logos:
                logo_list.append(logo.description)
            response += ", ".join(logo_list)

        print("[LogoDetection][response]: " + response)
        return response
