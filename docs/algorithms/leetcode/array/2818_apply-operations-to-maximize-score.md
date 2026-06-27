# Apply Operations to Maximize Score

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2818 |
| Difficulty | Hard |
| Topics | Array, Math, Stack, Greedy, Sorting, Monotonic Stack, Number Theory |
| Official Link | [apply-operations-to-maximize-score](https://leetcode.com/problems/apply-operations-to-maximize-score/) |

## Problem Description & Examples
### Goal
Given an array of integers and an integer `k`, you are tasked with selecting exactly `k` elements from the array. For each element, you can perform an operation: replace the element with the product of its prime factors (distinct). You want to maximize the product of the chosen `k` elements after performing these operations, where the selection must be made such that each element's contribution to the final product is determined by its "prime score" (the count of its distinct prime factors). Specifically, you must choose a subsequence of length `k` such that the product of the chosen elements is maximized, subject to the constraint that the elements are chosen based on their prime scores and their relative positions in the array.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the input array.
- `k`: An integer representing the number of elements to select.

**Return value**

- An integer representing the maximum possible product of `k` elements modulo 10^9 + 7.

### Examples
**Example 1**

- Input: `nums = [8, 3, 9, 3, 8], k = 2`
- Output: `81`
- Explanation: Prime scores are [1, 1, 1, 1, 1]. We pick 9 and 9 (or 8 and 9, etc). The max product is 81.

**Example 2**

- Input: `nums = [19, 12, 14, 6, 10, 18], k = 3`
- Output: `4788`

**Example 3**

- Input: `nums = [2, 4, 8, 16], k = 2`
- Output: `64`

---

## Underlying Base Algorithm(s)
1. **Sieve of Eratosthenes**: Precompute the number of distinct prime factors for all numbers up to the maximum value in `nums`.
2. **Monotonic Stack**: Determine the range `[L, R]` for each index `i` where `nums[i]` is the maximum element based on its prime score. This helps identify how many subsequences include `nums[i]`.
3. **Greedy Strategy**: Sort the elements by their values in descending order and pick the largest available elements until `k` elements are selected, using the counts derived from the monotonic stack.
4. **Modular Exponentiation**: Compute the final product modulo 10^9 + 7.

---

## Complexity Analysis
- **Time Complexity**: `O(N log(log M) + N)`, where `N` is the length of `nums` and `M` is the maximum value in `nums`. The sieve takes `O(M log log M)`, and the monotonic stack and sorting take `O(N log N)`.
- **Space Complexity**: `O(N + M)` to store the prime scores and the stack/auxiliary arrays.
