from collections import Counter


def solve(nums: list[int]) -> bool:
    unused = Counter(nums)
    endings = Counter()
    for value in nums:
        if unused[value] == 0:
            continue
        unused[value] -= 1
        if endings[value - 1] > 0:
            endings[value - 1] -= 1
            endings[value] += 1
        elif unused[value + 1] > 0 and unused[value + 2] > 0:
            unused[value + 1] -= 1
            unused[value + 2] -= 1
            endings[value + 2] += 1
        else:
            return False
    return True
