# Split Concatenated Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 555 |
| Difficulty | Medium |
| Topics | Array, String, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/split-concatenated-strings/) |

## Problem Description
### Goal
Given an ordered list of strings, independently choose either the original or reversed form of each string. Concatenate the chosen forms in the given order to create a loop, so the end connects back to the beginning.

Split that loop at any character position and read one complete linear traversal. Return the lexicographically largest string obtainable over all orientation choices and split positions. Every source string contributes all its characters exactly once, the circular order of string blocks cannot be permuted, and the selected cut may occur inside a block rather than only between strings.

### Function Contract
**Inputs**

- `strs`: a non-empty list of non-empty lowercase strings

**Return value**

- The lexicographically largest string obtainable by orientations and one circular split

### Examples
**Example 1**

- Input: `strs = ["abc", "xyz"]`
- Output: `"zyxcba"`

**Example 2**

- Input: `strs = ["abc"]`
- Output: `"cba"`

**Example 3**

- Input: `strs = ["aaa"]`
- Output: `"aaa"`
