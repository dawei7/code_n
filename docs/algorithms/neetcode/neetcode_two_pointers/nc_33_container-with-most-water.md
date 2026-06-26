## Problem Description & Examples
### Goal
Given an integer array `nums` and a sliding window of size `k`, return the maximum of each window as it slides from left to right.

### Function Contract
**Inputs**

- `nums`: List[int]
- `k`: int - window size

**Return value**

List[int] - max of each window

### Examples
**Example 1**

- Input: `nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3`
- Output: `[3, 3, 5, 5, 6, 7]`

**Example 2**

- Input: `nums = [-2, 94, 7, -90], k = 2`
- Output: `[94, 94, 7]`

**Example 3**

- Input: `nums = [-66, 45, 95, -84], k = 2`
- Output: `[45, 95, 95]`

---

## Underlying Base Algorithm(s)
- [Binary-search-style boundary reasoning](search_02_binary-search.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
