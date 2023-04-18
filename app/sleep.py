import random
import time

from config import DEFAULT_CONFIG
from services import (args, config_file, env_max_number, env_min_number,
                      env_sleep_time)
from tqdm import tqdm

data = dict()

list_max_number = [
    DEFAULT_CONFIG.get("max_number"),
    env_max_number,
    config_file["CONFIG_FILE"].get("max_number"),
    args.min_number,
]

list_max = [i for i in list_max_number if i is not None]

list_min_number = [
    DEFAULT_CONFIG.get("min_number"),
    env_min_number,
    config_file["CONFIG_FILE"].get("min_number"),
    args.min_number,
]

list_min = [i for i in list_min_number if i is not None]

list_sleep_time = [
    DEFAULT_CONFIG.get("sleep_time"),
    env_sleep_time,
    config_file["CONFIG_FILE"].get("sleep_time"),
    args.sleep_time,
]

list_sleep = [i for i in list_sleep_time if i is not None]

random_numbers = random.randrange(list_min[-1], list_max[-1])


def progress(times: int, number: int):
    for _ in tqdm(range(number)):
        time.sleep(times)
        pass


print(progress(times=list_sleep[-1], number=random_numbers))
