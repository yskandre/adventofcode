def first():
    lines = open("7/hh.txt", "r").read().splitlines()

    bag_lookup = {}

    for line in lines:
        container, t = line.split(" contain ")
        content = t.split(", ")
        bags = {}
        for bag in content:
            if("no other" in bag):
                break
            bags[" ".join(bag.split(" ")[1:3])] = int(bag[0])

        bag_lookup[" ".join(container.split(" ")[0:2])] = bags

    def find_bag(name: str):
        valid_bags = set()
        valid_bags.add(name)
        done = False
        while not done:
            done = True
            for bag, inner in bag_lookup.items():
                if any(b in valid_bags for b in inner) and bag not in valid_bags:
                    valid_bags.add(bag)
                    done = False

        valid_bags.remove(name)
        return len(valid_bags)

    print(find_bag("shiny gold"))


def second():
    lines = open("7/hh.txt", "r").read().splitlines()

    bag_lookup = {}

    for line in lines:
        container, t = line.split(" contain ")
        content = t.split(", ")
        bags = {}
        for bag in content:
            if("no other" in bag):
                break
            bags[" ".join(bag.split(" ")[1:3])] = int(bag[0])

        bag_lookup[" ".join(container.split(" ")[0:2])] = bags

    def count_inner(name: str):
        bags = [name]
        count = 0
        while bags:
            for k, v in bag_lookup[bags.pop()].items():
                bags += [k] * v
                count += v

        return count

    print(count_inner("shiny gold"))


if __name__ == "__main__":
    first()
    second()
