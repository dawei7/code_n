# Distinct Subsequences

| | |
|---|---|
| **ID** | `dp_29` |
| **Category** | dynamic |
| **Complexity (required)** | $O(M * N)$ Time, $O(N)$ Space |
| **Difficulty** | 7/10 |
| **Interview relevance** | 6/10 |
| **LeetCode Equivalent** | [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/) |

## Problem statement

Given two strings `s` and `t`, return the number of distinct subsequences of `s` which equals `t`.
A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions.

**Input:** A string `s` (the source) and a string `t` (the target).
**Output:** An integer representing the number of distinct subsequences.

## When to use it

- The classic string counting DP problem.
- Instead of finding the *longest* match (`LCS`) or the *shortest* edit path (`Edit Distance`), you are finding the *total number of exact matches*.

## Approach

**1. Define the State:**
Let `dp[i][j]` be the number of distinct subsequences of the prefix `s[0...i-1]` that perfectly match the prefix `t[0...j-1]`.
*(Note: 1-based indexing for prefixes makes the base cases much cleaner).*

**2. Find the Base Cases:**
- `dp[i][0] = 1`: If the target `t` is empty, there is exactly 1 way to form it from ANY string `s`: delete everything!
- `dp[0][j] = 0` (for j > 0): If the source `s` is empty, but the target `t` is not, there are 0 ways to form it.

**3. Find the Transition (The recurrence relation):**
We are comparing `s[i-1]` against `t[j-1]`.
- **Case A (The characters DO NOT match):**
  If `s[i-1] != t[j-1]`, then `s[i-1]` is completely useless for building our target. We MUST delete it! The number of ways is simply whatever ways we had without using this character.
  `dp[i][j] = dp[i-1][j]`
- **Case B (The characters DO match):**
  If `s[i-1] == t[j-1]`, we actually have a CHOICE!
  1. We can CHOOSE to use `s[i-1]` to match `t[j-1]`. In this case, the rest of the target `t[0...j-2]` must be formed by the rest of the source `s[0...i-2]`. (Ways: `dp[i-1][j-1]`).
  2. We can CHOOSE to ignore `s[i-1]` anyway! Maybe there's another identical character later on. We fall back to the ways we had without it. (Ways: `dp[i-1][j]`).
  Therefore, the total ways is the SUM of both choices!
  `dp[i][j] = dp[i-1][j-1] + dp[i-1][j]`

**4. Optimize Space:**
Notice that row `i` only relies on row `i-1`. Just like LCS, we can crush this into a 1D array of size N (the length of the target string `t`).
However, because `dp[j]` relies on `dp[j-1]` from the PREVIOUS row, we must iterate `j` BACKWARDS from right to left so we don't accidentally overwrite data we need!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dp_29: Distinct Subsequences.

dp[j] = number of distinct subsequences of s[0..i-1] that
match t[0..j-1]. Iterate s left-to-right; for each char
update dp right-to-left (like 0/1 knapsack) to avoid reuse.
"""


def solve(s, t, m, n):
    dp = [0] * (n + 1)
    dp[0] = 1  # Empty target matches every prefix of s once
    for i in range(1, m + 1):
        for j in range(n, 0, -1):
            if s[i - 1] == t[j - 1]:
                dp[j] += dp[j - 1]
    return dp[n]
```

</details>

## Walk-through

`s = "rabbbit"`, `t = "rabbit"`. M=7, N=6.
`dp` size 7 initialized to `[1, 0, 0, 0, 0, 0, 0]`.

1. **i = 1 ('r'):** matches `t[0]`. `j=1`: `dp[1] += dp[0]` -> `dp[1] = 1`.
   `dp` = `[1, 1, 0, 0, 0, 0, 0]` ("r" matches "r" once).
2. **i = 2 ('a'):** matches `t[1]`. `j=2`: `dp[2] += dp[1]` -> `dp[2] = 1`.
   `dp` = `[1, 1, 1, 0, 0, 0, 0]` ("ra" matches "ra" once).
3. **i = 3 ('b'):** matches `t[2], t[3]`.
   - `j=4` ('b'): `dp[4] += dp[3] = 0`.
   - `j=3` ('b'): `dp[3] += dp[2] = 1`.
   `dp` = `[1, 1, 1, 1, 0, 0, 0]` ("rab" matches "rab" once).
4. **i = 4 ('b'):** matches `t[2], t[3]`.
   - `j=4` ('b'): `dp[4] += dp[3] = 1`.
   - `j=3` ('b'): `dp[3] += dp[2] = 1 + 1 = 2`.
   `dp` = `[1, 1, 1, 2, 1, 0, 0]` ("rabb" has 2 ways to match "rab", 1 way for "rabb").
5. **i = 5 ('b'):** matches `t[2], t[3]`.
   - `j=4` ('b'): `dp[4] += dp[3] = 1 + 2 = 3`.
   - `j=3` ('b'): `dp[3] += dp[2] = 2 + 1 = 3`.
   `dp` = `[1, 1, 1, 3, 3, 0, 0]`.
6. **i = 6 ('i'):** matches `t[4]`. `j=5`: `dp[5] += dp[4]` -> `dp[5] = 3`.
7. **i = 7 ('t'):** matches `t[5]`. `j=6`: `dp[6] += dp[5]` -> `dp[6] = 3`.

Result `dp[6]` is 3. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(M * N)$ | $O(N)$ |
| **Average** | $O(M * N)$ | $O(N)$ |
| **Worst** | $O(M * N)$ | $O(N)$ |

The nested loops run strictly M x N times doing $O(1)$ additions. Time is $O(M \times N)$.
Space is $O(N)$ (where N is the length of the shorter target string `t`).

## Variants & optimizations

- **Rolling 1D Array vs 2D Array:** Unlike LCS, where you need a `temp` variable to simulate a true 1D update, here iterating `j` backward *naturally* preserves the `dp[j-1]` value! It is arguably the cleanest 1D optimization of any 2D string problem.

## Real-world applications

- **Bioinformatics Sequence Alignment:** Calculating the multiplicity or probability of a specific gene marker (the target) forming within a highly mutating parent DNA sequence (the source).

## Related algorithms in cOde(n)

- **[dp_04 - Longest Common Subsequence](dp_04_longest-common-subsequence.md)** — The fundamental string DP matrix that relies on `max()` rather than summation `+`.
- **[dp_03 - 0/1 Knapsack](dp_03_knapsack.md)** — Teaches the exact backward-looping trick used here to avoid overwriting the 1D state.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
