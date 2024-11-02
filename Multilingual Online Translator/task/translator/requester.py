import requests
from bs4 import BeautifulSoup, SoupStrainer

from language import Language
from translation import Translation


class Requester:
    headers = {'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36 Chrome/93.0.4577.82 Safari/537.36'}
    base_url = 'https://context.reverso.net/translation'
    translations_filter = SoupStrainer(id="translations-content")
    example_from_filter = SoupStrainer(class_="src ltr")
    example_to_filter = SoupStrainer(class_="trg ltr")

    def __init__(self, from_lang: Language, to_lang: Language):
        self.from_lang = from_lang
        self.lang_str = f"/{from_lang.name}-{to_lang.name}"

    def get_translations(self, word) -> Translation:
        url = self.base_url + self.lang_str + f'/{word}'
        response = requests.get(url, headers=self.headers)
        while not response.ok:
            print(f"Trying to connect to {url}, status={response.status_code}...")
            response = requests.get(url, headers=self.headers)
        print(f"{response.status_code} OK")
        return self.extract_translation(response.text)

    def extract_translation(self, text: str) -> Translation:
        terms = self.extract_translations(text)
        examples_from = self.extract_src_examples(text)
        examples_to = self.extract_trg_examples(text)
        if self.from_lang == Language.english:
            translation = Translation(terms, examples_from, examples_to)
        else:
            translation = Translation(terms, examples_to, examples_from)
        return translation

    @classmethod
    def extract_src_examples(cls, text):
        example_soup_from = BeautifulSoup(text, 'html.parser', parse_only=cls.example_from_filter)
        from_elements = example_soup_from.find_all("span", class_="text")
        examples_from = [example.text.strip() for example in from_elements]
        return examples_from

    @classmethod
    def extract_trg_examples(cls, text):
        example_soup_to = BeautifulSoup(text, 'html.parser', parse_only=cls.example_to_filter)
        to_elements = example_soup_to.find_all("span", class_="text")
        examples_to = [example.text.strip() for example in to_elements]
        return examples_to

    @classmethod
    def extract_translations(cls, text):
        translation_soup = BeautifulSoup(text, 'html.parser', parse_only=cls.translations_filter)
        term_elements = translation_soup.find_all("span", class_='display-term')
        return [term.text for term in term_elements]
