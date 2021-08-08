from classes import get_two_objects


def main():
    class1, class2 = get_two_objects()

    test = class1.get_attr1()

    if (test == 10):
        print(
            f'class1.attr1: {class1.get_attr1()}, class1.attr2: {class1.get_attr2()}')
        print(
            f'class2.attr1: {class2.get_attr1()}, class2.attr2: {class2.get_attr2()}')


if __name__ == "__main__":
    main()
