# Patching Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 330 |
| Difficulty | Hard |
| Topics | Array, Greedy |
| Official Link | [patching-array](https://leetcode.com/problems/patching-array/) |

## Problem Description & Examples
### Goal
Given a sorted array of positive integers and an integer `n`, determine the minimum number of elements to add to the array such that every integer in the range `[1, n]` can be formed by the sum of some subset of the modified array.

### Function Contract
**Inputs**

- `nums`: A sorted list of positive integers.
- `n`: An integer representing the upper bound of the target range `[1, n]`.

**Return value**

- An integer representing the minimum number of patches (additions) required.

### Examples
**Example 1**

- Input: `nums = [1, 3], n = 6`
- Output: `1`
- Explanation: We can form all numbers in [1, 6] by adding 2 to the array. The new array is [1, 2, 3].

**Example 2**

- Input: `nums = [1, 5, 10], n = 20`
- Output: `2`
- Explanation: We can add 2 and 4 to the array to cover all numbers up to 20.

**Example 3**

- Input: `nums = [1, 2, 2], n = 5`
- Output: `0`
- Explanation: All numbers in [1, 5] are already coverable.

---

## Underlying Base Algorithm(s)
The problem is solved using a **Greedy Strategy**. We maintain a variable `miss`, which represents the smallest sum in the range `[1, n]` that we cannot currently form. Initially, `miss = 1`. If the current element in the array is less than or equal to `miss`, we can extend our reachable range to `miss + nums[i]`. If the current element is greater than `miss` (or we have exhausted the array), we must add `miss` itself to the array to cover the gap, which doubles our reachable range to `2 * miss`.

---

## Complexity Analysis
- **Time Complexity**: `O(m + log n)`, where `m` is the length of the input array. We iterate through the array once and perform logarithmic steps relative to `n` when adding patches.
- **Space Complexity**: `O(1)`, as we only use a few variables to track the state.
