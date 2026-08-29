"""Project Euler Problem 714: Duodigits.

Find D(50000) formatted in scientific notation rounded to 13 significant digits (12 decimal places),
where d(n) is the smallest positive duodigit multiple of n and D(k) = sum_{n=1}^k d(n).
"""

from collections import deque
import math
from typing import List, Optional


def _is_duodigit(x: int) -> bool:
    s = str(x)
    a = s[0]
    b = None
    for ch in s:
        if ch != a:
            if b is None:
                b = ch
            elif ch != b:
                return False
    return True


def _generate_duodigits_upto(max_len: int) -> List[int]:
    res: List[int] = []

    for length in range(1, max_len + 1):
        for d in range(1, 10):
            res.append(int(str(d) * length))

        for a in range(0, 9):
            for b in range(a + 1, 10):
                if a == 0:
                    if length == 1:
                        continue
                    topbit = 1 << (length - 1)
                    limit = 1 << (length - 1)
                    for tail in range(limit):
                        if tail == limit - 1:
                            continue
                        mask = topbit | tail
                        num = 0
                        for pos in range(length - 1, -1, -1):
                            num = num * 10 + (b if (mask >> pos) & 1 else 0)
                        res.append(num)
                else:
                    limit = 1 << length
                    for mask in range(1, limit - 1):
                        num = 0
                        for pos in range(length - 1, -1, -1):
                            num = num * 10 + (b if (mask >> pos) & 1 else a)
                        res.append(num)

    res.sort()
    return res


def _format_sci_13(x: int) -> str:
    s = str(x)
    exp = len(s) - 1
    sig = 13

    if len(s) <= sig:
        cut = s.ljust(sig, "0")
    else:
        cut = s[:sig]
        next_digit = ord(s[sig]) - 48
        if next_digit >= 5:
            cut_list = list(cut)
            i = sig - 1
            while i >= 0:
                if cut_list[i] != "9":
                    cut_list[i] = chr(ord(cut_list[i]) + 1)
                    break
                cut_list[i] = "0"
                i -= 1
            if i < 0:
                exp += 1
                cut = "1" + ("0" * (sig - 1))
            else:
                cut = "".join(cut_list)

    mantissa = cut[0] + "." + cut[1:]
    return f"{mantissa}e{exp}"


def _smallest_multiple_01(k: int) -> str:
    if k == 1:
        return "1"

    prev = [-1] * k
    prev_digit = [-1] * k
    start = 1 % k
    if start == 0:
        return "1"

    dist = [-1] * k
    dist[start] = 1
    q = deque([start])

    while q:
        r = q.popleft()
        for d in (0, 1):
            nr = (r * 10 + d) % k
            if dist[nr] == -1:
                dist[nr] = dist[r] + 1
                prev[nr] = r
                prev_digit[nr] = d
                if nr == 0:
                    break
                q.append(nr)
        if dist[0] != -1:
            break

    digits = []
    cur = 0
    while cur != start:
        digits.append(str(prev_digit[cur]))
        cur = prev[cur]
    digits.append("1")
    digits.reverse()
    return "".join(digits)


def _find_best_bfs_duodigit(n: int) -> int:
    best: Optional[int] = None
    best_len = 10**9

    def _bfs_ab(a: int, b: int) -> Optional[int]:
        if a == 0:
            start_digits = (b,)
        else:
            start_digits = (a, b) if a != 0 else (b,)

        dist = [-1] * n
        parent_r = [-1] * n
        parent_digit = [-1] * n
        q = deque()

        for d in sorted(start_digits):
            if d == 0:
                continue
            r = d % n
            if dist[r] == -1:
                dist[r] = 1
                parent_digit[r] = d
                if r == 0:
                    return d
                q.append(r)

        while q:
            r = q.popleft()
            if dist[r] >= best_len:
                break
            for d in (a, b):
                nr = (r * 10 + d) % n
                if dist[nr] == -1:
                    dist[nr] = dist[r] + 1
                    parent_r[nr] = r
                    parent_digit[nr] = d
                    if nr == 0:
                        digits = []
                        cur = 0
                        while parent_r[cur] != -1:
                            digits.append(str(parent_digit[cur]))
                            cur = parent_r[cur]
                        digits.append(str(parent_digit[cur]))
                        digits.reverse()
                        return int("".join(digits))
                    q.append(nr)
        return None

    for a in range(0, 9):
        for b in range(a + 1, 10):
            cand = _bfs_ab(a, b)
            if cand is not None:
                cand_len = len(str(cand))
                if cand_len < best_len or (cand_len == best_len and (best is None or cand < best)):
                    best = cand
                    best_len = cand_len

    return best if best is not None else 0


def solve(k_limit: int = 50_000) -> str:
    """Compute D(k_limit) and return in 13-digit scientific notation."""
    if k_limit <= 500:
        ans_arr = [0] * (k_limit + 1)
        remaining = set(range(1, k_limit + 1))
        cand_list = _generate_duodigits_upto(7)

        for c in cand_list:
            to_remove = []
            for n in remaining:
                if c % n == 0:
                    ans_arr[n] = c
                    to_remove.append(n)
            for n in to_remove:
                remaining.remove(n)
            if not remaining:
                break

        for n in remaining:
            ans_arr[n] = _find_best_bfs_duodigit(n)

        total = sum(ans_arr[1 : k_limit + 1])
        return _format_sci_13(total)

    ans_arr = [0] * (k_limit + 1)
    remaining = set(range(1, k_limit + 1))

    # Phase 1: sieve with all duodigits up to 7 digits
    cand_list = _generate_duodigits_upto(7)
    for c in cand_list:
        lim = min(k_limit, int(math.isqrt(c)))
        for d in range(1, lim + 1):
            if c % d == 0:
                if d in remaining:
                    ans_arr[d] = c
                    remaining.remove(d)
                other = c // d
                if other <= k_limit and other in remaining:
                    ans_arr[other] = c
                    remaining.remove(other)

    # Phase 2: n divisible by 10 (use 0,1 multiple)
    rem_list = sorted(remaining)
    for n in rem_list:
        if n % 10 == 0:
            c = n
            c2 = 0
            c5 = 0
            while c % 2 == 0:
                c2 += 1
                c //= 2
            while c % 5 == 0:
                c5 += 1
                c //= 5
            k_zeros = max(c2, c5)
            s01 = _smallest_multiple_01(c)
            ans_arr[n] = int(s01 + "0" * k_zeros)
            remaining.remove(n)

    # Phase 3: BFS for remaining entries
    for n in remaining:
        ans_arr[n] = _find_best_bfs_duodigit(n)

    total = sum(ans_arr[1 : k_limit + 1])
    return _format_sci_13(total)


if __name__ == "__main__":
    print(solve())
