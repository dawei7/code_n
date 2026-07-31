# Fruits Into Baskets II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3477 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Binary Search, Segment Tree, Simulation, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/fruits-into-baskets-ii/) |

## Problem Description

### Goal

The arrays `fruits` and `baskets` have the same length $n$. Each `fruits[i]` is the quantity of one fruit type, while each `baskets[j]` is the capacity of one basket.

Process fruit types from left to right. For the current fruit type, choose the leftmost basket that is still available and whose capacity is greater than or equal to the fruit quantity. A chosen basket becomes unavailable because one basket may hold only one fruit type. When no available basket has sufficient capacity, that fruit type remains unplaced.

After every fruit type has been processed, return the number that remain unplaced. The leftmost rule is mandatory: it is not permissible to save an earlier qualifying basket by choosing a later or tighter-fitting one.

### Function Contract

**Inputs**

- `fruits`: A list of $n$ positive integers giving fruit quantities in processing order.
- `baskets`: A list of $n$ positive integers giving basket capacities in left-to-right order.

The shared length satisfies $1 \le n \le 100$, and every quantity and capacity is between $1$ and $1000$, inclusive.

**Return value**

Return the number of fruit types for which no qualifying available basket exists when that fruit is processed.

### Examples

**Example 1**

- Input: `fruits = [4, 2, 5]`, `baskets = [3, 5, 4]`
- Output: `1`

Quantity 4 uses the leftmost qualifying basket, capacity 5 at index 1. Quantity 2 then uses capacity 3 at index 0. The remaining capacity 4 cannot hold quantity 5, so one fruit type is unplaced.

**Example 2**

- Input: `fruits = [3, 6, 1]`, `baskets = [6, 4, 7]`
- Output: `0`

The fruits use basket capacities 6, 7, and 4 in that order. All three fruit types are placed.
