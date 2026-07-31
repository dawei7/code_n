# Minimum Deletions to Make Array Divisible

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2344 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Sorting, Heap (Priority Queue), Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/) |

## Problem Description

### Goal

Two arrays, `nums` and `numsDivide`, contain positive integers. Delete any
number of elements from `nums` so that the smallest remaining element divides
every value in `numsDivide`. An integer $x$ divides $y$ exactly when
`y % x == 0`.

Return the minimum number of deletions needed to achieve that condition.
Elements may be deleted from arbitrary positions, but `nums` must retain at
least one usable value. If no value occurring in `nums` can divide every
element of `numsDivide`, return `-1`.

### Function Contract

**Inputs**

- `nums`: A positive-integer array of length $n$.
- `numsDivide`: A positive-integer array of length $m$.

Both lengths lie in $[1,10^5]$, and every value in either array lies in
$[1,10^9]$.

**Return value**

The minimum deletions from `nums` that make its smallest remaining value divide
all of `numsDivide`, or `-1` if that is impossible.

### Examples

**Example 1**

- Input: `nums = [2,3,2,4,3]`, `numsDivide = [9,6,9,3,15]`
- Output: `2`
- Explanation: Deleting both 2s leaves 3 as the minimum, and 3 divides every
  value in `numsDivide`.

**Example 2**

- Input: `nums = [4,3,6]`, `numsDivide = [8,2,6,10]`
- Output: `-1`
- Explanation: No value in `nums` divides all four target values.
