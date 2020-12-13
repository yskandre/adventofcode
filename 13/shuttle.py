from os import TMP_MAX, times


def first():
    lines = open("13/ss.txt", "r").read().splitlines()

    timestamp = int(lines[0])
    busses = [int(i) for i in lines[1].split(',') if i != 'x']
    bb = "", float('inf')

    for bus in busses:
        time = ((timestamp // bus) + 1) * bus
        if time < bb[1]:
            bb = bus, time

    print(bb[0] * (bb[1] - timestamp))


def second():
    lines = open("13/ss.txt", "r").read().splitlines()

    busses = [(i, int(j))
              for i, j in enumerate(lines[1].split(',')) if j != "x"]
    timestamp = busses[0][1]
    # max(busses, key=lambda x: x[1])[1]

    done = False
    added = set()
    increment = 1

    while not done:
        done = True
        for i, v in busses:
            if (timestamp + i) % v == 0:
                if v not in added:
                    added.add(v)
                    increment *= v
            if not (timestamp + i) % v == 0:
                done = False
                timestamp += increment
                break

    print(timestamp)


if __name__ == "__main__":
    first()
    second()
