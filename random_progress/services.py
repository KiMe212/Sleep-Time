from time import sleep

from tqdm import tqdm


def filter_of_none(start_dict: dict):
    final_dict = {}
    for k, v in start_dict.items():
        if v is not None:
            final_dict.update({k: float(v)})
    return final_dict


def progress(time: int | float, number: int | float):
    for _ in tqdm(range(number)):
        sleep(time)
        pass
