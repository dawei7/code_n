"""Project Euler Problem 426: Box-Ball System.

Find the sum of squares of the final state elements in the Box-Ball System
starting with configuration (t_0, t_1, ..., t_{10_000_000}).
"""

from typing import Iterator, List


def _t_sequence_runs(n: int) -> Iterator[int]:
    s = 290797
    for _ in range(n + 1):
        yield (s % 64) + 1
        s = (s * s) % 50515093


def solve(n: int = 10_000_000) -> int:
    """Compute the sum of squares of soliton lengths using Takahashi-Satsuma stack reduction."""
    stack_sym: List[int] = [0]
    stack_len: List[int] = [10**18]

    sum_sq = 0
    total_balls = 0
    cur_sym = 1

    for run_len in _t_sequence_runs(n):
        if cur_sym == 1:
            total_balls += run_len

        if stack_sym[-1] == cur_sym:
            stack_len[-1] += run_len
        else:
            stack_sym.append(cur_sym)
            stack_len.append(run_len)

        while len(stack_len) >= 2 and stack_len[-1] >= stack_len[-2]:
            k = stack_len[-2]
            sum_sq += k * k

            cur_s = stack_sym[-1]
            cur_l = stack_len[-1] - k

            stack_sym.pop()
            stack_len.pop()
            stack_sym.pop()
            stack_len.pop()

            if cur_l > 0:
                if stack_sym[-1] == cur_s:
                    stack_len[-1] += cur_l
                else:
                    stack_sym.append(cur_s)
                    stack_len.append(cur_l)

        cur_sym ^= 1

    trailing_zeros = total_balls + 100
    if stack_sym[-1] == 0:
        stack_len[-1] += trailing_zeros
    else:
        stack_sym.append(0)
        stack_len.append(trailing_zeros)

    while len(stack_len) >= 2 and stack_len[-1] >= stack_len[-2]:
        k = stack_len[-2]
        sum_sq += k * k

        cur_s = stack_sym[-1]
        cur_l = stack_len[-1] - k

        stack_sym.pop()
        stack_len.pop()
        stack_sym.pop()
        stack_len.pop()

        if cur_l > 0:
            if stack_sym[-1] == cur_s:
                stack_len[-1] += cur_l
            else:
                stack_sym.append(cur_s)
                stack_len.append(cur_l)

    return sum_sq


if __name__ == "__main__":
    print(solve())
