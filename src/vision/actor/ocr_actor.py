from vision.OCR import OCR


class OCRActor(object):

    def __init__(self, say, command="DEFAULT"):
        self.say = say
        self.command = command

    def run(self, command):
        if self.command == "text":
            response = OCR.detect_text(OCR())
        else:
            response = OCR.detect_full_text(OCR())
        self.say(response)
