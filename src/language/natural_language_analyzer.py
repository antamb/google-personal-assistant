from language.natural_language_helpers import NaturalLanguageHelper

from vision.OCR import OCR


class LanguageAnalyzer:
    def __init__(self):
        self._language = NaturalLanguageHelper()

    def analyze_text_from_image(self):
        ocr = OCR()
        text_from_image = OCR.detect_text(ocr)
        response = self._language.get_entities_from_text(text_from_image)
        dir(response)
        entities = response.entities

        for entity in entities:
            print("{} {} {}".format(entity.name, entity.entity_type, entity.mentions))

        return "Language Analysis done"
