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
        with open(f"{query}.txt", 'w') as file:
            for idx, translation in enumerate(translations):
                trans = self.get_translations(translation, self.trg_lang[idx])
                file.write(trans)
                ex = self.get_examples(translation, self.trg_lang[idx])
                file.write(ex)
                print(trans + ex, end="")
        file.close()

    def get_examples(self, translation: Translation, lang: Language) -> str:
        if not translation.isEmpty():
            result = f"{lang.capitalized()} Examples:"
            for idx, example in enumerate(translation.examples):
                if idx < self.no_prints:
                    result += f"\n{example[0]}\n{example[1]}\n"
            result += "\n\n"
        else:
            result = ""
        return result

    def get_translations(self, translation: Translation, lang: Language) -> str:
        if not translation.isEmpty():
            result = f"{lang.capitalized()} Translations:"
            for idx, translation in enumerate(translation.translations):
                if idx < self.no_prints:
                    result += f"\n{translation}"
            result += "\n\n"
        else:
            result = f"No translations found for target language {lang.capitalized()}\n"
        return result

WELCOME_MSG = f"Hello, welcome to the translator. Translator supports:\n{Language.enumerate()}"
FROM_LANG_MSG = 'Type the number of your language:\n'
TO_LANG_MSG = "Type the number of a language you want to translate to or '0' to translate to all languages:\n"


def get_src_lang() -> Language:
    while True:
        from_choice = input(FROM_LANG_MSG)
        try:
            from_int = int(from_choice)
            from_lang = Language(from_int)
            if from_lang is Language.all:
                raise ValueError
            else:
                return from_lang
        except ValueError:
            print(f"Invalid choice: {from_choice}")


def get_trg_lang():
    while True:
        to_choice = input(TO_LANG_MSG)
        try:
            to_int = int(to_choice)
            to_lang = Language(to_int)
            return to_lang
        except ValueError:
            print(f"Invalid choice: {to_choice}")

if __name__ == '__main__':
    print(WELCOME_MSG)
    src_lang = get_src_lang()
    trg_lang = get_trg_lang()
    translator = Translator(src_lang, trg_lang)
    word = input("Type the word you want to translate:\n")
    print(f'You chose "{src_lang.capitalized()}" as a language to translate "{word}".')
    if translator:
        translator.translate(word)
