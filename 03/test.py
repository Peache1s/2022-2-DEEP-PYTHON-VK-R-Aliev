import copy
import pytest
from faker import Faker
from custom_list import CustomList


class TestCustomListAddSub:

    @pytest.mark.parametrize('data, exception', [(12, TypeError),
                                                 (True, TypeError),
                                                 (1.234, TypeError),
                                                 ])
    def test_wrong_type(self, data, exception):
        with pytest.raises(exception):
            CustomList(data)

    @pytest.mark.parametrize('first, second, expected', [([1, 2, 3], [2, 3, 4], [3, 5, 7]),
                                                         ([1, 2], [2, 3, 4], [3, 5, 4]),
                                                         ([1, 2, 3], [2, 3], [3, 5, 3])
                                                         ])
    def test_add_between_two_custom_lists(self, first, second, expected):
        first_clist, second_clist = CustomList(first), CustomList(second)
        copy_first, copy_second = copy.copy(first_clist), copy.copy(second_clist)
        res_clist = first_clist + second_clist
        assert copy_first == first_clist
        assert copy_second == second_clist
        assert res_clist == expected
        assert type(res_clist).__name__ == 'CustomList'

    @pytest.mark.parametrize('first, second, expected', [([1, 2, 3], [2, 3, 4], [-1, -1, -1]),
                                                         ([1, 2], [2, 3, 4], [-1, -1, 4]),
                                                         ([1, 2, 3], [2, 3], [-1, -1, 3])
                                                         ])
    def test_sub_between_two_custom_lists(self, first, second, expected):
        first_clist, second_clist = CustomList(first), CustomList(second)
        copy_first, copy_second = copy.copy(first_clist), copy.copy(second_clist)
        res_clist = first_clist - second_clist
        assert copy_first.elem_compare(first_clist)
        assert copy_second.elem_compare(second_clist)
        assert res_clist.elem_compare(expected)
        assert type(res_clist).__name__ == 'CustomList'

    @pytest.mark.parametrize('first, second, expected', [([1, 2, 3], [2, 3, 4], [3, 5, 7]),
                                                         ([1, 2], [2, 3, 4], [3, 5, 4]),
                                                         ([1, 2, 3], [2, 3], [3, 5, 3])
                                                         ])
    def test_add_one_list_one_clist(self, first, second, expected):
        first_clist = CustomList(first)
        copy_first, copy_second = copy.copy(first_clist), copy.copy(second)
        res_clist = first_clist + second
        assert second == copy_second
        assert copy_first.elem_compare(first_clist)
        assert type(res_clist).__name__ == 'CustomList'
        assert res_clist.elem_compare(expected)

    @pytest.mark.parametrize('first, second, expected', [([1, 2, 3], [2, 3, 4], [-1, -1, -1]),
                                                         ([1, 2], [2, 3, 4], [-1, -1, 4]),
                                                         ([1, 2, 3], [2, 3], [-1, -1, 3])
                                                         ])
    def test_sub_one_list_one_clist(self, first, second, expected):
        first_clist = CustomList(first)
        copy_first, copy_second = copy.copy(first_clist), copy.copy(second)
        res_clist = first_clist - second
        assert second == copy_second
        assert copy_first.elem_compare(first_clist)
        assert type(res_clist).__name__ == 'CustomList'
        assert res_clist.elem_compare(expected)

    @pytest.mark.parametrize('first, second, expected', [([1, 2, 3], [2, 3, 4], [3, 5, 7]),
                                                         ([1, 2], [2, 3, 4], [3, 5, 4]),
                                                         ([1, 2, 3], [2, 3], [3, 5, 3])
                                                         ])
    def test_iadd_two_custom_lists(self, first, second, expected):
        first_clist, second_clist = CustomList(first), CustomList(second)
        copy_second = copy.copy(second_clist)
        first_clist += second_clist
        assert copy_second.elem_compare(second_clist)
        assert type(first_clist).__name__ == 'CustomList'
        assert first_clist.elem_compare(expected)

    @pytest.mark.parametrize('first, second, expected', [([1, 2, 3], [2, 3, 4], [-1, -1, -1]),
                                                         ([1, 2], [2, 3, 4], [-1, -1, 4]),
                                                         ([1, 2, 3], [2, 3], [-1, -1, 3])
                                                         ])
    def test_isub_two_custom_lists(self, first, second, expected):
        first_clist, second_clist = CustomList(first), CustomList(second)
        copy_second = copy.copy(second_clist)
        first_clist -= second_clist
        assert copy_second.elem_compare(second_clist)
        assert type(first_clist).__name__ == 'CustomList'
        assert first_clist.elem_compare(expected)

    @pytest.mark.parametrize('first, second, expected', [([1, 2, 3], [2, 3, 4], [3, 5, 7]),
                                                         ([1, 2], [2, 3, 4], [3, 5, 4]),
                                                         ([1, 2, 3], [2, 3], [3, 5, 3])
                                                         ])
    def test_iadd_one_clist_one_list(self, first, second, expected):
        first_clist = CustomList(first)
        copy_second = copy.copy(second)
        first_clist += second
        assert copy_second == second
        assert type(first_clist).__name__ == 'CustomList'
        assert first_clist.elem_compare(expected)

    @pytest.mark.parametrize('first, second, expected', [([1, 2, 3], [2, 3, 4], [-1, -1, -1]),
                                                         ([1, 2], [2, 3, 4], [-1, -1, 4]),
                                                         ([1, 2, 3], [2, 3], [-1, -1, 3])
                                                         ])
    def test_isub_one_clist_one_list(self, first, second, expected):
        first_clist = CustomList(first)
        copy_second = copy.copy(second)
        first_clist -= second
        assert copy_second == second
        assert type(first_clist).__name__ == 'CustomList'
        assert first_clist.elem_compare(expected)

    @pytest.mark.parametrize('first, second, expected', [([1, 2, 3], [2, 3, 4], [3, 5, 7]),
                                                         ([1, 2], [2, 3, 4], [3, 5, 4]),
                                                         ([1, 2, 3], [2, 3], [3, 5, 3])
                                                         ])
    def test_radd_one(self, first, second, expected):
        copy_first = copy.copy(first)
        second_clist = CustomList(second)
        copy_second = copy.copy(CustomList(second))
        res_clist = first + second_clist
        assert type(res_clist).__name__ == 'CustomList'
        assert first == copy_first
        assert copy_second.elem_compare(second_clist)
        assert res_clist.elem_compare(expected)

    @pytest.mark.parametrize('first, second, expected', [([1, 2, 3], [2, 3, 4], [-1, -1, -1]),
                                                         ([1, 2], [2, 3, 4], [-1, -1, 4]),
                                                         ([1, 2, 3], [2, 3], [-1, -1, 3])
                                                         ])
    def test_rsub_one(self, first, second, expected):
        copy_first = copy.copy(first)
        second_clist = CustomList(second)
        copy_second = copy.copy(CustomList(second))
        res_clist = first - second_clist
        assert type(res_clist).__name__ == 'CustomList'
        assert first == copy_first
        assert copy_second.elem_compare(second_clist)
        assert res_clist.elem_compare(expected)


