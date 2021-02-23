from livestream import Livestream
from threading import Thread
import time

class LivestreamScraper(object):
    def __init__(self, livestream_data):
       self.__livestreams = self.__generate_livestreams(livestream_data)
       self.__threads = []
       
    # generate list of livestream objects
    def __generate_livestreams(self, livestream_data):
        return [Livestream(data) for data in livestream_data]

    # get current frame of each livestream
    def get_images(self):
        # reset image list
        images = []
        # retrieve current frame for each stream
        images = self.__retrieve_images()
        return images

    def __retrieve_images(self):
        # for keeping track of each frame and corresponding thread
        threads = []
        images = []
        # start each thread
        for i, stream in enumerate(self.__livestreams):
            thread = Thread(target = self.__append_images(stream, images))
            thread.start()
            threads.append(thread)
        # wait for all threads to complete
        for thread in threads:
            thread.join()
        # return list of current frames
        return images

    def __append_images(self, stream, images):
        frame = stream.get_current_frame()
        images.append(frame)
        stream.save_frame()