from unittest import TestCase

from random_progress.schemas import AppConfig
from random_progress.validators import validate_none, validate_data_types, \
    _validate_numbers_non_negative, _validate_numbers


def test_validate_data_types():
    test_dict = {
        "max_number": "200",
        "min_number": 2000,
        "sleep_time": 0.2
    }
    assert validate_data_types(test_dict) == {
        "max_number": 200,
        "min_number": 2000,
        "sleep_time": 0.2
    }


class DataTypes(TestCase):

    def test_validate_data_types(self):
        test_dict = {
            "max_number": "df",
            "min_number": 2000,
            "sleep_time": 0.2
        }
        with self.assertRaises(ValueError):
            validate_data_types(test_dict)


def test_validate_none():
    test_dict = {
        "max_number": None,
        "min_number": 2000,
        "sleep_time": 0.2
    }
    assert validate_none(test_dict) == {
        "min_number": 2000,
        "sleep_time": 0.2
    }


class TestValidateConfig(TestCase):

    def test_validate_numbers_non_negative(self):
        test_app = AppConfig(200, 1000, -0.2)
        with self.assertRaises(TypeError):
            _validate_numbers_non_negative(test_app)

    def test_validate_numbers(self):
        test_app = AppConfig(200, 100, 0.2)
        with self.assertRaises(TypeError):
            _validate_numbers(test_app)
