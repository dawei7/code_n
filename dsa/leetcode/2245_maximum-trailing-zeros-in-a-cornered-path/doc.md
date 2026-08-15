# Maximum Trailing Zeros in a Cornered Path

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2245 |
| Difficulty | Medium |
| Topics | Array, Matrix, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-trailing-zeros-in-a-cornered-path/) |

## Problem Description

### Goal

You are given an $m\times n$ grid of positive integers. A cornered path visits
adjacent cells while moving along one row or one column and may turn at most
once. If it turns, its movement after the corner must use the other axis. Each
horizontal segment may go left or right, and each vertical segment may go up
or down. The path cannot revisit a cell.

Multiply the values in every visited cell. Among all straight and one-turn
cornered paths, return the largest possible number of trailing zeroes in that
product.

### Function Contract

**Inputs**

- `grid`: A nonempty rectangular matrix with $m$ rows and $n$ columns, where $1\le m,n\le10^5$, $1\le mn\le10^5$, and every cell value is between $1$ and $1000$.

**Return value**

Return the maximum number of trailing zeroes in the product along any valid
path with at most one turn.

### Examples

#### Example 1

- **Input:** `grid = [[23,17,15,3,20],[8,1,20,27,11],[9,4,6,2,21],[40,9,1,10,6],[22,7,4,5,3]]`
- **Output:** `3`

#### Example 2

- **Input:** `grid = [[4,3,2],[7,6,1],[8,8,8]]`
- **Output:** `0`

#### Example 3

- **Input:** `grid = [[100]]`
- **Output:** `2`
