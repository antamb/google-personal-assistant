from vision.vision_helpers import VisionHelper


class ImageAttributesDetection:

    def __init__(self):
        self._vision = VisionHelper()

    def detect_attributes(self):
        image = self._vision.get_vision_image()
        props = image.detect_properties()
        print('Properties:')

        for color in props.colors:
            print('fraction: {}'.format(color.pixel_fraction))
            print('\tr: {}'.format(color.color.red))
            print('\tg: {}'.format(color.color.green))
            print('\tb: {}'.format(color.color.blue))
            print('\ta: {}'.format(color.color.alpha))

        response = "Image Attributes Detection done"
        return response

