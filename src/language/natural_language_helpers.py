from google.cloud import language


class NaturalLanguageHelper:

    def __init__(self):
        self._client = language.Client()

    def get_entities_from_text(self, text):
        document = self._client.document_from_text(content=text)
        entities = document.analyze_entities()
        return entities

    def get_entities_sentiments_from_text(self, text):
        document = self._client.document_from_text(content=text)
        entities_sentiments = document.analyze_entity_sentiment()
        return entities_sentiments

    def get_sentiments_from_text(self, text):
        document = self._client.document_from_text(content=text)
        sentiments = document.analyze_sentiment()
        return sentiments

    def get_syntax_from_text(self, text):
        document = self._client.document_from_text(content=text)
        syntax = document.analyze_syntax()
        return syntax



