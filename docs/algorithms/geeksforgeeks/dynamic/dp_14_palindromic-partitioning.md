# Palindrome Partitioning II

| | |
|---|---|
| **ID** | `dp_14` |
| **Category** | dynamic |
| **Complexity (required)** | $O(N^2)$ Time, $O(N^2)$ Space |
| **Difficulty** | 6/10 |
| **Interview relevance** | 7/10 |
| **LeetCode Equivalent** | [Palindrome Partitioning II](https://leetcode.com/problems/palindrome-partitioning-ii/) |

## Problem statement

Given a string `s`, partition `s` such that every substring of the partition is a palindrome.
Return the **minimum number of cuts** needed for a palindrome partitioning of `s`.

**Input:** A string `s`.
**Output:** An integer representing the minimum number of cuts.

## When to use it

- When a problem requires optimizing the grouping or segmentation of a 1D sequence based on a property that can be precomputed (like "is palindrome").
- It requires a classic **two-pass DP** approach: one pass to precompute palindromes, and one pass to find the minimum cuts.

## Approach

**1. Precompute Palindromes ($O(N^2)$):**
If we test `is_palindrome()` on the fly for every substring, the algorithm will become $O(N^3)$.
We use a 2D boolean array `is_pal[i][j]` which is `True` if `s[i...j]` is a palindrome.
- `s[i...j]` is a palindrome IF `s[i] == s[j]` AND `s[i+1...j-1]` is a palindrome.
- We build this table exactly like Interval DP, iterating by substring length!

**2. Find Minimum Cuts ($O(N^2)$):**
Let `dp[i]` be the minimum number of cuts required to perfectly partition the prefix `s[0...i]`.

**3. Find the Transition (The recurrence relation):**
To find `dp[i]`, we try placing the *last cut* at every possible index `j` (where 0 \le j \le i).
If we place a cut before index `j`, the final piece of the string is `s[j...i]`.
We CAN ONLY MAKE THIS CUT if `s[j...i]` is a valid palindrome!
If it is a valid palindrome, the total number of cuts for the prefix `s[0...i]` would be:
- The minimum cuts required for the prefix BEFORE the cut: `dp[j-1]`
- PLUS 1 (for the new cut we just made).
Therefore, `dp[i] = min( dp[i], 1 + dp[j-1] )` for all 0 \le j \le i where `is_pal[j][i]` is `True`.

*Base Case Optimization:* If the entire prefix `s[0...i]` is already a palindrome (`is_pal[0][i] == True`), we need 0 cuts! `dp[i] = 0`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dp_14: Palindromic Partitioning.

Min cuts to partition a string into all-palindromic substrings.
"""


def solve(s):
    n = len(s)
    if n <= 1:
        return 0
    is_pal = [[False] * n for _ in range(n)]
    for i in range(n):
        is_pal[i][i] = True
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2 or is_pal[i + 1][j - 1]:
                    is_pal[i][j] = True
    INF = float("inf")
    dp = [INF] * n
    for i in range(n):
        if is_pal[0][i]:
            dp[i] = 0
        else:
            for j in range(i):
                if is_pal[j + 1][i] and dp[j] + 1 < dp[i]:
                    dp[i] = dp[j] + 1
    return dp[n - 1]
```

</details>

## Walk-through

`s = "aab"`. N=3.
1. **Precompute `is_pal`:**
   - `"a"`: True. `"a"`: True. `"b"`: True.
   - `"aa"`: True. `"ab"`: False.
   - `"aab"`: False.
2. **DP Pass:**
   - `i = 0 ('a')`: `s[0...0]` is `"a"`, which is a palindrome! `dp[0] = 0`.
   - `i = 1 ('a')`: `s[0...1]` is `"aa"`, which is a palindrome! `dp[1] = 0`.
   - `i = 2 ('b')`: `s[0...2]` is `"aab"`, NOT a palindrome.
     - Try `j = 1 ('a')`: suffix `s[1...2]` is `"ab"` (False).
     - Try `j = 2 ('b')`: suffix `s[2...2]` is `"b"` (TRUE).
       - Valid cut before index 2! Cost is `1 + dp[1] = 1 + 0 = 1`.
       - `min_cuts = 1`.
   - `dp[2] = 1`.

Result `dp[2]` is 1. ✓ (The cuts are `"aa" | "b"`).

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N^2)$ | $O(N^2)$ |
| **Average** | $O(N^2)$ | $O(N^2)$ |
| **Worst** | $O(N^2)$ | $O(N^2)$ |

Step 1 (Precomputation) takes exactly $O(N^2)$ time to fill the boolean matrix.
Step 2 (DP) takes $O(N^2)$ time, iterating i from 0 to N, and j from 0 to i.
Total time complexity is $O(N^2)$.
Space complexity is $O(N^2)$ strictly for the `is_pal` boolean matrix. The `dp` array takes $O(N)$.

## Variants & optimizations

- **Palindrome Partitioning I (Backtracking):** Instead of returning the *minimum number* of cuts, return *all possible* valid partitions. You use the exact same `is_pal` precomputation array, but then run a DFS Backtracking algorithm (`bb_01`) to explore and append all valid branches to a global result list.
- **Center Expansion (Space Optimization):** You can skip building the $O(N^2)$ `is_pal` matrix and instead run a single pass! Expand around every possible "center" (like Manacher's algorithm) and update the `dp` array on the fly. This brings space complexity down to strictly $O(N)$!

## Real-world applications

- **Natural Language Processing:** Tokenizing continuous streams of speech or un-spaced text (like continuous Japanese or hashtags) into valid dictionary words.

## Related algorithms in cOde(n)

- **[dp_15 - Word Break](dp_15_word-break.md)** — The mathematically identical problem where validity is checked against a dictionary instead of a palindrome property.
- **[string_04 - Longest Palindromic Substring](../strings/string_04_longest-palindromic-substring.md)** — Uses the exact same $O(N^2)$ palindrome DP precomputation table.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
