"""
A module for pytest fixtures
"""
import pytest
from faker import Faker


@pytest.fixture()
def data_generator(number_of_keys_and_keywords = 10):
    fake = Faker()
    keys = [fake.unique.word() for _ in range(number_of_keys_and_keywords)]
    fields = keys
    keywords = [fake.unique.first_name() for _ in range(number_of_keys_and_keywords)]
    json_dict = {keys[i]: keywords[i] for i in range(number_of_keys_and_keywords)}
    return json_dict, fields, keywords
