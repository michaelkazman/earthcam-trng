from .imageconverter import ImageConverter

# convert image to a 32-byte representation
def convert_image(image):
    image_converter = ImageConverter()
    converted_image = image_converter.convert(image)
    return converted_image