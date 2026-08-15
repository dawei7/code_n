# Minimum Pair Removal to Sort Array I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3507 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Linked List, Heap (Priority Queue), Simulation, Doubly-Linked List, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/) |

## Problem Description

### Goal

Starting with `nums`, you may repeatedly replace two adjacent elements by their sum. The operation does not allow an arbitrary pair: among all adjacent pairs currently present, you must choose one whose sum is minimum. If several pairs share that minimum sum, the leftmost such pair must be selected.

Each replacement shortens the array by one and changes the neighboring pair sums for the newly created value. Return the minimum number of these prescribed operations needed for the array to become non-decreasing. An array is non-decreasing when every element after the first is at least the element immediately before it.

### Function Contract

**Inputs**

- `nums`: The integer array on which the pair-replacement process begins.

Let $n=\lvert\texttt{nums}\rvert$. The constraints are $1 \le n \le 50$ and $-1000 \le \texttt{nums[i]} \le 1000$.

**Return value**

Return the number of mandatory minimum-sum pair replacements performed before the array first becomes non-decreasing.

### Examples

#### Example 1

- **Input:** `nums = [5,2,3,1]`
- **Output:** `2`
- **Explanation:** First replace `(3,1)` by `4`, producing `[5,2,4]`. Then replace `(2,4)` by `6`; `[5,6]` is non-decreasing.

#### Example 2

- **Input:** `nums = [1,2,2]`
- **Output:** `0`
- **Explanation:** The initial array is already non-decreasing, so no replacement is needed.
