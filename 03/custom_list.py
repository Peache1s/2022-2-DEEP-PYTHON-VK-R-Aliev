class CustomList(list):

    def __init__(self, iter_obj):
        super().__init__(iter_obj)

    def __add__(self, addend):
        len_dif = self.__len__() - len(addend)
        min_len = min(len(self), len(addend))
        result_clist = CustomList(list(map(lambda x, y: x + y, self, addend)))
        result_clist.extend(self[min_len:]) if len_dif > 0 else result_clist.extend(addend[min_len:])
        return result_clist

    def __iadd__(self, addend):
        return self.__add__(addend)

    def __radd__(self, addend):
        return self.__add__(addend)

    def __sub__(self, deducted):
        """
        Subtraction method. There is no description in homework.md file about a case,
        when (CustomList1 - CustomList2) len(CustomList2) > len(CustomList1). In this
        case the remaining elements of CustomList2 are added to CustomList1
        WITHOUT "-".
        """
        len_dif = self.__len__() - len(deducted)
        min_len = min(len(self), len(deducted))
        result_clist = CustomList(list(map(lambda x, y: x - y, self, deducted)))
        result_clist.extend(self[min_len:]) if len_dif > 0 else result_clist.extend(deducted[min_len:])
        return result_clist

    def __rsub__(self, deducted):
        for i in range(len(self)):
            self[i] = -self[i]
        result_clist = self.__sub__([(-1) * deducted[i]
                                     for i in range(len(deducted))])
        len_dif = abs(len(deducted) - len(self))
        if len_dif != 0:
            for i in range(len(result_clist) - 1,
                           len(result_clist) - 1 - len_dif, -1):
                result_clist[i] = -result_clist[i]
        for i in range(len(self)):
            self[i] = -self[i]
        return result_clist

    def __lt__(self, another_list):
        return sum(self) < sum(another_list)

    def __le__(self, another_list):
        return sum(self) <= sum(another_list)

    def __eq__(self, another_list):
        return sum(self) == sum(another_list)

    def __ne__(self, another_list):
        return sum(self) != sum(another_list)

    def __gt__(self, another_list):
        return sum(self) > sum(another_list)

    def __ge__(self, another_list):
        return sum(self) >= sum(another_list)

    def __str__(self):
        return super().__str__() + '\n' + str(sum(self))
