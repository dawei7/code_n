# Number of Unequal Triplets in Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2475 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Sorting |
| Official Link | [number-of-unequal-triplets-in-array](https://leetcode.com/problems/number-of-unequal-triplets-in-array/) |

## Problem Description & Examples
### Goal
Given an array of integers, identify the total number of triplets (i, j, k) such that 0 <= i < j < k < n, and the values at these indices are mutually distinct (nums[i] != nums[j], nums[i] != nums[k], and nums[j] != nums[k]).

### Function Contract
**Inputs**

- `nums`: A list of integers where 1 <= nums.length <= 1000 and 1 <= nums[i] <= 1000.

**Return value**

- An integer representing the count of valid triplets that satisfy the inequality conditions.

### Examples
**Example 1**

- Input: `nums = [4,4,2,4,3]`
- Output: `3`
- Explanation: The valid triplets are (0, 2, 4), (1, 2, 4), and (2, 3, 4) corresponding to values (4, 2, 3).

**Example 2**

- Input: `nums = [1,1,1,1,1]`
- Output: `0`
- Explanation: No three elements are distinct.

**Example 3**

- Input: `nums = [1,3,1,2,4]`
- Output: `7`

---

## Underlying Base Algorithm(s)
The problem can be solved using a frequency map (Hash Table) approach. By counting the occurrences of each number, we can calculate the number of triplets by considering the distribution of elements. If we pick a number with frequency `a`, another with frequency `b`, and a third with frequency `c`, the number of ways to form a triplet is `a * b * c`. Alternatively, a brute-force approach with O(n^3) is acceptable given the constraints (n <= 1000), but the frequency approach is O(n).

---

## Complexity Analysis
- **Time Complexity**: O(n), where n is the length of the input array, as we iterate through the array once to build the frequency map and then iterate through the unique elements.
- **Space Complexity**: O(n) in the worst case to store the frequency map if all elements are unique.
