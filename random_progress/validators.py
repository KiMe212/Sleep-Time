from random_progress.schemas import AppConfig


def validate_config(config: AppConfig):
    _validate_numbers_non_negative(config)
    _validate_numbers(config)


def validate_data_types(config: dict):
    def _validate_none(config_dict: dict):
        dict_filter_none = dict()
        for k, v in config_dict.items():
            if v is not None:
                dict_filter_none[k] = v
        return dict_filter_none

    def _validate_type(start_dict: dict):
        final_dict = dict()
        for k, v in start_dict.items():
            try:
                final_dict[k] = float(v)
            except ValueError:
                raise ValueError("argument should be float")
        return final_dict

    return _validate_type(_validate_none(config))


def _validate_numbers_non_negative(app: AppConfig):
    for k, v in app.__dict__.items():
        if v < 0:
            raise TypeError("you write negative number")


def _validate_numbers(config: AppConfig):
    if config.min_number > config.max_number:
        raise TypeError("min number more max number")
