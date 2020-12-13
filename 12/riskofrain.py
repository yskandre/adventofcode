def first():
    lines = open("12/rr.txt", "r").read().splitlines()

    x, y = 0, 0
    dir = 0

    for line in lines:
        order, v = line[0], int(line[1:])
        if order == "N":
            y += v
        elif order == "E":
            x += v
        elif order == "S":
            y -= v
        elif order == "W":
            x -= v
        elif order == "L":
            dir -= v
        elif order == "R":
            dir += v
        elif order == "F":
            dir = dir % 360
            if dir == 0:
                # East
                x += v
            elif dir == 90:
                # South
                y -= v
            elif dir == 180:
                # West
                x -= v
            elif dir == 270:
                # North
                y += v

    print(abs(x)+abs(y))


def second():
    lines = open("12/rr.txt", "r").read().splitlines()

    x, y = 0, 0
    wx, wy = 10, 1

    for line in lines:
        order, v = line[0], int(line[1:])
        if order == "N":
            wy += v
        elif order == "E":
            wx += v
        elif order == "S":
            wy -= v
        elif order == "W":
            wx -= v
        elif order == "L":
            for _ in range(v // 90):
                wx, wy = -wy, wx
        elif order == "R":
            for _ in range(v // 90):
                wx, wy = wy, -wx
        elif order == "F":
            x += wx * v
            y += wy * v

    print(abs(x)+abs(y))


if __name__ == "__main__":
    first()
    second()
