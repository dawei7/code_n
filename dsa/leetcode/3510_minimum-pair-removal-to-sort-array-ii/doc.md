# Minimum Pair Removal to Sort Array II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3510 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Linked List, Heap (Priority Queue), Simulation, Doubly-Linked List, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/) |

## Problem Description

### Goal

Starting with `nums`, repeatedly replace two adjacent elements by their sum. The pair is not freely chosen: it must have the minimum sum among all adjacent pairs currently in the array. When several pairs share that minimum, the leftmost one must be selected.

Every replacement shortens the array by one and can change the sums and order relationships around the merged value. Return the minimum number of these prescribed operations required for the array to become non-decreasing, meaning each element is at least the one immediately before it.

This version permits up to $10^5$ elements and values with magnitude $10^9$, so the sequence of operations must be maintained without rescanning or shifting the whole current array after every merge.

### Function Contract

**Inputs**

- `nums`: The integer array on which the mandatory minimum-sum merge process begins.

Let $n=\lvert\texttt{nums}\rvert$. The constraints are $1 \le n \le 10^5$ and $-10^9 \le \texttt{nums[i]} \le 10^9$.

**Return value**

Return the number of minimum-sum adjacent-pair replacements performed before the array first becomes non-decreasing.

### Examples

**Example 1**

- Input: `nums = [5,2,3,1]`
- Output: `2`
- Explanation: Replace `(3,1)` by `4`, producing `[5,2,4]`. Then replace `(2,4)` by `6`; `[5,6]` is non-decreasing.

**Example 2**

- Input: `nums = [1,2,2]`
- Output: `0`
- Explanation: The original array is already non-decreasing.
