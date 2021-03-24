import pandas as pd
from scipy.stats import entropy

def calculate_entropy(image):
    r, g, b = split_image(image)
    r_series, g_series, b_series = pd.Series(r), pd.Series(g), pd.Series(b)
    r_count, g_count, b_count = r_series.value_counts(), g_series.value_counts(), b_series.value_counts()
    r_entropy, g_entropy, b_entropy = entropy(r_count), entropy(g_count), entropy(b_count)
    entropy_value = (r_entropy + g_entropy + b_entropy) / 3
    return entropy_value

def split_image(image):
    return image[:,:,2].flatten(), image[:,:,1].flatten(), image[:,:,0].flatten()