"""Project Euler Problem 685: Inverse Digit Sum II.

Find S(10000) mod 1000000007, where S(k) = sum_{n=1}^k f(n^3, n^4),
and f(s, m) is the m-th positive integer with digit sum s.
"""

from typing import Tuple

_MOD = 1_000_000_007
_INV9 = pow(9, _MOD - 2, _MOD)


def _comb(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)
    if k == 0:
        return 1
    res = 1
    for i in range(1, k + 1):
        res = (res * (n - k + i)) // i
    return res


def _count_deficit_sequences(length: int, deficit: int) -> int:
    if deficit < 0:
        return 0
    if length == 0:
        return 1 if deficit == 0 else 0

    res = 0
    max_j = deficit // 10
    for j in range(max_j + 1):
        d = deficit - 10 * j
        term = _comb(length, j) * _comb(d + length - 1, d)
        res = res - term if (j & 1) else res + term
    return res


def _count_len_with_digit_sum(length: int, digit_sum: int) -> int:
    deficit = 9 * length - digit_sum
    if deficit < 0:
        return 0
    total = _count_deficit_sequences(length, deficit)
    if deficit >= 9:
        total -= _count_deficit_sequences(length - 1, deficit - 9)
    return total


def _find_length_and_rank(digit_sum: int, m: int) -> Tuple[int, int]:
    length = (digit_sum + 8) // 9
    passed = 0
    while True:
        cnt = _count_len_with_digit_sum(length, digit_sum)
        if passed + cnt >= m:
            return length, m - passed
        passed += cnt
        length += 1


def _append_repeat_mod(prefix_mod: int, digit: int, count: int) -> int:
    if count <= 0:
        return prefix_mod
    pow10 = pow(10, count, _MOD)
    if digit == 0:
        block = 0
    else:
        block = digit * (pow10 - 1) % _MOD
        block = block * _INV9 % _MOD
    return (prefix_mod * pow10 + block) % _MOD


def _f_mod(digit_sum: int, m: int) -> int:
    length, k = _find_length_and_rank(digit_sum, m)
    deficit = 9 * length - digit_sum

    value_mod = 0
    for dig in range(1, 10):
        used = 9 - dig
        if used > deficit:
            continue
        cnt = _count_deficit_sequences(length - 1, deficit - used)
        if k > cnt:
            k -= cnt
        else:
            value_mod = dig % _MOD
            length -= 1
            deficit -= used
            break
    else:
        raise RuntimeError("Failed to choose leading digit")

    while length > 0:
        if deficit == 0:
            value_mod = _append_repeat_mod(value_mod, 9, length)
            break

        total = _count_deficit_sequences(length, deficit)
        tail = _count_deficit_sequences(length - 1, deficit)

        if tail > 0 and k > total - tail:
            need = total - k + 1
            lo = (deficit + 8) // 9
            hi = length
            while lo < hi:
                mid = (lo + hi) // 2
                if _count_deficit_sequences(mid, deficit) >= need:
                    hi = mid
                else:
                    lo = mid + 1
            t = lo
            prefix_9 = length - t
            if prefix_9 > 0:
                value_mod = _append_repeat_mod(value_mod, 9, prefix_9)
                k -= total - _count_deficit_sequences(t, deficit)
                length = t
                continue

        chosen = False
        for dig in range(0, 9):
            used = 9 - dig
            if used > deficit:
                continue
            cnt = _count_deficit_sequences(length - 1, deficit - used)
            if k > cnt:
                k -= cnt
            else:
                value_mod = (value_mod * 10 + dig) % _MOD
                length -= 1
                deficit -= used
                chosen = True
                break

        if not chosen:
            value_mod = (value_mod * 10 + 9) % _MOD
            length -= 1

    return value_mod


def solve(k_limit: int = 10_000) -> int:
    """Compute S(k_limit) = sum_{n=1}^{k_limit} f(n^3, n^4) modulo 1000000007."""
    total = 0
    for n in range(1, k_limit + 1):
        total = (total + _f_mod(n * n * n, n * n * n * n)) % _MOD
    return total


if __name__ == "__main__":
    print(solve())
