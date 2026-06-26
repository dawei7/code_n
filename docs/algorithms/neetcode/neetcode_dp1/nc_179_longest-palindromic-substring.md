## Problem Description & Examples
### Goal
Given a string `s`, return the longest palindromic substring in `s`.

### Function Contract
**Inputs**

- `s`: str

**Return value**

str - longest palindromic substring

### Examples
**Example 1**

- Input: `s = "babad"`
- Output: `"bab"`

**Example 2**

- Input: `s = 'd'`
- Output: `'d'`

**Example 3**

- Input: `s = 'ad'`
- Output: `'a'`

---

## Underlying Base Algorithm(s)
- [Climbing stairs recurrence](dp_02_climbing-stairs.md)
- [Coin change](dp_05_coin-change.md)
- [Longest increasing subsequence](dp_07_longest-increasing-subsequence.md)
- [House robber](dp_11_house-robber.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
