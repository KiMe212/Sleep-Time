import random
import time

from tqdm import tqdm

from app.config import DEFAULT_CONFIG
from app.servis import *

data = dict()

data['max_number'] = DEFAULT_CONFIG.get('max_number')
data['max_number'] = env_max_number
data['max_number'] = config_file['CONFIG_FILE'].get('max_number')
data['max_number'] = args.min_number

data['min_number'] = DEFAULT_CONFIG.get('min_number')
data['min_number'] = env_min_number
data['min_number'] = config_file['CONFIG_FILE'].get('min_number')
data['min_number'] = args.min_number

data['sleep_time'] = DEFAULT_CONFIG.get('max_number')
data['sleep_time'] = env_min_number
data['sleep_time'] = config_file['CONFIG_FILE'].get('sleep_time')
data['sleep_time'] = args.sleep_time

sleep_time = data['sleep_time']
random_numbers = random.randrange(data['min_number'], data['max_number'])


def progress(times: int, number: int):
    for _ in tqdm(range(number)):
        time.sleep(times)
        pass

print(progress())
