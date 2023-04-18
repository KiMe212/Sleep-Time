import argparse
import json
import os

from dotenv import load_dotenv

# Берется JSON файл
try:
    with open(
        "D:/Python/PYTHON_PROJECTS/pythonProjectefromVlad/time_sleeping.json"
    ) as file:
        config_file = json.loads(file.read())
except FileNotFoundError:
    config_file = None

# Ввод данных через терминал
parser = argparse.ArgumentParser()

parser.add_argument("-min_number", type=int, action="store")
parser.add_argument("-max_number", type=int, action="store")
parser.add_argument("-sleep_time", type=int, action="store")
args = parser.parse_args()

# Данные из переменного окружения
load_dotenv()
env_sleep_time = os.getenv("sleep_time")
env_max_number = os.getenv("max_number")
env_min_number = os.getenv("min_number")
