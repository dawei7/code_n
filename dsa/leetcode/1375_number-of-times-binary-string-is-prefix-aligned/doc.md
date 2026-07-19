# Number of Times Binary String Is Prefix-Aligned

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1375 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/number-of-times-binary-string-is-prefix-aligned/) |

## Problem Description

### Goal

A binary string of length `n` initially contains only zeroes. The array `flips` is a permutation of the positions from $1$ through $n$. At step `i`, the bit at position `flips[i]` changes permanently from `0` to `1`.

The string is prefix-aligned after a step when every bit from position $1$ through the number of completed steps is `1`; because exactly that many bits have been changed, all later positions are then still `0`. Count how many steps leave the string prefix-aligned.

### Function Contract

**Inputs**

- `flips`: a permutation of $1, 2, \ldots, n$ describing the order in which the `n` bits are turned on.

**Return value**

- The number of steps after which the bits equal a prefix of `1` values followed by only `0` values.

### Examples

**Example 1**

- Input: `flips = [3,2,4,1,5]`
- Output: `2`

**Example 2**

- Input: `flips = [4,1,2,3]`
- Output: `1`

**Example 3**

- Input: `flips = [1,2,3]`
- Output: `3`
