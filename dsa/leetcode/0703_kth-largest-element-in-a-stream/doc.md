# Kth Largest Element in a Stream

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 703 |
| Difficulty | Easy |
| Topics | Tree, Design, Binary Search Tree, Heap (Priority Queue), Binary Tree, Data Stream |
| Official Link | [LeetCode](https://leetcode.com/problems/kth-largest-element-in-a-stream/) |

## Problem Description
### Goal
A university admissions office receives applicant test scores as a stream and needs to track its cutoff dynamically. Initialize `KthLargest` with a rank `k` and any scores already received in `nums`.

Whenever `add(val)` submits another score, include it with every score seen so far and return the `k`th largest value in that combined multiset. Rank values after sorting from largest to smallest, counting duplicate score occurrences separately. The maintained state persists across additions; a returned cutoff does not remove a score.

### Function Contract
**Inputs**

- `k`: the one-based rank to maintain
- `nums`: values present before streaming begins
- `stream`: values added in order; the app-local adapter performs one native `add` operation for each value

**Return value**

- A list containing the `k`th largest value after every addition from `stream`

### Examples
**Example 1**

- Input: `k = 3, nums = [4,5,8,2], stream = [3,5,10,9,4]`
- Output: `[4,5,5,8,8]`

**Example 2**

- Input: `k = 1, nums = [], stream = [-3,-2,-4,0,4]`
- Output: `[-3,-2,-2,0,4]`

**Example 3**

- Input: `k = 2, nums = [0], stream = [-1,1,-2,-4,3]`
- Output: `[-1,0,0,0,1]`
