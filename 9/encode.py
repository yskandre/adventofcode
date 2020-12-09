from itertools import combinations


def first():
    lines = open("9/ee.txt", "r").read().splitlines()
    numbers = [int(i) for i in lines]

    for index in range(25, len(numbers)):
        done = True
        for x, y in combinations(numbers[index-25:index], 2):
            if x + y == numbers[index]:
                done = False
                break
        if done:
            print(numbers[index])
            break


def second():
    lines = open("9/ee.txt", "r").read().splitlines()
    numbers = [int(i) for i in lines]

    upper_bound = 611
    target = 466456641

    sum = 0
    list = []

    for ceiling in range(upper_bound):
        sum += numbers[ceiling]
        list.append(numbers[ceiling])
        while sum > target:
            sum -= list.pop(0)
        if sum == target:
            print(min(list) + max(list))
            break


if __name__ == "__main__":
    first()
    second()
