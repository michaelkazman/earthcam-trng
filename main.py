import warnings
import numpy as np
import cv2
from os import urandom
from converter.convert import convert_image
from scrambler.scramble import scramble_images
from scraper.scrape import get_images
from utils.utils import xor_images, calculate_entropy, verify_entropy, send_warnings

def main():
    # get images from image scraper
    images = get_images()

    # shuffle image order
    np.random.shuffle(images)

    # scramble images
    scrambled_images = scramble_images(images)

    # xor scrambled images
    xored_image = xor_images(scrambled_images)

    # calculate entropy value
    # runtime(calculate_entropy, xored_image)
    entropy = calculate_entropy(xored_image)

    # verify image has enough entropy
    if (not verify_entropy(entropy)):
        warnings.showwarning = send_warnings
        warnings.warn("Not enough entropy, using /dev/urandom fallback!")
        return os.urandom(32)

    # convert image
    converted_image = convert_image(xored_image)

    # return random bytes
    return convert_image

if __name__ == '__main__':
    random_bytes = main()
    print(random_bytes)
