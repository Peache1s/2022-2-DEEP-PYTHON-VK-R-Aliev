import os
import pytest
from faker import Faker


@pytest.fixture()
def file():
    file_name = Faker().word() + '.txt'
    line_list = []
    numbers_of_lines = Faker().random.randint(5, 10)
    words_from_every_line = []
    for _ in range(numbers_of_lines):
        line = " ".join([Faker().pystr(max_chars=5)
                         for _ in range(Faker().pyint(3, 7))])
        index = Faker().random.randint(0, len(line.split()) - 1)
        words_from_every_line.append(line.split()[index])
        line_list.append(line + '\n')

    words_from_one_line_lst = line_list[
        Faker().random.randint(0, numbers_of_lines - 1)]. \
        replace('\n', '').split()
    words_from_one_line = words_from_one_line_lst[
                          0:Faker().random.randint
                          (1, len(words_from_one_line_lst) - 1)]

    with open(file_name, 'w') as my_file:
        my_file.writelines(line_list)

    yield file_name, words_from_every_line, words_from_one_line
    os.remove(file_name)
