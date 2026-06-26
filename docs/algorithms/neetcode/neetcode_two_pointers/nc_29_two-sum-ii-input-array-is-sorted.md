## Problem Description & Examples
### Goal
Given a string `s`, find the length of the longest substring without repeating characters.

### Function Contract
**Inputs**

- `s`: str

**Return value**

int - length of longest substring without repeats

### Examples
**Example 1**

- Input: `s = "abcabcbb"`
- Output: `3`

**Example 2**

- Input: `s = 'f'`
- Output: `1`

**Example 3**

- Input: `s = 'af'`
- Output: `2`

---

## Underlying Base Algorithm(s)
- [Binary-search-style boundary reasoning](search_02_binary-search.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
