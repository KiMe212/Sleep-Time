from time import sleep

from tqdm import tqdm


def parsing(lst: list):
    pars_dict = dict()
    for i in lst:
        pars_dict.update(**i)
    return pars_dict


def progress(time: int | float, number: int | float):
    for _ in tqdm(range(number)):
        sleep(time)
        pass
