# language module

from enum import Enum
from typing import List, Type


class Language(Enum):
    all = 0
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

    def capitalized(self) -> str:
        return self.name.capitalize()

    @classmethod
    def enumerate(cls) -> str:
        return "\n".join([f"{lang.value}. {lang.capitalized()}"
                          for idx, lang in enumerate(cls) if idx > 0])

    @classmethod
    def get_all(cls):
        return [lang for idx, lang in enumerate(cls) if idx > 0]

