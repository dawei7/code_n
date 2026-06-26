## Problem Description & Examples
### Goal
Given an integer array `nums` of length `n`, return the concatenation of `nums` with itself.

### Function Contract
**Inputs**

- `nums`: List[int]

**Return value**

List[int] of length 2n

### Examples
**Example 1**

- Input: `nums = [1, 2, 1]`
- Output: `[1, 2, 1, 1, 2, 1]`

**Example 2**

- Input: `nums = [4, 5]`
- Output: `[4, 5, 4, 5]`

**Example 3**

- Input: `nums = [0]`
- Output: `[0, 0]`

---

## Underlying Base Algorithm(s)
trivial

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
