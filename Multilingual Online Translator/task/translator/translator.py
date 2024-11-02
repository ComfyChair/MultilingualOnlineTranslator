from requester import Requester
from translation import Translation
from language import Language

class Translator:

    def __init__(self, from_lang, to_lang):
        self.from_lang = from_lang
        self.to_lang = to_lang
        self.requester = Requester(from_lang, to_lang)

    def translate(self, word: str):
        translation = self.requester.get_translations(word)
        self.print_translations(translation)
        self.print_examples(translation)


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


if __name__ == '__main__':
    target_lang = input('Type "en" if you want to translate from French into English,'
                   ' or "fr" if you want to translate from English into French:\n')
    if target_lang == 'en':
        translator = Translator(from_lang=Language("fr"), to_lang=Language("en"))
    elif target_lang == 'fr':
        translator = Translator(from_lang=Language("en"), to_lang=Language("fr"))
    else:
        translator = None
        print(f"Sorry, {target_lang} is not (yet) supported.")
    word = input("Type the word you want to translate:\n")
    print(f'You chose "{target_lang}" as a language to translate "{word}".')
    if translator:
        translator.translate(word)
