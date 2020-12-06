def first():
    lines = open("2/pw.txt", "r").readlines()

    valid_passwords = 0

    for line in lines:
        line_args = line.split(" ")
        bounds = line_args[0].split("-")
        count = line_args[2].count(line_args[1][0])
        if int(bounds[0]) <= count <= int(bounds[1]):
            valid_passwords += 1

    print(valid_passwords)


def second():
    lines = open("2/pw.txt", "r").readlines()

    valid_passwords = 0

    for line in lines:
        line_args = line.split(" ")
        positions = line_args[0].split("-")

        if (line_args[2][int(positions[0])-1] == line_args[1][0]) ^ (line_args[2][int(positions[1])-1] == line_args[1][0]):
            valid_passwords += 1

    print(valid_passwords)


if __name__ == "__main__":
    first()
    second()
