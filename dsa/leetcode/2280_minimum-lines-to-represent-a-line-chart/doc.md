# Minimum Lines to Represent a Line Chart

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2280 |
| Difficulty | Medium |
| Topics | Array, Math, Geometry, Sorting, Number Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/) |

## Problem Description

### Goal

Each entry `stockPrices[i] = [day_i, price_i]` records a stock price on a
particular day. Plot these points in the plane, using days on the horizontal
axis and prices on the vertical axis. The line chart connects points that are
adjacent after ordering them by day.

A single straight line may represent several consecutive connections whenever
all of their points are collinear. Return the minimum number of straight lines
needed to represent the entire chart.

### Function Contract

**Inputs**

- `stockPrices`: An array of $n$ pairs `[day_i, price_i]`, where every `day_i` is distinct.

Here, $1 \le n \le 10^5$, every pair has exactly two entries, and
$1 \le \texttt{day\_i}, \texttt{price\_i} \le 10^9$.

**Return value**

The minimum number of straight lines whose consecutive portions represent the
day-ordered line chart. A chart containing only one point requires zero lines.

### Examples

#### Example 1

- **Input:** `stockPrices = [[1, 7], [2, 6], [3, 5], [4, 4], [5, 4], [6, 3], [7, 2], [8, 1]]`
- **Output:** `3`

#### Example 2

- **Input:** `stockPrices = [[3, 4], [1, 2], [7, 8], [2, 3]]`
- **Output:** `1`

#### Example 3

- **Input:** `stockPrices = [[5, 10]]`
- **Output:** `0`
