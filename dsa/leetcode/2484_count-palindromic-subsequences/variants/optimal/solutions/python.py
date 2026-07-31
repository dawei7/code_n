def solve(s):
    MODULUS = 1_000_000_007
    left_single = [0] * 10
    right_single = [0] * 10
    left_pairs = [[0] * 10 for _ in range(10)]
    right_pairs = [[0] * 10 for _ in range(10)]

    for ch in s:
        digit = ord(ch) - ord("0")
        for first in range(10):
            right_pairs[first][digit] += right_single[first]
        right_single[digit] += 1

    answer = 0

    for ch in s:
        digit = ord(ch) - ord("0")

        right_single[digit] -= 1
        for second in range(10):
            right_pairs[digit][second] -= right_single[second]

        for first in range(10):
            for second in range(10):
                answer += (
                    left_pairs[first][second]
                    * right_pairs[second][first]
                )
        answer %= MODULUS

        for first in range(10):
            left_pairs[first][digit] += left_single[first]
        left_single[digit] += 1

    return answer
