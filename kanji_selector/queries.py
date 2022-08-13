from typing import List

from . import data, models


def get_random_kanji() -> models.Kanji:
    level = data.get_levels()[0]
    return level.get_random_kanji()


def get_levels() -> List[models.Level]:
    return data.get_levels()
