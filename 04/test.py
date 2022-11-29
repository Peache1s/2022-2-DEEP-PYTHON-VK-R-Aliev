import random
import string
import pytest
from faker import Faker
from meta import CustomClass
from descriptor import Data


class TestMeta:
    def test_add_custom_for_methods_and_cls_attr(self):
        inst = CustomClass()
        assert inst.custom_public == 50
        assert inst._custom_protected == 100
        assert inst._custom_CustomClass__private == 150
        assert inst.custom_line() == 100
        assert CustomClass().custom_public == 50
        assert CustomClass()._custom_protected == 100
        assert CustomClass()._custom_CustomClass__private == 150
        with pytest.raises(AttributeError):
            assert inst.public
            assert inst._protected
            assert inst._custom_CustomClass__private
            assert inst.line()
            assert CustomClass().val
            assert CustomClass()._protected
            assert CustomClass()._custom_CustomClass__private

    @pytest.mark.parametrize('method', ['__str__',
                                        '__init__',
                                        '__new__',
                                        ])
    def test_access_to_magic_methods(self, method):
        assert hasattr(CustomClass(), method)
        assert not hasattr(CustomClass(), 'custom_' + method)

    def test_instance_attr(self):
        inst = CustomClass()
        assert inst.custom_val == 99
        assert inst._custom_val == 100
        assert inst._custom_CustomClass__val == 101
        with pytest.raises(AttributeError):
            assert inst.val
            assert inst._val
            assert inst._CustomClass__val

    def test_str(self):
        inst = CustomClass()
        assert str(inst) == "Custom_by_metaclass"

    def test_added_later_attr(self):
        inst = CustomClass()
        inst.dynamic = "added later"
        assert inst.custom_dynamic == "added later"
        with pytest.raises(AttributeError):
            inst.dynamic


class TestDescriptor:

    @pytest.mark.parametrize('value', [5, 0, -5
                                       ])
    def test_right_case_integer(self, value):
        inst = Data()
        inst.num = value
        assert inst.num == value

    @pytest.mark.parametrize('value',
                             [5.33, 'some_text', {5: 5},
                              (5, 5), [5, 5], {5, 6}
                              ])
    def test_wrong_case_integer(self, value):
        with pytest.raises(ValueError):
            inst = Data()
            inst.num = value

    @pytest.mark.parametrize('value', ['', 'some_text'])
    def test_right_case_string(self, value):
        inst = Data()
        inst.name = value
        assert inst.name == value

    @pytest.mark.parametrize('value',
                             [5.33, 5, {5: 5}, (5, 5), [5, 5], {5, 6}
                              ])
    def test_wrong_case_string(self, value):
        with pytest.raises(ValueError):
            inst = Data()
            inst.name = value

    def test_right_case_positive_integer(self):
        inst = Data()
        value = 5
        inst.num = value
        assert inst.num == value

    @pytest.mark.parametrize('value',
                             [5.33, 'some_text', {5: 5}, (5, 5), [5, 5], {5, 6}, 0, -5
                              ])
    def test_wrong_case_positive_integer(self, value):
        with pytest.raises(ValueError):
            inst = Data()
            inst.price = value

    def test_another_values_in_diff_inst(self):
        price_obj_1, num_obj_1, name_obj_1 = Data(), Data(), Data()
        price_obj_2, num_obj_2, name_obj_2 = Data(), Data(), Data()
        price_obj_1.price, num_obj_1.num, name_obj_1.name = \
            5, 6, 'some_text'
        price_obj_2.price, num_obj_2.num, name_obj_2.name = \
            7, 8, 'another_text'
        assert price_obj_1.price != price_obj_2.price
        assert num_obj_1.num != num_obj_2.num
        assert name_obj_1.name != name_obj_2.name


