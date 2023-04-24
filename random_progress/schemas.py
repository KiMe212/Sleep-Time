from dataclasses import dataclass


@dataclass()
class Item:
    min_number: int
    max_number: int
    sleep_time: int
