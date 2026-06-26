# Longest Palindromic Substring

| | |
|---|---|
| **ID** | `string_02` |
| **Category** | strings |
| **Complexity (required)** | $O(N^2)$ |
| **Difficulty** | 5/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) |

## Problem statement

Given a string `s`, return the **longest palindromic substring** in `s`.
A string is palindromic if it reads the same forward and backward.

**Input:** A string `s`.
**Output:** A string representing the longest palindrome.

**Example 1:**
`s = "babad"`
Output: `"bab"` (or `"aba"`).

**Example 2:**
`s = "cbbd"`
Output: `"bb"`.

## When to use it

- A classic interview problem used to test your ability to recognize and optimize "Expand Around Center" logic over naive $O(N^3)$ brute force.

## Approach

The naive brute force checks every possible substring to see if it is a palindrome. There are $O(N^2)$ substrings, and checking each takes $O(N)$ time, resulting in $O(N^3)$.

**Expand Around Center ($O(N^2)$):**
Every palindrome has a center. We can iterate through the string and treat every single character as a potential center of a palindrome, expanding outward to the left and right as long as the characters match!
However, palindromes can have two types of centers:
1. **Odd length** (e.g., `"aba"`): The center is a single character (`'b'`).
2. **Even length** (e.g., `"abba"`): The center is the invisible space *between* two identical characters (`'b'` and `'b'`).

Therefore, for each index `i`, we must attempt to expand outward twice:
- Expand treating `i` as the center (odd length).
- Expand treating `i` and `i+1` as the center (even length).

Keep track of the start and end indices of the longest valid expansion found across the entire string.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for string_02: Longest Palindromic Substring.

Expand around every center, track the longest palindrome, return
the leftmost on tie.
"""


def solve(s):
    n = len(s)
    if n == 0:
        return ""
    best_lo, best_hi = 0, 0

    def expand(lo, hi):
        while lo >= 0 and hi < n and s[lo] == s[hi]:
            lo -= 1
            hi += 1
        return lo + 1, hi - 1

    for c in range(n):
        lo, hi = expand(c, c)
        if hi - lo > best_hi - best_lo:
            best_lo, best_hi = lo, hi
        if c > 0:
            lo, hi = expand(c - 1, c)
            if hi - lo > best_hi - best_lo:
                best_lo, best_hi = lo, hi

    return s[best_lo:best_hi + 1]
```

</details>

## Walk-through

`s = "cbbd"`

- **i = 0 ('c'):**
  - Odd expand: `L=0, R=0` -> Matches 'c'. Expand -> `L=-1, R=1` (out of bounds). Length = 1.
  - Even expand: `L=0, R=1` -> 'c' != 'b'. Mismatch. Length = 0.
  - Max = 1. `max_len = 1`. `start = 0`. Current = `"c"`.
- **i = 1 ('b'):**
  - Odd expand: `L=1, R=1` -> Matches 'b'. Expand -> `L=0, R=2` ('c' != 'b'). Mismatch. Length = 1.
  - Even expand: `L=1, R=2` -> 'b' == 'b'. Matches! Expand -> `L=0, R=3` ('c' != 'd'). Mismatch. Length = 2.
  - Max = 2. `max_len = 2`. `start = 1 - (2-1)//2 = 1`. Current = `"bb"`.
- **i = 2 ('b'):**
  - Odd expand: Length = 1.
  - Even expand: `L=2, R=3` ('b' != 'd'). Length = 0.
- **i = 3 ('d'):**
  - Odd expand: Length = 1.

Final `start = 1`, `max_len = 2`.
Output: `s[1:3]` = `"bb"`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(1)$ |
| **Average** | $O(N^2)$ | $O(1)$ |
| **Worst** | $O(N^2)$ | $O(1)$ |

The outer loop runs N times. In the worst case (e.g., a string of all identical characters like `"aaaaa"`), the inner `expand_around_center` loop will expand all the way to the edges every single time, taking $O(N)$ operations per iteration. Thus, worst-case time is $O(N^2)$.
Space complexity is $O(1)$ because we only store integer indices representing the boundaries.

## Variants & optimizations

- **Dynamic Programming $O(N^2)$:** You can use a 2D boolean array `dp[i][j]` that represents whether the substring from index i to j is a palindrome. `dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]`. While this is $O(N^2)$ time, it requires $O(N^2)$ space, making the Expand Around Center method strictly superior in memory efficiency.
- **Manacher's Algorithm $O(N)$:** It is mathematically possible to find the longest palindromic substring in strictly linear $O(N)$ time! Manacher's algorithm achieves this by cleverly storing the expansion lengths in an array and utilizing the mirrored properties of smaller palindromes trapped inside larger palindromes to skip redundant expansion checks. However, it is notoriously complex and rarely expected in standard interviews.

## Real-world applications

- **Bioinformatics:** Detecting genomic palindromes in DNA sequences (e.g., restriction enzyme recognition sites), though biological palindromes often refer to reverse complements rather than direct sequence mirrors.

## Related algorithms in cOde(n)

- **[dynamic_27 - Longest Palindromic Subsequence](../dynamic/dp_27_longest-palindromic-subsequence.md)** — A closely related DP problem where characters don't need to be contiguous.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
