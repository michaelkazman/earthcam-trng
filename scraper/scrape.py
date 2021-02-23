from livestreamscraper import LivestreamScraper
import json

# parse stream json to list
def get_stream_data(file_name):
    with open(file_name, 'r') as json_file:
        json_data = json_file.read()
        data = json.loads(json_data)
        return data

# get list of images (as 2d numpy array)
def get_images():
    livestream_data = get_stream_data('livestream_data.json')
    scraper = LivestreamScraper(livestream_data)
    images = scraper.get_images()
    return images