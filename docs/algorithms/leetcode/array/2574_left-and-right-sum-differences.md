# Left and Right Sum Differences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2574 |
| Difficulty | Easy |
| Topics | Array, Prefix Sum |
| Official Link | [left-and-right-sum-differences](https://leetcode.com/problems/left-and-right-sum-differences/) |

## Problem Description & Examples
### Goal
Given an array of integers, construct a new array where each element at index `i` represents the absolute difference between the sum of all elements to the left of `i` and the sum of all elements to the right of `i`. If no elements exist on a side, the sum for that side is considered zero.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- A list of integers (`List[int]`) representing the absolute differences for each index.

### Examples
**Example 1**

- Input: `nums = [10, 4, 8, 3]`
- Output: `[15, 1, 11, 22]`

**Example 2**

- Input: `nums = [1]`
- Output: `[0]`

**Example 3**

- Input: `nums = [2, 5, 1, 6, 1]`
- Output: `[13, 6, 0, 5, 13]`

---

## Underlying Base Algorithm(s)
The problem utilizes the **Prefix Sum** technique. By maintaining a running total of elements encountered so far (left sum) and calculating the total sum of the array beforehand, the right sum for any index `i` can be derived efficiently as `total_sum - left_sum - nums[i]`.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array. We traverse the array twice: once to calculate the total sum and once to compute the differences.
- **Space Complexity**: `O(n)` to store the resulting array of differences.
