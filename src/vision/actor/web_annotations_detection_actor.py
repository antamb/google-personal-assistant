from vision.web_detection import WebAnnotationsDetection


class WebAnnotationsDetectionActor(object):

    def __init__(self, say, static_image):
        self.say = say
        self.static_image = static_image

    def run(self, command):
        response = WebAnnotationsDetection.detect_web_annotations(WebAnnotationsDetection(), self.static_image)
        self.say(response)
