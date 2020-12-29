from os import write


def first():
    lines = open("18/oo.txt", "r").read().splitlines()

    def add(a: int, b: int):
        return a + b

    def mult(a: int, b: int):
        return a * b

    def calc(line):
        num, bracket, curr_op = None, 0, None

        for i, c in enumerate(line):
            if c == ")":
                if bracket != 0:
                    bracket -= 1
                else:
                    return num
            elif c == "(":
                if bracket != 0:
                    bracket += 1
                    continue
                elif num and curr_op:
                    bracket += 1
                    num = curr_op(num, calc(line[i + 1:]))
                else:
                    bracket += 1
                    num = calc(line[i + 1:])
            elif bracket != 0:
                continue
            elif c == "+":
                curr_op = add
            elif c == "*":
                curr_op = mult
            else:
                if curr_op:
                    num = curr_op(num, int(c))
                else:
                    num = int(c)
        return num

    total = 0

    for line in lines:
        line = line.replace(" ", "")
        total += calc(line)

    print(total)


def second():
    lines = open("18/oo.txt", "r").read().splitlines()

    def calc(line):
        num, num_store, bracket, curr_op = None, 1, 0, None

        for i, c in enumerate(line):
            if c == ")":
                if bracket != 0:
                    bracket -= 1
                else:
                    return num * num_store
            elif c == "(":
                if bracket != 0:
                    bracket += 1
                    continue
                if num:
                    bracket += 1
                    if curr_op == "+":
                        num += calc(line[i + 1:])
                    elif curr_op == "*":
                        num_store *= num
                        num = calc(line[i + 1:])
                else:
                    bracket += 1
                    num = calc(line[i + 1:])
            elif bracket != 0:
                continue
            elif c == "+":
                curr_op = "+"
            elif c == "*":
                curr_op = "*"
            else:
                if curr_op == "+":
                    num += int(c)
                elif curr_op == "*":
                    num_store *= num
                    num = int(c)
                else:
                    num = int(c)
        return num * num_store

    total = 0

    for line in lines:
        line = line.replace(" ", "")
        total += calc(line)

    print(total)


if __name__ == "__main__":
    first()
    second()
