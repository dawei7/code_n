# Missing Number In Arithmetic Progression

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1228 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/missing-number-in-arithmetic-progression/) |

## Problem Description

### Goal

An array originally formed an arithmetic progression: the difference between every pair of consecutive values was the same. Exactly one value that was neither the first nor the last was removed from that array.

You are given the remaining values in their original order as `arr`. Return the removed value. The input is guaranteed to come from such a valid removal, and the progression may be increasing, decreasing, or constant.

### Function Contract

**Inputs**

- `arr`: The $n$ remaining progression values, where $3\le n\le1000$ and $0\le\texttt{arr[i]}\le10^5$.

**Return value**

- The unique interior value removed from the original arithmetic progression.

### Examples

**Example 1**

- Input: `arr = [5,7,11,13]`
- Output: `9`

The original progression was `[5,7,9,11,13]` with common difference `2`.

**Example 2**

- Input: `arr = [15,13,12]`
- Output: `14`

The original progression was decreasing by `1`.

**Example 3**

- Input: `arr = [0,0,0,0,0]`
- Output: `0`

Removing one value from a constant progression leaves the same values.
