# Special Binary String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 761 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Divide and Conquer, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/special-binary-string/) |

## Problem Description

### Goal

A binary string is special when it contains the same number of `1` and `0` characters and every prefix has at least as many `1`s as `0`s. The input string `s` is guaranteed to be special.

In one move, choose two consecutive, nonempty special substrings of `s` and swap their positions. You may perform the move any number of times. Return the lexicographically largest string obtainable while preserving the characters; every intermediate arrangement must arise through the allowed adjacent special-substring swaps.

### Function Contract

**Inputs**

- `s`: a special binary string.

**Return value**

- The lexicographically largest special string obtainable through any number of allowed adjacent-special-substring swaps.

### Examples

**Example 1**

- Input: `s = "11011000"`
- Output: `"11100100"`
- Explanation: Optimizing and reordering the special blocks inside the outer pair produces the larger string.

**Example 2**

- Input: `s = "10"`
- Output: `"10"`
- Explanation: The only nonempty special block cannot be improved.

**Example 3**

- Input: `s = "101100"`
- Output: `"110010"`
- Explanation: The top-level blocks `"10"` and `"1100"` can be swapped, and the longer block is lexicographically larger.
