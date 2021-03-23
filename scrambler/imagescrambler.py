import copy

import cv2
import numpy as np


class ImageScrambler(object):

    def scramble1(self, image):
        """
        Flattens it into 2d array first
        """
        rows, columns, pixels = image.shape
        reshaped = copy.deepcopy(image.reshape(rows * columns, pixels))
        np.random.shuffle(reshaped)
        return reshaped.reshape(rows, columns, pixels)

    def scramble2(self, image):
        copied_img = copy.deepcopy(image)
        for row in copied_img:
            # for pixel in row:
            #     np.random.shuffle(pixel)
            np.random.shuffle(row)
        np.random.shuffle(copied_img)
        return copied_img


if __name__ == '__main__':
    scrambler = ImageScrambler()
    image = cv2.imread('rainbow.jpg')
    scrambled1 = scrambler.scramble1(image)
    scrambled2 = scrambler.scramble2(image)
    cv2.imwrite('scrambled_rainbow.jpg', scrambled1)
    cv2.imshow('image 1', scrambled1)
    cv2.imshow('image 2', scrambled2)
    cv2.waitKey()
