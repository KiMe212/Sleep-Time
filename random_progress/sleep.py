import argparse
import json
import random

from dotenv import dotenv_values

from random_progress.config import DEFAULT_CONFIG
from random_progress.schemas import Item
from random_progress.services import filter_of_none

# write on terminal
parser = argparse.ArgumentParser()
parser.add_argument("-min_number", type=int, action="store")
parser.add_argument("-max_number", type=int, action="store")
parser.add_argument("-sleep_time", type=int, action="store")
args = parser.parse_args()
argses = {
    "min_number": args.min_number,
    "max_number": args.max_number,
    "sleep_time": args.sleep_time,
}
dict_args = filter_of_none(argses)

# read JSON file
try:
    with open(
        "D:/Python/PYTHON_PROJECTS/pythonProjectefromVlad/time_sleeping.json"
    ) as file:
        config_file = json.loads(file.read())
except FileNotFoundError:
    config_file = None
dict_json_file = filter_of_none(config_file)

# env environment
env_config = dotenv_values()
dict_env = filter_of_none(env_config)

# default
dict_default = dict(DEFAULT_CONFIG)

item = Item(**{**dict_default, **dict_env, **dict_json_file, **dict_args})
random_numbers = random.randrange(item.min_number, item.max_number)
