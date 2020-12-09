def first():
    lines = open("8/hh.txt", "r").read().splitlines()

    visited = set()
    pointer = 0
    acc = 0

    while pointer not in visited:
        visited.add(pointer)
        action, value = lines[pointer].split(" ")
        if action == "acc":
            acc += int(value)
        if action == "jmp":
            pointer += int(value)
            continue
        pointer += 1

    print(acc)


def second():
    lines = open("8/hh.txt", "r").read().splitlines()

    visited = set()
    pointer = 0
    acc = 0
    changed_op = 0

    while max(pointer, changed_op) < len(lines):
        if pointer in visited or pointer < 0:
            visited = set()
            pointer = 0
            acc = 0
            changed_op += 1
        visited.add(pointer)
        action, value = lines[pointer].split(" ")
        if changed_op == pointer and action != "acc":
            action = "jmp" if action == "nop" else "nop"
        if action == "acc":
            acc += int(value)
        if action == "jmp":
            pointer += int(value)
            continue
        pointer += 1

    print(pointer, changed_op, acc)


if __name__ == "__main__":
    first()
    second()
