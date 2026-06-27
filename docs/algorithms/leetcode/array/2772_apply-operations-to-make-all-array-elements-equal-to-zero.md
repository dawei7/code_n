# Apply Operations to Make All Array Elements Equal to Zero

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2772 |
| Difficulty | Medium |
| Topics | Array, Prefix Sum |
| Official Link | [apply-operations-to-make-all-array-elements-equal-to-zero](https://leetcode.com/problems/apply-operations-to-make-all-array-elements-equal-to-zero/) |

## Problem Description & Examples
### Goal
Determine if it is possible to reduce all elements of an integer array to zero by repeatedly applying an operation: choose a subarray of length `k` and subtract a constant value from every element within that subarray. You can perform this operation any number of times.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the array to be modified.
- `k`: An integer representing the fixed length of the subarray chosen for the subtraction operation.

**Return value**

- `bool`: Returns `True` if it is possible to make all elements in the array zero, otherwise returns `False`.

### Examples
**Example 1**

- Input: `nums = [2, 2, 3, 1, 1, 0]`, `k = 3`
- Output: `True`

**Example 2**

- Input: `nums = [1, 3, 1, 2]`, `k = 2`
- Output: `False`

**Example 3**

- Input: `nums = [0, 1, 3, 3, 2, 1]`, `k = 4`
- Output: `False`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Difference Array** (or a sliding window with a running sum) approach. Since each operation affects a range of length `k`, we process the array from left to right. We maintain a running total of the subtractions applied to the current index. If the current element (after accounting for previous operations) is non-zero, we must initiate a new operation starting at this index. If the remaining length of the array is less than `k`, or if the required subtraction would result in a negative value, the transformation is impossible.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the array, as we iterate through the array once.
- **Space Complexity**: `O(n)` to store the difference array (or `O(1)` if modifying the input array in-place, though `O(n)` is safer for tracking state).
