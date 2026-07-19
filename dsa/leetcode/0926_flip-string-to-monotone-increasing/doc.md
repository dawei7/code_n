# Flip String to Monotone Increasing

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 926 |
| Difficulty | Medium |
| Topics | String, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/flip-string-to-monotone-increasing/) |

## Problem Description
### Goal

A binary string is monotone increasing when it contains some number of `0` characters followed by some number of `1` characters. Either group may be empty, so an all-zero string and an all-one string also satisfy the definition. Equivalently, no `0` may appear after a `1`.

You are given a binary string `s`. In one flip, change a selected `0` to `1` or a selected `1` to `0`. Return the minimum number of flips required to make the entire string monotone increasing.

### Function Contract
**Inputs**

- `s`: a binary string of length $n$, where $1\le n\le10^5$ and every character is either `"0"` or `"1"`.

**Return value**

The minimum number of individual character flips needed to turn `s` into a monotone increasing binary string.

### Examples
**Example 1**

- Input: `s = "00110"`
- Output: `1`
- Explanation: Flipping the final character produces `"00111"`.

**Example 2**

- Input: `s = "010110"`
- Output: `2`
- Explanation: Two flips can produce `"011111"` or `"000111"`.

**Example 3**

- Input: `s = "00011000"`
- Output: `2`
- Explanation: Flipping both `1` characters produces an all-zero string.
