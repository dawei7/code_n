# Sort an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 912 |
| Difficulty | Medium |
| Topics | Array, Divide and Conquer, Sorting, Heap (Priority Queue), Merge Sort, Bucket Sort, Radix Sort, Counting Sort |
| Official Link | [LeetCode](https://leetcode.com/problems/sort-an-array/) |

## Problem Description
### Goal
Given an integer array `nums`, rearrange and return its elements in ascending order. Repeated values must appear with their original multiplicities, and negative values participate in the same numeric ordering. The output must contain every original occurrence.

Do not use a built-in sorting function. The algorithm must run in $O(n\log n)$ time and should use the smallest possible amount of auxiliary space.

### Function Contract
Let $n=\lvert\texttt{nums}\rvert$.

**Inputs**

- `nums`: an integer array with $1 \leq n \leq 5\cdot 10^4$ and $-5\cdot 10^4 \leq \texttt{nums}[i] \leq 5\cdot 10^4$.

**Return value**

Return `nums`'s values in ascending order without losing or duplicating any occurrence.

### Examples
**Example 1**

- Input: `nums = [5,2,3,1]`
- Output: `[1,2,3,5]`

**Example 2**

- Input: `nums = [5,1,1,2,0,0]`
- Output: `[0,0,1,1,2,5]`

The repeated zeroes and ones remain repeated in the result.
