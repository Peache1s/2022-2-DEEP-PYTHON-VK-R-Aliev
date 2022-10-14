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

    def __new__(mcs, name, bases, class_dict, **kwargs):
        new_class_dict = {}
        for attr_name, value in class_dict.items():
            new_class_dict[customize_word(attr_name)] = value
        return super().__new__(mcs, name, bases, new_class_dict, **kwargs)

    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        new_instance_dict = {}
        for attr, value in instance.__dict__.items():
            new_instance_dict[customize_word(attr)] = value
        instance.__dict__ = new_instance_dict
        return instance


class CustomClass(metaclass=CustomMeta):

    public = 50
    _protected = 100
    __private = 150

    def __init__(self, val1=99, val2=100, val3=101):
        self.val = val1
        self._val = val2
        self.__val = val3

    def __getattrfromclass__(self, attr):
        """
        This method was added to get attributes from class methods.
        I made a custom magic method so that it doesn't get renamed.
        """
        return super().__getattribute__(customize_word(attr))

    def __setattr__(self, key, value):
        new_key = customize_word(key)
        return super().__setattr__(new_key, value)

    def line(self):
        return self.__getattrfromclass__('public') * \
               self.__getattrfromclass__('_protected')

    def __str__(self):
        return "Custom_by_metaclass"
