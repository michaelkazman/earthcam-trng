import warnings
import numpy as np

from converter.convert import convert_image
from scrambler.scramble import scramble_images
from scraper.scrape import get_images
from utils.utils import xor_images, calculate_entropy, verify_entropy, send_warnings

import os, cv2

def main():
    # get images from image scraper
    #images = get_images()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    images = [
        cv2.imread(f'{dir_path}/images/lasvegas_cam.png'), 
        cv2.imread(f'{dir_path}/images/shibuya_cam.png'), 
        cv2.imread(f'{dir_path}/images/kusatsu_onsen_cam.png'), 
    ]

    # shuffle image order
    np.random.shuffle(images)

    # scramble images
    scrambled_images = scramble_images(images)
    cv2.imwrite(f'{dir_path}/scrambler/example_photos/lasvegas_cam_shuffled.png', scrambled_images[0])
    cv2.imwrite(f'{dir_path}/scrambler/example_photos/shibuya_cam_shuffled.png', scrambled_images[1])
    cv2.imwrite(f'{dir_path}/scrambler/example_photos/kusatsu_onsen_cam_shuffled.png', scrambled_images[2])

    # xor scrambled images
    xored_image = xor_images(scrambled_images)

    # calculate entropy value
    # runtime(calculate_entropy, xored_image)
    entropy = calculate_entropy(xored_image)

    # verify image has enough entropy
    if (not verify_entropy(entropy)):
        warnings.showwarning = send_warnings
        warnings.warn("Not enough entropy, using /dev/urandom fallback!")

    # convert image
    converted_image = convert_image(xored_image)

    print(converted_image)

    # return random bytes
    return convert_image


if __name__ == '__main__':
    print(main())
