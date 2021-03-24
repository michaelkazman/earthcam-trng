from scraper.scrape import get_images
from scrambler.scramble import scramble_images
from converter.convert import convert_image
from utils.utils import xor_images, calculate_entropy, verify_entropy, send_warnings
from scrambler.imagescrambler import ImageScrambler

import numpy as np
import warnings
import sys
import cv2
import os

if __name__ == '__main__':
    # get images from image scraper
    images = get_images()

    # shuffle image order
    np.random.shuffle(images)

    # scramble images
    scrambled_images = scramble_images(images)

    # xor scrambled images
    xored_image = xor_images(scrambled_images)

    # calculate entropy value
    entropy = calculate_entropy(xored_image)

    # verify image has enough entropy
    if (not verify_entropy(entropy)):
        warnings.showwarning = send_warnings
        warnings.warn("Not enough entropy, using /dev/urandom fallback!")
    
    # convert image
    converted_image = convert_image(np.array([1, 2, 3]))
    