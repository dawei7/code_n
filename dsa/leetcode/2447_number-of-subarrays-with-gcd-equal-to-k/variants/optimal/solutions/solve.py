from math import gcd


def solve(nums: list[int], k: int) -> int:
    ending_counts: dict[int, int] = {}
    answer = 0

    for value in nums:
        next_counts = {value: 1}
        for previous_gcd, count in ending_counts.items():
            current_gcd = gcd(previous_gcd, value)
            next_counts[current_gcd] = next_counts.get(current_gcd, 0) + count

        ending_counts = next_counts
        answer += ending_counts.get(k, 0)

    return answer
