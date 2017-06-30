from vision.vision_helpers import VisionHelper


class OCR:

    def __init__(self):
        self._vision = VisionHelper()

    def detect_full_text(self):
        image = self._vision.get_vision_image()
        full_text = image.detect_full_text()
        response = ""
        for page in full_text.pages:
            for block in page.blocks:
                block_words = []
                for paragraph in block.paragraphs:
                    block_words.extend(paragraph.words)

                block_symbols = []
                for word in block_words:
                    block_symbols.extend(word.symbols)

                block_text = ''
                for symbol in block_symbols:
                    block_text = block_text + symbol.text
                response += block_text + "\n"

        print("[OCR][detect_full_text]: " + response)
        return response

    def detect_text(self):
        image = self._vision.get_vision_image()
        texts = image.detect_full_text()
        response = ""

        for text in texts:
            response += text.description
            response += ", "

        print("[OCR][detect_text]: " + response)
        return response
