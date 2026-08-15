"""Project Euler 305: Reflexive Position

Find sum_{k=1}^{13} f(3^k), where f(n) is the starting position of the n-th occurrence of n
in the Champernowne-like concatenated string S = 123456789101112...
"""

from __future__ import annotations

import bisect


def start_pos(x: int) -> int:
    """Returns the 1-based start position of integer x in the Champernowne string S."""
    l_len = len(str(x))
    pos = 1
    for d in range(1, l_len):
        pos += d * 9 * (10 ** (d - 1))
    pos += l_len * (x - 10 ** (l_len - 1))
    return pos


def find_f(n: int) -> int:
    """Finds the starting index of the n-th occurrence of string n in S

    using sparse boundary candidate generation and O(1) arithmetic counting per length/offset.
    """
    w = str(n)
    k = len(w)

    # 1. Collect all boundary/split occurrences (Case 2) where W spans across adjacent numbers
    case2_positions: set[int] = set()
    for s in range(1, k):
        a = w[:s]
        b = w[s:]
        len_a = len(a)
        len_b = len(b)

        for l_val in range(len_a, k + 4):
            j = l_val - len_a
            if len_b >= l_val:
                x_plus_1 = int(b[:l_val])
                x = x_plus_1 - 1
                if len(str(x)) == l_val and str(x).endswith(a):
                    stream = ""
                    nxt = x + 1
                    while len(stream) < len_b:
                        stream += str(nxt)
                        nxt += 1
                    if stream.startswith(b):
                        case2_positions.add(start_pos(x) + j)
            else:
                if k > l_val:
                    for x in range(10 ** (l_val - 1), 10**l_val):
                        if str(x).endswith(a):
                            stream = ""
                            nxt = x + 1
                            while len(stream) < len_b:
                                stream += str(nxt)
                                nxt += 1
                            if stream.startswith(b):
                                case2_positions.add(start_pos(x) + j)
                else:
                    free_len = l_val - k
                    if int(a) + 1 < 10**len_a:
                        for mid_val in range(10**free_len):
                            mid_str = (
                                f"{mid_val:0{free_len}d}" if free_len > 0 else ""
                            )
                            x_plus_1 = int(
                                b + mid_str + f"{int(a) + 1:0{len_a}d}"
                            )
                            x = x_plus_1 - 1
                            if len(str(x)) == l_val and str(x).endswith(a):
                                case2_positions.add(start_pos(x) + j)
                    else:
                        for mid_val in range(10**free_len):
                            mid_str = (
                                f"{mid_val:0{free_len}d}" if free_len > 0 else ""
                            )
                            x = int(b + mid_str + a)
                            if len(str(x)) == l_val and str(x + 1).startswith(
                                b
                            ):
                                case2_positions.add(start_pos(x) + j)

    case2_sorted = sorted(list(case2_positions))

    # 2. Function to count total occurrences of W starting at or before pos_limit
    def count_up_to(pos_limit: int) -> int:
        cnt = bisect.bisect_right(case2_sorted, pos_limit)
        for l_val in range(1, 16):
            base_l = start_pos(10 ** (l_val - 1))
            for j in range(l_val):
                if j + k <= l_val:
                    s_len = l_val - j - k
                    p_len = j
                    if pos_limit < base_l + j:
                        continue
                    max_allowed_x = 10 ** (l_val - 1) + (
                        pos_limit - j - base_l
                    ) // l_val
                    if max_allowed_x > 10**l_val - 1:
                        max_allowed_x = 10**l_val - 1
                    if max_allowed_x < 10 ** (l_val - 1):
                        continue

                    p_min = (
                        10 ** (p_len - 1)
                        if p_len > 0
                        else (0 if w[0] != "0" else 1)
                    )
                    if p_len == 0 and w[0] == "0":
                        continue
                    p_max = 10**p_len - 1 if p_len > 0 else 0

                    shift = 10 ** (s_len + k)
                    mid = int(w) * (10**s_len)

                    full_p_max = (
                        max_allowed_x - mid - (10**s_len - 1)
                    ) // shift
                    if full_p_max >= p_min:
                        valid_full_p = min(p_max, full_p_max) - p_min + 1
                        cnt += valid_full_p * (10**s_len)

                    partial_p = full_p_max + 1
                    if p_min <= partial_p <= p_max:
                        base_x = partial_p * shift + mid
                        if base_x <= max_allowed_x:
                            cnt += max_allowed_x - base_x + 1
        return cnt

    # Binary search for the minimal index pos such that count_up_to(pos) >= n
    low = 1
    high = 10**18
    while low < high:
        mid = (low + high) // 2
        if count_up_to(mid) >= n:
            high = mid
        else:
            low = mid + 1

    return low


def solve(max_k: int = 13) -> str:
    """Calculates sum_{k=1}^{max_k} f(3^k)."""
    total = sum(find_f(3**k) for k in range(1, max_k + 1))
    return str(total)


if __name__ == "__main__":
    print(solve())
