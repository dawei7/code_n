# Largest Perimeter Triangle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 976 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/largest-perimeter-triangle/) |

## Problem Description

### Goal

An integer array `nums` supplies available side lengths. Choose three entries and use those lengths as the sides of a triangle whose area is non-zero. Among every valid choice, return the largest possible perimeter, which is the sum of its three side lengths.

Each chosen side comes from a separate array position, so equal lengths may be used when they occur multiple times. A valid triangle must satisfy the strict triangle inequality; three collinear lengths whose two smaller sides sum exactly to the largest have zero area and are not allowed. Return `0` when no three entries can form a qualifying triangle.

### Function Contract

**Inputs**

- `nums`: a list of $N$ positive integer side lengths, where $3 \le N \le 10^4$ and $1 \le \texttt{nums[i]} \le 10^6$.

For candidate sides sorted as $a\le b\le c$, non-zero area is equivalent to $a+b>c$.

**Return value**

- The greatest perimeter $a+b+c$ among valid triples, or `0` if none exists.

### Examples

**Example 1**

- Input: `nums = [2, 1, 2]`
- Output: `5`
- Explanation: lengths $1$, $2$, and $2$ satisfy $1+2>2$.

**Example 2**

- Input: `nums = [1, 2, 1, 10]`
- Output: `0`
- Explanation: no selection of three lengths satisfies the strict triangle inequality.
