# Count Pairs Whose Sum is Less than Target

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2824 |
| Difficulty | Easy |
| Topics | Array, Two Pointers, Binary Search, Sorting |
| Official Link | [count-pairs-whose-sum-is-less-than-target](https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/) |

## Problem Description & Examples
### Goal
Given a list of integers and a target value, determine the total number of unique index pairs (i, j) such that i < j and the sum of the elements at these indices is strictly less than the target.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).
- `target`: An integer representing the threshold sum.

**Return value**

- An integer representing the count of valid pairs (i, j) where `i < j` and `nums[i] + nums[j] < target`.

### Examples
**Example 1**

- Input: `nums = [-1, 1, 2, 3, 1], target = 2`
- Output: `3`
- Explanation: Valid pairs are (0, 1), (0, 3), and (0, 4) because their sums are 0, 2, and 0 respectively, all < 2.

**Example 2**

- Input: `nums = [-6, 2, 5, -2, -7, -1, 3], target = -2`
- Output: `10`

**Example 3**

- Input: `nums = [1, 2, 3, 4, 5], target = 10`
- Output: `10`

---

## Underlying Base Algorithm(s)
The optimal approach utilizes **Sorting** combined with the **Two Pointers** technique. By sorting the array first, we can efficiently determine how many elements, when paired with a fixed element at the left pointer, satisfy the condition. If `nums[left] + nums[right] < target`, then all elements between `left` and `right` also satisfy the condition when paired with `nums[left]`, allowing us to count them in constant time and increment the `left` pointer.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)` due to the sorting step, where `n` is the length of the input array. The two-pointer traversal itself is `O(n)`.
- **Space Complexity**: `O(1)` or `O(n)` depending on the sorting implementation's space requirements (Python's Timsort uses `O(n)`).
