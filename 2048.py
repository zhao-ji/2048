#!/usr/bin/env python
# coding: utf-8

import random

def init():

    print "welcome to 2048 !\n".swapcase().center(80)
    print "use the 'a' 's' 'd' 'w' to moving !\n".swapcase().center(80)

    value = [
                [' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' '],
            ]

    random_position_1, random_position_2 = random.sample(range(15), 2)
    row_1, line_1 = divmod(random_position_1, 4)
    row_2, line_2 = divmod(random_position_2, 4)
    value[row_1][line_1] = 2
    value[row_2][line_2] = random.choice([2, 4])

    display(value)
    return value

def display(value):
    print "-----------------".center(80)
    print "| {0[0]} | {0[1]} | {0[2]} | {0[3]} |".format(value[0]).center(80)
    print "-----------------".center(80)
    print "| {0[0]} | {0[1]} | {0[2]} | {0[3]} |".format(value[1]).center(80)
    print "-----------------".center(80)
    print "| {0[0]} | {0[1]} | {0[2]} | {0[3]} |".format(value[2]).center(80)
    print "-----------------".center(80)
    print "| {0[0]} | {0[1]} | {0[2]} | {0[3]} |".format(value[3]).center(80)
    print "-----------------".center(80)

class Operate:
    'user operate'
    value = None

    def __init__(self, init_value):
        self.value = init_value

    def left(self):
        self.value = map(self.single_row_move_to_left, self.value)

    def up(self):
        updown_value = map(list, zip(*self.value))
        after_operate_updown_value = map(self.single_row_move_to_left, updown_value)
        after_operate_value = map(list, zip(*after_operate_updown_value))
        self.value = after_operate_value

    def right(self):
        reversed_value = map(list, map(reversed, self.value))
        after_operate_reversed_value = map(self.single_row_move_to_left, reversed_value)
        after_operate_value = map(list, map(reversed, after_operate_reversed_value))
        self.value = after_operate_value

    def down(self):
        updown_value = map(list, zip(*self.value))
        reversed_updown_value = map(list, map(reversed, updown_value))
        after_operate_reversed_updown_value = map(self.single_row_move_to_left,
                                                reversed_updown_value)
        after_operate_updown_value = map(list, map(reversed,\
                                            after_operate_reversed_updown_value))
        after_operate_value = map(list, zip(*after_operate_updown_value))
        self.value = after_operate_value

    def single_row_move_to_left(self, _list_):
        _list_ = filter(lambda x: x is not ' ', _list_)
        for i, j in enumerate(_list_):
            if i < len(_list_) - 1 and j == _list_[i+1]:
                _list_[i] = j * 2
                del _list_[i+1]
        _list_.extend([' ']*(4-len(_list_)))
        return _list_

    def add_random_value(self):
        random_value = random.choice([2,4])
        available_position = [(i, j) for i in range(4)\
                                        for j in range(4)\
                                            if self.value[i][j]== ' ' ]
        random_row, random_line = random.choice(available_position)
        self.value[random_row][random_line] = random_value

if __name__ == '__main__':
    value = init()
    operate = Operate(value)
    operate_dict = {
        'w':operate.up, 'W':operate.up,
        's':operate.down, 'S':operate.down,
        'a':operate.left, 'A':operate.left,
        'd':operate.right, 'D':operate.right,
    }
    while True:
        operate_letter = raw_input("please input your operate: ".center(80))
        if operate_letter not in ['a', 'A', 's', 'S', 'd', 'D', 'w', 'W']:
            print "your input wrong letter !".center(80)
            continue
        operate_dict[operate_letter]()
        if reduce(lambda x, y: x + y, map(len, map(lambda z: filter(lambda x: x is not ' ', z), operate.value))) == 15:
            print "your fail !".center(80)
            break
        operate.add_random_value()
        display(operate.value)
