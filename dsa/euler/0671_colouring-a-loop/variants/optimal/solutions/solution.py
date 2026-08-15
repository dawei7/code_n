"""Project Euler Problem 671: Colouring a Loop.

Find F_10(10004003002001) mod 1000004321, where F_k(n) is the number of valid k-coloured tilings
of a 2xn closed loop with 1x1, 1x2, and 1x3 tiles with no 4 corners meeting.
"""

from typing import Dict, Iterable, List, Tuple

_MOD = 1_000_004_321

# State encoding: (v_prev, t_state, b_state, top_color, bottom_color)
# Row states: 0 = free, 1 = incoming tile ends here, 2 = incoming tile continues.
State = Tuple[int, int, int, int, int]


def _next_from_incoming(row_state: int) -> int:
    if row_state == 1:
        return 0
    if row_state == 2:
        return 1
    raise ValueError("row_state must be incoming")


def _next_from_length(length: int) -> int:
    if length == 1:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2
    raise ValueError("length must be 1, 2, or 3")


def _normalize_colors(fixed: int, top: int, bottom: int) -> Tuple[int, int]:
    mapping: Dict[int, int] = {}
    next_label = fixed

    def norm(label: int) -> int:
        nonlocal next_label
        if label < fixed:
            return label
        if label not in mapping:
            mapping[label] = next_label
            next_label += 1
        return mapping[label]

    return norm(top), norm(bottom)


def _valid_state(state: State) -> bool:
    v_prev, t_state, b_state, top_color, bottom_color = state
    if t_state not in (0, 1, 2) or b_state not in (0, 1, 2):
        return False
    if v_prev == 1:
        if t_state != 0 or b_state != 0:
            return False
        if top_color != bottom_color:
            return False
    else:
        if top_color == bottom_color:
            return False
    return True


def _transitions(state: State, k: int, fixed: int) -> Dict[State, int]:
    v_prev, t_state, b_state, top_color, bottom_color = state
    if not _valid_state(state):
        return {}

    in_t = t_state != 0
    in_b = b_state != 0

    total_other = k - fixed
    other_labels = sorted({c for c in (top_color, bottom_color) if c >= fixed})
    m_val = len(other_labels)
    unused_other = total_other - m_val
    existing_labels = list(range(fixed)) + other_labels

    out: Dict[State, int] = {}

    def add(
        v_cur: int,
        t_next: int,
        b_next: int,
        new_top: int,
        new_bottom: int,
        weight: int,
    ) -> None:
        if weight <= 0:
            return
        if v_prev == 0 and v_cur == 0 and not in_t and not in_b:
            return
        if v_cur == 1 and (t_next != 0 or b_next != 0):
            return
        top_n, bottom_n = _normalize_colors(fixed, new_top, new_bottom)
        ns = (v_cur, t_next, b_next, top_n, bottom_n)
        out[ns] = (out.get(ns, 0) + weight) % _MOD

    def single_choices(
        forbidden: Iterable[int],
    ) -> Iterable[Tuple[int, int, bool]]:
        forbid = set(forbidden)
        for label in existing_labels:
            if label not in forbid:
                yield (label, 1, False)
        if unused_other > 0:
            yield (-1, unused_other, True)

    def pair_choices(
        forbid_top: Iterable[int], forbid_bottom: Iterable[int]
    ) -> Iterable[Tuple[int, int, int]]:
        forbid_t = set(forbid_top)
        forbid_b = set(forbid_bottom)
        existing_t = [
            label for label in existing_labels if label not in forbid_t
        ]
        existing_b = [
            label for label in existing_labels if label not in forbid_b
        ]

        for ct in existing_t:
            for cb in existing_b:
                if ct != cb:
                    yield (ct, cb, 1)
        if unused_other > 0:
            for ct in existing_t:
                yield (ct, -1, unused_other)
            for cb in existing_b:
                yield (-1, cb, unused_other)
            if unused_other > 1:
                yield (-1, -1, unused_other * (unused_other - 1))

    # Case 1: both rows incoming
    if in_t and in_b:
        add(
            0,
            _next_from_incoming(t_state),
            _next_from_incoming(b_state),
            top_color,
            bottom_color,
            1,
        )
        return out

    # Case 2: top incoming, bottom new
    if in_t and not in_b:
        t_next = _next_from_incoming(t_state)
        for cb, weight, is_new in single_choices(
            (bottom_color, top_color)
        ):
            actual_cb = fixed + m_val if is_new else cb
            for length in (1, 2, 3):
                b_next = _next_from_length(length)
                add(0, t_next, b_next, top_color, actual_cb, weight)
        return out

    # Case 3: bottom incoming, top new
    if not in_t and in_b:
        b_next = _next_from_incoming(b_state)
        for ct, weight, is_new in single_choices(
            (top_color, bottom_color)
        ):
            actual_ct = fixed + m_val if is_new else ct
            for length in (1, 2, 3):
                t_next = _next_from_length(length)
                add(0, t_next, b_next, actual_ct, bottom_color, weight)
        return out

    # Case 4: neither incoming
    # Option A: vertical domino
    for label, mult, is_new in single_choices((top_color, bottom_color)):
        c = fixed + m_val if is_new else label
        add(1, 0, 0, c, c, mult)

    # Option B: two horizontal tiles
    for lt in (1, 2, 3):
        t_next = _next_from_length(lt)
        for lb in (1, 2, 3):
            b_next = _next_from_length(lb)
            for ct, cb, mult in pair_choices((top_color,), (bottom_color,)):
                if ct == -1:
                    ct_label = fixed + m_val
                    if cb == -1:
                        cb_label = fixed + m_val + 1
                    else:
                        cb_label = cb
                else:
                    ct_label = ct
                    if cb == -1:
                        cb_label = fixed + m_val
                    else:
                        cb_label = cb
                add(0, t_next, b_next, ct_label, cb_label, mult)

    return out


