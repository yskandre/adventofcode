def first():
    lines = open("3/tt.txt", "r").read().splitlines()

    trees = 0
    x = 0
    width = len(lines[0])

    for line in lines:
        if line[x % width] == "#":
            trees += 1
        x += 3

    print(trees)


def second():
    lines = open("3/tt.txt", "r").read().splitlines()

    trees = 1
    movements = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    height, width = len(lines), len(lines[0])

    for i, (dx, dy) in enumerate(movements):
        count = 0
        x, y = 0, 0
        while y < height - 1:
            if lines[y][x % width] == "#":
                count += 1
            x += dx
            y += dy
        trees *= count

    print(trees)


if __name__ == "__main__":
    first()
    second()
