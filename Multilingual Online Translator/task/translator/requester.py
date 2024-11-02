# requester module

import re
from typing import List

import requests
from bs4 import BeautifulSoup, SoupStrainer

from language import Language
from translation import Translation


class Requester:
    headers = {'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36 Chrome/93.0.4577.82 Safari/537.36'}
    base_url = 'https://context.reverso.net/translation'
    translations_filter = SoupStrainer(id="translations-content")
    example_filter = SoupStrainer(id="examples-content")

    def __init__(self, from_lang: Language, to_lang: List[Language]):
        self.from_lang = from_lang
        self.lang_str = [f"/{from_lang.name}-{lang.name}" for lang in to_lang]

    def get_translations(self, word) -> List[Translation]:
        urls = [self.base_url + lang + f'/{word}' for lang in self.lang_str]
        responses = []
        for url in urls:
            try:
                response = requests.get(url, headers=self.headers)
                if response.ok:
                    responses.append(self.extract_translation(response.text))
                elif response.status_code == 404:
                    print(f"Sorry, unable to find {word}")
                    break
            except requests.exceptions.RequestException:
                print(f"Something wrong with your internet connection")
                break
        return responses

    def extract_translation(self, text: str) -> Translation:
        terms = self.extract_terms(text)
        examples_from , examples_to = self.extract_examples(text)
        return Translation(terms, examples_from, examples_to)

    @classmethod
    def extract_examples(cls, content):
        example_soup = BeautifulSoup(content, 'html.parser', parse_only=cls.example_filter)
        src_elements = example_soup.find_all("div", class_=re.compile("src (ltr|rtl)"))
        src_texts = [example.find("span", class_="text").text.strip() for example in src_elements]
        trg_elements = example_soup.find_all("div", class_=re.compile("trg (ltr|rtl)"))
        to_texts = [example.find("span", class_="text").text.strip() for example in trg_elements]
        return src_texts, to_texts

    @classmethod
    def extract_terms(cls, text):
        term_soup = BeautifulSoup(text, 'html.parser', parse_only=cls.translations_filter)
        term_elements = term_soup.find_all("span", class_='display-term')
        return [term.text for term in term_elements]
