## Problem Description & Examples
### Goal
You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`-th day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:
- After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
- You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

### Function Contract
**Inputs**

- `prices`: List[int]

**Return value**

int - maximum profit

### Examples
**Example 1**

- Input: `prices = [1, 2, 3, 0, 2]`
- Output: `3`

**Example 2**

- Input: `prices = [49, 27, 3]`
- Output: `0`

**Example 3**

- Input: `prices = [37, 49]`
- Output: `12`

---

## Underlying Base Algorithm(s)
- [Longest common subsequence](dp_04_longest-common-subsequence.md)
- [Edit distance](dp_08_edit-distance.md)
- [Unique paths](dp_10_unique-paths.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
