from vision.vision_helpers import VisionHelper


class WebAnnotationsDetection:

    def __init__(self):
        self._vision = VisionHelper()

    def detect_web_annotations(self):
        image = self._vision.get_vision_image(True)
        notes = image.detect_web()

        if notes.pages_with_matching_images:
            print('\n{} Pages with matching images retrieved')

            for page in notes.pages_with_matching_images:
                print('Score : {}'.format(page.score))
                print('Url   : {}'.format(page.url))

        if notes.full_matching_images:
            print('\n{} Full Matches found: '.format(
                len(notes.full_matching_images)))

            for image in notes.full_matching_images:
                print('Score:  {}'.format(image.score))
                print('Url  : {}'.format(image.url))

        if notes.partial_matching_images:
            print('\n{} Partial Matches found: '.format(
                len(notes.partial_matching_images)))

            for image in notes.partial_matching_images:
                print('Score: {}'.format(image.score))
                print('Url  : {}'.format(image.url))

        if notes.web_entities:
            print('\n{} Web entities found: '.format(len(notes.web_entities)))

            for entity in notes.web_entities:
                print('Score      : {}'.format(entity.score))
                print('Description: {}'.format(entity.description))

        response = "Web Detection done"
        return response

