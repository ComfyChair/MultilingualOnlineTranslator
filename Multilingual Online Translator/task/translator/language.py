# language module
from enum import Enum


class Language(Enum):
    english = "en"
    french = "fr"
    spanish = "es"

    def capitalized(self):
        return self.name.capitalize()