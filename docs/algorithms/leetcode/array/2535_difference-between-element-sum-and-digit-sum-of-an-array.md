# Difference Between Element Sum and Digit Sum of an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2535 |
| Difficulty | Easy |
| Topics | Array, Math |
| Official Link | [difference-between-element-sum-and-digit-sum-of-an-array](https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/) |

## Problem Description & Examples
### Goal
Calculate the absolute difference between the sum of all integers in a given array and the sum of all individual digits that compose those integers.

### Function Contract
**Inputs**

- `nums`: A list of positive integers (`List[int]`).

**Return value**

- An integer representing the absolute difference between the element sum and the digit sum.

### Examples
**Example 1**

- Input: `nums = [1, 15, 6, 3]`
- Output: `9`
- Explanation: Element sum = 1+15+6+3 = 25. Digit sum = 1+1+5+6+3 = 16. Difference = |25 - 16| = 9.

**Example 2**

- Input: `nums = [1, 2, 3, 4]`
- Output: `0`
- Explanation: Element sum = 1+2+3+4 = 10. Digit sum = 1+2+3+4 = 10. Difference = |10 - 10| = 0.

**Example 3**

- Input: `nums = [10, 20, 30]`
- Output: `30`
- Explanation: Element sum = 60. Digit sum = 1+0+2+0+3+0 = 6. Difference = |60 - 6| = 54. (Wait, correction: 60 - 6 = 54).

---

## Underlying Base Algorithm(s)
The problem utilizes basic arithmetic summation and digit extraction. Digit extraction is performed by repeatedly applying the modulo operator (`% 10`) to isolate the last digit and integer division (`// 10`) to shift the number until it reaches zero.

---

## Complexity Analysis
- **Time Complexity**: `O(n * k)`, where `n` is the number of elements in the array and `k` is the average number of digits per integer.
- **Space Complexity**: `O(1)`, as we only store a few integer variables for the running sums regardless of the input size.
