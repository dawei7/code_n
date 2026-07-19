# Number of Good Ways to Split a String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1525 |
| Difficulty | Medium |
| Topics | Hash Table, String, Dynamic Programming, Bit Manipulation |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-good-ways-to-split-a-string/) |

## Problem Description
### Goal

Split a lowercase string at one boundary between adjacent characters, producing a nonempty left part and a nonempty right part whose concatenation is the original string. A split is good when the two parts contain the same number of distinct letters.

Count how many of the $n-1$ possible boundaries are good and return that count. Letter frequencies do not need to match across the pieces; only the number of different letters present on each side matters.

### Function Contract
**Inputs**

- `s`: A lowercase English string of length $n$, where $1 \leq n \leq 10^5$.

**Return value**

Return the number of indices $i$ with $1 \leq i < n$ for which `s[:i]` and `s[i:]` contain equal numbers of distinct letters.

### Examples
**Example 1**

- Input: `s = "aacaba"`
- Output: `2`
- Explanation: Splits `("aac", "aba")` and `("aaca", "ba")` each have two distinct letters on both sides.

**Example 2**

- Input: `s = "abcd"`
- Output: `1`
- Explanation: Only `("ab", "cd")` balances two distinct letters on each side.

**Example 3**

- Input: `s = "aaaa"`
- Output: `3`
- Explanation: Every nonempty piece contains only the letter `a`.
