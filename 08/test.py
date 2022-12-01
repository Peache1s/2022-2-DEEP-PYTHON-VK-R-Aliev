import sys
sys.argv = ['fetcher.py', '10', 'urls.txt']
from fetcher import Fetcher
import os


def test_file_with_one_url(event_loop):
    with open('test.txt', 'w') as file:
        file.write('https://www.hltv.org\n')
    fetcher = Fetcher(1, 'test.txt')
    event_loop.run_until_complete(fetcher.process())
    assert {1: 1} == fetcher.corr_dict
    assert fetcher.inv_url_counter == 0
    assert fetcher.timeout_counter == 0
    assert sum(fetcher.corr_dict.values()) == 1
    os.remove('test.txt')


def test_with_incorrect_url(event_loop):
    with open('test.txt', 'w') as file:
        file.write('www.hltvorg\n')
    fetcher = Fetcher(1, 'test.txt')
    event_loop.run_until_complete(fetcher.process())
    assert {1 : 0} == fetcher.corr_dict
    assert fetcher.inv_url_counter == 1
    assert fetcher.timeout_counter == 0
    assert sum(fetcher.corr_dict.values()) == 0
    os.remove('test.txt')


def test_with_couple_right_urls(event_loop):
    with open('test.txt', 'w') as file:
        file.write('https://www.hltv.org\n')
        file.write('https://www.apple.com\n')
        file.write('https://www.samsung.com\n')
    fetcher = Fetcher(1, 'test.txt')
    event_loop.run_until_complete(fetcher.process())
    assert {1: 3} == fetcher.corr_dict
    assert fetcher.inv_url_counter == 0
    assert fetcher.timeout_counter == 0
    assert sum(fetcher.corr_dict.values()) == 3
    os.remove('test.txt')


def test_with_correct_and_incorrect(event_loop):
    with open('test.txt', 'w') as file:
        file.write('https://www.hltv.org\n')
        file.write('https://www.apple.com\n')
        file.write('htwww.samsung\n')
    fetcher = Fetcher(1, 'test.txt')
    event_loop.run_until_complete(fetcher.process())
    assert {1: 2} == fetcher.corr_dict
    assert fetcher.inv_url_counter == 1
    assert fetcher.timeout_counter == 0
    assert sum(fetcher.corr_dict.values()) == 2
    os.remove('test.txt')

def test_with_correct_and_incorrect_urls_with_couple_workers(event_loop):
    with open('test.txt', 'w') as file:
        file.write('https://www.hltv.org\n')
        file.write('https://www.apple.com\n')
        file.write('htwww.samsung\n')
    fetcher = Fetcher(3, 'test.txt')
    event_loop.run_until_complete(fetcher.process())
    assert len(fetcher.corr_dict) == 3
    assert fetcher.inv_url_counter == 1
    assert fetcher.timeout_counter == 0
    assert sum(fetcher.corr_dict.values()) == 2
    os.remove('test.txt')


def test_with_correct_urls_with_couple_workers(event_loop):
    with open('test.txt', 'w') as file:
        file.write('https://www.hltv.org\n')
        file.write('https://www.apple.com\n')
        file.write('https://www.samsung.com\n')
    fetcher = Fetcher(3, 'test.txt')
    event_loop.run_until_complete(fetcher.process())
    assert len(fetcher.corr_dict) == 3
    assert fetcher.inv_url_counter == 0
    assert fetcher.timeout_counter == 0
    assert sum(fetcher.corr_dict.values()) == 3
    os.remove('test.txt')
