# Sum of Squares of Special Elements 

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2778 |
| Difficulty | Easy |
| Topics | Array, Enumeration |
| Official Link | [sum-of-squares-of-special-elements](https://leetcode.com/problems/sum-of-squares-of-special-elements/) |

## Problem Description & Examples
### Goal
Given a 1-indexed array of integers, identify all "special" elements. An element at index `i` (where `1 <= i <= n`) is considered special if `n` is divisible by `i`. The objective is to calculate the sum of the squares of all such special elements.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the array.

**Return value**

- An integer representing the sum of the squares of all elements `nums[i-1]` where `i` divides the length of the array.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4]`
- Output: `21`
- Explanation: The length `n = 4`. Divisors of 4 are 1, 2, and 4. The elements at these indices are `nums[0]=1`, `nums[1]=2`, and `nums[3]=4`. Sum of squares: `1^2 + 2^2 + 4^2 = 1 + 4 + 16 = 21`.

**Example 2**

- Input: `nums = [2, 7, 1, 19, 18, 3]`
- Output: `63`
- Explanation: The length `n = 6`. Divisors of 6 are 1, 2, 3, and 6. The elements are `nums[0]=2`, `nums[1]=7`, `nums[2]=1`, and `nums[5]=3`. Sum of squares: `2^2 + 7^2 + 1^2 + 3^2 = 4 + 49 + 1 + 9 = 63`.

---

## Underlying Base Algorithm(s)
The problem utilizes a linear scan (enumeration) approach. By iterating through the array indices from 1 to `n`, we check the divisibility condition `n % i == 0` for each index. If the condition holds, we add the square of the corresponding element to a running total.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of the input array, as we iterate through the array exactly once.
- **Space Complexity**: `O(1)`, as we only use a single variable to store the running sum.
