# Maximum Product of the Length of Two Palindromic Substrings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1960 |
| Difficulty | Hard |
| Topics | String, Rolling Hash, Manacher's Algorithm |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-substrings/) |

## Problem Description
### Goal
Given a zero-indexed lowercase string `s`, choose two non-intersecting
substrings. Both chosen substrings must be palindromes of odd length, and the
first must end before the second begins.

More precisely, choose indices $i\le j<k\le l$ so that `s[i:j + 1]` and
`s[k:l + 1]` are odd-length palindromes. Return the maximum possible product
of their lengths. A substring is contiguous, and a palindrome reads identically
from left to right and right to left.

### Function Contract
**Inputs**

- `s`: a lowercase English string of length $N$, where
  $2\le N\le10^5$.

**Return value**

- The maximum product of the lengths of two non-overlapping odd-length
  palindromic substrings.

### Examples
**Example 1**

- Input: `s = "ababbb"`
- Output: `9`

**Example 2**

- Input: `s = "zaaaxbbby"`
- Output: `9`

**Example 3**

- Input: `s = "racecarxaba"`
- Output: `21`
