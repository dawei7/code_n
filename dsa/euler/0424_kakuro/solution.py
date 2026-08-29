"""Project Euler Problem 424: Kakuro.

Solve 200 cryptic kakuro puzzles and find the sum of the decoded 10-digit numbers A..J.
"""

from collections import defaultdict, deque
from dataclasses import dataclass
from itertools import permutations
from pathlib import Path
from typing import Dict, Iterator, List, Optional, Tuple

ALL10 = (1 << 10) - 1
DIGITS_1_9 = sum(1 << d for d in range(1, 10))


def _popcount(x: int) -> int:
    return x.bit_count()


def _iter_bits(mask: int) -> Iterator[int]:
    while mask:
        b = mask & -mask
        yield b.bit_length() - 1
        mask ^= b


def _split_tokens(line: str) -> List[str]:
    out: List[str] = []
    cur: List[str] = []
    depth = 0
    for ch in line.strip():
        if ch == "," and depth == 0:
            out.append("".join(cur))
            cur.clear()
            continue
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        cur.append(ch)
    out.append("".join(cur))
    return out


def _parse_puzzle(line: str) -> Tuple[int, List[Tuple[str, Optional[object]]]]:
    toks = _split_tokens(line)
    n = int(toks[0])
    cells = toks[1:]
    grid: List[Tuple[str, Optional[object]]] = []
    for t in cells:
        if t == "X":
            grid.append(("X", None))
        elif t == "O":
            grid.append(("O", None))
        elif len(t) == 1 and "A" <= t <= "J":
            grid.append(("L", t))
        elif t.startswith("(") and t.endswith(")"):
            inside = t[1:-1]
            parts = inside.split(",")
            sums = {}
            for part in parts:
                sums[part[0]] = part[1:]
            grid.append(("C", sums))
        else:
            raise ValueError(f"Unknown token: {t}")
    return n, grid


TUPLES_BY_LEN_SUM: Dict[Tuple[int, int], List[Tuple[int, ...]]] = defaultdict(
    list
)
MASKS_BY_LEN_SUM: Dict[Tuple[int, int], List[int]] = defaultdict(list)
for _L in range(1, 10):
    for _p in permutations(range(1, 10), _L):
        _s = sum(_p)
        TUPLES_BY_LEN_SUM[(_L, _s)].append(_p)
    for (_L, _s), _tups in list(TUPLES_BY_LEN_SUM.items()):
        _mset = set()
        for _tp in _tups:
            _m = 0
            for _d in _tp:
                _m |= 1 << _d
            _mset.add(_m)
        MASKS_BY_LEN_SUM[(_L, _s)] = list(_mset)


@dataclass(slots=True)
class _RunConstraint:
    sum_kind: str
    sum_letters: Tuple[int, ...]
    cells: Tuple[int, ...]
    length: int


