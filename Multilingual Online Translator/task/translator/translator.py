# translator module

from requester import Requester
from translation import Translation
from language import Language


class Translator:

    def __init__(self, from_lang, to_lang):
        self.from_lang = from_lang
        self.to_lang = to_lang
        self.requester = Requester(from_lang, to_lang)

    def translate(self, query: str):
        translation = self.requester.get_translations(query)
        if translation:
            self.print_translations(translation)
            self.print_examples(translation)
        else:
            print(f'Translation not found: {query}')


    def print_examples(self, translation: Translation):
        print(f"\n{self.to_lang.capitalized()} Examples:")
        for idx, example in enumerate(translation.examples):
            if idx < 5:
                print(example[0])
                print(example[1])
                print()


    def print_translations(self, translation: Translation):
        print(f"\n{self.to_lang.capitalized()} Translations:")
        for idx, translation in enumerate(translation.translations):
            if idx < 5:
                print(translation)

WELCOME_MSG = f"Hello, welcome to the translator. Translator supports:\n{Language.enumerate()}"

if __name__ == '__main__':
    print(WELCOME_MSG)
    from_lang = Language(int(input('Type the number of your language:\n')))
    to_lang = Language(int(input('Type the number of language you want to translate to:\n')))
    translator = Translator(from_lang, to_lang)
    word = input("Type the word you want to translate:\n")
    print(f'You chose "{from_lang.capitalized()}" as a language to translate "{word}".')
    if translator:
        translator.translate(word)
