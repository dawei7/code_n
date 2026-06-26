## Problem Description & Examples
### Goal
You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.

You may assume that you have an infinite number of each kind of coin.

### Function Contract
**Inputs**

- `coins`: List[int]
- `amount`: int

**Return value**

int - minimum number of coins, or -1

### Examples
**Example 1**

- Input: `coins = [1, 2, 5], amount = 11`
- Output: `3`

**Example 2**

- Input: `coins = [7], amount = 24`
- Output: `-1`

**Example 3**

- Input: `coins = [3, 10], amount = 27`
- Output: `9`

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