def _build_csp(line: str):
    n, grid = _parse_puzzle(line)
    dom = [ALL10] * 10

    first_letters = set()
    for _, info in grid:
        if info and isinstance(info, dict):
            for code in info.values():
                if len(code) == 2:
                    first_letters.add(ord(code[0]) - ord("A"))
    for l_idx in first_letters:
        dom[l_idx] &= ~1

    white_idx = {}
    white_cells = []
    for r in range(n):
        for c in range(n):
            kind, info = grid[r * n + c]
            if kind in ("O", "L"):
                w_id = len(white_cells)
                white_idx[(r, c)] = w_id
                white_cells.append((r, c, kind, info))

    num_white = len(white_cells)
    dom.extend([DIGITS_1_9] * num_white)

    for w_id, (_, _, kind, info) in enumerate(white_cells):
        if kind == "L":
            l_idx = ord(info) - ord("A")
            pass

    runs: List[_RunConstraint] = []
    for r in range(n):
        c = 0
        while c < n:
            kind, info = grid[r * n + c]
            if kind == "C" and info and "h" in info:
                code = info["h"]
                code_vars = tuple(ord(ch) - ord("A") for ch in code)
                rcells = []
                c2 = c + 1
                while c2 < n and grid[r * n + c2][0] in ("O", "L"):
                    rcells.append(white_idx[(r, c2)] + 10)
                    c2 += 1
                if rcells:
                    runs.append(
                        _RunConstraint(
                            "h", code_vars, tuple(rcells), len(rcells)
                        )
                    )
                c = c2
            else:
                c += 1

    for c in range(n):
        r = 0
        while r < n:
            kind, info = grid[r * n + c]
            if kind == "C" and info and "v" in info:
                code = info["v"]
                code_vars = tuple(ord(ch) - ord("A") for ch in code)
                rcells = []
                r2 = r + 1
                while r2 < n and grid[r2 * n + c][0] in ("O", "L"):
                    rcells.append(white_idx[(r2, c)] + 10)
                    r2 += 1
                if rcells:
                    runs.append(
                        _RunConstraint(
                            "v", code_vars, tuple(rcells), len(rcells)
                        )
                    )
                r = r2
            else:
                r += 1

    var_to_runs = [[] for _ in range(10 + num_white)]
    for r_id, run in enumerate(runs):
        for lv in run.sum_letters:
            var_to_runs[lv].append(r_id)
        for cv in run.cells:
            var_to_runs[cv].append(r_id)

    return dom, runs, var_to_runs, white_cells


def _enforce_all_diff_letters(dom: List[int]) -> bool:
    assigned_mask = 0
    assigned_count = 0
    for v in range(10):
        m = dom[v]
        if m == 0:
            return False
        if (m & (m - 1)) == 0:
            if assigned_mask & m:
                return False
            assigned_mask |= m
            assigned_count += 1

    if assigned_count > 0:
        for v in range(10):
            m = dom[v]
            if (m & (m - 1)) != 0:
                new_m = m & ~assigned_mask
                if new_m == 0:
                    return False
                dom[v] = new_m
    return True


