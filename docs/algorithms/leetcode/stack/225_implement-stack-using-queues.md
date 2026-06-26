# Implement Stack using Queues

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_47` |
| Frontend ID | 225 |
| Difficulty | Easy |
| Topics | Stack, Design, Queue |
| Official Link | [implement-stack-using-queues](https://leetcode.com/problems/implement-stack-using-queues/) |

## Problem Description & Examples
### Goal
Design a class that collects prices and returns the span of the current price's day - the maximum number of consecutive days (ending today) the price was <= today's price.

`solve(prices)` simulates adding prices and returns the span for each.

### Function Contract
**Inputs**

- `prices`: List[int]

**Return value**

List[int] - span for each price

### Examples
**Example 1**

- Input: `prices = [100, 80, 60, 70, 60, 75, 85]`
- Output: `[1, 1, 1, 2, 1, 4, 6]`

**Example 2**

- Input: `prices = [10, 20, 30]`
- Output: `[1, 2, 3]`

**Example 3**

- Input: `prices = [30, 20, 10]`
- Output: `[1, 1, 1]`

---

## Underlying Base Algorithm(s)
- [Balanced parentheses / stack invariant](stack_01_balanced-parentheses.md)
- [Monotonic stack histogram](stack_04_largest-rectangle-in-histogram.md)
- [Trapping rain water](stack_06_trapping-rain-water.md)

---

## Complexity Analysis
- **Time Complexity**: `O(1)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
