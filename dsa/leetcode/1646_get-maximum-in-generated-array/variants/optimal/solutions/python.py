def solve(n: int) -> int:
    if n == 0:
        return 0

    nums = [0] * (n + 1)
    nums[1] = 1
    maximum = 1
    for index in range(2, n + 1):
        half = index // 2
        nums[index] = nums[half] if index % 2 == 0 else nums[half] + nums[half + 1]
        maximum = max(maximum, nums[index])
    return maximum
