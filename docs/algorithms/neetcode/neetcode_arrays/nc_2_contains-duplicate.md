## Problem Description & Examples
### Goal
Given an integer array `nums`, return `True` if any value appears **at least twice** in the array, or `False` if every element is distinct.

### Function Contract
**Inputs**

- `nums`: List[int]

**Return value**

bool - True if there is a duplicate

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 1]`
- Output: `True`

**Example 2**

- Input: `nums = [1, 2, 3, 4]`
- Output: `False`

**Example 3**

- Input: `nums = [4, 5, 6, 4]`
- Output: `True`

---

## Underlying Base Algorithm(s)
- [Two Sum / hash lookup](hash_01_two-sum.md)
- [Grouping by hash key](hash_04_group-anagrams.md)
- [Set-based sequence reasoning](hash_06_longest-consecutive-sequence.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
