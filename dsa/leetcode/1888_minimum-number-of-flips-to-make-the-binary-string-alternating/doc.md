# Minimum Number of Flips to Make the Binary String Alternating

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/) |
| Frontend ID | 1888 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Dynamic Programming, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Given a binary string `s`, two operations may be applied in any order and any number of times. A type-1 operation removes the first character and appends it to the end, cyclically rotating the string left by one position. A type-2 operation chooses any one position and flips its bit from `0` to `1` or from `1` to `0`.

A binary string is alternating when every adjacent pair contains different characters, as in `010` or `1010`. Use type-1 rotations freely, and return the minimum number of type-2 flips needed to obtain an alternating string. Only bit flips contribute to the returned cost.

### Function Contract

**Inputs**

- `s`: a binary string of length $N$ containing only `0` and `1`.
- $1 \le N \le 10^5$.

**Return value**

- Return the minimum number of type-2 bit flips needed after choosing any number of type-1 left rotations.

### Examples

**Example 1**

- Input: `s = "111000"`
- Output: `2`

Two left rotations produce `100011`; flipping its third and sixth characters yields `101010`.

**Example 2**

- Input: `s = "010"`
- Output: `0`

The original string is already alternating.

**Example 3**

- Input: `s = "1110"`
- Output: `1`

Flipping the second character produces `1010`.
