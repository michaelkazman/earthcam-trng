
class ImageConverter(object):
    def __init__(self):
        print('Converter Initialized!')

    def convert(self, image):
        return image.flatten().tobytes()[:32]
