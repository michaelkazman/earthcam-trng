from scipy.stats import entropy

import numpy as np
import pandas as pd
import logging

# consecutively xor a list of images together
def xor_images(images):
    for i in range(len(images) - 1):
        xored_image = np.bitwise_xor(images[i], images[i + 1])
        images[i+1] = xored_image
    return images[-1]

# calculate average entropy of each r, g, and b channels
def calculate_entropy(image):
    r, g, b = split_image(image)
    r_series, g_series, b_series = pd.Series(r), pd.Series(g), pd.Series(b)
    r_count, g_count, b_count = r_series.value_counts(), g_series.value_counts(), b_series.value_counts()
    r_entropy, g_entropy, b_entropy = entropy(r_count), entropy(g_count), entropy(b_count)
    entropy_value = (r_entropy + g_entropy + b_entropy) / 3
    return entropy_value

# split image into (r, g, b) values
# opencv encodes images as (b, g, r)
def split_image(image):
    return image[:,:,2].flatten(), image[:,:,1].flatten(), image[:,:,0].flatten()

# verify if the provided entropy is "random" enough
# to be considered secure
def verify_entropy(image):
    entropy_threshold = 5.00
    return image >= entropy_threshold

# custom warning (incase a lack of entropy exists)
def send_warnings(message, category, filename, lineno, file=None, line=None):
    logging.warning(f'{filename}:{lineno}:\n\t{category.__name__}:{message}')