class TestMetaWithParametrizeEval:

    @pytest.mark.parametrize('attr_or_method,old_attr_or_method ,expected',
                             [('custom_public', 'public', 50),
                              ('_custom_protected', '_protected', 100),
                              ('_custom_CustomClass__private',
                               '_CustomClass__private', 150),
                              ('custom_line()', 'line()', 100)])
    def test_add_custom_for_methods_and_cls_attr(self,
                                                 attr_or_method,
                                                 old_attr_or_method, expected):
        code_eval = compile(f'CustomClass().{attr_or_method}',
                            filename='test', mode='eval')
        res = eval(code_eval)
        assert res == expected
        with pytest.raises(AttributeError):
            code_eval = compile(f'CustomClass().{old_attr_or_method}',
                                filename='test', mode='eval')
            eval(code_eval)

    @pytest.mark.parametrize('inst_attr, old_inst_attr, expected',
                             [('custom_val', 'val', 99),
                              ('_custom_val', '_val', 100),
                              ('_custom_CustomClass__val',
                               '_CustomClass__val', 101)
                              ])
    def test_instance_attr(self, inst_attr, old_inst_attr, expected):

        code_eval = compile(f'CustomClass().{inst_attr}',
                            filename='test', mode='eval')
        res = eval(code_eval)
        assert res == expected
        with pytest.raises(AttributeError):
            code_eval = compile(f'CustomClass().{old_inst_attr}',
                                filename='test', mode='eval')
            eval(code_eval)

    def test_added_later_attribute(self):
        new_attr = ''.join(random.choice(string.ascii_lowercase)
                           for _ in range(10))
        new_value = ''.join(random.choice(string.ascii_lowercase)
                            for _ in range(10))
        inst = CustomClass()
        inst.new_attr = new_value
        new_custom_attr = 'custom_' + new_attr
        try:
            code_exec = compile(f'inst.{new_attr} = new_value'
                                f'\ninst.{new_custom_attr}==new_value'
                                f'\n', filename='test',
                                mode='exec')
            exec(code_exec)
            assert True
        except AttributeError:
            assert False

        with pytest.raises(AttributeError):
            code_exec = compile(f'inst.{new_attr}==new_value\n',
                                filename='test',
                                mode='exec')
            exec(code_exec)


class TestDescriptorWithRandomData:
    rand_string = Faker().word()

    @pytest.mark.parametrize('value', [Faker().pyint(),
                                       0,
                                       -Faker().pyint(),
                                       ])
    def test_right_case_integer(self, value):
        inst = Data()
        inst.num = value
        assert inst.num == value

    @pytest.mark.parametrize('value',
                             [Faker().pyfloat(),
                              Faker().word(),
                              {Faker().pyint(): Faker().pyint()},
                              (Faker().pyint(), Faker().pyint()),
                              [Faker().pyint(), Faker().pyint()],
                              {Faker().pyint(), Faker().pyint()}
                              ])
    def test_wrong_case_integer(self, value):
        with pytest.raises(ValueError):
            inst = Data()
            inst.num = value

    @pytest.mark.parametrize('value', ['', rand_string])
    def test_right_case_string(self, value):
        inst = Data()
        inst.name = value
        assert inst.name == value

    @pytest.mark.parametrize('value',
                             [Faker().pyfloat(),
                              Faker().pyint(),
                              {Faker().pyint(): Faker().pyint()},
                              (Faker().pyint(), Faker().pyint()),
                              [Faker().pyint(), Faker().pyint()],
                              {Faker().pyint(), Faker().pyint()}
                              ])
    def test_wrong_case_string(self, value):
        with pytest.raises(ValueError):
            inst = Data()
            inst.name = value

    def test_right_case_positive_integer(self):
        inst = Data()
        value = Faker().pyint()
        inst.num = value
        assert inst.num == value

    @pytest.mark.parametrize('value',
                             [Faker().pyfloat(),
                              Faker().word(),
                              {Faker().pyint(): Faker().pyint()},
                              (Faker().pyint(), Faker().pyint()),
                              [Faker().pyint(), Faker().pyint()],
                              {Faker().pyint(), Faker().pyint()},
                              0,
                              -Faker().pyint()
                              ])
    def test_wrong_case_positive_integer(self, value):
        with pytest.raises(ValueError):
            inst = Data()
            inst.price = value

    def test_another_values_in_diff_inst(self):
        price_obj_1, num_obj_1, name_obj_1 = Data(), Data(), Data()
        price_obj_2, num_obj_2, name_obj_2 = Data(), Data(), Data()
        price_obj_1.price, num_obj_1.num, name_obj_1.name = \
            Faker().pyint(), Faker().random.randint(-1000, 1000), \
            Faker().word()
        price_obj_2.price, num_obj_2.num, name_obj_2.name = \
            Faker().pyint(), Faker().random.randint(-1000, 1000), \
            Faker().word()
        assert price_obj_1.price != price_obj_2.price
        assert num_obj_1.num != num_obj_2.num
        assert name_obj_1.name != name_obj_2.name
