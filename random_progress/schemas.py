from dataclasses import dataclass


@dataclass()
class Item:
    min_number: int
    max_number: int
    sleep_time: int


def validate(d: dict):
    for k, v in d.items():
        if type(v) is not (int, float) or v < 0:
            print()
        return d
