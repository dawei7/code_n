## Problem Description & Examples
### Goal
Given two strings `s1` and `s2`, return `True` if `s2` contains a permutation of `s1` as a substring.

### Function Contract
**Inputs**

- `s1`: str - pattern
- `s2`: str - text

**Return value**

bool - True if s2 contains a permutation of s1

### Examples
**Example 1**

- Input: `s1 = "ab", s2 = "eidbaooo"`
- Output: `True`

**Example 2**

- Input: `s1 = 'f', s2 = 'fafcffcf'`
- Output: `True`

**Example 3**

- Input: `s1 = 'a', s2 = 'baeccb'`
- Output: `True`

---

## Underlying Base Algorithm(s)
- [Binary-search-style boundary reasoning](search_02_binary-search.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
