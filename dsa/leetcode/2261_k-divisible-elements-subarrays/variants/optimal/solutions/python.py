def solve(nums: list[int], k: int, p: int) -> int:
    root: dict[int, dict] = {}
    distinct = 0

    for left in range(len(nums)):
        node = root
        divisible = 0
        for right in range(left, len(nums)):
            divisible += nums[right] % p == 0
            if divisible > k:
                break
            value = nums[right]
            if value not in node:
                node[value] = {}
                distinct += 1
            node = node[value]

    return distinct
