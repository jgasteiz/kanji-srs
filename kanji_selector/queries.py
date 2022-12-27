from typing import List

from . import data, models


class UnableToGetLevel(Exception):
    pass


class UnableToGetGroup(Exception):
    pass


def get_random_kanji() -> models.Kanji:
    return data.get_levels()[0].get_random_kanji()


def get_level_names() -> List[str]:
    return [level.name for level in data.get_levels()]


def get_level(level_name: str) -> models.Level:
    """
    Raises UnableToGetLevel if the given level name can't be found.
    """
    try:
        return [level for level in data.get_levels() if level.name == level_name][0]
    except IndexError:
        raise UnableToGetLevel(f"Level {level_name} not found.")


def get_level_group(level_name: str, group_index: int) -> models.Group | None:
    """
    Raises UnableToGetLevel if the given level name can't be found.
    Raises UnableToGetGroup if the given group index can't be found.
    """
    try:
        return get_level(level_name).get_group(group_index)
    except IndexError:
        raise UnableToGetGroup(f"Group {group_index} in level {level_name} not found.")
