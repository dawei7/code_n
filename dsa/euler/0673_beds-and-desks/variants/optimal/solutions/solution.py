"""Project Euler Problem 673: Beds and Desks.

Find the number of permutations of 500 students that preserve both the roommate pairings
and the desk partner pairings, modulo 999999937.
"""

from collections import defaultdict
import os
from typing import List, Optional, Tuple

_MOD = 999_999_937


def _parse_pairs(text: str) -> List[Tuple[int, int]]:
    out: List[Tuple[int, int]] = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        a_str, b_str = line.split(",")
        out.append((int(a_str), int(b_str)))
    return out


def _load_data_files() -> Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]:
    cur = os.path.abspath(__file__)
    pkg_dir = cur
    while (
        os.path.basename(pkg_dir) != "0673_beds-and-desks"
        and os.path.dirname(pkg_dir) != pkg_dir
    ):
        pkg_dir = os.path.dirname(pkg_dir)

    beds_path = os.path.join(pkg_dir, "beds.txt")
    desks_path = os.path.join(pkg_dir, "desks.txt")

    with open(beds_path, "r", encoding="utf-8") as f:
        beds_text = f.read()
    with open(desks_path, "r", encoding="utf-8") as f:
        desks_text = f.read()

    return _parse_pairs(beds_text), _parse_pairs(desks_text)


def solve(
    n: int = 500,
    bed_pairs: Optional[List[Tuple[int, int]]] = None,
    desk_pairs: Optional[List[Tuple[int, int]]] = None,
    mod: int = _MOD,
) -> int:
    """Find the number of permutations satisfying student room and desk invariants modulo 999999937."""
    if bed_pairs is None or desk_pairs is None:
        bed_pairs, desk_pairs = _load_data_files()

    b_map = list(range(n + 1))
    d_map = list(range(n + 1))

    for a, b in bed_pairs:
        b_map[a] = b
        b_map[b] = a
    for a, b in desk_pairs:
        d_map[a] = b
        d_map[b] = a

    visited = [False] * (n + 1)
    type_count = defaultdict(int)
    type_aut = {}

    for start in range(1, n + 1):
        if visited[start]:
            continue

        stack = [start]
        visited[start] = True
        comp: List[int] = []
        while stack:
            v = stack.pop()
            comp.append(v)
            for u in (b_map[v], d_map[v]):
                if not visited[u]:
                    visited[u] = True
                    stack.append(u)

        k = len(comp)
        has_loop = any((b_map[v] == v) or (d_map[v] == v) for v in comp)

        if not has_loop:
            key = ("C", k)
            aut = k
        else:
            if k % 2 == 1:
                key = ("P", k, "BD")
                aut = 1
            else:
                end_colour = "BD"
                for v in comp:
                    if b_map[v] == v and d_map[v] != v:
                        end_colour = "B"
                        break
                    if d_map[v] == v and b_map[v] != v:
                        end_colour = "D"
                        break
                key = ("P", k, end_colour)
                aut = 2

        type_count[key] += 1
        type_aut[key] = aut

    fact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = (fact[i - 1] * i) % mod

    ans = 1
    for key, m in type_count.items():
        a = type_aut[key]
        ans = (ans * pow(a, m, mod)) % mod
        ans = (ans * fact[m]) % mod
    return ans


if __name__ == "__main__":
    print(solve())
