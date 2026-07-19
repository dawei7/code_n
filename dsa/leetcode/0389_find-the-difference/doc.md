# Find the Difference

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 389 |
| Difficulty | Easy |
| Topics | Hash Table, String, Bit Manipulation, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-difference/) |

## Problem Description
### Goal
Given a lowercase string `s`, string `t` was formed by adding exactly one character occurrence to `s` and then shuffling all occurrences. Repeated letters may be present in either string, and the added character may equal a character already present.

Return the extra character occurrence. Comparing only sets is insufficient because multiplicity identifies the difference, while original positions provide no information after shuffling. The guarantee ensures exactly one answer and `len(t) = len(s) + 1`. When `s` is empty, return the sole character of `t`; the function returns a character rather than its index.

### Function Contract
**Inputs**

- `s`: the original lowercase string
- `t`: a permutation of all characters in `s` plus one extra lowercase character

**Return value**

- Return the character occurrence that was added to form `t`.

### Examples
**Example 1**

- Input: `s = "abcd", t = "abcde"`
- Output: `"e"`

**Example 2**

- Input: `s = "", t = "y"`
- Output: `"y"`

**Example 3**

- Input: `s = "aabb", t = "ababa"`
- Output: `"a"`
