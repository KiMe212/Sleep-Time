import argparse
import json
import random
from json import JSONDecodeError

from dotenv import dotenv_values

from random_progress.config import DEFAULT_CONFIG
from random_progress.schemas import AppConfig
from random_progress.services import parsing
from random_progress.validators import check_none_and_type, validate_negative


def write_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("-min_number", type=float, action="store", help="write float")
    parser.add_argument("-max_number", type=float, action="store", help="write float")
    parser.add_argument("-sleep_time", type=float, action="store", help="write float")
    args = parser.parse_args()
    argses = {
        "min_number": args.min_number,
        "max_number": args.max_number,
        "sleep_time": args.sleep_time,
    }
    return argses


def read_config_file():
    # read JSON file
    try:
        with open(
            "D:/Python/PYTHON_PROJECTS/pythonProjectefromVlad/time_sleeping.json"
        ) as file:
            config_file = json.loads(file.read())
    except (FileNotFoundError, JSONDecodeError):
        config_file = {}
    return config_file


def read_env():
    # env environment
    env_config = dict(dotenv_values())
    return env_config


filtered_configs = list(
    map(
        check_none_and_type,
        [DEFAULT_CONFIG, read_env(), read_config_file(), write_cli()],
    )
)
try:
    app_config = AppConfig(**parsing(filtered_configs))
    validate_negative(app_config.__dict__)

    if app_config.min_number > app_config.max_number:
        raise TypeError("max_number should be more min_number")
except TypeError as err:
    raise TypeError(err)

random_numbers = random.randrange(app_config.min_number, app_config.max_number)
