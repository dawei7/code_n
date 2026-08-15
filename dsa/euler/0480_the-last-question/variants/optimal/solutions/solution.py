"""Project Euler Problem 480: The Last Question.

Find W(P(legionary) + P(calorimeters) - P(annihilate) + P(orchestrated) - P(fluttering)),
the word at the combined lexicographic index formed by anagrams of length <= 15
from 'thereisasyetinsufficientdataforameaningfulanswer'.
"""

from collections import Counter
from math import comb
from typing import Dict, List

PHRASE = "thereisasyetinsufficientdataforameaningfulanswer"
MAX_LEN = 15


def _count_words(
    avail: Dict[str, int], letters: List[str], max_len: int
) -> int:
    dp = [0] * (max_len + 1)
    dp[0] = 1
    for c in letters:
        cap = avail[c]
        if cap == 0:
            continue
        new_dp = [0] * (max_len + 1)
        for k in range(max_len + 1):
            if dp[k] == 0:
                continue
            for j in range(min(cap, max_len - k) + 1):
                new_dp[k + j] += dp[k] * comb(k + j, j)
        dp = new_dp
    return sum(dp[1:])


def _position(
    word: str,
    counts: Dict[str, int],
    letters: List[str],
    max_len: int = MAX_LEN,
) -> int:
    avail = counts.copy()
    rem_len = max_len
    ans = 0
    for ch in word:
        ans += 1
        for c in letters:
            if c < ch and avail[c] > 0:
                avail[c] -= 1
                ans += 1 + _count_words(avail, letters, rem_len - 1)
                avail[c] += 1
        avail[ch] -= 1
        rem_len -= 1
    return ans


def _word_at(
    target_p: int,
    counts: Dict[str, int],
    letters: List[str],
    max_len: int = MAX_LEN,
) -> str:
    avail = counts.copy()
    word: List[str] = []
    rem_len = max_len
    p = target_p

    while p > 0 and rem_len > 0:
        found = False
        for c in letters:
            if avail[c] == 0:
                continue
            avail[c] -= 1
            cnt = 1 + _count_words(avail, letters, rem_len - 1)
            if p == 1:
                word.append(c)
                return "".join(word)
            if p <= cnt:
                word.append(c)
                p -= 1
                rem_len -= 1
                found = True
                break
            else:
                p -= cnt
                avail[c] += 1
        if not found:
            break

    return "".join(word)


def solve(phrase: str = PHRASE, max_len: int = MAX_LEN) -> str:
    """Compute W(P(legionary) + P(calorimeters) - P(annihilate) + P(orchestrated) - P(fluttering))."""
    counts = Counter(phrase)
    letters = sorted(counts.keys())

    words = [
        ("legionary", 1),
        ("calorimeters", 1),
        ("annihilate", -1),
        ("orchestrated", 1),
        ("fluttering", -1),
    ]

    target_p = 0
    for w, sign in words:
        target_p += sign * _position(w, counts, letters, max_len)

    return _word_at(target_p, counts, letters, max_len)


if __name__ == "__main__":
    print(solve())
