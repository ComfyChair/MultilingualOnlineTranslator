# translator module

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
        for idx, translation in enumerate(translations):
            self.print_translations(translation, self.trg_lang[idx])
            self.print_examples(translation, self.trg_lang[idx])

    def print_examples(self, translation: Translation, lang: Language):
        if not translation.isEmpty():
            print(f"\n{lang.capitalized()} Examples:")
            for idx, example in enumerate(translation.examples):
                if idx < self.no_prints:
                    print(example[0])
                    print(example[1])
                    print()

    def print_translations(self, translation: Translation, lang: Language):
        if not translation.isEmpty():
            print(f"\n{lang.capitalized()} Translations:")
            for idx, translation in enumerate(translation.translations):
                if idx < self.no_prints:
                    print(translation)
        else:
            print(f"\n No translations found for target language {lang.capitalized()}")

WELCOME_MSG = f"Hello, welcome to the translator. Translator supports:\n{Language.enumerate()}"
FROM_LANG_MSG = 'Type the number of your language:\n'
TO_LANG_MSG = "Type the number of a language you want to translate to or '0' to translate to all languages:\n"

if __name__ == '__main__':
    print(WELCOME_MSG)
    from_lang = Language(int(input(FROM_LANG_MSG)))
    to_lang = Language(int(input(TO_LANG_MSG)))
    translator = Translator(from_lang, to_lang)
    word = input("Type the word you want to translate:\n")
    print(f'You chose "{from_lang.capitalized()}" as a language to translate "{word}".')
    if translator:
        translator.translate(word)
