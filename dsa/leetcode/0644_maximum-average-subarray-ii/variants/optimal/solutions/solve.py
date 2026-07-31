def solve(nums: list[int], k: int) -> float:
    def feasible(average: float) -> bool:
        current_prefix = sum(value - average for value in nums[:k])
        if current_prefix >= 0:
            return True

        eligible_prefix = 0.0
        minimum_prefix = 0.0
        for right in range(k, len(nums)):
            current_prefix += nums[right] - average
            eligible_prefix += nums[right - k] - average
            minimum_prefix = min(minimum_prefix, eligible_prefix)
            if current_prefix - minimum_prefix >= 0:
                return True
        return False

    lower = float(min(nums))
    upper = float(max(nums))
    for _ in range(60):
        middle = (lower + upper) / 2
        if feasible(middle):
            lower = middle
        else:
            upper = middle
    return lower
