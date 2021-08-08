from typing import TypeVar, NewType

# TestClass = TypeVar('TestClass')  # ODER man kann
# TestClass = NewType('TestClass' TestClass)  # -> Error


class TestClass():
    TestClass = TypeVar('TestClass')

    name: str

    def __init__(self, name: str):
        self.name = name

    def printClass(self) -> None:
        print("Name: " + self.name)

    def addClass(self, op2: TestClass) -> TestClass:
        self.name = self.name + ", " + op2.name
        toReturn: TestClass = TestClass(self.name)
        return toReturn

    def testFunct1(self) -> (str, int):
        return "test1", 10


def testFuntion01(test: str) -> None:
    print(test)


def testFunktio02(test: str) -> str:
    print(test)
    return test + " haha funktioniert"


testFuntion01("Das its mein TEST 01")
test: str = testFunktio02("Das ist mein TEST 02")
print(test)

myTest01: TestClass = TestClass("kirill")
myTest01.printClass()
check = myTest02 = TestClass("arnold")
print("INIT-Return: " + str(myTest02))
print("INIT-Return: " + str(check))
myTest02.printClass()
myTest03: TestClass = myTest01.addClass(myTest02)
myTest03.printClass()
# myTest03: TestClass = "test"
myTest03.printClass()
check.printClass()
print('INIT-Return: ' + str(myTest03))
print("INIT-Return: " + str(check))


a, b = myTest01.testFunct1()
print(a, b)
