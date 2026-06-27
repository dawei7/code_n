# Distribute Elements Into Two Arrays I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3069 |
| Difficulty | Easy |
| Topics | Array, Simulation |
| Official Link | [distribute-elements-into-two-arrays-i](https://leetcode.com/problems/distribute-elements-into-two-arrays-i/) |

## Problem Description & Examples
### Goal
Given an array of integers, distribute its elements into two separate arrays based on a specific rule: the first element goes to the first array, the second goes to the second array, and subsequent elements are appended to the array whose last element is greater, or to the first array if the last elements are equal.

### Function Contract
**Inputs**

- `nums`: A list of integers (`List[int]`).

**Return value**

- A list containing two lists of integers, representing the final state of the two distributed arrays.

### Examples
**Example 1**

- Input: `nums = [2, 1, 3]`
- Output: `[[2, 3], [1]]`

**Example 2**

- Input: `nums = [5, 4, 3, 8]`
- Output: `[[5, 3], [4, 8]]`

**Example 3**

- Input: `nums = [3, 3, 3, 3]`
- Output: `[[3, 3], [3, 3]]`

---

## Underlying Base Algorithm(s)
The problem is solved using a direct simulation approach. By maintaining two lists and tracking their last elements, we iterate through the input array once and apply the conditional logic to determine the destination of each element.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we perform a single pass over the elements.
- **Space Complexity**: `O(n)`, as we store all elements of the input array across the two resulting lists.
