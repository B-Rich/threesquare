#/usr/bin/python3.4
__author__ = 'suber1'

import numpy as np
import magic_square as ms


def acell(x=1, y=1, letter=None):
    """ return the value of the letter-designated cell given the relations
        described below """
    if letter == "a":
        return x - y
    elif letter == "b":
        return x - 2*y
    elif letter == "c":
        return x + 3*y
    elif letter == "f":
        return x + 4*y
    elif letter == "g":
        return x
    elif letter == "k":
        return x - 4*y
    elif letter == "m":
        return x - 3*y
    elif letter == "p":
        return x + 2*y
    elif letter == "r":
        return x + y
    elif not letter:
        print("a cell-designating letter was not supplied for x,y = {}{}".format(x, y))
    else:
        print("{} is not a cell-designating-letter".format(letter))
    return 0


def grid(x, y, cells=['a', 'b', 'c', 'f', 'g', 'k', 'm', 'p', 'r']):
    """ given an x and y, return the numeric value of
        the 9 square-of-square cells using the acell() function """
    return np.array([acell(x=x, y=y, letter=cell) for cell in cells], dtype=np.float128).reshape((3, 3))


def mycheck(A):
    try:
        assert(np.sum(np.vstack(A)) == np.sum(np.hstack(A)))
    except AssertionError as e:
        print("not a magic square")
        return 0
    # WARNING, diagonals not yet checked!
    return 1


def assess_grid(A):
    awin = ms.ismagic(A)
    print("looks like: {}".format(A))
    print("the grid is 'magic':  {}".format(awin))
    if awin:
        print("it has a 'magic constant' = {}".format(ms.magic_constant(A)))
    return awin

if __name__ == "__main__":

    q = grid(5, 1)
    print("I say: {}".format(mycheck(q)))
    r = assess_grid(q)
