# translator module
import argparse

from requester import Requester
from translation import Translation
from language import Language


class Translator:

    def __init__(self, src_lang: Language, trg_lang: Language):
        self.src_lang = src_lang
        if trg_lang is Language.all:
            self.trg_lang = Language.get_all()
            self.trg_lang.remove(src_lang)
            self.no_prints = 1
        else:
            self.trg_lang = [trg_lang,]
            self.no_prints = 5
        self.requester = Requester(src_lang, self.trg_lang)

    def translate(self, query: str):
        translations = self.requester.get_translations(query)
        with open(f"{query}.txt", 'w') as file:
            for idx, translation in enumerate(translations):
                trans = self.get_translations(translation, self.trg_lang[idx])
                file.write(trans)
                ex = self.get_examples(translation, self.trg_lang[idx])
                file.write(ex)
                print(trans + ex, end="")
        file.close()

    def get_examples(self, translation: Translation, lang: Language) -> str:
        result = f"{lang.capitalized()} Examples:"
        for idx, example in enumerate(translation.examples):
            if idx < self.no_prints:
                result += f"\n{example[0]}\n{example[1]}\n"
        result += "\n\n"
        return result

    def get_translations(self, translation: Translation, lang: Language) -> str:
        result = f"{lang.capitalized()} Translations:"
        for idx, translation in enumerate(translation.translations):
            if idx < self.no_prints:
                result += f"\n{translation}"
        result += "\n\n"
        return result

class CustomParser(argparse.ArgumentParser):
    def _check_value(self, action, value):
        # converted value must be one of the choices (if specified)
        if action.choices is not None and value not in action.choices:
            msg = f"Sorry, the program doesn't support {value}"
            raise argparse.ArgumentError(None, msg)
    def error(self, message):
        print(message)
        self.exit(1)

parser = CustomParser()
parser.add_argument("from_lang", choices=Language.names(), help="Source language")
parser.add_argument("to_lang", choices=["all", *Language.names()], help="Target language")
parser.add_argument("query", help="The word you want to translate")

if __name__ == '__main__':
    src_lang = Language[parser.parse_args().from_lang]
    trg_lang = Language[parser.parse_args().to_lang]
    translator = Translator(src_lang, trg_lang)
    word = parser.parse_args().query
    translator.translate(word)
