class Class1:
    def __init__(self) -> None:
        self._attr1 = 10
        self._attr2 = 'ten'

    def get_attr1(self) -> int:
        return self._attr1

    def get_attr2(self) -> str:
        return self._attr2


class Class2:
    def __init__(self) -> None:
        self._attr1 = 20
        self._attr2 = 'twenty'

    def get_attr1(self) -> int:
        return self._attr1

    def get_attr2(self) -> str:
        return self._attr2


def get_two_objects():
    class1: Class1 = Class1()
    class2: Class2 = Class2()

    return class1, class2
