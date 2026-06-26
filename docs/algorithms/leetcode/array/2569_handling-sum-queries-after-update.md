# Handling Sum Queries After Update

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2569 |
| Difficulty | Hard |
| Topics | Array, Segment Tree |
| Official Link | [handling-sum-queries-after-update](https://leetcode.com/problems/handling-sum-queries-after-update/) |

## Problem Description & Examples
### Goal
You are given two binary arrays of equal length and a series of queries. The queries involve either flipping the bits in a range of the first array or calculating the total sum of the first array. The second array acts as a multiplier for the first array's values during sum calculations. Specifically, the sum is defined as the sum of `nums1[i] * nums2[i]` for all indices `i`.

### Function Contract
**Inputs**

- `nums1`: List[int] (Initial binary array)
- `nums2`: List[int] (Binary array used for weighted sum)
- `queries`: List[List[int]] (List of queries where each query is `[type, l, r]`)

**Return value**

- List[int]: A list containing the results of all type-3 (sum) queries.

### Examples
**Example 1**

- Input: `nums1 = [1,0,1], nums2 = [0,0,0], queries = [[1,1,1],[2,1,0],[3,0,0]]`
- Output: `[0]`

**Example 2**

- Input: `nums1 = [1], nums2 = [5], queries = [[2,0,0],[3,0,0]]`
- Output: `[5]`

---

## Underlying Base Algorithm(s)
The problem requires efficient range updates (flipping bits) and range sum queries. A **Segment Tree with Lazy Propagation** is the optimal data structure. Each node in the tree stores the count of `1`s in its range. When a flip operation occurs, the count of `1`s becomes `(range_length - current_count_of_1s)`. The weighted sum is calculated by maintaining the sum of `nums2` for indices where `nums1` is `1`.

---

## Complexity Analysis
- **Time Complexity**: `O((n + q) log n)`, where `n` is the length of the arrays and `q` is the number of queries. Each segment tree operation takes logarithmic time.
- **Space Complexity**: `O(n)`, required to store the segment tree nodes (typically 4n nodes).
