"""Project Euler Problem 419: Look and Say Sequence.

Find A(n), B(n), C(n) mod 2^30 for n = 10^12, where A, B, C are the counts of digits 1, 2, 3
in the n-th term of the look-and-say sequence.
"""

from typing import Dict, List, Tuple

MOD_MASK = (1 << 30) - 1


def _say(s: str) -> str:
    if not s:
        return ""
    out_parts: List[str] = []
    n = len(s)
    i = 0
    while i < n:
        ch = s[i]
        j = i + 1
        while j < n and s[j] == ch:
            j += 1
        out_parts.append(str(j - i))
        out_parts.append(ch)
        i = j
    return "".join(out_parts)


def _spl00_at(s: str, j: int) -> bool:
    n = len(s)
    if j + 2 < n and s[j] == "1" and s[j + 1] == "1" and s[j + 2] == "1":
        return True
    if j == n - 1 and s[j] == "1":
        return False
    if j + 1 < n and s[j] == "1" and s[j + 1] == "1":
        return False
    if j + 2 < n and s[j] == "1" and s[j + 1] == "2" and s[j + 2] == "2":
        return False
    if j + 2 < n and s[j] == "1" and s[j + 1] == "3" and s[j + 2] == "3":
        return False
    if j < n and s[j] == "2":
        return False
    if (
        j + 3 < n
        and s[j] == "3"
        and s[j + 1] == "1"
        and s[j + 2] == "1"
        and s[j + 3] == "1"
    ):
        return False
    if (
        j + 3 < n
        and s[j] == "3"
        and s[j + 1] == "2"
        and s[j + 2] == "2"
        and s[j + 3] == "2"
    ):
        return False
    if j + 1 < n and s[j] == "3" and s[j + 1] == "3":
        return False
    return True


def _spl0_at(s: str, i: int) -> bool:
    n = len(s)
    ch = s[i]
    if ch == "1" and i == n - 1:
        return True
    if ch == "1" and i + 2 < n and s[i + 1] == "2" and s[i + 2] == "2":
        return _spl00_at(s, i + 3)
    if ch == "2":
        return _spl00_at(s, i + 1)
    if ch == "3" and i == n - 1:
        return True
    if ch == "3" and i + 2 < n and s[i + 1] == "2" and s[i + 2] == "2":
        return _spl00_at(s, i + 3)
    return False


def _split_elements(s: str) -> List[str]:
    if not s:
        return []
    parts: List[str] = []
    start = 0
    n = len(s)
    for i in range(n):
        if _spl0_at(s, i):
            parts.append(s[start : i + 1])
            start = i + 1
    if start < n:
        parts.append(s[start:])
    return parts


def _mat_mul(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
    m = len(a)
    res = [[0] * m for _ in range(m)]
    for i in range(m):
        ai = a[i]
        ri = res[i]
        for k in range(m):
            a_val = ai[k]
            if a_val:
                bk = b[k]
                for j in range(m):
                    ri[j] = (ri[j] + a_val * bk[j]) & MOD_MASK
    return res


def _vec_mul(v: List[int], m_mat: List[List[int]]) -> List[int]:
    m = len(v)
    out = [0] * m
    for i, a_val in enumerate(v):
        if a_val:
            row = m_mat[i]
            for j in range(m):
                out[j] = (out[j] + a_val * row[j]) & MOD_MASK
    return out


def _vec_mul_pow(
    v: List[int], m_mat: List[List[int]], exp: int
) -> List[int]:
    while exp > 0:
        if exp & 1:
            v = _vec_mul(v, m_mat)
        exp >>= 1
        if exp:
            m_mat = _mat_mul(m_mat, m_mat)
    return v


def _build_decay_system(
    seed_term: str,
) -> Tuple[
    List[str],
    List[List[int]],
    List[int],
    List[int],
    List[int],
    List[int],
]:
    seed_elements = _split_elements(seed_term)

    elems: List[str] = []
    idx: Dict[str, int] = {}

    def _add(e: str) -> int:
        j = idx.get(e)
        if j is None:
            j = len(elems)
            idx[e] = j
            elems.append(e)
        return j

    for e in seed_elements:
        _add(e)

    p = 0
    while p < len(elems):
        e = elems[p]
        d = _split_elements(_say(e))
        for child in d:
            _add(child)
        p += 1

    m = len(elems)
    m_mat = [[0] * m for _ in range(m)]
    for i, e in enumerate(elems):
        d = _split_elements(_say(e))
        row = m_mat[i]
        for child in d:
            row[idx[child]] += 1

    ones = [0] * m
    twos = [0] * m
    threes = [0] * m
    for i, e in enumerate(elems):
        ones[i] = e.count("1")
        twos[i] = e.count("2")
        threes[i] = e.count("3")

    v0 = [0] * m
    for e in seed_elements:
        v0[idx[e]] += 1

    return elems, m_mat, ones, twos, threes, v0


def solve(n_val: int = 10**12) -> str:
    """Find A(n_val), B(n_val), C(n_val) mod 2^30 using Conway's element decay matrix."""
    term = "1"
    for _ in range(1, min(n_val, 40)):
        term = _say(term)

    if n_val <= 40:
        return f"{term.count('1')},{term.count('2')},{term.count('3')}"

    _, m_mat, ones, twos, threes, v = _build_decay_system(term)
    v = _vec_mul_pow(v, m_mat, n_val - 40)

    a_cnt = 0
    b_cnt = 0
    c_cnt = 0
    for i, cnt in enumerate(v):
        if cnt:
            a_cnt = (a_cnt + cnt * ones[i]) & MOD_MASK
            b_cnt = (b_cnt + cnt * twos[i]) & MOD_MASK
            c_cnt = (c_cnt + cnt * threes[i]) & MOD_MASK
    return f"{a_cnt},{b_cnt},{c_cnt}"


if __name__ == "__main__":
    print(solve())