class TestCustomListAddSubWithRandomData:

    @staticmethod
    def expect_add(lst1, lst2):
        len_dif = len(lst1) - len(lst2)
        min_len = min(len(lst1), len(lst2))
        expect = [lst1[i] + lst2[i] for i in range(min_len)]
        expect.extend(lst1[min_len:]) if len_dif > 0 else expect.extend(lst2[min_len:])
        return expect

    @staticmethod
    def expect_sub(lst1, lst2):
        len_dif = len(lst1) - len(lst2)
        min_len = min(len(lst1), len(lst2))
        expect = [lst1[i] - lst2[i] for i in range(min_len)]
        expect.extend(lst1[min_len:]) if len_dif > 0 else expect.extend(lst2[min_len:])
        return expect

    @pytest.mark.parametrize('data', [([Faker().random.randint(1, 256) for _ in range(10)]),
                                      ((Faker().random.randint(1, 256) for _ in range(10))),
                                      (str(Faker().random.randint(10000, 100000))),
                                      ({Faker().random.randint(1, 256) for _ in range(10)}),
                                      ({Faker().random.randint(1, 256): Faker().word()
                                        for _ in range(10)}),
                                      ])
    def test_right_type(self, data):
        assert type(CustomList(data)).__name__ == 'CustomList'

    @pytest.mark.parametrize('first, second', [([Faker().random.randint(1, 256) for _ in range(10)],
                                                [Faker().random.randint(1, 256) for _ in range(10)]),
                                               ([Faker().random.randint(1, 256) for _ in range(10)],
                                                [Faker().random.randint(1, 256) for _ in
                                                 range(Faker().random.randint(11, 15))]),
                                               ([Faker().random.randint(1, 256) for _ in
                                                 range(Faker().random.randint(11, 15))],
                                                [Faker().random.randint(1, 256) for _ in range(10)])
                                               ])
    def test_add_between_two_custom_lists(self, first, second):
        first_clist, second_clist = CustomList(first), CustomList(second)
        copy_first, copy_second = copy.copy(first_clist), copy.copy(second_clist)
        res_clist = first_clist + second_clist
        assert copy_first.elem_compare(first_clist)
        assert copy_second.elem_compare(second_clist)
        assert res_clist.elem_compare(self.expect_add(first, second))

    @pytest.mark.parametrize('first, second', [([Faker().random.randint(1, 256) for _ in range(10)],
                                                [Faker().random.randint(1, 256) for _ in range(10)]),
                                               ([Faker().random.randint(1, 256) for _ in range(10)],
                                                [Faker().random.randint(1, 256) for _ in
                                                 range(Faker().random.randint(11, 15))]),
                                               ([Faker().random.randint(1, 256) for _ in
                                                 range(Faker().random.randint(11, 15))],
                                                [Faker().random.randint(1, 256) for _ in range(10)])
                                               ])
    def test_sub_between_two_custom_lists(self, first, second):
        first_clist, second_clist = CustomList(first), CustomList(second)
        copy_first, copy_second = copy.copy(first_clist), copy.copy(second_clist)
        res_clist = first_clist - second_clist
        assert copy_first.elem_compare(first_clist)
        assert copy_second.elem_compare(second_clist)
        assert res_clist.elem_compare(self.expect_sub(first, second))

    @pytest.mark.parametrize('first, second', [([Faker().random.randint(1, 256) for _ in range(10)],
                                                [Faker().random.randint(1, 256) for _ in range(10)]),
                                               ([Faker().random.randint(1, 256) for _ in range(10)],
                                                [Faker().random.randint(1, 256) for _ in
                                                 range(Faker().random.randint(11, 15))]),
                                               ([Faker().random.randint(1, 256) for _ in
                                                 range(Faker().random.randint(11, 15))],
                                                [Faker().random.randint(1, 256) for _ in range(10)])
                                               ])
    def test_add_one_list_one_clist(self, first, second):
        first_clist = CustomList(first)
        copy_first, copy_second = copy.copy(first_clist), copy.copy(second)
        res_clist = first_clist + second
        assert second == copy_second
        assert copy_first.elem_compare(first_clist)
        assert type(res_clist).__name__ == 'CustomList'
        assert res_clist.elem_compare(self.expect_add(first, second))

    @pytest.mark.parametrize('first, second', [([Faker().random.randint(1, 256) for _ in range(10)],
                                                [Faker().random.randint(1, 256) for _ in range(10)]),
                                               ([Faker().random.randint(1, 256) for _ in range(10)],
                                                [Faker().random.randint(1, 256) for _ in
                                                 range(Faker().random.randint(11, 15))]),
                                               ([Faker().random.randint(1, 256) for _ in
                                                 range(Faker().random.randint(11, 15))],
                                                [Faker().random.randint(1, 256) for _ in range(10)])
                                               ])
    def test_sub_one_list_one_clist(self, first, second):
        first_clist = CustomList(first)
        copy_first, copy_second = copy.copy(first_clist), copy.copy(second)
        res_clist = first_clist - second
        assert second == copy_second
        assert copy_first.elem_compare(first_clist)
        assert type(res_clist).__name__ == 'CustomList'
        assert res_clist.elem_compare(self.expect_sub(first, second))

    @pytest.mark.parametrize('first, second', [([Faker().random.randint(1, 256) for _ in range(10)],
                                                [Faker().random.randint(1, 256) for _ in range(10)]),
                                               ([Faker().random.randint(1, 256) for _ in range(10)],
                                                [Faker().random.randint(1, 256) for _ in
                                                 range(Faker().random.randint(11, 15))]),
                                               ([Faker().random.randint(1, 256) for _ in
                                                 range(Faker().random.randint(11, 15))],
                                                [Faker().random.randint(1, 256) for _ in range(10)])
                                               ])
    def test_iadd_two_custom_lists(self, first, second):
        first_clist, second_clist = CustomList(first), CustomList(second)
        copy_second = copy.copy(second_clist)
        first_clist += second_clist
        assert copy_second.elem_compare(second_clist)
        assert type(first_clist).__name__ == 'CustomList'
        assert first_clist.elem_compare(self.expect_add(first, second))

    @pytest.mark.parametrize('first, second', [([Faker().random.randint(1, 256) for _ in range(10)],
                                                [Faker().random.randint(1, 256) for _ in range(10)]),
                                               ([Faker().random.randint(1, 256) for _ in range(10)],
                                                [Faker().random.randint(1, 256) for _ in
                                                 range(Faker().random.randint(11, 15))]),
                                               ([Faker().random.randint(1, 256) for _ in
                                                 range(Faker().random.randint(11, 15))],
                                                [Faker().random.randint(1, 256) for _ in range(10)])
                                               ])
    def test_isub_two_custom_lists(self, first, second):
        first_clist, second_clist = CustomList(first), CustomList(second)
        copy_second = copy.copy(second_clist)
        first_clist -= second_clist
        assert copy_second.elem_compare(second_clist)
        assert type(first_clist).__name__ == 'CustomList'
        assert first_clist.elem_compare(self.expect_sub(first, second))

    @pytest.mark.parametrize('first, second', [([Faker().random.randint(1, 256) for _ in range(10)],
                                                [Faker().random.randint(1, 256) for _ in range(10)]),
                                               ([Faker().random.randint(1, 256) for _ in range(10)],
                                                [Faker().random.randint(1, 256) for _ in
                                                 range(Faker().random.randint(11, 15))]),
                                               ([Faker().random.randint(1, 256) for _ in
                                                 range(Faker().random.randint(11, 15))],
                                                [Faker().random.randint(1, 256) for _ in range(10)])
                                               ])
    def test_radd_one(self, first, second):
        copy_first = copy.copy(first)
        second_clist = CustomList(second)
        copy_second = copy.copy(CustomList(second))
        res_clist = first + second_clist
        assert type(res_clist).__name__ == 'CustomList'
        assert first == copy_first
        assert copy_second.elem_compare(second_clist)
        assert res_clist.elem_compare(self.expect_add(first, second))

    @pytest.mark.parametrize('first, second', [([Faker().random.randint(1, 256) for _ in range(10)],
                                                [Faker().random.randint(1, 256) for _ in range(10)]),
                                               ([Faker().random.randint(1, 256) for _ in range(10)],
                                                [Faker().random.randint(1, 256) for _ in
                                                 range(Faker().random.randint(11, 15))]),
                                               ([Faker().random.randint(1, 256) for _ in
                                                 range(Faker().random.randint(11, 15))],
                                                [Faker().random.randint(1, 256) for _ in range(10)])
                                               ])
    def test_rsub_one(self, first, second):
        copy_first = copy.copy(first)
        second_clist = CustomList(second)
        copy_second = copy.copy(CustomList(second))
        res_clist = first - second_clist
        assert type(res_clist).__name__ == 'CustomList'
        assert first == copy_first
        assert copy_second == second_clist
        assert res_clist.elem_compare(self.expect_sub(first, second))

    @pytest.mark.parametrize('first, second', [([Faker().random.randint(1, 256) for _ in range(10)],
                                                [Faker().random.randint(1, 256) for _ in range(10)]),
                                               ([Faker().random.randint(1, 256) for _ in range(10)],
                                                [Faker().random.randint(1, 256) for _ in
                                                 range(Faker().random.randint(11, 15))]),
                                               ([Faker().random.randint(1, 256) for _ in
                                                 range(Faker().random.randint(11, 15))],
                                                [Faker().random.randint(1, 256) for _ in range(10)])
                                               ])
    def test_iadd_one_clist_one_list(self, first, second):
        first_clist = CustomList(first)
        copy_second = copy.copy(second)
        first_clist += second
        assert copy_second == second
        assert type(first_clist).__name__ == 'CustomList'
        assert first_clist.elem_compare(self.expect_add(first, second))

    @pytest.mark.parametrize('first, second', [([Faker().random.randint(1, 256) for _ in range(10)],
                                                [Faker().random.randint(1, 256) for _ in range(10)]),
                                               ([Faker().random.randint(1, 256) for _ in range(10)],
                                                [Faker().random.randint(1, 256) for _ in
                                                 range(Faker().random.randint(11, 15))]),
                                               ([Faker().random.randint(1, 256) for _ in
                                                 range(Faker().random.randint(11, 15))],
                                                [Faker().random.randint(1, 256) for _ in range(10)])
                                               ])
    def test_isub_one_clist_one_list(self, first, second):
        first_clist = CustomList(first)
        copy_second = copy.copy(second)
        first_clist -= second
        assert copy_second == second
        assert type(first_clist).__name__ == 'CustomList'
        assert first_clist.elem_compare(self.expect_sub(first, second))


