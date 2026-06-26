## Problem Description & Examples
### Goal
Given strings `s` and `t`, find the minimum window in `s` that contains all characters of `t` (including duplicates). If there is no such window, return `""`.

### Function Contract
**Inputs**

- `s`: str
- `t`: str

**Return value**

str - shortest window in s containing all chars of t

### Examples
**Example 1**

- Input: `s = "ADOBECODEBANC", t = "ABC"`
- Output: `"BANC"`

**Example 2**

- Input: `s = 'GAHDH', t = 'G'`
- Output: `'G'`

**Example 3**

- Input: `s = 'GDDBBC', t = 'B'`
- Output: `'B'`

---

## Underlying Base Algorithm(s)
- [Binary-search-style boundary reasoning](search_02_binary-search.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
