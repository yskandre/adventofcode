import numpy as np


def first():
    lines = open("17/cc.txt", "r").read().splitlines()

    cubes = np.zeros((13, len(lines) + 12, len(lines[0]) + 12), int)

    for i, line in enumerate(lines):
        for j, letter in enumerate(line):
            if letter == "#":
                cubes[6, i + 6, j + 6] = 1

    temp = cubes.copy()

    for _ in range(6):
        for (z, x, y), v in np.ndenumerate(cubes):
            actives = cubes[max(0, z-1):min(z+2, cubes.shape[0]), max(0, x-1):min(
                x+2, cubes.shape[1]), max(0, y-1):min(y+2, cubes.shape[2])].sum()
            if v:
                if actives - 1 not in [2, 3]:
                    temp[z, x, y] = 0
            elif actives == 3:
                temp[z, x, y] = 1
        cubes = temp.copy()

    print(cubes.sum())


def second():
    lines = open("17/cc.txt", "r").read().splitlines()

    cubes = np.zeros((13, len(lines) + 12, len(lines[0]) + 12, 13), int)

    for i, line in enumerate(lines):
        for j, letter in enumerate(line):
            if letter == "#":
                cubes[6, i + 6, j + 6, 6] = 1

    temp = cubes.copy()

    for _ in range(6):
        for (z, x, y, w), v in np.ndenumerate(cubes):
            actives = cubes[max(0, z-1):min(z+2, cubes.shape[0]), max(0, x-1):min(
                x+2, cubes.shape[1]), max(0, y-1):min(y+2, cubes.shape[2]), max(0, w-1):min(w+2, cubes.shape[3])].sum()
            if v:
                if actives - 1 not in [2, 3]:
                    temp[z, x, y, w] = 0
            elif actives == 3:
                temp[z, x, y, w] = 1
        cubes = temp.copy()

    print(cubes.sum())


if __name__ == "__main__":
    first()
    second()
