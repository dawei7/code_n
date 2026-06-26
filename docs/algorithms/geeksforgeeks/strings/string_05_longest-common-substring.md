# Longest Common Substring

| | |
|---|---|
| **ID** | `string_05` |
| **Category** | strings |
| **Complexity (required)** | $O(N * M)$ |
| **Difficulty** | 5/10 |
| **Interview relevance** | 8/10 |
| **LeetCode Equivalent** | [Maximum Length of Repeated Subarray](https://leetcode.com/problems/maximum-length-of-repeated-subarray/) |

## Problem statement

Given two strings `S1` and `S2`, find the length of the **longest common substring**.
A substring is a strictly *contiguous* sequence of characters within a string.

*(Note: Do not confuse this with the Longest Common Subsequence, where the characters do not need to be contiguous).*

**Input:** Two strings `S1` and `S2`.
**Output:** An integer representing the length of the longest common substring.

**Example:**
`S1 = "ABCDGH"`, `S2 = "ACDGHR"`
Output: `4`. (The longest common substring is `"CDGH"`).

## When to use it

- A classic Dynamic Programming text-processing problem.
- Used in plagiarism detection to find identical blocks of text.

## Approach

We can solve this using a 2D Dynamic Programming table.
Let `dp[i][j]` be the length of the longest common substring that **strictly ends at** `S1[i-1]` and `S2[j-1]`.

If `S1[i-1] == S2[j-1]`, it means the characters match! The longest common substring ending at these two characters is exactly `1` greater than the longest common substring ending at the characters immediately preceding them:
`dp[i][j] = dp[i-1][j-1] + 1`

If `S1[i-1] != S2[j-1]`, the characters don't match. Since a substring must be contiguous, the streak is broken! The length of a common substring ending exactly at this mismatch is zero:
`dp[i][j] = 0`

To find the global longest common substring, we simply maintain a `max_len` variable and update it whenever `dp[i][j]` is calculated.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for string_05: Longest Common Substring.

DP with a single rolling row. dp[i][j] = length of the longest
common suffix of s[:i] and t[:j].
"""


def solve(s, t):
    m, n = len(s), len(t)
    if m == 0 or n == 0:
        return 0
    prev = [0] * (n + 1)
    best = 0
    for i in range(1, m + 1):
        cur = [0] * (n + 1)
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                cur[j] = prev[j - 1] + 1
                if cur[j] > best:
                    best = cur[j]
        prev = cur
    return best
```

</details>

## Walk-through

`S1 = "ABCA"`, `S2 = "BC"`
`n = 4, m = 2`. `dp` is 5x3.

**i = 1 ('A'):**
- `j = 1 ('B')`: 'A' != 'B' -> `dp[1][1] = 0`
- `j = 2 ('C')`: 'A' != 'C' -> `dp[1][2] = 0`

**i = 2 ('B'):**
- `j = 1 ('B')`: 'B' == 'B' -> `dp[2][1] = dp[1][0] + 1 = 1`. `max = 1`.
- `j = 2 ('C')`: 'B' != 'C' -> `dp[2][2] = 0`

**i = 3 ('C'):**
- `j = 1 ('B')`: 'C' != 'B' -> `dp[3][1] = 0`
- `j = 2 ('C')`: 'C' == 'C' -> `dp[3][2] = dp[2][1] + 1 = 1 + 1 = 2`. `max = 2`.

**i = 4 ('A'):**
- Mismatches all around.

Output: `2`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N * M)$ | $O(N * M)$ |
| **Average** | $O(N * M)$ | $O(N * M)$ |
| **Worst** | $O(N * M)$ | $O(N * M)$ |

The nested loops strictly execute N x M times, where N and M are the lengths of the two strings. Time complexity is exactly $O(N \cdot M)$.
Space complexity is $O(N \cdot M)$ to store the 2D DP array.

## Variants & optimizations

- **Space Optimization $O(M)$:** Notice that to compute row `i`, we only ever look at row `i-1`. We do not need the entire 2D matrix in memory! We can just keep two 1D arrays (`prev_row` and `curr_row`) of size M, alternating between them, which drops the space complexity to $O(M)$.
- **Suffix Automaton / Suffix Tree $O(N + M)$:** By building a suffix tree of `S1` and threading `S2` through it, you can solve this problem in strictly linear time. This is astronomically faster but the data structures are incredibly complex to implement in an interview.

## Real-world applications

- **Data Deduplication:** Finding identical byte-chunks in binary files to compress them by referencing a single shared memory location.

## Related algorithms in cOde(n)

- **[dp_12 - Longest Common Subsequence](../dynamic/dp_12_lcs.md)** — The related DP problem where gaps are allowed. (The only difference is that on a mismatch, it carries over `max(dp[i-1][j], dp[i][j-1])` instead of resetting to `0`!)
- **[suffix_array_01 - Suffix Array](../suffix_array/suffix_array_01_construction.md)** — The $O(N \log N)$ data structure that can also solve this problem in near-linear time using the Longest Common Prefix (LCP) array.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
