import csv
import os.path
from functools import lru_cache
from pathlib import Path
from typing import List

from . import models, settings


@lru_cache
def get_levels() -> List[models.Level]:
    kanji_levels = []
    for level_name in settings.LEVELS:
        csv_path = os.path.join(
            Path(__file__).resolve().parent, f"levels/{level_name}.csv"
        )
        with open(csv_path) as f:
            reader = csv.DictReader(f)
            csv_kanji = [_get_kanji_from_csv_row(row) for row in reader]
            kanji_levels.append(
                models.Level(
                    name=level_name,
                    groups=_get_groups(items=csv_kanji, group_size=10),
                )
            )
    return kanji_levels


def _get_kanji_from_csv_row(row: dict) -> models.Kanji:
    return models.Kanji(
        kanji=row["kanji"],
        on_yomi=row["on-yomi"],
        kun_yomi=row["kun-yomi"],
        meaning=row["meaning"],
        examples=row["examples"],
    )


def _get_groups(items: List[models.Kanji], group_size: int) -> List[models.Group]:
    groups = []
    group_index = 1
    for i in range(0, len(items), group_size):
        groups.append(models.Group(index=group_index, kanji_list=items[i : i + 10]))
        group_index += 1
    return groups
