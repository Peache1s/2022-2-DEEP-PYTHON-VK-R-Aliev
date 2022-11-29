import re


def customize_word(word):
    start_lst = ['custom', '_custom', '__custom']
    check_lst = [word.startswith(start_lst[i]) for i in range(len(start_lst))]

    if not re.fullmatch('__[a-z]+__', word) and True not in check_lst:
        if word.startswith('__'):
            return '__custom_' + word[2:]
        if word.startswith('_'):
            return '_custom_' + word[1:]
        return 'custom_' + word
    return word


class CustomMeta(type):

    @staticmethod
    def new_set_attr(self, name, val):
        object.__setattr__(self, customize_word(name), val)

    def __new__(mcs, name, bases, class_dict, **kwargs):
        new_class_dict = {}
        for attr_name, value in class_dict.items():
            new_class_dict[customize_word(attr_name)] = value

        new_class_dict['__setattr__'] = mcs.new_set_attr
        return super().__new__(mcs, name, bases, new_class_dict, **kwargs)


class CustomClass(metaclass=CustomMeta):

    public = 50
    _protected = 100
    __private = 150

    def __init__(self, val1=99, val2=100, val3=101):
        self.val = val1
        self._val = val2
        self.__val = val3

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"
