# Super Egg Drop

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 887 |
| Difficulty | Hard |
| Topics | Math, Binary Search, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/super-egg-drop/) |

## Problem Description
### Goal
You have `k` identical eggs and a building with floors labeled from `1` through `n`. An unknown integer threshold $f$ satisfies $0 \leq f \leq n$: an egg dropped above floor $f$ breaks, while an egg dropped at or below floor $f$ does not break.

In one move, choose any floor from `1` through `n` and drop an unbroken egg there. A broken egg cannot be used again, but an egg that survives remains available. Return the minimum number of moves needed to determine $f$ with certainty, accounting for the worst possible sequence of outcomes.

### Function Contract
**Inputs**

- `k`: the number of identical eggs, where $1 \leq k \leq 100$.
- `n`: the number of floors, where $1 \leq n \leq 10^4$.

**Return value**

Return the minimum worst-case number of egg drops required to identify the threshold floor $f$ exactly.

### Examples
**Example 1**

- Input: `k = 1, n = 2`
- Output: `2`

With one egg, testing floor `1` and then floor `2` when necessary is the only way to distinguish all three possible threshold values.

**Example 2**

- Input: `k = 2, n = 6`
- Output: `3`

**Example 3**

- Input: `k = 3, n = 14`
- Output: `4`
