def digit_sum(value: int) -> int:
    return sum(map(int, str(value)))


def solve(nums: list[int]) -> int:
    target = sorted(nums, key=lambda value: (digit_sum(value), value))
    position = {value: index for index, value in enumerate(nums)}
    swaps = 0

    for index, value in enumerate(target):
        current = position[value]
        if current == index:
            continue

        displaced = nums[index]
        nums[index], nums[current] = nums[current], nums[index]
        position[value] = index
        position[displaced] = current
        swaps += 1

    return swaps
