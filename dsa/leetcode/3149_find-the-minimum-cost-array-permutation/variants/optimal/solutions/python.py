def solve(nums: list[int]) -> list[int]:
    from functools import lru_cache

    n = len(nums)
    full_mask = (1 << n) - 1

    @lru_cache(None)
    def best(mask: int, last: int) -> int:
        if mask == full_mask:
            return abs(nums[last] - 0)

        answer = float("inf")
        for nxt in range(n):
            if mask & (1 << nxt):
                continue
            answer = min(answer, abs(nums[last] - nxt) + best(mask | (1 << nxt), nxt))
        return int(answer)

    result = [0]
    mask = 1
    last = 0
    while mask != full_mask:
        target = best(mask, last)
        for nxt in range(n):
            if mask & (1 << nxt):
                continue
            if abs(nums[last] - nxt) + best(mask | (1 << nxt), nxt) == target:
                result.append(nxt)
                mask |= 1 << nxt
                last = nxt
                break

    return result
