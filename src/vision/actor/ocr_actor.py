from vision.ocr import OCR


class OCRActor(object):

    def __init__(self, say):
        self.say = say

    def run(self, command):
        if command == "text":
            response = OCR.detect_text(OCR())
        else:
            response = OCR.detect_full_text(OCR())
        self.say(response)