class TestCustomListCompare:

    @pytest.mark.parametrize('first, second, expect', [([1, 1, 1], [2, 2, 2], True),
                                                       ([2, 2, 2], [1, 1, 1], False),
                                                       ([1, 1, 1], [1, 1, 1], False),
                                                       ([1, 2, 3], [2, 2, 2], False),
                                                       ([12, 8], [11, 12, 3], True)])
    def test_lt(self, first, second, expect):
        return (CustomList(first) < CustomList(second)) == expect

    @pytest.mark.parametrize('first, second, expect', [([2, 2, 2], [1, 1, 1], True),
                                                       ([1, 1, 1], [2, 2, 2], False),
                                                       ([1, 1, 1], [1, 1, 1], False),
                                                       ([2, 2, 2], [1, 2, 3], False),
                                                       ([11, 12, 3], [12, 8], True)])
    def test_gt(self, first, second, expect):
        return (CustomList(first) > CustomList(second)) == expect

    @pytest.mark.parametrize('first, second, expect', [([1, 1, 1], [1, 1, 1], True),
                                                       ([1, 2, 3], [2, 2, 2], True),
                                                       ([1, 1, 2], [1, 1, 1], False),
                                                       ([16], [4, 10, 2], True)])
    def test_eq(self, first, second, expect):
        return (CustomList(first) == CustomList(second)) == expect

    @pytest.mark.parametrize('first, second, expect', [([1, 1, 1], [1, 1, 1], False),
                                                       ([1, 2, 3], [2, 2, 2], False),
                                                       ([1, 1, 2], [1, 1, 1], True),
                                                       ([16], [4, 10, 2], False)])
    def test_ne(self, first, second, expect):
        return (CustomList(first) != CustomList(second)) == expect

    @pytest.mark.parametrize('first, second, expect', [([1, 1, 1], [2, 2, 2], True),
                                                       ([2, 2, 2], [1, 1, 1], False),
                                                       ([1, 1, 1], [1, 1, 1], True),
                                                       ([1, 2, 3], [2, 2, 2], True),
                                                       ([12, 8], [11, 12, 3], True),
                                                       ([16], [4, 10, 2], True)])
    def test_le(self, first, second, expect):
        return (CustomList(first) <= CustomList(second)) == expect

    @pytest.mark.parametrize('first, second, expect', [([2, 2, 2], [1, 1, 1], True),
                                                       ([1, 1, 1], [2, 2, 2], False),
                                                       ([1, 1, 1], [1, 1, 1], True),
                                                       ([2, 2, 2], [1, 2, 3], True),
                                                       ([11, 12, 3], [12, 8], True),
                                                       ([16], [4, 10, 2], True)])
    def test_ge(self, first, second, expect):
        return (CustomList(first) >= CustomList(second)) == expect


class TestCustomListMethods:

    def test_str(self):
        expected_lst = [Faker().random.randint(1, 256) for _ in range(10)]
        expected_str = str(expected_lst) + '\n' + str(sum(expected_lst))
        return str(CustomList(expected_lst)) == expected_str

    @pytest.mark.parametrize('first,  second, expect', [([2, 2, 2], [1, 1, 1], False),
                                                        ([1, 1, 1], [2, 2, 2], False),
                                                        ([1, 1, 1], [1, 1, 1], True),
                                                        ([1, 2, 3], [1, 2, 3], True),
                                                        ([11, 12, 3], [11, 12], False),
                                                        ([16], [4, 10, 2], False)])
    def test_elem_compare(self, first, second, expect):
        assert CustomList(first).elem_compare(second) == expect
