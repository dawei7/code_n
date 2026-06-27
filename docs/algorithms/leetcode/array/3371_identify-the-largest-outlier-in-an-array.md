# Identify the Largest Outlier in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3371 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Counting, Enumeration |
| Official Link | [identify-the-largest-outlier-in-an-array](https://leetcode.com/problems/identify-the-largest-outlier-in-an-array/) |

## Problem Description & Examples
### Goal
Given an array of integers, identify the "outlier." An outlier is defined as an element in the array such that the sum of all other elements in the array (excluding the outlier itself) equals twice the value of some other element present in the array. If multiple such outliers exist, return the largest one.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the input array.

**Return value**

- An integer representing the largest value in the array that satisfies the outlier condition.

### Examples
**Example 1**

- Input: `nums = [2, 3, 5, 10]`
- Output: `10`
- Explanation: The sum is 20. If 10 is the outlier, the sum of the rest is 10. Since 10/2 = 5, and 5 is in the array, 10 is a valid outlier.

**Example 2**

- Input: `nums = [-2, -1, -3, -6, 4]`
- Output: `4`
- Explanation: The sum is -8. If 4 is the outlier, the sum of the rest is -12. Since -12/2 = -6, and -6 is in the array, 4 is a valid outlier.

**Example 3**

- Input: `nums = [1, 1, 1, 1, 6, 6]`
- Output: `6`
- Explanation: The sum is 16. If 6 is the outlier, the sum of the rest is 10. Since 10/2 = 5 (not in array). If 1 is the outlier, the sum of the rest is 15. Since 15/2 = 7.5 (not in array).

---

## Underlying Base Algorithm(s)
The problem relies on a Hash Map (or Frequency Dictionary) to achieve O(N) lookup time. By calculating the total sum of the array first, we can iterate through each element `x` and treat it as a potential outlier. If `x` is the outlier, the sum of the remaining elements is `total_sum - x`. The condition requires that `(total_sum - x) / 2` exists in the array. We use a frequency map to verify the existence of this value efficiently, ensuring we account for cases where the "special" element might be the same as the outlier.

---

## Complexity Analysis
- **Time Complexity**: `O(N)`, where N is the number of elements in the array. We iterate through the array twice: once to calculate the total sum and build the frequency map, and once to check the outlier condition.
- **Space Complexity**: `O(N)` to store the frequency map of the elements in the array.
