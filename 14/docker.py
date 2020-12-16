from itertools import product


def first():
    lines = open("14/dd.txt", "r").read().splitlines()

    segments = []
    temp = []

    for line in lines:
        if "mask" in line:
            if temp:
                segments.append(temp.copy())
            temp = [line]
        else:
            temp.append(line)

    segments.append(temp.copy())

    memory = {}

    for seg in segments:
        mask = seg[0][7:]
        for op in seg[1:]:
            data = op.split(" = ")
            slot = data[0][4:-1]
            binary = str(bin(int(data[1])))[2:]
            bin_36 = "0" * (36 - len(binary)) + binary
            result = ""
            for i, bit in enumerate(mask):
                result += bin_36[i] if bit == "X" else mask[i]

            memory[slot] = result

    print(sum(map(lambda x: int(x, 2), memory.values())))


def second():
    lines = open("14/dd.txt", "r").read().splitlines()

    segments = []
    temp = []

    for line in lines:
        if "mask" in line:
            if temp:
                segments.append(temp.copy())
            temp = [line]
        else:
            temp.append(line)

    segments.append(temp.copy())

    memory = {}

    def calc_slot(slot, i, slots, slot_36, mask):
        if len(slot) == 36:
            slots.add(slot)
        elif mask[i] == "X":
            calc_slot(slot + "0", i + 1, slots, slot_36, mask)
            calc_slot(slot + "1", i + 1, slots, slot_36, mask)
        elif mask[i] == "1":
            calc_slot(slot + "1", i + 1, slots, slot_36, mask)
        else:
            calc_slot(slot + slot_36[i], i + 1, slots, slot_36, mask)

    for seg in segments:
        mask = seg[0][7:]
        x_bits = []
        for i, bit in enumerate(mask):
            if bit == "X":
                x_bits.append(i)

        for op in seg[1:]:
            data = op.split(" = ")
            slot_bin = str(bin(int(data[0][4:-1])))[2:]
            slot_36 = "0" * (36 - len(slot_bin)) + slot_bin
            decimal = int(data[1])
            slots = set()
            calc_slot("", 0, slots, slot_36, mask)

            for slot in slots:
                memory[slot] = decimal

    print(sum(memory.values()))


if __name__ == "__main__":
    first()
    second()
