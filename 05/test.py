import os
import pytest
from faker import Faker
from lru_cache import LRUCache
from filter_file import filter_file


class TestLRUCache:

    @pytest.mark.parametrize("limit, expected", [(0, 0),
                                                 (50, True)
                                                 ])
    def test_single_set(self, limit, expected):
        cache = LRUCache(limit)
        assert len(cache) == 0
        assert cache.set('key', 'value') == expected
        assert len(cache) == min(limit, 1)

    def test_get_singe(self):
        cache = LRUCache(3)
        cache.set('key1', 'val1')
        assert cache.get('key1') == 'val1'
        assert len(cache) == 1

    def test_get_non_existing(self):
        cache = LRUCache(3)
        assert cache.get('key1') is None

    def test_set_existing(self):
        cache = LRUCache(3)
        cache.set('key1', 'val1')
        assert not cache.set('key1', 'val2')
        assert cache.get('key1') == 'val2'
        assert len(cache) == 1

    def test_single_capacity(self):
        cache = LRUCache(1)
        assert cache.set('key1', 'val1')
        cache.set('key2', 'val2')
        assert cache.get('key1') is None
        assert cache.get('key2') == 'val2'

    def test_existing_and_get(self):
        cache = LRUCache(2)
        cache.set('key1', 'val1')
        cache.set('key2', 'val2')
        cache.set('key1', 'val4')
        cache.set('key3', 'val3')
        assert cache.get('key2') is None
        assert cache.get('key1') == 'val4'
        assert cache.get('key3') == 'val3'

    def test_shift_to_end_after_get(self):
        cache = LRUCache(3)
        cache.set('key1', 'val1')
        cache.set('key2', 'val2')
        cache.set('key3', 'val3')
        cache.get('key1')
        assert cache[2] == 'val1'

    def test_from_task(self):
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")
        assert cache.get("k3") is None  # None
        assert cache.get("k2") == 'val2'  # "val2"
        assert cache.get("k1") == 'val1'  # "val1"
        cache.set("k3", "val3")
        assert cache.get("k3") == 'val3'  # "val3"
        assert cache.get("k2") is None  # None
        assert cache.get("k1") == 'val1'  # "val1"


class TestLRUCacheWithRandomData:

    @pytest.mark.parametrize("limit, expected", [(0, 0),
                                                 (Faker().pyint(1, 100), True)
                                                 ])
    def test_single_set(self, limit, expected):
        cache = LRUCache(limit)
        assert len(cache) == 0
        assert cache.set(Faker().word(), Faker().word()) == expected
        assert len(cache) == min(limit, 1)

    def test_get_singe(self):
        cache = LRUCache(Faker().pyint(1, 100))
        key, value = Faker().word(), Faker().word()
        cache.set(key, value)
        assert cache.get(key) == value

    def test_get_non_existing(self):
        cache = LRUCache(Faker().pyint(1, 100))
        key = Faker().word()
        assert cache.get(key) is None

    def test_set_existing(self):
        cache = LRUCache(Faker().pyint(2, 100))
        key, value, new_value = Faker().word(), Faker().word(), Faker().word()
        cache.set(key, value)
        assert not cache.set(key, new_value)
        assert cache.get(key) == new_value
        assert len(cache) == 1

    def test_shift_to_end_after_get(self):
        limit = Faker().pyint(2, 20)
        cache = LRUCache(limit)
        check_index = Faker().random.randint(0, limit - 1)
        for i in range(limit):
            key, value = Faker().pystr(), Faker().pystr()
            cache.set(key, value)
            if i == check_index:
                check_key, check_value = key, value
        cache.get(check_key)
        assert cache[limit - 1] == check_value

    def test_shift_to_end_after_reset(self):
        limit = Faker().pyint(2, 20)
        cache = LRUCache(limit)
        check_index = Faker().random.randint(0, limit - 1)
        for i in range(limit):
            key, value = Faker().pystr(), Faker().pystr()
            cache.set(key, value)
            if i == check_index:
                check_key = key
        new_value = Faker().pystr()
        cache.set(check_key, new_value)
        assert cache[limit - 1] == new_value

    def test_set_more_limit(self):
        limit = Faker().pyint(2, 20)
        extra_set_numb = Faker().pyint(1, 4)
        cache = LRUCache(limit)
        removed_lst = []
        for i in range(limit + extra_set_numb):
            key, value = Faker().pystr(), Faker().pystr()
            if i <= extra_set_numb - 1:
                removed_lst.append(key)
            cache.set(key, value)
        get_list = [cache.get(key) for key in removed_lst]
        assert get_list == [None] * extra_set_numb
        assert len(cache) == limit


class TestFilterFile:

    def test_empty_file(self):
        file_name = Faker().word() + '.txt'
        with open(file_name, 'w+'):
            counter = 0
            for _ in filter_file(file_name, []):
                counter += 1
            assert counter == 0
        os.remove(file_name)

    def test_one_word_from_every_line(self, file):
        filename, words_from_every_line = (file[0], file[1])
        with open(filename, 'r'):
            counter = 0
            for _ in filter_file(filename, words_from_every_line):
                counter += 1
            assert counter == len(words_from_every_line)

    def test_one_word_from_every_line_and_word_from_one_line(self, file):
        filename, words_from_every_line, words_from_one_line, \
        number_of_lines = file
        with open(filename, 'r'):
            counter = 0
            words_from_every_line.extend(words_from_one_line)
            for _ in filter_file(filename, words_from_every_line):
                counter += 1
            assert counter == number_of_lines

    def test_part_of_words_with_adding_rnd_words(self, file):
        filename, words_from_every_line = (file[0], file[1])
        num_of_exist_word = Faker(). \
            random.randint(1, len(words_from_every_line))
        new_words = words_from_every_line[0:num_of_exist_word]
        new_words.extend([Faker().pystr() for _ in
                          range(Faker().random.randint(1, 5))])

        with open(filename, 'r'):
            counter = 0
            for _ in filter_file(filename, new_words):
                counter += 1
            assert counter == num_of_exist_word
