from itertools import product


def first():
    data = open("19/mm.txt", "r").read().split("\n\n")

    rules = {}
    msgs = data[1].splitlines()
    patterns = set()

    for line in data[0].splitlines():
        id, matches = line.split(": ")
        rules[id] = matches.split(" | ")

    def pattern_builder(id):
        pattern_set = set()
        for sub_rules in rules[id]:
            rule_list = []
            for s in sub_rules.split(" "):
                if s in ['"a"', '"b"']:
                    return {s[1]}
                rule_list.append(pattern_builder(s))
            pattern_set = pattern_set | (
                set("".join(p) for p in product(*rule_list)))
        return pattern_set

    patterns = pattern_builder("0")

    print(sum(msg in patterns for msg in msgs))


def second():
    data = open("19/mm.txt", "r").read().split("\n\n")

    rules = {}
    msgs = data[1].splitlines()
    patterns = set()

    for line in data[0].splitlines():
        id, matches = line.split(": ")
        rules[id] = matches.split(" | ")

    def pattern_builder(id):
        pattern_set = set()
        for sub_rules in rules[id]:
            rule_list = []
            for s in sub_rules.split(" "):
                if s in ['"a"', '"b"']:
                    return {s[1]}
                rule_list.append(pattern_builder(s))
            pattern_set = pattern_set | (
                set("".join(p) for p in product(*rule_list)))
        return pattern_set

    patterns_42 = pattern_builder("42")
    patterns_31 = pattern_builder("31")

    total = 0

    for msg in msgs:
        if len(msg) % 8 != 0 or msg[:8] not in patterns_42:
            continue
        end = False
        c_31, c_42 = 0, 1
        seg = msg[8:]
        while len(seg) > 0:
            if not end:
                if seg[:8] in patterns_42:
                    c_42 += 1
                else:
                    end = True
                    if seg[:8] in patterns_31:
                        c_31 += 1
                    else:
                        break
            else:
                if seg[:8] in patterns_31:
                    c_31 += 1
                else:
                    break
            seg = seg[8:]
        if c_31 + c_42 == len(msg) // 8 and 0 < c_31 < c_42:
            total += 1

    print(total)


if __name__ == "__main__":
    # first()
    second()
