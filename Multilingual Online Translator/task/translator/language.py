# language module

from enum import Enum


class Language(Enum):
    arabic = 1
    german = 2
    english = 3
    spanish = 4
    french = 5
    hebrew = 6
    japanese = 7
    dutch = 8
    polish = 9
    portuguese = 10
    romanian = 11
    russian = 12
    turkish = 13

    @classmethod
    def enumerate(cls):
        return "\n".join([f"{lang.value}. {lang.capitalized()}" for lang in cls])

    def capitalized(self):
        return self.name.capitalize()