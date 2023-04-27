from random_progress.schemas import AppConfig


def validate_none(config: dict):
    dict_filter_none = {k: v for k, v in config.items() if v is not None}
    return dict_filter_none


def validate_config(config: AppConfig):
    _validate_numbers_non_negative(config)
    _validate_numbers(config)
    _validate_data_types(config)


def _validate_data_types(config: AppConfig):
    final_dict = dict()
    for k, v in config.__dict__.items():
        try:
            final_dict[k] = float(v)
        except ValueError:
            raise ValueError("argument should be float")
    return final_dict


def _validate_numbers_non_negative(app: AppConfig):
    for k, v in app.__dict__.items():
        if v < 0:
            raise TypeError("you write negative number")


def _validate_numbers(config: AppConfig):
    if config.min_number > config.max_number:
        raise TypeError("min number more max number")
