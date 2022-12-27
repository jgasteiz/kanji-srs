import random
from typing import List, Tuple

from pydantic import BaseModel


class Kanji(BaseModel):
    kanji: str
    on_yomi: str
    kun_yomi: str
    meaning: str
    examples: str


class Group(BaseModel):
    """
    Group of Kanji that belong to a specific level.
    """

    index: int
    kanji_list: List[Kanji]

    def get_random_kanji(self) -> Kanji:
        return random.choice(self.kanji_list)


class Level(BaseModel):
    """
    Level of Kanji, like N5, N4, N3, etc.
    """

    name: str
    groups: List[Group]

    def get_random_kanji(self) -> Kanji:
        return random.choice(self.groups).get_random_kanji()

    def get_group(self, group_index: int) -> Group:
        """
        Raises IndexError if a group for the given index can't be found.
        """
        return [_ for _ in self.groups if _.index == group_index][0]
