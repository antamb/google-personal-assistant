from language.natural_language_helpers import NaturalLanguageHelper


class LanguageAnalyzer:

    def __init__(self):
        self._language = NaturalLanguageHelper()

    def analyze_text(self, text):
        response = self._language.get_entities_from_text(text)
        dir(response)
        entities = response.entities

        for entity in entities:
            print("{} {} {}".format(entity.name, entity.entity_type, entity.mentions))

        return "Language Analysis done"


