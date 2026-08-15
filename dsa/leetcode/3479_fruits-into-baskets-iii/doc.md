# Fruits Into Baskets III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3479 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Segment Tree, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/fruits-into-baskets-iii/) |

## Problem Description

### Goal

The arrays `fruits` and `baskets` have the same length $n$. Each `fruits[i]` is the quantity of one fruit type, and each `baskets[j]` is the capacity of one basket.

Process fruit types from left to right. The current fruit type must use the leftmost basket that is still available and whose capacity is greater than or equal to its quantity. Once selected, a basket becomes unavailable because one basket can hold only one fruit type. If no available basket is large enough, the fruit type remains unplaced.

Return the number of fruit types left unplaced after processing the entire fruit array. The leftmost qualifying position is part of the rule; choosing a later or tighter-fitting basket is not allowed.

### Function Contract

**Inputs**

- `fruits`: A list of $n$ positive integers giving fruit quantities in processing order.
- `baskets`: A list of $n$ positive integers giving basket capacities in positional order.

The common length satisfies $1 \le n \le 10^5$, and every quantity and capacity is between $1$ and $10^9$, inclusive.

**Return value**

Return the number of fruit types for which no qualifying available basket exists when that fruit type is processed.

### Examples

#### Example 1

- **Input:** `fruits = [4, 2, 5]`, `baskets = [3, 5, 4]`
- **Output:** `1`

Quantity 4 uses capacity 5 at index 1, the first sufficient basket. Quantity 2 then uses capacity 3 at index 0. Capacity 4 cannot hold the final quantity 5, leaving one fruit type unplaced.

#### Example 2

- **Input:** `fruits = [3, 6, 1]`, `baskets = [6, 4, 7]`
- **Output:** `0`

The fruit types use basket capacities 6, 7, and 4 in order, so none remain unplaced.
