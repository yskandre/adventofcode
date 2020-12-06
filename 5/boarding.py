def first():
    lines = open("5/bb.txt", "r").read().splitlines()

    ids = []

    for line in lines:
        row_nr, col_nr = 0, 0

        row = line[:7]
        col = line[7:]

        for i, v in enumerate(reversed(row)):
            if v == "B":
                row_nr += 2**i

        for i, v in enumerate(reversed(col)):
            if v == "R":
                col_nr += 2**i

        ids.append(row_nr * 8 + col_nr)

    print(max(ids))


def second():
    lines = open("5/bb.txt", "r").read().splitlines()

    ids = []

    for line in lines:
        row_nr, col_nr = 0, 0

        row = line[:7]
        col = line[7:]

        for i, v in enumerate(reversed(row)):
            if v == "B":
                row_nr += 2**i

        for i, v in enumerate(reversed(col)):
            if v == "R":
                col_nr += 2**i

        ids.append(row_nr * 8 + col_nr)

    for i in range(max(ids)):
        if i not in ids and i - 1 in ids and i + 1 in ids:
            print(i)


if __name__ == "__main__":
    first()
    second()
