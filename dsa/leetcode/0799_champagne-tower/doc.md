# Champagne Tower

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 799 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/champagne-tower/) |

## Problem Description

### Goal

Champagne glasses form a triangular tower, with one glass in row `0`, two in row `1`, and so on. Each glass holds one cup; any amount above one cup overflows equally into the two glasses immediately below it.

Pour `poured` cups into the top glass and let all overflow propagate downward. Return how full the zero-indexed glass `(query_row, query_glass)` becomes, capped at `1.0` because excess continues to lower rows. Empty capacity in one branch does not flow sideways into another glass.

### Function Contract

**Inputs**

- `poured`: the nonnegative number of cups poured into the top glass.
- `query_row`: the zero-based row containing the queried glass.
- `query_glass`: the zero-based position within that row.

**Return value**

- The queried glass's fill amount, capped at `1.0` because a glass holds one cup.

### Examples

**Example 1**

- Input: `poured = 1, query_row = 1, query_glass = 1`
- Output: `0.0`
- Explanation: The top glass is exactly full, so nothing reaches the second row.

**Example 2**

- Input: `poured = 2, query_row = 1, query_glass = 1`
- Output: `0.5`
- Explanation: One excess cup leaves the top and splits equally between its two children.

**Example 3**

- Input: `poured = 4, query_row = 2, query_glass = 1`
- Output: `0.5`
- Explanation: Each glass in row one receives `1.5` cups and sends `0.25` cup to the middle glass below.
