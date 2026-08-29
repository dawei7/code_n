"""Project Euler Problem 679: Freefarea.

Find f(30), the number of words of length 30 over {A, E, F, R} that contain all four keywords
FREE, FARE, AREA, REEF exactly once.
"""

from typing import Dict, List, Set, Tuple

_KEYWORDS = ["FREE", "FARE", "AREA", "REEF"]
_ALPHABET = ["A", "E", "F", "R"]


def _build_automaton(
    keywords: List[str], alphabet: List[str]
) -> Tuple[List[str], Dict[Tuple[int, str], Tuple[int, int]]]:
    prefixes: Set[str] = set()
    for kw in keywords:
        for i in range(len(kw) + 1):
            prefixes.add(kw[:i])

    prefix_list = sorted(prefixes)
    state_to_id = {p: i for i, p in enumerate(prefix_list)}

    trans: Dict[Tuple[int, str], Tuple[int, int]] = {}
    for p in prefix_list:
        for ch in alphabet:
            new_s = p + ch
            next_p = ""
            for k in range(len(new_s), -1, -1):
                suf = new_s[len(new_s) - k :]
                if suf in prefix_list:
                    next_p = suf
                    break

            match_mask = 0
            for idx, kw in enumerate(keywords):
                if new_s.endswith(kw):
                    match_mask |= 1 << idx

            trans[(state_to_id[p], ch)] = (state_to_id[next_p], match_mask)

    return prefix_list, trans


def solve(
    target_len: int = 30,
    keywords: List[str] = _KEYWORDS,
    alphabet: List[str] = _ALPHABET,
) -> int:
    """Compute f(n) using Aho-Corasick suffix automaton dynamic programming with keyword bitmasks."""
    prefix_list, trans = _build_automaton(keywords, alphabet)
    state_to_id = {p: i for i, p in enumerate(prefix_list)}

    dp: Dict[Tuple[int, int], int] = {(state_to_id[""], 0): 1}

    for _ in range(target_len):
        next_dp: Dict[Tuple[int, int], int] = {}
        for (u, mask), count in dp.items():
            for ch in alphabet:
                next_u, matches = trans[(u, ch)]
                if mask & matches:
                    continue
                new_mask = mask | matches
                key = (next_u, new_mask)
                next_dp[key] = next_dp.get(key, 0) + count
        dp = next_dp

    full_mask = (1 << len(keywords)) - 1
    ans = sum(count for (u, mask), count in dp.items() if mask == full_mask)
    return ans


if __name__ == "__main__":
    print(solve())
