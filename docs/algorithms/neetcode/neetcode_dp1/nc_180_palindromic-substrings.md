## Problem Description & Examples
### Goal
Given a string `s`, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward. A substring is a contiguous sequence of characters within the string.

### Function Contract
**Inputs**

- `s`: str

**Return value**

int - count of palindromic substrings

### Examples
**Example 1**

- Input: `s = "abc"`
- Output: `3`

**Example 2**

- Input: `s = 'a'`
- Output: `1`

**Example 3**

- Input: `s = 'aa'`
- Output: `3`

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
