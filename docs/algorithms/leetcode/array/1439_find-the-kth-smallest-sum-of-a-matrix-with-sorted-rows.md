# Find the Kth Smallest Sum of a Matrix With Sorted Rows

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1439 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Heap (Priority Queue), Matrix |
| Official Link | [find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows](https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/) |

## Problem Description & Examples
### Goal
Given a matrix whose rows are sorted in non-decreasing order, choose exactly one value from each row. Return the `k`th smallest possible sum among all such choices.

### Function Contract
**Inputs**

- `mat`: a row-sorted integer matrix.
- `k`: the one-based rank of the desired sum.

**Return value**

The `k`th smallest row-pick sum.

### Examples
**Example 1**

- Input: `mat = [[1,3,11],[2,4,6]], k = 5`
- Output: `7`

**Example 2**

- Input: `mat = [[1,3,11],[2,4,6]], k = 9`
- Output: `17`

**Example 3**

- Input: `mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7`
- Output: `9`

---

## Underlying Base Algorithm(s)
Iterative k-way merge with a bounded heap/list. Maintain the smallest `k` sums after processing each row by combining the current candidates with that row and truncating back to `k`.

---

## Complexity Analysis
- **Time Complexity**: `O(m * k * n log(k n))` for `m` rows and `n` columns with straightforward bounded merging.
- **Space Complexity**: `O(k n)` during each merge, reducible to `O(k)` with heap pruning.
