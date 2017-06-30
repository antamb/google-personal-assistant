from vision.vision_helpers import VisionHelper


class ExplicitContentDetection:

    def __init__(self):
        self._vision = VisionHelper()

    def detect_explicit_content(self):
        image = self._vision.get_vision_image()
        explicit_content = image.detect_safe_search()

        response = "{} {} {} {}".format(explicit_content.adult,
                                        explicit_content.medical,
                                        explicit_content.spoof,
                                        explicit_content.violence)
        print("[LandMarkDetection][response]: " + response)
        return response
