import copy
import cv2
import numpy as np
import os


class ImageScrambler(object):

    def scramble1(self, image):
        """
        Flattens it into 2d array first
        """
        rows, columns, pixels = image.shape
        reshaped = copy.deepcopy(image.reshape(rows * columns * pixels))
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

    def __call__(self, images):
        scrambled_images = []
        for img in images:
            scrambled_images.append(self.scramble1(img))
        return scrambled_images


if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    image_names = ['flag', 'david', 'egg', 'kusatsu_onsen_cam', 'lasvegas_cam', 'shibuya_cam', 'white']
    for image_name in image_names:
        scrambler = ImageScrambler()
        image = cv2.imread(f'{dir_path}/{image_name}.jpg')
        scrambled1 = scrambler.scramble1(image)
        scrambled2 = scrambler.scramble2(image)
        cv2.imwrite(f'{dir_path}/scrambled/{image_name}_1.jpg', scrambled1)
        cv2.imwrite(f'{dir_path}/scrambled/{image_name}_2.jpg', scrambled2)
