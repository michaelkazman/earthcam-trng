import cv2
import os
from utils.utils import calculate_entropy

class ImageConverter(object):
    def __init__(self, image):
        self.entropy = calculate_entropy(image)
    
    def get_entropy(self):
        return self.entropy

if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    image_names = ['flag', 'david', 'egg', 'kusatsu_onsen_cam', 'lasvegas_cam', 'shibuya_cam', 'white']
    for image_name in image_names:
        for i in [1, 2]:
            print(image_name + '-------------------------')
            dir_path = os.path.dirname(os.path.realpath(__file__))
            image = cv2.imread(f'{dir_path}/scrambled/{image_name}_{i}.jpg')
            image_converter = ImageConverter(image)
            print(image_converter.get_entropy())
        