import random
from time import sleep

from tqdm import trange

from random_progress.services import get_config


def progress():
    config = get_config()
    random_number = random.randrange(config.min_number, config.max_number)
    for _ in trange(random_number):
        sleep(config.sleep_time)
