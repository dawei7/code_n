# Maximum Product of Two Elements in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1464 |
| Difficulty | Easy |
| Topics | Array, Sorting, Heap (Priority Queue) |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/) |

## Problem Description
### Goal

Given an integer array `nums`, choose two different indices $i$ and $j$. Subtract `1` from each of the two selected values, then multiply the results to obtain `(nums[i] - 1) * (nums[j] - 1)`.

Return the largest product obtainable from any valid pair of distinct indices. Equal values may be selected when they occur at different positions; it is the indices, rather than the numeric values, that must be different.

### Function Contract
**Inputs**

- `nums`: an array of $n$ integers, where $2 \le n \le 500$ and $1 \le \texttt{nums[i]} \le 10^3$.

**Return value**

Return the maximum value of `(nums[i] - 1) * (nums[j] - 1)` over all index pairs satisfying $i \ne j$.

### Examples
**Example 1**

- Input: `nums = [3,4,5,2]`
- Output: `12`
- Explanation: Choosing the values at indices `1` and `2` gives `(4 - 1) * (5 - 1) = 12`.

**Example 2**

- Input: `nums = [1,5,4,5]`
- Output: `16`
- Explanation: The two occurrences of `5` have different indices, so both may be selected.

**Example 3**

- Input: `nums = [3,7]`
- Output: `12`
- Explanation: With exactly two entries, the only valid pair gives `(3 - 1) * (7 - 1) = 12`.
