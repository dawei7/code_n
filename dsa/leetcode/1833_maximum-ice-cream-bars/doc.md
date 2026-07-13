# Maximum Ice Cream Bars

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1833 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting, Counting Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-ice-cream-bars](https://leetcode.com/problems/maximum-ice-cream-bars/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-ice-cream-bars/).

### Goal
Given ice cream costs and a coin budget, buy as many bars as possible.

### Function Contract
**Inputs**

- `costs`: the price of each ice cream bar.
- `coins`: the available budget.

**Return value**

Return the maximum number of bars that can be bought.

### Examples
**Example 1**

- Input: `costs = [1,3,2,4,1], coins = 7`
- Output: `4`

**Example 2**

- Input: `costs = [10,6,8,7,7,8], coins = 5`
- Output: `0`

**Example 3**

- Input: `costs = [1,6,3,1,2,5], coins = 20`
- Output: `6`

---

## Solution
### Approach
Sort costs ascending and greedily buy the cheapest remaining bar while the budget allows it. This maximizes the count because every chosen expensive bar could be replaced by a cheaper available bar.

### Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(1)` besides sorting storage

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
