"""Project Euler Problem 551: Sum of Digits Sequence.

Find a_{10^15}, where a_0 = 1, a_1 = 1, and a_{n+1} = a_n + S(a_n) for n >= 1,
with S(x) being the sum of decimal digits of x.
"""

from typing import Dict, Tuple


def _digit_sum(n: int) -> int:
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


def solve(target_n: int = 10**15) -> int:
    """Compute a_{target_n} using hierarchical multi-scale block digit-sum jump table DP."""
    if target_n <= 1:
        return 1

    memo: Dict[Tuple[int, int, int], Tuple[int, int]] = {}

    def get_jump(k: int, r: int, s: int) -> Tuple[int, int]:
        key = (k, r, s)
        if key in memo:
            return memo[key]

        if k == 1:
            steps = 0
            curr_r = r
            while curr_r < 10:
                curr_r += s + curr_r
                steps += 1
            res = (steps, curr_r - 10)
            memo[key] = res
            return res

        base = 10 ** (k - 1)
        hi = r // base
        lo = r % base
        steps = 0

        while hi < 10:
            sub_steps, next_lo = get_jump(k - 1, lo, s + hi)
            steps += sub_steps
            hi += 1
            while next_lo >= base:
                hi += 1
                next_lo -= base
            lo = next_lo

        res = (steps, hi * base + lo - 10**k)
        memo[key] = res
        return res

    x = 1
    steps_left = target_n - 1

    while steps_left > 0:
        advanced = False
        str_x = str(x)
        max_k = min(len(str_x) + 1, 16)
        for k in range(max_k, 0, -1):
            base = 10**k
            p = x // base
            r = x % base
            s = _digit_sum(p)
            jump_steps, next_r = get_jump(k, r, s)
            if jump_steps <= steps_left:
                steps_left -= jump_steps
                x = (p + 1) * base + next_r
                advanced = True
                break
        if not advanced:
            x += _digit_sum(x)
            steps_left -= 1

    return x


if __name__ == "__main__":
    print(solve())
