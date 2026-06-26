## Problem Description & Examples
### Goal
You are given an integer array `nums` and an integer `target`.

You want to build an expression out of nums by adding one of the symbols `+` and `-` before each integer in nums and then concatenate all the integers.

Return the number of different expressions that you can build, which evaluate to `target`.

### Function Contract
**Inputs**

- `nums`: List[int]
- `target`: int

**Return value**

int - number of ways

### Examples
**Example 1**

- Input: `nums = [1, 1, 1, 1, 1], target = 3`
- Output: `5`

**Example 2**

- Input: `nums = [4, 1, 3], target = 8`
- Output: `1`

**Example 3**

- Input: `nums = [5, 1], target = -2`
- Output: `0`

---

## Underlying Base Algorithm(s)
- [Longest common subsequence](dp_04_longest-common-subsequence.md)
- [Edit distance](dp_08_edit-distance.md)
- [Unique paths](dp_10_unique-paths.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
