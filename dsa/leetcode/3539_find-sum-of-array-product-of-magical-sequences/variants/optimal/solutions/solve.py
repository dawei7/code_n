from functools import cache


def solve(m: int, k: int, nums: list[int]) -> int:
    modulus = 1_000_000_007

    combinations = [[0] * (m + 1) for _ in range(m + 1)]
    for total in range(m + 1):
        combinations[total][0] = 1
        combinations[total][total] = 1
        for chosen in range(1, total):
            combinations[total][chosen] = (
                combinations[total - 1][chosen - 1] + combinations[total - 1][chosen]
            ) % modulus

    powers = []
    for value in nums:
        row = [1] * (m + 1)
        for count in range(1, m + 1):
            row[count] = row[count - 1] * value % modulus
        powers.append(row)

    @cache
    def dp(
        index: int,
        remaining: int,
        set_bits: int,
        carry: int,
    ) -> int:
        if index == len(nums):
            return int(remaining == 0 and set_bits + carry.bit_count() == k)

        answer = 0
        for take in range(remaining + 1):
            combined = carry + take
            next_set_bits = set_bits + (combined & 1)
            if next_set_bits <= k:
                answer += (
                    combinations[remaining][take]
                    * powers[index][take]
                    * dp(
                        index + 1,
                        remaining - take,
                        next_set_bits,
                        combined >> 1,
                    )
                )

        return answer % modulus

    return dp(0, m, 0, 0)
