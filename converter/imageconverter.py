
class ImageConverter(object):
    def convert(self, image):
        return image.flatten().tobytes()[:32]
