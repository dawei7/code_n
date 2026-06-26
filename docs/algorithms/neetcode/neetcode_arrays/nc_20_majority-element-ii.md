## Problem Description & Examples
### Goal
Given an integer array `nums`, return all elements that appear more than `n/3` times. The answer can be in any order.

### Function Contract
**Inputs**

- `nums`: List[int]

**Return value**

List[int] - elements appearing more than n/3 times

### Examples
**Example 1**

- Input: `nums = [3, 2, 3]`
- Output: `[3]`

**Example 2**

- Input: `nums = [25, 25, 25]`
- Output: `[25]`

**Example 3**

- Input: `nums = [9, 9, 9]`
- Output: `[9]`

---

## Underlying Base Algorithm(s)
- [Two Sum / hash lookup](hash_01_two-sum.md)
- [Grouping by hash key](hash_04_group-anagrams.md)
- [Set-based sequence reasoning](hash_06_longest-consecutive-sequence.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
