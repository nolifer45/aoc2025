import unittest

from data import data, test_data, test_data2


def parse_data(data):
    directions = []
    distances = []
    data = data.splitlines()
    for line in data:
        for char in line:
            if char.isalpha():
                direction = char
            else:
                distance = int(line[1:])
        directions.append(direction)
        distances.append(distance)
    return {"directions": directions, "distances": distances}


    
def counter(start, distance, direction):
    zeros = 0
    if direction == "L":
       for i in range(distance):
           start -= 1
           if start < 0:
               start = 99
           elif start == 0:
                zeros += 1
    elif direction == "R":
       for i in range(distance):
           start += 1
           if start > 99:
               start = 0
               zeros += 1
    return start, zeros


def part1(data):
    start = 50
    zeros = 0
    for i in range(len(data["directions"])):

        if data["directions"][i] == "L":
            start, new_zeros = counter(start, data["distances"][i], "L")
            zeros += new_zeros

        elif data["directions"][i] == "R":
            start, new_zeros = counter(start, data["distances"][i], "R")
            zeros += new_zeros
    
        print("Current position:", start)
        print("Number of times crossed zero:", zeros)
        
    return zeros

class TestDay1(unittest.TestCase):
    def setUp(self):
        self.data = test_data
        self.test_data2 = test_data2
    def test_part1(self):
        self.assertEqual(parse_data(self.data), {'directions': ['L', 'L', 'R', 'L', 'R', 'L', 'L', 'L', 'R', 'L'],
                                                 'distances': [68, 30, 48, 5, 60, 55, 1, 99, 14, 82]})
        self.assertEqual(part1(parse_data(self.data)), 6)

    def test_part2(self):
        pass



if __name__ == "__main__":           
    print(part1(parse_data(data)))