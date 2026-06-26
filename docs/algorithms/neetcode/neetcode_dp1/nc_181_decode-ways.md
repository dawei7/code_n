## Problem Description & Examples
### Goal
A message containing letters from A-Z can be encoded into numbers using the mapping `A -> "1"`, `B -> "2"`, ..., `Z -> "26"`.

To decode an encoded message, all the digits must be grouped then mapped back into letters. For example, `"11106"` can be mapped into `"AAJF"` or `"KJF"`. Note that grouping `(1, 11, 06)` is invalid because `"06"` cannot be mapped into `'F'` since `"6"` is different from `"06"`.

Given a string `s` containing only digits, return the number of ways to decode it.

### Function Contract
**Inputs**

- `s`: str

**Return value**

int - number of ways to decode

### Examples
**Example 1**

- Input: `s = "12"`
- Output: `2`

**Example 2**

- Input: `s = '8'`
- Output: `1`

**Example 3**

- Input: `s = '18'`
- Output: `2`

---

## Underlying Base Algorithm(s)
- [Climbing stairs recurrence](dp_02_climbing-stairs.md)
- [Coin change](dp_05_coin-change.md)
- [Longest increasing subsequence](dp_07_longest-increasing-subsequence.md)
- [House robber](dp_11_house-robber.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
