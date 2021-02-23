from livestreamscraper import LivestreamScraper
from threading import Thread
import json

def get_stream_data(file_name):
    with open(file_name, 'r') as json_file:
        json_data = json_file.read()
        data = json.loads(json_data)
        return data

if __name__ == '__main__':
    livestream_data = get_stream_data('livestream_data.json')
    scraper = LivestreamScraper(livestream_data)
    images = scraper.get_images()
    print(len(images))