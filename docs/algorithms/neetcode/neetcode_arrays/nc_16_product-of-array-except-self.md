## Problem Description & Examples
### Goal
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`. You must solve it without division and in O(n) time.

### Function Contract
**Inputs**

- `nums`: List[int]

**Return value**

List[int] - product of all elements except self

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4]`
- Output: `[24, 12, 8, 6]`

**Example 2**

- Input: `nums = [2, 3]`
- Output: `[3, 2]`

**Example 3**

- Input: `nums = [-6, 8]`
- Output: `[8, -6]`

---

## Underlying Base Algorithm(s)
- [Two Sum / hash lookup](hash_01_two-sum.md)
- [Grouping by hash key](hash_04_group-anagrams.md)
- [Set-based sequence reasoning](hash_06_longest-consecutive-sequence.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
