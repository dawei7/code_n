# Maximum Tastiness of Candy Basket

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2517 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-tastiness-of-candy-basket/) |

## Problem Description

### Goal

You are given an array of positive integers `price`, where `price[i]` is the price of the $i$th available candy, and a positive integer `k`.

A basket must contain exactly `k` distinct candies. Its tastiness is the smallest absolute price difference among every pair of candies placed in that basket. The candies themselves must be distinct choices, but different candies may have equal prices.

Choose a valid basket whose tastiness is as large as possible and return that maximum value.

### Function Contract

**Inputs**

- `price`: A list of $n$ positive candy prices, where $2 \le k \le n \le 10^5$ and $1 \le \texttt{price[i]} \le 10^9$.
- `k`: The exact number of distinct candies to select.

Let $R = \max(\texttt{price}) - \min(\texttt{price})$ denote the complete price range.

**Return value**

Return the greatest achievable value of the minimum absolute price difference among all pairs in a basket of exactly `k` candies.

### Examples

#### Example 1

- **Input:** `price = [13, 5, 1, 8, 21, 2], k = 3`
- **Output:** `8`
- **Explanation:** Selecting the candies priced `13`, `5`, and `21` produces pairwise differences `8`, `8`, and `16`, so the basket's tastiness is `8`.

#### Example 2

- **Input:** `price = [1, 3, 1], k = 2`
- **Output:** `2`
- **Explanation:** Select one candy priced `1` and the candy priced `3`.

#### Example 3

- **Input:** `price = [7, 7, 7, 7], k = 2`
- **Output:** `0`
- **Explanation:** Any two distinct candies have equal prices, so their price difference is zero.
