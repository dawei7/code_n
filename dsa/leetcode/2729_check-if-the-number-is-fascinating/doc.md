# Check if The Number is Fascinating

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2729 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/check-if-the-number-is-fascinating/) |

## Problem Description

### Goal

An integer `n` has exactly three decimal digits. Form one decimal sequence by concatenating `n`, `2 * n`, and `3 * n` in that order.

The number is called fascinating precisely when this combined sequence contains each digit from `1` through `9` exactly once and contains no `0`. Determine whether `n` satisfies that condition. Concatenation joins decimal representations rather than adding their numeric values; for example, concatenating `121` and `371` produces `121371`.

### Function Contract

**Inputs**

- `n`: An integer with $100 \le n \le 999$.

**Return value**

Return `true` if the decimal concatenation of `n`, `2 * n`, and `3 * n` uses every digit from `1` through `9` exactly once and no other digit; otherwise return `false`.

### Examples

**Example 1**

- Input: `n = 192`
- Output: `true`
- Explanation: Concatenating `192`, `384`, and `576` gives `192384576`, which contains each nonzero decimal digit once.

**Example 2**

- Input: `n = 100`
- Output: `false`
- Explanation: The sequence `100200300` contains zeros and repeats other digits.

**Example 3**

- Input: `n = 219`
- Output: `true`
- Explanation: The sequence is `219438657`, another permutation of the digits from `1` through `9`.
