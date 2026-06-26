## Problem Description & Examples
### Goal
You are given an integer array `cost` where `cost[i]` is the cost of `i`-th step on a staircase. Once you pay the cost, you can either climb one or two steps. You can either start from the step with index `0`, or the step with index `1`.

Return the minimum cost to reach the top of the floor.

### Function Contract
**Inputs**

- `cost`: List[int]

**Return value**

int - minimum cost to reach the top

### Examples
**Example 1**

- Input: `cost = [10, 15, 20]`
- Output: `15`

**Example 2**

- Input: `cost = [25, 49]`
- Output: `25`

**Example 3**

- Input: `cost = [9, 37]`
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
