def check_none_and_type(start_dict: dict):
    final_dict = dict()
    for k, v in start_dict.items():
        if v is not None:
            try:
                final_dict[k] = float(v)
            except ValueError:
                raise ValueError("argument should be float")
    return final_dict


def validate_negative(app):
    for k, v in app.items():
        if v < 0:
            raise TypeError("you write negative number")
