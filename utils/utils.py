import numpy as np
from scipi.stats.entropy import entropy

def xor_images(img_list):
    base = img_list[0]
    for i in range(1, len(img_list)):
        base = np.bitwise_xor(base, img_list[i]).astype(np.uint8)
    return base