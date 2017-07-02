from vision.vision_helpers import VisionHelper


class WebAnnotationsDetection:
    def __init__(self):
        self._vision = VisionHelper()

    def detect_web_annotations(self, static_image=True):
        image = self._vision.get_vision_image(static_image)
        notes = image.detect_web()

        nb_pages = len(notes.pages_with_matching_images)
        if notes.pages_with_matching_images:
            print('\n{} matching pages')
            for page in notes.pages_with_matching_images:
                print('Url   : {}'.format(page.url))

        nb_full_matches = len(notes.full_matching_images)
        if notes.full_matching_images:
            print('\n{} full matches: '.format(nb_full_matches))

            for image in notes.full_matching_images:
                print('url  : {}'.format(image.url))

        nb_partial_matches = len(notes.partial_matching_images)
        if notes.partial_matching_images:
            print('\n{} partial matches: '.format(nb_partial_matches))

            for image in notes.partial_matching_images:
                print('url  : {}'.format(image.url))

        nb_web_entities_matches = len(notes.web_entities)
        if notes.web_entities:
            print('\n{} web entities: '.format(nb_web_entities_matches))

            for entity in notes.web_entities:
                print('Description: {}'.format(entity.description))

        response = "Web annotations Detection done. Found: {} pages with matching image, {} full match, {} partial matches and {} web entities".format(
            nb_pages, nb_full_matches,
            nb_partial_matches, nb_web_entities_matches)
        return response
