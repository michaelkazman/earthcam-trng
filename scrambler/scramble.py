from .imagescrambler import ImageScrambler

# scramble list of images
def scramble_images(images):
    image_scrambler = ImageScrambler()
    scrambled_images = [image_scrambler.scramble(image) for image in images]
    return scrambled_images