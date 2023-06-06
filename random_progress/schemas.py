from dataclasses import dataclass


@dataclass()
class AppConfig:
    min_number: float
    max_number: float
    sleep_time: float
