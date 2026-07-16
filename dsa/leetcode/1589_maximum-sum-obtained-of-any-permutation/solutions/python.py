def solve(nums: list[int], requests: list[list[int]]) -> int:
    length = len(nums)
    difference = [0] * (length + 1)
    for left, right in requests:
        difference[left] += 1
        difference[right + 1] -= 1

    coverage: list[int] = []
    active = 0
    for index in range(length):
        active += difference[index]
        coverage.append(active)

    values = sorted(nums)
    coverage.sort()
    return sum(value * count for value, count in zip(values, coverage)) % 1_000_000_007
