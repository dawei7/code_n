# Maximum Subarray With Equal Products

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3411 |
| Difficulty | Easy |
| Topics | Array, Math, Sliding Window, Enumeration, Number Theory |
| Official Link | [maximum-subarray-with-equal-products](https://leetcode.com/problems/maximum-subarray-with-equal-products/) |

## Problem Description & Examples
### Goal
Given an array of integers, identify the length of the longest contiguous subarray where the product of all elements in the subarray is equal to the product of the greatest common divisor (GCD) and the least common multiple (LCM) of all elements in that same subarray.

### Function Contract
**Inputs**

- `nums`: A list of positive integers (`List[int]`).

**Return value**

- An integer representing the length of the longest subarray satisfying the condition `product(subarray) == gcd(subarray) * lcm(subarray)`.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 1, 4, 5, 1]`
- Output: `3`
- Explanation: The subarray `[1, 2, 3]` has product 6, GCD 1, and LCM 6. 1 * 6 = 6.

**Example 2**

- Input: `nums = [2, 4, 8]`
- Output: `2`
- Explanation: The subarray `[2, 4]` has product 8, GCD 2, and LCM 4. 2 * 4 = 8.

**Example 3**

- Input: `nums = [1, 1, 1]`
- Output: `3`
- Explanation: The entire array satisfies the condition.

---

## Underlying Base Algorithm(s)
The problem is solved using a brute-force enumeration approach. Since the product of elements grows exponentially, it will quickly exceed the limits of standard integer types (though Python handles arbitrary-precision integers). Given the constraints typical for this difficulty level, an $O(N^2)$ approach checking all possible subarrays is efficient enough. We maintain the running product, GCD, and LCM for each starting position to avoid redundant calculations.

---

## Complexity Analysis
- **Time Complexity**: $O(N^2 \cdot \log(\max(nums)))$, where $N$ is the length of the array. The nested loops iterate through all subarrays, and GCD/LCM calculations take logarithmic time relative to the values.
- **Space Complexity**: $O(1)$, as we only store a few variables for the current subarray metrics.
