# Minimum Relative Loss After Buying Chocolates

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2819 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Sorting, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-relative-loss-after-buying-chocolates/) |

## Problem Description

### Goal

An array `prices` gives the prices of available chocolates. Each query has the form `[k, m]` and defines a separate purchase in which Bob must select exactly `m` chocolates under a payment threshold `k`.

For a chocolate priced at most `k`, Bob pays its entire price and Alice pays nothing. For a price greater than `k`, Bob pays exactly `k` and Alice pays the remaining amount. If their total payments are $b$ and $a$, respectively, Bob's relative loss is $b-a$.

For every query, choose exactly the requested number of chocolates so that Bob's relative loss is minimized. Return the minimum loss for each query in the original query order; a loss may be negative when Alice's total payment exceeds Bob's.

### Function Contract

**Inputs**

- `prices`: A list of $n$ positive chocolate prices.
- `queries`: A list of $q$ pairs `[k, m]`, where `k` is the payment threshold and `m` is the exact number of chocolates to select.

The constraints are $1 \leq n,q \leq 10^5$, $1 \leq \texttt{prices[i]},k \leq 10^9$, and $1 \leq m \leq n$.

**Return value**

Return a list of $q$ integers, where entry `i` is the minimum possible value of Bob's payment minus Alice's payment for `queries[i]`.

### Examples

#### Example 1

- **Input:** `prices = [1,9,22,10,19], queries = [[18,4],[5,2]]`
- **Output:** `[34,-21]`
- **Explanation:** The first query can choose prices `[1,9,10,22]`; the second benefits from choosing the expensive prices `[19,22]`.

#### Example 2

- **Input:** `prices = [1,5,4,3,7,11,9], queries = [[5,4],[5,7],[7,3],[4,5]]`
- **Output:** `[4,16,7,1]`
- **Explanation:** Each query applies its own threshold and exact selection count to the same price collection.

#### Example 3

- **Input:** `prices = [5,6,7], queries = [[10,1],[5,3],[3,3]]`
- **Output:** `[5,12,0]`
- **Explanation:** A threshold above every price favors the cheapest chocolate, while queries selecting all prices have no choice of subset.
