def solve(nums: list[int], k: int) -> bool:
    last_seen: dict[int, int] = {}
    for index, value in enumerate(nums):
        if value in last_seen and index - last_seen[value] <= k:
            return True
        last_seen[value] = index
    return False
