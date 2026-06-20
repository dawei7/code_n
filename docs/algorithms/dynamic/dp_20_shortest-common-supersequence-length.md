# Shortest Common Supersequence

| | |
|---|---|
| **ID** | `dp_20` |
| **Category** | dynamic |
| **Complexity (required)** | $O(M * N)$ Time, $O(M * N)$ Space |
| **Difficulty** | 5/10 |
| **Interview relevance** | 7/10 |
| **LeetCode Equivalent** | [Shortest Common Supersequence](https://leetcode.com/problems/shortest-common-supersequence/) |

## Problem statement

Given two strings `str1` and `str2`, return the shortest string that has both `str1` and `str2` as subsequences. If there are multiple valid strings, return any of them.
A string `S` is a supersequence of string `A` if `A` is a subsequence of `S`.

**Input:** Two strings `str1` (length M) and `str2` (length N).
**Output:** A string representing the shortest common supersequence. (Sometimes asked just for the length).

## When to use it

- To show absolute mastery over the Longest Common Subsequence (LCS) matrix.
- This problem is the literal mirror image of LCS. Instead of finding the intersection, we are constructing the optimal union!

## Approach

**The Mathematical Reduction:**
If we just smash `str1` and `str2` together end-to-end, the length is M + N. This is a valid supersequence, but it's not the shortest.
Why? Because any characters that both strings *share in the exact same order* (their Longest Common Subsequence) are being counted twice!
To make the supersequence as short as possible, we must overlap the LCS.
The length of the Shortest Common Supersequence (SCS) is mathematically proven to be exactly: `M + N - LCS(str1, str2)`.

**Constructing the String:**
If the question asks for the actual string, we cannot use the $O(N)$ space optimization for LCS. We must build the full M x N DP table.
Once the table is built, we start at the bottom-right corner `(m, n)` and trace our way back to `(0, 0)`:
1. If `str1[i-1] == str2[j-1]`: This character is part of the LCS! We only need to write it ONCE. Add it to our result, and move diagonally up-left `(i-1, j-1)`.
2. If they do NOT match: We must include the character that leads to the larger LCS path!
   - If `dp[i-1][j] > dp[i][j-1]`, it means the optimal path came from above. We add `str1[i-1]` and move UP.
   - Otherwise, the optimal path came from the left. We add `str2[j-1]` and move LEFT.
3. If we hit the top edge (`i=0`), we just append the rest of `str2`. If we hit the left edge (`j=0`), we append the rest of `str1`.
4. The resulting string is built backwards, so reverse it at the end!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dp_20: Shortest Common Supersequence (Length).

The shortest string that has both s1 and s2 as subsequences.
The length is n1 + n2 - LCS(s1, s2). Compute LCS first, then
combine the lengths.
"""


def solve(s1, s2, n1, n2):
    if n1 == 0:
        return n2
    if n2 == 0:
        return n1
    dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    for i in range(n1):
        for j in range(n2):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
    lcs = dp[n1][n2]
    return n1 + n2 - lcs
```

</details>

## Walk-through

`str1 = "abac"`, `str2 = "cab"`. M=4, N=3.
LCS is `"ab"`.
Matrix `dp`:
```
    c a b
  0 0 0 0
a 0 0 1 1
b 0 0 1 2
a 0 0 1 2
c 0 1 1 2
```
Traceback starts at `i=4, j=3` (`dp[4][3] = 2`).
1. `str1[3] ('c') != str2[2] ('b')`. `dp[3][3]`(2) > `dp[4][2]`(1). Move UP. Append `'c'`. `i=3, j=3`.
2. `str1[2] ('a') != str2[2] ('b')`. `dp[2][3]`(2) >= `dp[3][2]`(1). Move UP. Append `'a'`. `i=2, j=3`.
3. `str1[1] ('b') == str2[2] ('b')`. Match! Move DIAG. Append `'b'`. `i=1, j=2`.
4. `str1[0] ('a') == str2[1] ('a')`. Match! Move DIAG. Append `'a'`. `i=0, j=1`.
5. `i=0`, loop terminates.
6. Flush remaining `j`: `str2` has `j=1` left. Append `str2[0] ('c')`.
Reversed Result: `"cab"` -> `"b"` -> `"ab"` -> `"aab"` -> `"caab"`.
Wait, reverse of `['c', 'a', 'b', 'a', 'c']` is `"cabac"`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(M * N)$ | $O(M * N)$ |
| **Average** | $O(M * N)$ | $O(M * N)$ |
| **Worst** | $O(M * N)$ | $O(M * N)$ |

Building the LCS matrix takes strictly $O(M \times N)$ time.
Tracing back takes at most $O(M + N)$ steps. Total time is $O(M \times N)$.
Space is strictly $O(M \times N)$ for the DP matrix. We cannot optimize this to $O(\min(M, N)$) because the traceback requires the entire historical path grid to make routing decisions.

## Variants & optimizations

- **Shortest Common Supersequence of Multiple Strings:** If you have K strings, the DP state becomes K-dimensional ($O(N^K)$), which is NP-Hard! You usually approximate it using Greedy algorithms or Hamiltonian paths on overlap graphs.

## Real-world applications

- **Data Compression:** Finding the shortest instruction tape that can generate two different output sequences by branching at specific indices (a fundamental concept in Kolmogorov complexity).

## Related algorithms in cOde(n)

- **[dp_04 - Longest Common Subsequence](dp_04_longest-common-subsequence.md)** — The exact same table.
- **[dp_08 - Edit Distance](dp_08_edit-distance.md)** — Another string DP that requires full matrix traceback to print the exact edit instructions.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
