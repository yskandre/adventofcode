from operator import truediv
from os import name
import numpy as np


def first():
    lines = open("11/ss.txt", "r").read().splitlines()

    n_arr = np.zeros((len(lines), len(lines[0])), int)

    for i, line in enumerate(lines):
        for j, letter in enumerate(line):
            if letter == "L":
                n_arr[i, j] = 1

    occupied = np.zeros_like(n_arr)
    temp_occ = np.zeros_like(n_arr)

    done = False

    while not done:
        done = True
        for (x, y), v in np.ndenumerate(n_arr):
            if v:
                if occupied[x, y]:
                    if occupied[max(0, x-1):min(x+2, occupied.shape[0]), max(0, y-1):min(y+2, occupied.shape[1])].sum() - 1 >= 4:
                        temp_occ[x, y] = 0
                        done = False
                elif occupied[max(0, x-1):min(x+2, occupied.shape[0]), max(0, y-1):min(y+2, occupied.shape[1])].sum() == 0:
                    temp_occ[x, y] = 1
                    done = False
        occupied = temp_occ.copy()

    print(occupied.sum())


def second():
    lines = open("11/ss.txt", "r").read().splitlines()

    n_arr = np.zeros((len(lines), len(lines[0])), int)

    for i, line in enumerate(lines):
        for j, letter in enumerate(line):
            if letter == "L":
                n_arr[i, j] = 1

    occupied = np.zeros_like(n_arr)
    temp_occ = np.zeros_like(n_arr)

    done = False

    while not done:
        done = True
        for (x, y), v in np.ndenumerate(n_arr):
            if v:
                if occupied[x, y]:
                    count = 0
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            dx, dy = x + i, y + j
                            while dx >= 0 and dx < n_arr.shape[0] and dy >= 0 and dy < n_arr.shape[1]:
                                if n_arr[dx, dy]:
                                    if occupied[dx, dy]:
                                        count += 1
                                    break
                                dx += i
                                dy += j
                    if count - 1 >= 5:
                        temp_occ[x, y] = 0
                        done = False
                else:
                    occupy = True
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            dx, dy = x + i, y + j
                            while dx >= 0 and dx < n_arr.shape[0] and dy >= 0 and dy < n_arr.shape[1]:
                                if n_arr[dx, dy]:
                                    if occupied[dx, dy]:
                                        occupy = False
                                    break
                                dx += i
                                dy += j
                    if occupy:
                        temp_occ[x, y] = 1
                        done = False
        occupied = temp_occ.copy()

    print(occupied.sum())


if __name__ == "__main__":
    # first()
    second()
