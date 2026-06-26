# Longest Repeating Subsequence

| | |
|---|---|
| **ID** | `string_14` |
| **Category** | strings |
| **Complexity (required)** | $O(N^2)$ Time, $O(N^2)$ Space |
| **Difficulty** | 5/10 |
| **Interview relevance** | 4/10 |
| **GeeksForGeeks Equivalent** | [Longest Repeating Subsequence](https://www.geeksforgeeks.org/longest-repeating-subsequence/) |

## Problem statement

Given a string `s`, find the length of the longest repeating **subsequence**, such that the two subsequences don't have the same string character at the same position.
(i.e., The identical characters in the two subsequences must originate from different indices in the original string).

**Input:** A string `s`.
**Output:** An integer representing the length.

## When to use it

- A classic 2D Dynamic Programming string problem.
- It is a direct, genius modification of the foundational **Longest Common Subsequence (LCS)** algorithm. If you know LCS, you know this!

## Approach

**1. The "Self-Comparison" Insight:**
In the standard Longest Common Subsequence (LCS) problem, you are given `str1` and `str2`. You find the longest sequence of characters that exist in both strings in the same order.
What if we run LCS on the EXACT SAME STRING? `LCS(s, s)`?
The answer will just be the entire string! Every character perfectly matches itself! `s[i] == s[i]`.

**2. The "Different Index" Modification:**
The problem asks for a repeating subsequence where the characters come from *different indices*.
So, we still run `LCS(s, s)`. BUT, we add one tiny, critical condition:
When we are comparing `s[i]` with `s[j]`, they are only allowed to "match" and increment the sequence length IF `s[i] == s[j]` **AND** `i != j`!
If `i == j`, it means we are looking at the exact same physical character in the original string. We treat it as a mismatch!

**3. The DP Table:**
We build an N+1 x N+1 DP matrix.
- `dp[i][j]` represents the length of the Longest Repeating Subsequence between the prefix `s[0...i-1]` and `s[0...j-1]`.
- If `s[i-1] == s[j-1]` AND `i != j`: We found a valid repeating character! `dp[i][j] = 1 + dp[i-1][j-1]`.
- Otherwise: We take the maximum of skipping a character from either prefix! `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for string_14: Longest Repeating Subsequence.

dp[i][j] = LRS length of s[i..] and s[j..] (with i != j).
"""


def solve(s, n):
    if n == 0:
        return 0
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if s[i] == s[j] and i != j:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
    return dp[0][0]
```

</details>

## Walk-through

`s = "AABEBCDD"`
`N = 8`.

1. **`i=1` ('A'), `j=1` ('A'):** Match, but `i == j`. Treat as mismatch. `dp[1][1] = 0`.
2. **`i=1` ('A'), `j=2` ('A'):** Match! AND `i != j` (1 != 2).
   - `dp[1][2] = 1 + dp[0][1] = 1 + 0 = 1`.
...
After filling the entire table, the matches that triggered `1 + dp[i-1][j-1]` were:
- 'A' at index 0 and 'A' at index 1.
- 'B' at index 2 and 'B' at index 4.
- 'D' at index 6 and 'D' at index 7.
The longest sequence of these matches without crossing paths is `"ABD"`.
`dp[8][8] = 3`. ✓

*(The repeating subsequence is "ABD". The first one uses indices `0, 2, 6`. The second one uses indices `1, 4, 7`.)*

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N^2)$ | $O(N^2)$ |
| **Average** | $O(N^2)$ | $O(N^2)$ |
| **Worst** | $O(N^2)$ | $O(N^2)$ |

We iterate through an N x N matrix. Every cell takes $O(1)$ constant time to evaluate.
Time complexity is strictly $O(N^2)$.
Space complexity is $O(N^2)$ to store the DP table.

## Variants & optimizations

- **Space Optimization $O(N)$:** Notice in the transition formula `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`, we only ever look at the CURRENT row `i` and the PREVIOUS row `i-1`. We do not need the entire matrix in memory! We can just keep two arrays: `prev_row` and `curr_row`. This instantly drops the space complexity to $O(N)$!
- **Print the Subsequence:** If the problem asks you to actually return the string `"ABD"` instead of just `3`, you start at `dp[n][n]` and trace backwards. If `dp[i][j] == dp[i-1][j-1] + 1`, you add `s[i-1]` to your string and move diagonally up-left. Otherwise, move to the max of `(i-1, j)` or `(i, j-1)`. Reverse the final string!

## Real-world applications

- **Data Compression Analysis:** Finding intrinsic patterns and long-range redundancies inside a single data stream (like an audio file) to design custom Dictionary-based compression algorithms (like LZ77/LZ78).

## Related algorithms in cOde(n)

- **[dynamic_01 - Longest Common Subsequence](../dynamic/dp_01_longest-common-subsequence.md)** — The foundational algorithm that this entire problem is built on top of.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
