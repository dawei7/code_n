from math import gcd


def solve(nums: list[int], k: int) -> int:
    answer = 0
    n = len(nums)

    for left in range(n):
        common = 0
        minimum_twos = 100
        minimum_count = 0

        for right in range(left, n):
            value = nums[right]
            common = gcd(common, value)
            twos = (value & -value).bit_length() - 1
            if twos < minimum_twos:
                minimum_twos = twos
                minimum_count = 1
            elif twos == minimum_twos:
                minimum_count += 1

            multiplier = 2 if minimum_count <= k else 1
            answer = max(answer, (right - left + 1) * common * multiplier)

    return answer
