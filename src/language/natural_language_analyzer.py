from language.natural_language_helpers import NaturalLanguageHelper


class LanguageAnalyzer:

    def __init__(self):
        self._language = NaturalLanguageHelper()

    def analyze_text(self, text):
        entities = self._language.get_entities_from_text(text)


