def solve(nums: list[int], queries: list[list[int]]) -> int:
    n = len(nums)

    def check(k: int) -> bool:
        possible = [1] * n
        masks = [(1 << (value + 1)) - 1 for value in nums]
        for left, right, value in queries[:k]:
            shift = 1 << value
            for index in range(left, right + 1):
                possible[index] = (possible[index] | (possible[index] * shift)) & masks[index]
        for index, value in enumerate(nums):
            if (possible[index] >> value) & 1 == 0:
                return False
        return True

    # Binary search for the minimum k in [0, len(queries)]
    low = 0
    high = len(queries)
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        if check(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans
