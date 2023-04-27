import argparse
import json
from json import JSONDecodeError

from dotenv import dotenv_values

from random_progress.config import DEFAULT_CONFIG
from random_progress.schemas import AppConfig
from random_progress.validators import validate_none, validate_config


def get_config():
    config_data = _get_config_data()
    try:
        app_config = AppConfig(**config_data)
        validate_config(app_config)
        return app_config
    except TypeError as err:
        raise TypeError(err)


def _get_config_data():
    env_config = validate_none(_get_env_config())
    json_config = validate_none(_get_json_config())
    cli_config = validate_none(_get_cli_config())
    return {**DEFAULT_CONFIG, **env_config, **json_config, **cli_config}


def _get_cli_config():
    args_params = get_args()
    sleep_and_number_args = {
        "min_number": args_params.min_number,
        "max_number": args_params.max_number,
        "sleep_time": args_params.sleep_time,
    }
    return sleep_and_number_args


def _get_json_config():
    path_args = get_args()
    try:
        with open(path_args.path) as file:
            config_file = json.loads(file.read())
    except (FileNotFoundError, JSONDecodeError):
        config_file = {}
    return config_file


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-min_number", type=float, action="store", help="write min number")
    parser.add_argument("-max_number", type=float, action="store", help="write max number")
    parser.add_argument("-sleep_time", type=float, action="store", help="write sleep time  ")
    parser.add_argument("-path", type=str, default="time_sleeping.json", help="write path to the file JSON")

    args = parser.parse_args()
    return args


def _get_env_config():
    env_config = dict(dotenv_values())
    return env_config
