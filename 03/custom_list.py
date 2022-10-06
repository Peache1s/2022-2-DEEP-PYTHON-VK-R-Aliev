

class CustomList(list):

    def __init__(self, iter_obj):
        super().__init__(iter_obj)
        self.sum = None

    def __add__(self, addend):
        len_dif = self.__len__() - len(addend)
        abs_len_dif = abs(len_dif)
        addend.extend([0]*abs_len_dif) if len_dif > 0\
            else self.extend([0]*abs_len_dif)
        result_clist = CustomList(list(map(lambda x, y: x + y, self, addend)))
        if len_dif > 0:
            del addend[len(addend) - 1:len(addend) - 1 - abs_len_dif:-1]
        elif len_dif < 0:
            del self[len(addend) - 1:len(addend) - 1 - abs_len_dif:-1]
        return result_clist

    def __iadd__(self, addend):
        len_dif = self.__len__() - len(addend)
        abs_len_dif = abs(len_dif)
        addend.extend([0]*abs_len_dif) if len_dif > 0 \
            else self.extend([0]*abs_len_dif)
        self = CustomList(list(map(lambda x, y: x + y, self, addend)))
        if len_dif > 0:
            del addend[len(addend) - 1:len(addend) - 1 - abs_len_dif:-1]
        return self

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
        abs_len_dif = abs(len_dif)
        deducted.extend([0]*abs_len_dif) if len_dif > 0 else self.extend([0]*abs_len_dif)
        temp_list = list(map(lambda x, y: x - y, self, deducted))
        if len_dif < 0:
            reverse_list = list(map(lambda x: -x,
                                    temp_list[len(temp_list) - 1:
                                              len(temp_list) - 1 - abs_len_dif: -1]))
            temp_list[len(temp_list) - 1:
                      len(temp_list) - 1 - abs_len_dif: -1] = reverse_list

        if len_dif > 0:
            del deducted[len(deducted) - 1:len(deducted) - 1 - abs_len_dif:-1]
        elif len_dif < 0:
            del self[len(deducted) - 1:len(deducted) - 1 - abs_len_dif:-1]
        return CustomList(temp_list)

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
        if self.sum:
            self.sum = sum(self)
            return self.sum < sum(another_list)
        return sum(self) < sum(another_list)

    def __le__(self, another_list):
        if self.sum:
            self.sum = sum(self)
            return self.sum < sum(another_list)
        return sum(self) <= sum(another_list)

    def __eq__(self, another_list):
        if self.sum:
            self.sum = sum(self)
            return self.sum == sum(another_list)
        return sum(self) == sum(another_list)

    def __ne__(self, another_list):
        if self.sum:
            self.sum = sum(self)
            return self.sum != sum(another_list)
        return sum(self) != sum(another_list)

    def __gt__(self, another_list):
        if self.sum:
            self.sum = sum(self)
            return self.sum > sum(another_list)
        return sum(self) > sum(another_list)

    def __ge__(self, another_list):
        if self.sum:
            self.sum = sum(self)
            return self.sum >= sum(another_list)
        return sum(self) >= sum(another_list)

    def __str__(self):
        return super().__str__() + '\n' + str(self.sum) \
            if self.sum else super().__str__() + '\n' + str(sum(self))

    def elem_compare(self, compared):
        return super().__eq__(compared)
