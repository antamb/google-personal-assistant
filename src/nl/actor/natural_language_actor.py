from nl.natural_language_analyzer import LanguageAnalyzer


class LanguageAnalyzerActor(object):

    def __init__(self, say):
        self.say = say

    def run(self, command):
        response = LanguageAnalyzer.analyze_text_from_image(LanguageAnalyzer())
        self.say(response)
