def first():
    lines = open("6/cc.txt", "r").read().splitlines()

    count = 0
    customs = set()

    for line in lines:
        if line != "":
            customs |= set(line)
        else:
            count += len(customs)

            customs.clear()

    if len(customs) > 0:
        count += len(customs)

    print(count)


def second():
    lines = open("6/cc.txt", "r").read().splitlines()

    count = 0
    customs = None

    for line in lines:
        if line != "":
            if customs == None:
                customs = set(line)
            else:
                customs &= set(line)
        else:
            count += len(customs)

            customs = None

    if len(customs) > 0:
        count += len(customs)

    print(count)


if __name__ == "__main__":
    first()
    second()
