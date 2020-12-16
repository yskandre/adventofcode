def first():
    lines = open("15/rr.txt", "r").read().splitlines()

    lookup_table = {}
    prev = 0
    curr = int(lines[0].split(",")[0])
    turn = 1

    for num in map(lambda i: int(i), lines[0].split(",")[1:]):
        prev = curr
        curr = num
        lookup_table[prev] = turn
        turn += 1

    while turn < 2020:
        if curr in lookup_table:
            prev = curr
            curr = turn - lookup_table[prev]
            lookup_table[prev] = turn
        else:
            prev = curr
            curr = 0
            lookup_table[prev] = turn
        turn += 1

    print(curr)


def second():
    lines = open("15/rr.txt", "r").read().splitlines()

    lookup_table = {}
    prev = 0
    curr = int(lines[0].split(",")[0])
    turn = 1

    for num in map(lambda i: int(i), lines[0].split(",")[1:]):
        prev = curr
        curr = num
        lookup_table[prev] = turn
        turn += 1

    while turn < 30000000:
        if curr in lookup_table:
            prev = curr
            curr = turn - lookup_table[prev]
            lookup_table[prev] = turn
        else:
            prev = curr
            curr = 0
            lookup_table[prev] = turn
        turn += 1

    print(curr)


if __name__ == "__main__":
    first()
    second()
