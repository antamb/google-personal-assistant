from google.cloud.vision.likelihood import Likelihood


class Constants:
    RATINGS = [Likelihood.VERY_LIKELY.name, Likelihood.LIKELY.name, Likelihood.POSSIBLE.name]

    @staticmethod
    def get_timestamp():
        import time
        ts = time.time()
        import datetime
        return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')



