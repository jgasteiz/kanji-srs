import csv
import os.path
import random
from pathlib import Path


def get_random_kanji() -> dict:
    csv_path = os.path.join(Path(__file__).resolve().parent, "csv/n5.csv")
    with open(csv_path) as f:
        reader = csv.DictReader(f)
        return random.choice([row for row in reader])
