class String:

    def __set_name__(self, owner, name):
        self.name = name
        self._name = f"_{name}"

    def __set__(self, obj, val):
        if isinstance(val, str):
            return setattr(obj, self._name, val)
        raise ValueError("The value must be a string")

    def __get__(self, obj, objtype):
        return getattr(obj, self._name)


class Integer:

    def __set_name__(self, owner, num):
        self.num = num
        self._num = f"_{num}"

    def __set__(self, obj, val):
        if isinstance(val, int):
            return setattr(obj, self._num, val)
        raise ValueError("The value must be a int")

    def __get__(self, obj, objtype):
        return getattr(obj, self._num)


class PositiveInteger:
    def __set_name__(self, owner, price):
        self.price = price
        self._price = f"_{price}"

    def __set__(self, obj, val):
        if isinstance(val, int) and val > 0:
            return setattr(obj, self._price, val)
        raise ValueError("The value must be a positive int")

    def __get__(self, obj, objtype):
        return getattr(obj, self._price)


class Data:
    name = String()
    num = Integer()
    price = PositiveInteger()
