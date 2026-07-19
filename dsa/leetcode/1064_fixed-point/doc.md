# Fixed Point

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1064 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/fixed-point/) |

## Problem Description

### Goal

Given an array `arr` of distinct integers sorted in **ascending order**, find an index `i` whose stored value equals the index itself, so `arr[i] == i`. Such an index is called a fixed point.

Return the smallest index satisfying that equality. More than one fixed point may exist, so finding any match is insufficient when an earlier match is present. If the array contains no fixed point, return `-1`.

### Function Contract

**Inputs**

- `arr`: an ascending array of $N$ distinct integers, where $1 \le N < 10^4$ and each value lies between $-10^9$ and $10^9$.

**Return value**

- The smallest index `i` for which `arr[i] == i`, or `-1` if no such index exists.

### Examples

**Example 1**

- Input: `arr = [-10, -5, 0, 3, 7]`
- Output: `3`
- Explanation: `arr[3]` equals `3`.

**Example 2**

- Input: `arr = [0, 2, 5, 8, 17]`
- Output: `0`

**Example 3**

- Input: `arr = [-10, -5, 3, 4, 7, 9]`
- Output: `-1`
