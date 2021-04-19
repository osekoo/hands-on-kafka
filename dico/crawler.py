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
        content = definition_elt.text
        print(f'content: {content}')
        content = re.sub(r'(\n\s*)+\n+', '\n\n', content)
        print(f'content: {content}')
        return content if definition_elt else None


class CrawlerEN(Crawler):

    def __init__(self):
        self.base_url = 'https://dictionnaire.lerobert.com/definition/{word}'

    def get_definition(self, word: str):
        request_url = self.base_url.replace('{word}', word)
        page = requests.get(request_url)
        soup_handler = BeautifulSoup(page.content, 'html.parser')
        definition_elt = soup_handler.select_one('body > div.ws-c > main > section.def > div.b')

        return definition_elt.text if definition_elt else None
