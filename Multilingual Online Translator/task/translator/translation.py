# translation module

from dataclasses import dataclass
from typing import Tuple, List


@dataclass
class Translation:
    translations: List[str]
    examples: List[Tuple[str, str]]

    def __init__(self, terms: List[str], examples_from: List[str], examples_to: List[str]):
        self.translations = terms
        self.examples = list(zip(examples_from, examples_to))
