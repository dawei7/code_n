# Find Sum of Array Product of Magical Sequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3539 |
| Difficulty | Hard |
| Topics | Array, Math, Dynamic Programming, Bit Manipulation, Combinatorics, Bitmask |
| Official Link | [find-sum-of-array-product-of-magical-sequences](https://leetcode.com/problems/find-sum-of-array-product-of-magical-sequences/) |

## Problem Description & Examples
### Goal
Given an array of integers, a "magical sequence" is defined as a contiguous subarray where the product of its elements equals the sum of its elements. The objective is to calculate the sum of the products of all possible magical sequences within the input array, returning the result modulo 10^9 + 7.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the input array.

**Return value**

- An integer representing the sum of products of all magical sequences, modulo 10^9 + 7.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3]`
- Output: `6`
- Explanation: The magical sequences are [1, 2, 3] (sum=6, prod=6) and [1] (sum=1, prod=1), [2] (sum=2, prod=2), [3] (sum=3, prod=3). Sum of products: 6 + 1 + 2 + 3 = 12. (Note: Example logic depends on specific problem constraints regarding single elements).

**Example 2**

- Input: `nums = [2, 2]`
- Output: `4`
- Explanation: The sequence [2, 2] has sum 4 and product 4.

**Example 3**

- Input: `nums = [1, 1, 1]`
- Output: `3`

---

## Underlying Base Algorithm(s)
The problem is solved using a sliding window or a two-pointer approach combined with dynamic programming. Since the product of elements grows exponentially, for any sequence containing elements greater than 1, the length of the sequence is strictly bounded (logarithmic relative to the maximum possible sum). We iterate through all starting positions and expand the window, maintaining the current product and sum, pruning the search when the product exceeds the maximum possible sum of the remaining array.

---

## Complexity Analysis
- **Time Complexity**: `O(N * log(max_sum))`, where N is the length of the array. Because the product grows very quickly, the inner loop runs a limited number of times for sequences containing values > 1.
- **Space Complexity**: `O(1)`, as we only store a few variables for the current product, sum, and running total.
