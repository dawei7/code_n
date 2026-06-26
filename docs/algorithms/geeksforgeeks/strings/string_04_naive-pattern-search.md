# Naive Pattern Search

| | |
|---|---|
| **ID** | `string_04` |
| **Category** | strings |
| **Complexity (required)** | $O(N * M)$ |
| **Difficulty** | 1/10 |
| **Interview relevance** | 5/10 |
| **LeetCode Equivalent** | [Implement strStr()](https://leetcode.com/problems/implement-strstr/) |

## Problem statement

Given two strings: a `text` of length `N` and a `pattern` of length `M`.
Find all starting indices in `text` where `pattern` exists as a contiguous substring.

**Input:** Two strings `text` and `pattern`.
**Output:** A list of integers representing the starting indices of matches.

**Example:**
`text = "AABAACAADAABAABA"`, `pattern = "AABA"`
Output: `[0, 9, 12]`.

## When to use it

- When the pattern is very short (e.g., M \le 5) or the text is very short, making the overhead of building complex auxiliary data structures (like KMP's LPS array) unnecessary.
- As a baseline brute-force algorithm to understand the exact problem that KMP and Rabin-Karp are designed to solve.

## Approach

We simply align the `pattern` with the `text` starting at index 0. We check character by character.
- If all characters match, we record the starting index.
- If a mismatch occurs at any point, we completely abandon the current comparison, shift the pattern exactly 1 space to the right, and start the comparison all over again from the first character of the pattern.

We repeat this process until the end of the `text`. The last valid starting position for the pattern is index `N - M`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for string_04: Naive Pattern Search.

Slide the pattern across the text, compare character-by-character.
"""


def solve(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0:
        return 0
    if m > n:
        return -1
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            return i
    return -1
```

</details>

## Walk-through

`text = "ABCA"`, `pattern = "BC"`.
`N = 4, M = 2`. Loop `i` from `0` to `4 - 2 = 2`.

**i = 0:**
- Compare `text[0]` ('A') with `pattern[0]` ('B').
- Mismatch! Break.

**i = 1:**
- Compare `text[1]` ('B') with `pattern[0]` ('B'). Match!
- Compare `text[2]` ('C') with `pattern[1]` ('C'). Match!
- Loop finishes. `match_found = True`. Append `1` to result.

**i = 2:**
- Compare `text[2]` ('C') with `pattern[0]` ('B').
- Mismatch! Break.

Output: `[1]`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(1)$ |
| **Average** | $O(N * M)$ | $O(1)$ |
| **Worst** | $O(N * M)$ | $O(1)$ |

The outer loop runs N - M + 1 times.
The inner loop runs up to M times.
In the worst-case scenario (e.g., `text = "AAAAAAAAAB"`, `pattern = "AAAB"`), the inner loop successfully checks almost the entire pattern before failing on the very last character, resulting in exactly $O(N \times M)$ comparisons.
Space complexity is $O(1)$ (excluding the space to hold the returned list of matched indices).

## Variants & optimizations

- **Language Built-ins:** In almost all high-level programming languages, the built-in string searching function (e.g., `text.find(pattern)` in Python, or `text.indexOf(pattern)` in Java) is highly optimized. While they may conceptually fall back to a naive search for small strings, they use SIMD instructions or variants of the Boyer-Moore algorithm under the hood. For coding interviews, you should use the built-in functions unless specifically asked to implement a pattern-matching algorithm from scratch.

## Real-world applications

- **Small Text Snippets:** Because algorithms like KMP and Rabin-Karp have overhead (allocating memory for arrays or doing heavy modulo arithmetic), Naive Search is actually the strictly faster and more optimal choice in the real world when searching for very short strings.

## Related algorithms in cOde(n)

- **[string_03 - KMP String Matching](string_03_kmp-string-matching.md)** — The optimized $O(N+M)$ version that skips redundant checks.
- **[string_06 - Rabin-Karp](string_06_rabin-karp.md)** — An optimized version that uses rolling hashes to skip the inner loop checks.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
