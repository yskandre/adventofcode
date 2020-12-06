def first():
    lines = open("1/rr.txt", "r").readlines()

    for i in range(len(lines)):
        for j in range(i, len(lines)):
            if (int(lines[i]) + int(lines[j])) == 2020:
                print(int(lines[i]) * int(lines[j]))


def second():
    lines = open("1/rr.txt", "r").readlines()

    for i in range(len(lines)):
        for j in range(i, len(lines)):
            for k in range(j, len(lines)):
                if (int(lines[i]) + int(lines[j]) + int(lines[k])) == 2020:
                    print(int(lines[i]) * int(lines[j]) * int(lines[k]))


if __name__ == "__main__":
    first()
    second()
