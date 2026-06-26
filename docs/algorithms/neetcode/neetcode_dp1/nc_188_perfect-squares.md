## Problem Description & Examples
### Goal
Given an integer `n`, return the least number of perfect square numbers that sum to `n`.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, `1`, `4`, `9`, and `16` are perfect squares while `3` and `11` are not.

### Function Contract
**Inputs**

- `n`: int

**Return value**

int - minimum perfect squares needed

### Examples
**Example 1**

- Input: `n = 12`
- Output: `3`

**Example 2**

- Input: `n = 2`
- Output: `2`

**Example 3**

- Input: `n = 1`
- Output: `1`

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
