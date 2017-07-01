from google.cloud.language.entity import EntityType

from nl.natural_language_helpers import NaturalLanguageHelper

from vision.OCR import OCR


class LanguageAnalyzer:
    def __init__(self):
        self._language = NaturalLanguageHelper()

    def analyze_text_from_image(self):
        ocr = OCR()
        text_from_image = OCR.detect_text(ocr)
        analyzed_text = self._language.get_entities_from_text(text_from_image)
        dir(analyzed_text)
        entities = analyzed_text.entities

        response = ""
        nb_entities = len(entities)
        if nb_entities > 1:
            response += "I analyzed {} entities from the text on the image"
        elif nb_entities == 1:
            response += "I analyzed {} entity from the text on the image"
        else:
            response += "I didn't detect any entity in the text"

        entity_name_type = {EntityType.EVENT: [],
                            EntityType.PERSON: [],
                            EntityType.LOCATION: [],
                            EntityType.ORGANIZATION: []}
        for entity in entities:
            if entity.entity_type == EntityType.EVENT.name:
                entity_name_type[EntityType.EVENT].append(entity.name)
            if entity.entity_type == EntityType.PERSON.name:
                entity_name_type[EntityType.PERSON].append(entity.name)
            if entity.entity_type == EntityType.LOCATION.name:
                entity_name_type[EntityType.LOCATION].append(entity.name)
            if entity.entity_type == EntityType.ORGANIZATION.name:
                entity_name_type[EntityType.ORGANIZATION].append(entity.name)

            if len(entity_name_type[EntityType.EVENT]) > 0:
                response += "{} events".format(len(entity_name_type[EntityType.EVENT]))
            if len(entity_name_type[EntityType.PERSON]) > 0:
                response += "{} personss".format(len(entity_name_type[EntityType.PERSON]))
            if len(entity_name_type[EntityType.LOCATION]) > 0:
                response += "{} locations".format(len(entity_name_type[EntityType.LOCATION]))
            if len(entity_name_type[EntityType.ORGANIZATION]) > 0:
                response += "{} organizations".format(len(entity_name_type[EntityType.ORGANIZATION]))

        return "Language Analysis done"
