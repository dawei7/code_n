# Maximum Containers on a Ship

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3492 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-containers-on-a-ship/) |

## Problem Description

### Goal

A ship has a square cargo deck with `n` rows and `n` columns. Every deck cell can hold at most one container, so the physical layout provides exactly $n^2$ available positions. Each container has the same weight `w`; containers cannot be split, and every loaded container contributes that full weight.

The combined weight of all loaded containers must not exceed `maxWeight`. Determine the greatest number of containers that can be placed while respecting both the finite number of deck cells and the ship's total weight capacity.

### Function Contract

**Inputs**

- `n`: The positive side length of the square cargo deck.
- `w`: The positive weight of each identical container.
- `maxWeight`: The ship's positive maximum permitted container weight.

The inputs satisfy $1\le n\le1000$, $1\le w\le1000$, and $1\le\texttt{maxWeight}\le10^9$.

**Return value**

Return the maximum whole number of containers that can be loaded without exceeding either limit.

### Examples

#### Example 1

- **Input:** `n = 2, w = 3, maxWeight = 15`
- **Output:** `4`
- **Explanation:** The four deck cells can all be occupied because their combined weight is `12`.

#### Example 2

- **Input:** `n = 3, w = 5, maxWeight = 20`
- **Output:** `4`
- **Explanation:** Although the deck has nine cells, the weight capacity permits only four containers.
