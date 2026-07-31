MODULUS = 1_000_000_007


def solve(nums: list[int]) -> int:
    nums.sort()
    answer = 0
    weighted_minima = 0
    for strength in nums:
        answer = (answer + strength * strength * (strength + weighted_minima)) % MODULUS
        weighted_minima = (2 * weighted_minima + strength) % MODULUS
    return answer
