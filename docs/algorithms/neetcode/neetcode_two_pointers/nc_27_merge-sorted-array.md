## Problem Description & Examples
### Goal
Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

### Function Contract
**Inputs**

- `height`: List[int]

**Return value**

int - total water trapped

### Examples
**Example 1**

- Input: `height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]`
- Output: `6`

**Example 2**

- Input: `height = [6, 6]`
- Output: `0`

**Example 3**

- Input: `height = [2, 9]`
- Output: `0`

---

## Underlying Base Algorithm(s)
- [Binary-search-style boundary reasoning](search_02_binary-search.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
