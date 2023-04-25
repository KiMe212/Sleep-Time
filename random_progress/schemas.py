from dataclasses import dataclass


@dataclass()
class AppConfig:
    min_number: int
    max_number: int
    sleep_time: int
