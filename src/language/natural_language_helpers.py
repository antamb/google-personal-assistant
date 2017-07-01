from google.cloud import language

from vision.OCR import OCR

class NaturalLanguageHelper:

    def __init__(self):
        self._client = language.Client()

    def get_entities_from_text(self, text):
        document = self._client.document_from_text(content=text)
        response = document.analyze_entities()
        return response

    def get_entities_sentiments_from_text(self, text):
        document = self._client.document_from_text(content=text)
        response = document.analyze_entity_sentiment()
        return response

    def get_sentiments_from_text(self, text):
        document = self._client.document_from_text(content=text)
        response = document.analyze_sentiment()
        return response

    def get_syntax_from_text(self, text):
        document = self._client.document_from_text(content=text)
        response = document.analyze_syntax()
        return response