def _build_matrix(
    k: int, fixed: int, seed_states: List[State]
) -> Tuple[List[List[int]], Dict[State, int]]:
    states: List[State] = []
    index: Dict[State, int] = {}
    queue: List[State] = []

    for s in seed_states:
        ns = _valid_state(s) and (
            s[0],
            s[1],
            s[2],
            *_normalize_colors(fixed, s[3], s[4]),
        )
        if not ns or not _valid_state(ns):
            continue
        if ns not in index:
            index[ns] = len(states)
            states.append(ns)
            queue.append(ns)

    qi = 0
    while qi < len(queue):
        s = queue[qi]
        qi += 1
        for ns in _transitions(s, k, fixed):
            if ns not in index:
                index[ns] = len(states)
                states.append(ns)
                queue.append(ns)

    size = len(states)
    mat = [[0] * size for _ in range(size)]
    for s in states:
        i = index[s]
        for ns, w in _transitions(s, k, fixed).items():
            j = index[ns]
            mat[i][j] = (mat[i][j] + w) % _MOD

    return mat, index


def _mat_mul(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
    n = len(a)
    out = [[0] * n for _ in range(n)]
    for i in range(n):
        ai = a[i]
        for k in range(n):
            val_a = ai[k]
            if val_a:
                bk = b[k]
                for j in range(n):
                    out[i][j] = (out[i][j] + val_a * bk[j]) % _MOD
    return out


def _mat_pow(a: List[List[int]], exp: int) -> List[List[int]]:
    n = len(a)
    result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    base = a
    e = exp
    while e > 0:
        if e & 1:
            result = _mat_mul(result, base)
        e //= 2
        if e:
            base = _mat_mul(base, base)
    return result


def _modinv(a: int, mod: int = _MOD) -> int:
    return pow(a, mod - 2, mod)


def solve(k: int = 10, n: int = 10_004_003_002_001) -> int:
    """Compute F_k(n) modulo 1000004321 using color symmetry reduced transfer matrix trace."""
    fixed_same = 1
    same_start = (1, 0, 0, 0, 0)
    mat_same, idx_same = _build_matrix(k, fixed_same, [same_start])
    pow_same = _mat_pow(mat_same, n)
    same_count = pow_same[idx_same[same_start]][idx_same[same_start]]

    fixed_diff = 2
    diff_starts = [(0, t, b, 0, 1) for t in (0, 1, 2) for b in (0, 1, 2)]
    mat_diff, idx_diff = _build_matrix(k, fixed_diff, diff_starts)
    pow_diff = _mat_pow(mat_diff, n)
    diff_count = 0
    for s in diff_starts:
        if s in idx_diff:
            i = idx_diff[s]
            diff_count = (diff_count + pow_diff[i][i]) % _MOD

    marked = (k * same_count + k * (k - 1) * diff_count) % _MOD
    inv_n = _modinv(n % _MOD, _MOD)
    return (marked * inv_n) % _MOD


if __name__ == "__main__":
    print(solve())
