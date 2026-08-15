"""Project Euler Problem 442: Eleven-free Integers.

Find E(10^18), the 10^18-th positive eleven-free integer.
An integer is eleven-free if its decimal expansion does not contain
any substring representing a power of 11 except 1.
"""

from collections import deque
from typing import Dict, List, Tuple


def _build_automaton(
    patterns: List[str],
) -> Tuple[List[List[int]], List[bool]]:
    trie: List[Dict] = [{"next": {}, "fail": 0, "is_match": False}]
    for pat in patterns:
        curr = 0
        for ch in pat:
            if ch not in trie[curr]["next"]:
                trie[curr]["next"][ch] = len(trie)
                trie.append({"next": {}, "fail": 0, "is_match": False})
            curr = trie[curr]["next"][ch]
        trie[curr]["is_match"] = True

    queue = deque()
    for ch, nxt in trie[0]["next"].items():
        queue.append(nxt)

    while queue:
        u = queue.popleft()
        if trie[trie[u]["fail"]]["is_match"]:
            trie[u]["is_match"] = True
        for ch, v in trie[u]["next"].items():
            f = trie[u]["fail"]
            while f > 0 and ch not in trie[f]["next"]:
                f = trie[f]["fail"]
            if ch in trie[f]["next"] and trie[f]["next"][ch] != v:
                trie[v]["fail"] = trie[f]["next"][ch]
            else:
                trie[v]["fail"] = 0
            queue.append(v)

    num_states = len(trie)
    trans = [[0] * 10 for _ in range(num_states)]
    is_bad = [trie[i]["is_match"] for i in range(num_states)]

    for u in range(num_states):
        for d in range(10):
            ch = str(d)
            curr = u
            while curr > 0 and ch not in trie[curr]["next"]:
                curr = trie[curr]["fail"]
            if ch in trie[curr]["next"]:
                trans[u][d] = trie[curr]["next"][ch]
            else:
                trans[u][d] = 0

    return trans, is_bad


def solve(target: int = 10**18) -> int:
    """Find the target-th eleven-free integer using Aho-Corasick automaton digit DP and binary search."""
    patterns: List[str] = []
    p = 11
    for _ in range(1, 20):
        patterns.append(str(p))
        p *= 11

    trans, is_bad = _build_automaton(patterns)

    def count_eleven_free(n_val: int) -> int:
        if n_val <= 0:
            return 0
        digits = [int(c) for c in str(n_val)]
        length = len(digits)
        memo: Dict[Tuple[int, int, bool, bool], int] = {}

        def dp(
            idx: int, state: int, is_less: bool, is_started: bool
        ) -> int:
            if is_bad[state]:
                return 0
            if idx == length:
                return 1 if is_started else 0
            key = (idx, state, is_less, is_started)
            if key in memo:
                return memo[key]

            limit = 9 if is_less else digits[idx]
            total = 0
            for d in range(limit + 1):
                next_less = is_less or (d < limit)
                if not is_started and d == 0:
                    total += dp(idx + 1, 0, next_less, False)
                else:
                    next_state = trans[state][d]
                    if not is_bad[next_state]:
                        total += dp(idx + 1, next_state, next_less, True)

            memo[key] = total
            return total

        return dp(0, 0, False, False)

    low = 1
    high = 10**22
    while low < high:
        mid = (low + high) // 2
        if count_eleven_free(mid) >= target:
            high = mid
        else:
            low = mid + 1

    return low


if __name__ == "__main__":
    print(solve())
