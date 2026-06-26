# Minimum Operations to Make Array Equal II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2541 |
| Difficulty | Medium |
| Topics | Array, Math, Greedy |
| Official Link | [minimum-operations-to-make-array-equal-ii](https://leetcode.com/problems/minimum-operations-to-make-array-equal-ii/) |

## Problem Description & Examples
### Goal
Given two integer arrays of equal length and an integer `k`, determine the minimum number of operations required to make the arrays identical. In one operation, you can choose two indices `i` and `j`, add `k` to `nums1[i]`, and subtract `k` from `nums1[j]`. If `k` is 0, you can only perform the operation if the arrays are already identical.

### Function Contract
**Inputs**

- `nums1`: List[int] - The target array to be modified.
- `nums2`: List[int] - The reference array.
- `k`: int - The constant value used for incrementing/decrementing elements.

**Return value**

- `int`: The minimum number of operations required, or -1 if it is impossible to make the arrays equal.

### Examples
**Example 1**

- Input: `nums1 = [4,3,1,4], nums2 = [1,3,7,1], k = 3`
- Output: `2`

**Example 2**

- Input: `nums1 = [3,8,5,2], nums2 = [2,4,1,6], k = 1`
- Output: `-1`

**Example 3**

- Input: `nums1 = [10,10], nums2 = [10,10], k = 0`
- Output: `0`

---

## Underlying Base Algorithm(s)
The problem relies on the invariant that the sum of elements in `nums1` must equal the sum of elements in `nums2` because each operation preserves the total sum. Furthermore, for each index `i`, the difference `nums1[i] - nums2[i]` must be perfectly divisible by `k` (if `k > 0`). We calculate the total positive difference (or negative difference) required to balance the arrays. Since each operation moves `k` from one index to another, the number of operations is simply the sum of all positive differences divided by `k`.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the arrays, as we iterate through the arrays once to calculate differences and sums.
- **Space Complexity**: `O(1)`, as we only use a few variables to track the running sums and differences.