def _process_run(
    run: _RunConstraint, dom: List[int]
) -> Tuple[bool, Optional[Tuple[int, int]], Optional[Tuple[int, int]]]:
    l_vars = run.sum_letters
    cells = run.cells
    l_len = run.length

    if len(l_vars) == 1:
        s_masks = dom[l_vars[0]]
        possible_sums = [d for d in _iter_bits(s_masks) if d >= 1]
    else:
        t_mask, u_mask = dom[l_vars[0]], dom[l_vars[1]]
        possible_sums = [
            10 * t + u
            for t in _iter_bits(t_mask)
            if t >= 1
            for u in _iter_bits(u_mask)
        ]

    if not possible_sums:
        return False, None, None

    valid_sums = []
    valid_tuples = []
    for s in possible_sums:
        tups = TUPLES_BY_LEN_SUM.get((l_len, s))
        if not tups:
            continue
        for tp in tups:
            ok = True
            for d, cv in zip(tp, cells):
                if not (dom[cv] & (1 << d)):
                    ok = False
                    break
            if ok:
                valid_sums.append(s)
                valid_tuples.append(tp)

    if not valid_tuples:
        return False, None, None

    if len(l_vars) == 1:
        new_s_mask = 0
        for s in valid_sums:
            new_s_mask |= 1 << s
        new_t_mask = None
        new_u_mask = new_s_mask
    else:
        new_t_mask = 0
        new_u_mask = 0
        for s in valid_sums:
            new_t_mask |= 1 << (s // 10)
            new_u_mask |= 1 << (s % 10)

    cell_masks = [0] * l_len
    for tp in valid_tuples:
        for i, d in enumerate(tp):
            cell_masks[i] |= 1 << d

    changed = False
    if len(l_vars) == 1:
        lv = l_vars[0]
        cur = dom[lv]
        upd = cur & new_u_mask
        if upd == 0:
            return False, None, None
        if upd != cur:
            dom[lv] = upd
            changed = True
    else:
        lv0, lv1 = l_vars
        cur0, cur1 = dom[lv0], dom[lv1]
        upd0, upd1 = cur0 & new_t_mask, cur1 & new_u_mask
        if upd0 == 0 or upd1 == 0:
            return False, None, None
        if upd0 != cur0:
            dom[lv0] = upd0
            changed = True
        if upd1 != cur1:
            dom[lv1] = upd1
            changed = True

    for cv, nm in zip(cells, cell_masks):
        cur = dom[cv]
        upd = cur & nm
        if upd == 0:
            return False, None, None
        if upd != cur:
            dom[cv] = upd
            changed = True

    return True, None, None


def _propagate(
    dom: List[int],
    runs: List[_RunConstraint],
    var_to_runs: List[List[int]],
    white_cells: List[Tuple[int, int, str, Optional[str]]],
) -> bool:
    for w_id, (_, _, kind, info) in enumerate(white_cells):
        if kind == "L":
            l_idx = ord(info) - ord("A")
            cv = 10 + w_id
            m = dom[l_idx] & dom[cv]
            if m == 0:
                return False
            dom[l_idx] = m
            dom[cv] = m

    if not _enforce_all_diff_letters(dom):
        return False

    q = deque(range(len(runs)))
    in_q = [True] * len(runs)

    while q:
        r_id = q.popleft()
        in_q[r_id] = False

        old_dom = list(dom)
        ok, _, _ = _process_run(runs[r_id], dom)
        if not ok:
            return False

        for w_id, (_, _, kind, info) in enumerate(white_cells):
            if kind == "L":
                l_idx = ord(info) - ord("A")
                cv = 10 + w_id
                m = dom[l_idx] & dom[cv]
                if m == 0:
                    return False
                dom[l_idx] = m
                dom[cv] = m

        if not _enforce_all_diff_letters(dom):
            return False

        for v in range(len(dom)):
            if dom[v] != old_dom[v]:
                for nr_id in var_to_runs[v]:
                    if not in_q[nr_id]:
                        q.append(nr_id)
                        in_q[nr_id] = True

    return True


def _select_var(dom: List[int]) -> Optional[int]:
    best_v = None
    best_size = 999
    for v in range(10):
        sz = _popcount(dom[v])
        if sz > 1 and sz < best_size:
            best_size = sz
            best_v = v
    if best_v is not None:
        return best_v
    for v in range(10, len(dom)):
        sz = _popcount(dom[v])
        if sz > 1 and sz < best_size:
            best_size = sz
            best_v = v
    return best_v


def _solve_csp(
    dom: List[int],
    runs: List[_RunConstraint],
    var_to_runs: List[List[int]],
    white_cells: List[Tuple[int, int, str, Optional[str]]],
) -> Optional[List[int]]:
    if not _propagate(dom, runs, var_to_runs, white_cells):
        return None

    var = _select_var(dom)
    if var is None:
        return dom

    for d in _iter_bits(dom[var]):
        new_dom = list(dom)
        new_dom[var] = 1 << d
        sol = _solve_csp(new_dom, runs, var_to_runs, white_cells)
        if sol is not None:
            return sol
    return None


def _mapping_to_number(sol_dom: List[int]) -> int:
    digits = []
    for v in range(10):
        d = (sol_dom[v] & -sol_dom[v]).bit_length() - 1
        digits.append(str(d))
    return int("".join(digits))


def _solve_puzzle(line: str) -> int:
    dom, runs, var_to_runs, white_cells = _build_csp(line)
    sol_dom = _solve_csp(dom, runs, var_to_runs, white_cells)
    if sol_dom is None:
        raise ValueError("No solution found for puzzle line")
    return _mapping_to_number(sol_dom)


def solve(puzzle_count: int = 200) -> int:
    """Solve the 200 Kakuro puzzles from kakuro200.txt and return the sum of the 10-digit answers."""
    data_path = Path(__file__).resolve().parent.parent.parent / "kakuro200.txt"
    if not data_path.is_file():
        data_path = Path("kakuro200.txt")
    if not data_path.is_file():
        data_path = Path("dsa/euler/0424_kakuro/kakuro200.txt")

    with open(data_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    total = 0
    for line in lines[:puzzle_count]:
        total += _solve_puzzle(line)
    return total


if __name__ == "__main__":
    print(solve())
