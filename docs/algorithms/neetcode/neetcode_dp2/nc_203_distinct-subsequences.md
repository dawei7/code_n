## Problem Description & Examples
### Goal
Given two strings `s` and `t`, return the number of distinct subsequences of `s` which equals `t`.

### Function Contract
**Inputs**

- `s`: str
- `t`: str

**Return value**

int - number of distinct subsequences

### Examples
**Example 1**

- Input: `s = "rabbbit", t = "rabbit"`
- Output: `3`

**Example 2**

- Input: `s = 'bbbaabb', t = 'bab'`
- Output: `12`

**Example 3**

- Input: `s = 'cca', t = 'ca'`
- Output: `2`

---

## Underlying Base Algorithm(s)
- [Longest common subsequence](dp_04_longest-common-subsequence.md)
- [Edit distance](dp_08_edit-distance.md)
- [Unique paths](dp_10_unique-paths.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
