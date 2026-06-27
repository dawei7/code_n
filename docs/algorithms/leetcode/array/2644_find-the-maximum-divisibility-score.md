# Find the Maximum Divisibility Score

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2644 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [find-the-maximum-divisibility-score](https://leetcode.com/problems/find-the-maximum-divisibility-score/) |

## Problem Description & Examples
### Goal
Given two integer arrays, `nums` and `divisors`, determine which divisor yields the highest "divisibility score." The score for a specific divisor is defined as the count of elements in `nums` that are perfectly divisible by that divisor. If multiple divisors share the same maximum score, return the smallest divisor among them.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the dividend pool.
- `divisors`: A list of integers representing the potential divisors.

**Return value**

- An integer representing the divisor that achieves the highest divisibility score. In the event of a tie in scores, the smallest divisor is returned.

### Examples
**Example 1**

- Input: `nums = [4, 7, 9, 3, 9]`, `divisors = [5, 2, 3]`
- Output: `3`
- Explanation: 5 divides 0 elements, 2 divides 1 element (4), and 3 divides 2 elements (9, 9). 3 is the winner.

**Example 2**

- Input: `nums = [20, 14, 21, 10]`, `divisors = [5, 7, 5]`
- Output: `5`
- Explanation: 5 divides 2 elements (20, 10), 7 divides 2 elements (14, 21). Since 5 < 7, we return 5.

**Example 3**

- Input: `nums = [12]`, `divisors = [10, 16]`
- Output: `10`
- Explanation: Neither divisor divides 12. We return the smaller divisor, 10.

---

## Underlying Base Algorithm(s)
The problem is solved using a linear scan (brute force) approach. We iterate through each divisor and, for each, perform a nested iteration over the `nums` array to count how many elements satisfy the divisibility condition (`num % divisor == 0`). We maintain a running maximum score and the corresponding best divisor found so far.

---

## Complexity Analysis
- **Time Complexity**: O(N * M), where N is the length of `nums` and M is the length of `divisors`. We check every divisor against every number in the input array.
- **Space Complexity**: O(1), as we only store a few integer variables to track the maximum score and the best divisor, regardless of input size.
