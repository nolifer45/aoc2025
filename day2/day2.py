import unittest

from data import test_data, test_data2, data


class AnyClass:
    def __init__(self, value):
        self.value = value


def parser(string: str):
    string = string.split(",")
    string = [start_stop.split("-") for start_stop in string]
    for item in string:
        item[0] = int(item[0])
        item[1] = int(item[1])
    return string


def number_intervals(list_of_intervals: list[int]) -> list[int]:
    start = list_of_intervals[0]
    end = list_of_intervals[1]
    all_intervals = set()
    for i in range(end - start):
        all_intervals.add(start + i)
    all_intervals.add(end)
    return list(all_intervals)


def check_repeat(number_list: int):
    repeat = 0
    for number in number_list:
        if len(str(number)) % 2 == 0:
           if split_string_in_halfs(str(number)):
               print("It's a match!", number)
               repeat += number
    return repeat


def split_string_in_halfs(string: str):
    print("Splitting string in halfs...")
    print(string)
    print(len(string) % 2)
    if len(string) % 2 == 0:
        a = string[:len(string) // 2]
        b = string[len(string) // 2:]
        if a == b:
            return True
        elif split_string_in_halfs(a) or split_string_in_halfs(b):
            return True
    else:
        return False

def check_next_char(string: str):
    seq = ""
    seq2 = ""
    for char in string:
        if seq:
            if char == seq[0]:
        seq += char



def main():
    intervals = parser(test_data2)
    true_intervals = []
    total= 0
    for interval in intervals:
        true_intervals.append(number_intervals(interval))
    for interval in true_intervals:
        total += check_repeat(interval)
    print("#######",total,"########")
    #print(true_intervals)
    #print(test_data2)
    pass



class test_day1(unittest.TestCase):
    def setUp(self):
        self.test_data = test_data
        self.test_data2 = test_data2

    def test_part1(self):
        self.assertTrue("This is a dummy test" == "This is a dummy test")
        #print(parser(self.test_data))

    def test_part2(self):
        pass


if __name__ == "__main__":
    main()
