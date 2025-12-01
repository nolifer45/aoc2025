import unittest

from data import test_data, test_data2


class AnyClass:
    def __init__(self, value):
        self.value = value


def parser(string: str):
    string = string.split("\n")

    data_dict = {}

    for row in string:
        pass


def do_the_thing(parsed_data):
    pass


def main():
    print("Just testing")
    pass



class test_day1(unittest.TestCase):
    def setUp(self):
        self.test_data = test_data
        self.test_data2 = test_data2

    def test_part1(self):
        self.assertTrue("This is a dummy test" == "This is a dummy test")

    def test_part2(self):
        pass


if __name__ == "__main__":
    main()
