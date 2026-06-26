## Problem Description & Examples
### Goal
Given an integer array `arr` and two integers `k` and `threshold`, return the number of sub-arrays of size `k` and average >= `threshold`.

### Function Contract
**Inputs**

- `arr`: List[int]
- `k`: int - subarray size
- `threshold`: int

**Return value**

int - count of subarrays with average >= threshold

### Examples
**Example 1**

- Input: `arr = [2, 2, 2, 2, 5, 5, 5, 8], k = 3, threshold = 4`
- Output: `3`

**Example 2**

- Input: `arr = [50], k = 1, threshold = 68`
- Output: `0`

**Example 3**

- Input: `arr = [18, 73], k = 1, threshold = 74`
- Output: `0`

---

## Underlying Base Algorithm(s)
- [Window with character state](hash_03_longest-substring-without-repeating.md)
- [Window frequency counting](hash_05_count-distinct-in-window.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
