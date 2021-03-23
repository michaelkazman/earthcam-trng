from livestream import Livestream
from threading import Thread
from random import sample


class LivestreamScraper(object):
    def __init__(self, livestream_data, img_dir):
        self.__num_streams = 3
        self.__livestreams = self.__generate_livestreams(livestream_data)
        self.__threads = []
        self.__img_dir = img_dir

    # generate list of livestream objects
    def __generate_livestreams(self, livestream_data):
        live_streams = sample(livestream_data, self.__num_streams)
        return [Livestream(data) for data in live_streams]

    # get current frame of each livestream
    def get_images(self):
        # reset image list
        images = []
        # retrieve current frame for each stream
        images = self.__retrieve_images()
        return images

    # retrieve images (uses mutli-threading)
    def __retrieve_images(self):
        # for keeping track of each frame and corresponding thread
        threads = []
        images = []
        # start each thread
        for i, stream in enumerate(self.__livestreams):
            thread = Thread(target=self.__append_images, daemon=True, args=(stream, images))
            thread.start()
            threads.append(thread)
        # wait for all threads to complete
        for thread in threads:
            thread.join()
        # return list of current frames
        return images

    # append images to list (from stream object)
    def __append_images(self, stream, images):
        frame = stream.get_current_frame()
        images.append(frame)
        stream.save_frame(self.__img_dir)
