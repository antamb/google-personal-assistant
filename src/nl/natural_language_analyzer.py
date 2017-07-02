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
            response += "I analyzed {} entities from the text on the image: ".format(nb_entities)
        elif nb_entities == 1:
            response += "I analyzed one entity from the text on the image: ".format(nb_entities)
        else:
            response += "I didn't detect any entity in the text"
            return response

        entity_name_type = {EntityType.EVENT: [],
                            EntityType.PERSON: [],
                            EntityType.LOCATION: [],
                            EntityType.ORGANIZATION: []}
        for entity in entities:
            if entity.entity_type == EntityType.EVENT:
                entity_name_type[EntityType.EVENT].append(entity.name)
            if entity.entity_type == EntityType.PERSON:
                entity_name_type[EntityType.PERSON].append(entity.name)
            if entity.entity_type == EntityType.LOCATION:
                entity_name_type[EntityType.LOCATION].append(entity.name)
            if entity.entity_type == EntityType.ORGANIZATION:
                entity_name_type[EntityType.ORGANIZATION].append(entity.name)

        nb_events = len(entity_name_type[EntityType.EVENT])
        if nb_events > 0:
            print("[EVENTS]: " + ", ".join(entity_name_type[EntityType.EVENT]))
        if nb_events > 1:
            response += "{} events".format(len(entity_name_type[EntityType.EVENT]))
        elif nb_events == 1:
            response += "one event"

        nb_persons = len(entity_name_type[EntityType.PERSON])
        if nb_persons > 0:
            print("[PERSONS]: " + ", ".join(entity_name_type[EntityType.PERSON]))
        if nb_events > 0 and nb_persons > 0:
            response += ", "
        if nb_persons > 1:
            response += "{} persons".format(len(entity_name_type[EntityType.PERSON]))
        elif nb_persons == 1:
            response += "one person"

        nb_locations = len(entity_name_type[EntityType.LOCATION])
        if nb_locations > 0:
            print("[LOCATIONS]: " + ", ".join(entity_name_type[EntityType.LOCATION]))
        if nb_persons > 0 and nb_locations > 0:
            response += ", "
        if nb_locations > 1:
            response += "{} locations".format(len(entity_name_type[EntityType.LOCATION]))
        elif nb_locations == 1:
            response += "one location"

        nb_organizations = len(entity_name_type[EntityType.ORGANIZATION])
        if nb_organizations > 0:
            print("[ORGANIZATIONS]: " + ", ".join(entity_name_type[EntityType.ORGANIZATION]))
        if nb_organizations > 0 and nb_locations > 0:
            response += ", "
            
        if nb_organizations > 1:
            response += "{} organizations".format(len(entity_name_type[EntityType.ORGANIZATION]))
        elif nb_organizations == 1:
            response += "one organization"

        return response
