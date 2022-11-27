"""
The module with testing functions
"""
from random import randint
import copy
import json
import random
import pytest
from faker import Faker
import mock
from parse_json import parse_json, keyword_callback


class TestParseFunction:

    def test_identical_and_uniq_fields_and_keys(self, data_generator):
        """
        Function tests the case when keywords match the words in the json_str values
        and required_fields match json_str keys completely

        :param data_generator: pytest fixture, which generates json_str, required_fields, keywords
        """
        with mock.patch('parse_json.keyword_callback') as mock_method:
            json_dict, fields, keywords = data_generator
            parse_json(json.dumps(json_dict), mock_method, fields, keywords)
            assert len(keywords) == mock_method.call_count

    def test_repetitions(self, data_generator):
        """
        The function tests the case when all words in keywords are contained in json_str and some
        are contained multiple times. required_fields == keys in json_str
        :param data_generator: pytest fixture, which generates json_str, required_fields, keywords
        :return:
        """
        with mock.patch('parse_json.keyword_callback') as mock_method:
            json_dict, fields, keywords = data_generator
            rep_len = randint(1, len(keywords) - 1)
            list_for_rep = keywords[:rep_len]
            for word in list_for_rep:
                json_dict[random.choice(fields)] += ' ' + word
            parse_json(json.dumps(json_dict), mock_method, fields, keywords)
            assert len(keywords) + rep_len == mock_method.call_count

    def test_random_fields_and_keys(self, data_generator):
        """
        The function test the case, when required fields and fields of json_str don't match
        and values of json_str contain more words than keywords
        :param data_generator: pytest fixture, which generates json_str, required_fields, keywords
        """
        with mock.patch('parse_json.keyword_callback') as mock_method:
            json_dict, fields, keywords = data_generator
            numb_of_add_fields, numb_of_add_keyw = randint(5, 15), randint(5, 15)
            add_fields = list(set((Faker().unique.word() for _ in range(numb_of_add_fields)))
                              - set(fields))
            add_keyw = list(set((Faker().unique.first_name() for _ in range(numb_of_add_keyw)))
                            - set(keywords))
            numb_of_words_for_old_f = randint(1, len(add_keyw) - 1)
            numb_of_words_for_new_f = len(add_keyw) - numb_of_words_for_old_f
            words_for_old_fields = add_keyw[:numb_of_words_for_old_f]
            words_for_new_fields = add_keyw[numb_of_words_for_old_f:]
            for word in words_for_old_fields:
                json_dict[random.choice(fields)] += ' ' + word
            pos = 0
            for field in add_fields:
                if numb_of_words_for_new_f > 1:
                    word_numb = randint(1, numb_of_words_for_new_f)
                    json_dict[field] = ' '.join(words_for_new_fields[pos:word_numb + pos])
                    pos += word_numb
                    numb_of_words_for_new_f -= word_numb
                else:
                    print(words_for_new_fields, numb_of_words_for_new_f)
                    json_dict[field] = words_for_new_fields[len(words_for_new_fields) - 1]
                if numb_of_words_for_new_f == 0: break
            answer = parse_json(json.dumps(json_dict), mock_method, fields, keywords)
            assert len(keywords) == mock_method.call_count
            assert set(answer) == set(keywords)

    def test_add_random_keywords(self, data_generator):
        """
        The function tests the case when keywords have additional words
        :param data_generator: pytest fixture, which generates json_str, required_fields, keywords

        """
        with mock.patch('parse_json.keyword_callback') as mock_method:
            json_dict, fields, keywords = data_generator
            exc_answer = copy.copy(keywords)
            new_keywords = [Faker().unique.first_name() for _ in range(randint(5, 15))]
            keywords.extend(new_keywords)
            answer = parse_json(json.dumps(json_dict), mock_method, fields, keywords)
            assert len(exc_answer) == mock_method.call_count
            assert set(exc_answer) == set(answer)

    def test_none_keywords(self, data_generator):
        with mock.patch('parse_json.keyword_callback') as mock_method:
            json_dict, fields, keywords = data_generator
            assert mock_method.call_count == 0
            assert parse_json(json.dumps(json_dict), mock_method, fields) == []

    def test_run_without_word_handler(self, data_generator):
        json_dict, fields, keywords = data_generator
        with pytest.raises(TypeError):
            parse_json(json_str=json.dumps(json_dict), keywords=keywords, required_fields=fields)


class TestKeywordCallback:

    @pytest.mark.parametrize('input_word, expected_flag', [(Faker().word(), False),
                                                      (Faker().random_uppercase_letter() +
                                                       Faker().word(), True),
                                                      (Faker().random_uppercase_letter()*7, False),
                                                      (str(Faker().random.randint(1, 1000)), False),
                                                      (Faker().random_uppercase_letter() + Faker().word() +
                                                       str(Faker().random.randint(1, 1000)), False),
                                                      (Faker().random_element(elements=('<', '>', '$', '%', '#', '*', '@', '!')), False)
                                                      ])
    def test_keyword_callback(self, input_word, expected_flag):
        """
        The function tests the handler function with various string format types.
        :param input_word:The word for testing in handler function
        :param expected: True or False
        """
        expected_word = copy.copy(input_word)
        if expected_flag:
            expected_word = expected_word.capitalize()
        keyword_callback(input_word)
        assert input_word == expected_word
