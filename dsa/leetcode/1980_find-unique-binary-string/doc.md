# Find Unique Binary String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1980 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Backtracking |
| Official Link | [LeetCode](https://leetcode.com/problems/find-unique-binary-string/) |

## Problem Description
### Goal
You are given `n` distinct binary strings in the array `nums`. The array
contains exactly `n` strings, and every string has exactly `n` characters,
each either `0` or `1`.

Construct and return any binary string of length `n` that does not occur in
`nums`. Several strings may satisfy the requirement; no lexicographic,
numeric, or other tie-breaking rule is imposed. The returned value only needs
to be missing from the supplied collection; it does not need to identify or
represent every other binary string that is absent.

### Function Contract
**Inputs**

- `nums`: a list of $N$ distinct binary strings, where $1 \le N \le 16$.
- Every entry has length $N$ and contains only `0` and `1`.

**Return value**

- Any length-$N$ binary string absent from `nums`.

### Examples
**Example 1**

- Input: `nums = ["01", "10"]`
- Output: `"11"`

**Example 2**

- Input: `nums = ["00", "01"]`
- Output: `"10"`

**Example 3**

- Input: `nums = ["111", "011", "001"]`
- Output: `"000"`
