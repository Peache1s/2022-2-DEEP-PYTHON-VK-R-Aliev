
import pytest
from meta import CustomClass
from faker import Faker


class TestMeta:

    @pytest.mark.parametrize('attr_or_method,old_attr_or_method ,expected', [('custom_public', 'public', 50),
                                                 ('_custom_protected', '_protected', 100),
                                                 ('_custom_CustomClass__private', '_CustomClass__private',150),
                                                 ('custom_line()', 'line()', 5000)])
    def test_custom_add_for_methods_and_cls_attr(self, attr_or_method, old_attr_or_method , expected):
        code_eval = compile(f'CustomClass().{attr_or_method}', filename='test', mode='eval')
        res = eval(code_eval)
        assert res == expected
        with pytest.raises(AttributeError):
            code_eval = compile(f'CustomClass().{old_attr_or_method}', filename='test', mode='eval')
            eval(code_eval)

    @pytest.mark.parametrize('method',          [('__str__'),
                                                 ('__init__'),
                                                 ('__new__'),
                                                 ('__getattrfromclass__')])
    def test_access_to_magic_methods(self, method):
        assert hasattr(CustomClass(), method)
        assert hasattr(CustomClass(), 'custom_' + method) == False


    @pytest.mark.parametrize('inst_attr, old_inst_attr, expected', [('custom_val', 'val', 99),
                                                                    ('_custom_val', '_val', 100),
                                                                    ('_custom_CustomClass__val', '_CustomClass__val', 101)
                                                                    ])
    def test_instance_attr(self, inst_attr,old_inst_attr, expected):
        code_eval = compile(f'CustomClass().{inst_attr}', filename='test', mode='eval')
        res = eval(code_eval)
        assert res == expected
        with pytest.raises(AttributeError):
            code_eval = compile(f'CustomClass().{old_inst_attr}', filename='test', mode='eval')
            eval(code_eval)

    def test_str(self):
        inst = CustomClass()
        assert str(inst) == "Custom_by_metaclass"

    # def test_added_later_attribute(self):
    #     new_attr = Faker().word()
    #     new_value = Faker().word()
    #     code_eval = compile(f'inst=CustomClass()\ninst.{new_attr} = {new_value}\nx = inst.{new_attr}', filename='test',
    #                         mode='exec')
    #
    #     res = exec(code_eval)
    #     print(res)
    #     assert res == new_value
