# Earliest Second to Mark Indices II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3049 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Greedy, Heap (Priority Queue) |
| Official Link | [earliest-second-to-mark-indices-ii](https://leetcode.com/problems/earliest-second-to-mark-indices-ii/) |

## Problem Description & Examples
### Goal
Determine the earliest time (in seconds) by which all indices in an array can be marked. You are given an array `nums` representing the initial values of indices and a sequence `changeIndices` representing the index to be targeted at each second. At each second `s`, you can either decrement the value of `nums[changeIndices[s]]` (if it's > 0), mark the index `changeIndices[s]` (if its value is 0), or do nothing. Marking an index is only possible if its value is 0.

### Function Contract
**Inputs**

- `nums`: A list of integers where `nums[i]` is the initial value of index `i`.
- `changeIndices`: A list of integers where `changeIndices[s]` is the index targeted at second `s` (1-indexed).

**Return value**

- An integer representing the minimum time required to mark all indices. If it is impossible to mark all indices, return -1.

### Examples
**Example 1**

- Input: `nums = [3, 2, 3], changeIndices = [1, 3, 2, 2, 2, 2, 3]`
- Output: `6`

**Example 2**

- Input: `nums = [0, 0, 1, 2], changeIndices = [1, 2, 1, 2, 1, 2, 1, 2]`
- Output: `7`

**Example 3**

- Input: `nums = [1, 2, 3], changeIndices = [1, 2, 3]`
- Output: `-1`

---

## Underlying Base Algorithm(s)
The problem is solved using **Binary Search on the Answer** combined with a **Greedy strategy**. Since the feasibility of marking all indices is monotonic (if it's possible at time `T`, it's possible at `T+1`), we binary search for the minimum time. For a fixed time `T`, we verify feasibility by prioritizing indices that have the largest initial values to be reduced to zero, using a min-heap to track the "cost" of reducing values and ensuring we have enough spare seconds to perform the marking operations.

---

## Complexity Analysis
- **Time Complexity**: `O(N log N + M log M)` where `N` is the length of `nums` and `M` is the length of `changeIndices`. The binary search takes `O(log M)` steps, and each check involves heap operations and array traversals.
- **Space Complexity**: `O(N + M)` to store the indices, the heap, and the auxiliary arrays used during the feasibility check.
