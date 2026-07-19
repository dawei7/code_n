def solve(nums: list[int]) -> list[int]:
    seen = set()
    result = []
    for num in nums:
        if num in seen:
            result.append(num)
        else:
            seen.add(num)
    return result
