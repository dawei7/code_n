"""Project Euler Problem 473: Phigital Number Base.

Find the sum of all positive integers not exceeding 10^10 whose phigital representation is palindromic.
"""

from decimal import Decimal, getcontext
from math import ceil, log
from typing import List, Set, Tuple

getcontext().prec = 25


def _fibonacci(n: int) -> int:
    v1, v2, v3 = 1, 1, 0
    for rec in bin(n)[3:]:
        calc = v2 * v2
        v1, v2, v3 = v1 * v1 + calc, (v1 + v3) * v2, calc + v3 * v3
        if rec == "1":
            v1, v2, v3 = v1 + v2, v1, v2
    return v2


def solve(limit: int = 10**10) -> int:
    """Compute the sum of palindromic phigital integers up to limit using Fibonacci basis generation."""
    gr = Decimal(1 + Decimal(5).sqrt()) / Decimal(2)
    pow_lim = ceil(log(limit, float(gr)))
    fib_nums = [0] + [_fibonacci(i) for i in range(1, pow_lim + 60)]

    possib: List[Decimal] = []
    for n in range(1, pow_lim + 1):
        if n % 2 == 0:
            t = Decimal(fib_nums[n] + fib_nums[n + 1]) * gr + Decimal(
                fib_nums[n - 1] - fib_nums[n + 2]
            )
        else:
            t = Decimal(fib_nums[n] - fib_nums[n + 1]) * gr + Decimal(
                fib_nums[n - 1] + fib_nums[n + 2]
            )
        if t < limit:
            possib.append(t)

    principal = [1, 2]
    derived: Set[int] = set()
    main_items: List[Tuple[Decimal, List[int]]] = [(Decimal(2), [1, 0])]
    sub_items: List[Tuple[Decimal, List[int]]] = [(Decimal(2), [1, 0])]

    for x in range(1, len(possib) - 2):
        for y in range(x + 2, len(possib)):
            t_val = possib[x] + possib[y]
            if t_val < limit:
                if round(t_val, 1) == t_val:
                    principal.append(int(t_val))
                    main_items.append((t_val, [x, y]))
                    sub_items.append((t_val, [x, y]))

    sub_items.sort(key=lambda item: item[0])
    count = 0
    prev_sum_1 = 0
    prev_sum_2 = 1

    while sub_items:
        curr_sum = sum(principal) + sum(derived)
        if (
            round(curr_sum, 1) == round(prev_sum_2, 1)
            and round(prev_sum_2, 1) == round(prev_sum_1, 1)
        ):
            return int(curr_sum)
        prev_sum_1 = prev_sum_2
        prev_sum_2 = curr_sum

        count += 1
        a_val, b_indices = sub_items.pop(0)
        if a_val > limit / 2:
            break

        for x in range(count, len(main_items)):
            c_val, d_indices = main_items[x]
            if a_val + c_val < limit:
                min_diff = min(
                    abs(i - j) for i in b_indices for j in d_indices
                )
                if min_diff >= 2:
                    sub_items.append((a_val + c_val, b_indices + d_indices))
                    main_items.append(
                        (a_val + c_val, b_indices + d_indices)
                    )
                    derived.add(int(a_val + c_val))

    return int(sum(principal) + sum(derived))


if __name__ == "__main__":
    print(solve())
