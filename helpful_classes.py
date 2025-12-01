import unittest
from typing import List


class GameBoard:
    def __init__(self, values: List[List]):
        self.board = {}
        for y, row in enumerate(values):
            for x, cell in enumerate(row):
                self.board.update({(x,y): cell})
        self.current_position = (0,0)

        self.max_y = None
        self.max_x = None

    def get_position(self):
        return self.current_position

    def get_current_value(self):
        return self.board[self.current_position]

    def get_board(self):
        return self.board

    def move(self, position):
        if position not in self.board:
            print("Invalid position")
        else:
            self.current_position = position

    def move_left(self):
        if self.current_position[0] > 0:
            self.current_position = (self.current_position[0] - 1, self.current_position[1])

    def move_right(self):
        if self.current_position[0] < self.max_x:
            self.current_position = (self.current_position[0] + 1, self.current_position[1])

    def move_up(self):
        if self.current_position[1] > 0:
            self.current_position = (self.current_position[0] - 1, self.current_position[1])

    def move_down(self):
        if self.current_position[1] < self.max_y:
            self.current_position = (self.current_position[0] + 1, self.current_position[1])

    def get_max_x(self):
        if self.max_x is None:
            self.max_x = max([key[0] for key in self.board.keys()])
        return self.max_x

    def get_max_y(self):
        if self.max_y is None:
            self.max_y = max([key[1] for key in self.board.keys()])
        return self.max_y



class test_zone(unittest.TestCase):
    def setUp(self):
        self.game = GameBoard([["abc", "def", "ghi"],
                               ["jkl", "mno", "pqr"],
                               ["tuv", "wx", "yz"]])


    def test_zone(self):
        self.assertEqual(self.game.get_board(), self.game.board)
        self.assertEqual({(0, 0): 'abc',
                          (0, 1): 'jkl',
                          (0, 2): 'tuv',
                          (1, 0): 'def',
                          (1, 1): 'mno',
                          (1, 2): 'wx',
                          (2, 0): 'ghi',
                          (2, 1): 'pqr',
                          (2, 2): 'yz'}, self.game.board)
        self.assertEqual(self.game.get_current_value(), 'abc')
        self.assertEqual(self.game.current_position, (0,0))

        self.game.move((3,3))
        self.assertEqual(self.game.get_current_value(), 'abc', "We haven't moved yet")
        self.game.move_left()
        self.assertEqual(self.game.get_current_value(), "abc", "We haven't moved yet")
        self.game.move_up()
        self.assertEqual(self.game.get_current_value(), "abc", "We haven't moved yet")
