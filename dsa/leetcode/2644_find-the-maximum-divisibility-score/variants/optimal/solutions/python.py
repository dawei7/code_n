def solve(nums: list[int], divisors: list[int]) -> int:
    best_divisor = min(divisors)
    best_score = -1

    for divisor in divisors:
        score = sum(value % divisor == 0 for value in nums)
        if score > best_score or (score == best_score and divisor < best_divisor):
            best_divisor = divisor
            best_score = score

    return best_divisor
