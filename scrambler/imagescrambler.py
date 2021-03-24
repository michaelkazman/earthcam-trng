import numpy as np

class ImageScrambler(object):
    # randomly scramble every r, g, and b value together
    # to generate random pixels of n^k unique colors, where
    # n is how many possible rgb values exist and k is the # of color values
    def scramble(self, image):
        rows, columns, pixels = image.shape
        flattened_image = image.flatten()
        np.random.shuffle(flattened_image)
        shuffled_image = flattened_image.reshape(rows, columns, pixels)
        return shuffled_image

    # scramble pixel locations around (while leaving pixel colors intact)
    def scramble_pixels(self, image):
        rows, columns, pixels = image.shape
        flattened_image = image.reshape(rows * columns, pixels)
        np.random.shuffle(flattened_image)
        shuffled_image = flattened_image.reshape(rows, columns, pixels)
        return shuffled_image