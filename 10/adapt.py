import math


def first():
    lines = open("10/aa.txt", "r").read().splitlines()

    single_steps = 0
    triple_steps = 1

    nums = [int(line) for line in lines]
    nums.sort()

    prev = 0

    for num in nums:
        if num - prev == 1:
            single_steps += 1
        elif num - prev == 3:
            triple_steps += 1
        prev = num

    print(single_steps*triple_steps)


def second():
    lines = open("10/aa.txt", "r").read().splitlines()

    nums = [0] + [int(line) for line in lines]
    nums.sort()
    nums.append(max(nums) + 3)

    split_sequences = []
    temp_sequence = []

    for i in range(len(nums) - 1):
        if nums[i + 1] - nums[i] == 3:
            if temp_sequence:
                temp_sequence.append(nums[i])
                split_sequences.append(temp_sequence.copy())
                temp_sequence.clear()
        else:
            temp_sequence.append(nums[i])

    variations = 1

    def trib(n):
        if n in [1, 2]:
            return 1
        if n == 3:
            return 2
        return (trib(n-1) + trib(n-2) + trib(n-3))

    for seq in split_sequences:
        print(trib(len(seq)))
        variations *= trib(len(seq))

    print(variations)


if __name__ == "__main__":
    first()
    second()
