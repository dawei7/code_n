# Count Almost Equal Pairs I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3265 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Sorting, Counting, Enumeration |
| Official Link | [count-almost-equal-pairs-i](https://leetcode.com/problems/count-almost-equal-pairs-i/) |

## Problem Description & Examples
### Goal
Determine the total number of pairs of indices `(i, j)` such that `i < j` where the integers `nums[i]` and `nums[j]` are "almost equal." Two numbers are considered almost equal if they are identical or if one can be transformed into the other by swapping exactly one pair of digits.

### Function Contract
**Inputs**

- `nums`: A list of positive integers.

**Return value**

- An integer representing the count of pairs `(i, j)` with `i < j` that satisfy the almost equal condition.

### Examples
**Example 1**

- Input: `nums = [3, 12, 30, 17, 21]`
- Output: `2`
- Explanation: The pairs are (3, 30) and (12, 21).

**Example 2**

- Input: `nums = [1, 1, 1, 1]`
- Output: `6`
- Explanation: All pairs are identical, thus almost equal.

**Example 3**

- Input: `nums = [123, 231]`
- Output: `1`
- Explanation: 123 can become 231 by swapping '1' and '2'.

---

## Underlying Base Algorithm(s)
The solution utilizes a brute-force comparison approach optimized by string normalization. Since the constraints are small (N <= 100), we iterate through all pairs `(i, j)`. For each pair, we check if they are equal or if one can be transformed into the other by swapping two digits. To handle different lengths, we pad the shorter number with leading zeros to match the length of the longer number.

---

## Complexity Analysis
- **Time Complexity**: `O(N^2 * D)`, where `N` is the number of elements in `nums` and `D` is the number of digits (max 7). We perform a constant number of swaps and comparisons for each pair.
- **Space Complexity**: `O(D)` to store the string representations of the numbers during comparison.
