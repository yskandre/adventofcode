def first():
    lines = open("16/tt.txt", "r").read().splitlines()

    data = []
    temp = []

    for line in lines:
        if line == "":
            data.append(temp)
        elif "ticket" in line:
            temp = []
        else:
            temp.append(line)

    data.append(temp)

    rules = {}

    for rule in data[0]:
        name, constraints = rule.split(": ")
        rules[name] = [tuple(map(int, r.split('-')))
                       for r in constraints.split(' or ')]

    sum = 0

    for ticket in data[2]:
        for v in map(int, ticket.split(",")):
            if not any((rule[0][0] <= v <= rule[0][1]) or (rule[1][0] <= v <= rule[1][1]) for rule in rules.values()):
                sum += int(v)
                break

    print(sum)


def second():
    lines = open("16/tt.txt", "r").read().splitlines()

    data = []
    temp = []

    for line in lines:
        if line == "":
            data.append(temp)
        elif "ticket" in line:
            temp = []
        else:
            temp.append(line)

    data.append(temp)

    rules = {}

    for rule in data[0]:
        name, constraints = rule.split(": ")
        rules[name] = [tuple(map(int, r.split('-')))
                       for r in constraints.split(' or ')]

    sum = 0
    valid_tickets = []

    for ticket in data[2]:
        for v in map(int, ticket.split(",")):
            if not any((rule[0][0] <= v <= rule[0][1]) or (rule[1][0] <= v <= rule[1][1]) for rule in rules.values()):
                break
        else:
            valid_tickets.append(ticket)

    rule_lookup = {}

    for name, rule in rules.items():
        viable_pos = set()
        for i in range(len(data[1][0].split(","))):
            for ticket in valid_tickets:
                if not (rule[0][0] <= int(ticket.split(",")[i]) <= rule[0][1] or rule[1][0] <= int(ticket.split(",")[i]) <= rule[1][1]):
                    break
            else:
                viable_pos.add(i)

        rule_lookup[name] = viable_pos

    rule_index = {}

    for rule in sorted(rule_lookup, key=lambda x: len(rule_lookup[x])):
        for idx in rule_lookup[rule]:
            if idx not in rule_index:
                rule_index[idx] = rule

    result = 1

    for idx, rule in rule_index.items():
        if "departure" in rule:
            result *= int(data[1][0].split(",")[idx])

    print(result)


if __name__ == "__main__":
    first()
    second()
