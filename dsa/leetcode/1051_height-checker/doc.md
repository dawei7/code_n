# Height Checker

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1051 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Sorting, Counting Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/height-checker/) |

## Problem Description

### Goal

A school is arranging students in one line for its annual photo. The requested arrangement is **non-decreasing order** by height; let `expected[i]` be the height that should appear at 0-indexed position `i` in that ordering.

The array `heights` gives the students' current order, with `heights[i]` representing the student at position `i`. Return the number of indices for which `heights[i] != expected[i]`. Students with equal heights are indistinguishable for this comparison.

### Function Contract

**Inputs**

- `heights`: the $N$ current heights, where $1 \le N \le 100$ and every height lies in $[1,H]$, with $H=100$.

**Return value**

- The number of positions whose current height differs from the height at that position in non-decreasing order.

### Examples

**Example 1**

- Input: `heights = [1,1,4,2,1,3]`
- Output: `3`
- Explanation: The expected order is `[1,1,1,2,3,4]`; indices `2`, `4`, and `5` differ.

**Example 2**

- Input: `heights = [5,1,2,3,4]`
- Output: `5`
- Explanation: Every position differs from `[1,2,3,4,5]`.

**Example 3**

- Input: `heights = [1,2,3,4,5]`
- Output: `0`
