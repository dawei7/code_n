# Rearranging Fruits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2561 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Greedy, Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Rearranging Fruits](https://leetcode.com/problems/rearranging-fruits/) |

## Problem Description

### Goal

Two baskets each contain $n$ fruits. Arrays `basket1` and `basket2` record the cost of every fruit in their respective baskets. The baskets are considered equal when sorting their costs would produce identical arrays, so only the multiplicity of each cost matters.

In one operation, choose one fruit from each basket and swap them. The operation costs the smaller of the two selected fruit costs before the swap. You may perform any number of operations. Return the minimum total cost needed to make the baskets equal, or `-1` when no sequence of cross-basket swaps can do so.

### Function Contract

**Inputs**

- `basket1`: A list of $n$ positive fruit costs, where $1 \le n \le 10^5$ and every cost is at most $10^9$.
- `basket2`: Another list of exactly $n$ fruit costs under the same bounds.

**Return value**

- The minimum total swap cost that makes the two baskets equal as multisets, or `-1` if equalization is impossible.

### Examples

#### Example 1

- **Input:** `basket1 = [4, 2, 2, 2], basket2 = [1, 4, 1, 2]`
- **Output:** `1`
- **Explanation:** Swapping a `2` from the first basket with a `1` from the second costs `1` and equalizes their sorted contents.

#### Example 2

- **Input:** `basket1 = [2, 3, 4, 1], basket2 = [3, 2, 5, 1]`
- **Output:** `-1`
- **Explanation:** The combined multiplicities of `4` and `5` are odd, so neither value can be divided equally between the baskets.

#### Example 3

- **Input:** `basket1 = [1, 100, 100], basket2 = [1, 200, 200]`
- **Output:** `2`
- **Explanation:** Routing the exchange of `100` and `200` through the shared minimum fruit `1` uses two swaps costing `1` each.
