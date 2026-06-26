## Problem Description & Examples
### Goal
Given an input string `s` and a pattern `p`, implement regular expression matching with support for `.` and `*` where:
- `.` Matches any single character.
- `*` Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

### Function Contract
**Inputs**

- `s`: str
- `p`: str

**Return value**

bool - True if pattern matches s

### Examples
**Example 1**

- Input: `s = "aa", p = "a*"`
- Output: `True`

**Example 2**

- Input: `s = 'ba', p = 'b.'`
- Output: `True`

**Example 3**

- Input: `s = 'ab', p = 'ab*'`
- Output: `True`

---

## Underlying Base Algorithm(s)
- [Longest common subsequence](dp_04_longest-common-subsequence.md)
- [Edit distance](dp_08_edit-distance.md)
- [Unique paths](dp_10_unique-paths.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
