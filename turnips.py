#/usr/bin/python3.4
__author__ = 'suber1'
import numpy as np
import magic_square as ms
import sys


def acell(x=1, y=1, letter=None):
    """ return the value of the letter-designated cell given the relations
        described below. Letters follow written diagram"""
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
    """ given an x and y, return the numeric value of each of
        the 9 square-of-square cells using the acell() function """
    return np.array([acell(x=x, y=y, letter=cell) for cell in cells], dtype=np.float128).reshape((3, 3))


def mycheck(A):
    try:
        assert(np.sum(np.vstack(A)) == np.sum(np.hstack(A)) == np.sum(np.diag(A))*3)
    except AssertionError:
        print("My check says its NOT a magic square:")
        print A
        return 0
    # WARNING, all diagonals not yet checked!
    # But this is enough to detect most of the baddies as
    # they are far more often non-center-crossing lines
    return 1


def assess_grid(A):
    """
    not using it just now
    """
    awin = ms.ismagic(A)
    #print("looks like: ")
    #print("{}".format(A))
    #print("'magic?':  {}".format((True if awin else False)))
    #if awin:
    #    print("it has a 'magic constant' = {}".format(ms.magic_constant(A)))
    if A.any() < 0:
        print("A value is negative, and so requires imagination I don't have")
        return 0
    return awin


def checkroots(A):
    r = np.sqrt(A)
    return r


def main(val_x=64, val_y=8):
    """
    :param val_x: a base value; the center-square value
    :param val_y: the modulating value to calculate other cells
    :return: roots of the nine obtained cell-values
    """
    q = grid(val_x, val_y)
    if not mycheck(q):
        print("I say old chap - that isn't a magic square! {}".format(mycheck(q)))
    if not np.any(q < 1):
        r = checkroots(q)      # broadcasting over the 3x3 grid
        print("x={}, y={}".format(val_x, val_y))
        print r
    else:
        print("Could not get real roots for all the values that arise from x={}, y={}".format(val_x, val_y))


if __name__ == "__main__":
    try:
        q1, q2 = (int(sys.argv[1]), int(sys.argv[2])) or (50, 100)
        r1, r2 = (int(sys.argv[3]), int(sys.argv[4])) or (1, 10)
    except IndexError, TypeError:
        print("using default values of ranges")
        print("to use your own try 'python turnips.py x1 x2 y1 y2' where x1..y2 are your positive integers")
        q1, q2 = 50, 150
        r1, r2 = 3, 45

    print("chosen x-range is {} to {}.  y-range is {} to {}".format(q1, q2, r1, r2))
    for q in xrange(q1, q2):
        for r in xrange(r1, r2):
            main(val_x=q, val_y=r)

