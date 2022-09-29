"""
This module contains homework functions
"""

import json
import re
from copy import copy


def keyword_callback(word):
    """
    The function for word handling. A format is: the first character is uppercase, the rest are
    lowercase. Only english letters.

    :param word: word for handling
    :return: If word fits the format returns True, else False
    """
    if re.fullmatch('^[A-Z][a-z]+', word):
        return True
    return False


def parse_json(json_str: str, word_handler, required_fields=None, keywords=None):
    """
    Parse json_functions for parsing json string. This function takes json string,
    fields for handling, names for searching and name of function for word handling.

    :param json_str: json for parsing
    :param word_handler: function for handling words
    :param required_fields: list of keys in json_str to handle
    :param keywords: list of keys to search in json_str values
    :return: list of words, that fit the format of word_handler
    """
    json_dict = json.loads(json_str)
    if required_fields is None:
        required_fields = list(json_dict.keys())
    result_words = []

    for field in required_fields:
        if field in json_dict:
            words = json_dict[field].split()
            inters_words = list(set(words) & set(keywords))
            new_inters_words = copy(inters_words)

            for word in inters_words:
                count = words.count(word)
                if count > 1:
                    new_inters_words.extend([word] * (count - 1))

            for word in new_inters_words:
                if word_handler(word):
                    result_words.append(word)
    return result_words
