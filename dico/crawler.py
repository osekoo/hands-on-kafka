import requests
from bs4 import BeautifulSoup
import re


class Crawler:
    def get_definition(self, word: str):
        pass


class CrawlerFR(Crawler):

    def __init__(self):
        self.base_url = 'https://dictionnaire.lerobert.com/definition/{word}'

    def get_definition(self, word: str):
        request_url = self.base_url.replace('{word}', word)
        page = requests.get(request_url)
        soup_handler = BeautifulSoup(page.content, 'html.parser')
        definition_elt = soup_handler.select_one('body > div.ws-c > main > section.def > div.b')
        return re.sub(r'(\n\s*)+\n+', '\n\n', definition_elt.text) if definition_elt else None


class CrawlerEN(Crawler):

    def __init__(self):
        self.base_url = 'https://www.dictionary.com/browse/{word}'

    def get_definition(self, word: str):
        request_url = self.base_url.replace('{word}', word)
        page = requests.get(request_url)
        soup_handler = BeautifulSoup(page.content, 'html.parser')
        selector = '#top-definitions > div:nth-child(1) > section.q7ELwPUtygkuxUXXOE9t.LVt92HnYuY17Vv04474m'
        definition_elt = soup_handler.select_one(selector)
        return re.sub(r'(\n\s*)+\n+', '\n\n', definition_elt.text) if definition_elt else None
