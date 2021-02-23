from streamlink import Streamlink
import cv2

class Livestream(object):
    def __init__(self, stream_data):
        # streamlink (low overhead for consecutive retreivals)
        self.__session = Streamlink()
        self.__url = stream_data['url']
        self.__tag = stream_data['tag']
        self.__frame = None
        # for saving frames locally
        image_path =  '../images/{0}.jpg'.format(stream_data['image_path'])
        self.__image_path = image_path

    # get current frame of stream
    def get_current_frame(self):
        # update stream link
        stream_link = self.__get_stream_link()
        # capture frame of video stream
        try:
            capture = cv2.VideoCapture(stream_link, cv2.CAP_FFMPEG)
            (status, frame) = self.__read_stream(capture)
            if status:
                self.__frame = frame
                return frame
        # repeat process
        except cv2.error as e:
            self.get_current_frame()

    # save last recorded frame (for testing / debugging)
    def save_frame(self):
        if (self.__frame is not None):
            cv2.imwrite(self.__image_path, self.__frame)

    # retrieve url for the current live stream chunk
    def __get_stream_link(self):
        streams = self.__session.streams(self.__url)
        stream = streams[self.__tag]
        return stream.url

    # helper function for reading in stream data as a tuple
    def __read_stream(self, capture):
        if capture.isOpened():
            return capture.read()
        return (False, None)

    def get_url(self):
        return self.__url