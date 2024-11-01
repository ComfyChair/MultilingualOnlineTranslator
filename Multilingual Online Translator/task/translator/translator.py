import itertools

from requester import Requester

choose_lang_str = ('Type "en" if you want to translate from French into English,'
                   ' or "fr" if you want to translate from English into French:\n')



def main():
    from_lang, to_lang = get_language_choice()
    requester = Requester(from_lang, to_lang)
    word = input("Type the word you want to translate:\n")
    print(f'You chose "{to_lang}" as a language to translate "{word}".')
    translations, examples_from, examples_to = requester.get_translations(word)
    print("Translations")
    print(translations)
    examples_interleaved = list(itertools.chain(*zip(examples_from, examples_to)))
    print(examples_interleaved)


def get_language_choice() -> tuple[str, str]:
    target_lang = input(choose_lang_str)
    if target_lang == "en":
        from_lang = "fr"
    else:
        from_lang = "en"
    return from_lang, target_lang


if __name__ == '__main__':
    main()
