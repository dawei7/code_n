# Sum of Floored Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1862 |
| Difficulty | Hard |
| Topics | Array, Math, Binary Search, Counting, Enumeration, Prefix Sum |
| Official Link | [sum-of-floored-pairs](https://leetcode.com/problems/sum-of-floored-pairs/) |

## Problem Description & Examples
### Goal
For every ordered pair `(i, j)`, compute `floor(nums[i] / nums[j])` and sum all values modulo `1_000_000_007`.

### Function Contract
**Inputs**

- `nums`: a list of positive integers.

**Return value**

Return the sum of floored pair values modulo `1_000_000_007`.

### Examples
**Example 1**

- Input: `nums = [2,5,9]`
- Output: `10`

**Example 2**

- Input: `nums = [7,7,7,7,7,7,7]`
- Output: `49`

**Example 3**

- Input: `nums = [1,2,3]`
- Output: `7`

---

## Underlying Base Algorithm(s)
Count frequencies of each value and build prefix counts over values. For each possible denominator `d` present in `nums`, group numerators by quotient: values in `[q*d, (q+1)*d - 1]` contribute `q`. Prefix counts give how many numerators fall in each range.

---

## Complexity Analysis
- **Time Complexity**: `O(M log M)` over value ranges, where `M = max(nums)`
- **Space Complexity**: `O(M)`
