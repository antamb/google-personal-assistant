import base64
import io
import sys

import time

from google.cloud.gapic.videointelligence.v1beta1 import (video_intelligence_service_client)

from camera import CameraUtils


class VideoIntelligence:

    @staticmethod
    def get_labels():
        client = (video_intelligence_service_client.
                  VideoIntelligenceServiceClient())
        features = [4]

        file = CameraUtils.take_video()
        with io.open(file, "rb") as video:
            content_base64 = base64.b64encode(video.read())

        operation = client.annotate_video(
            '', features, input_content=content_base64)
        print('\nProcessing video for label annotations:')

        while not operation.done():
            sys.stdout.write('.')
            sys.stdout.flush()
            time.sleep(15)

        print('\nDone processing video')

        results = operation.result().annotation_results[0]

        response = ""
        for i, label in enumerate(results.label_annotations):
            response += 'Label detected: {}'.format(label.description)
            print('Locations:')

            for l, location in enumerate(label.locations):
                positions = 'Entire video'
                if (location.segment.start_time_offset != -1 or
                            location.segment.end_time_offset != -1):
                    positions = '{} to {}'.format(
                        location.segment.start_time_offset / 1000000.0,
                        location.segment.end_time_offset / 1000000.0)
                print('\t{}: {}'.format(l, positions))

            print('\n')

        if response == "":
            response += "No label detected"
        return response
