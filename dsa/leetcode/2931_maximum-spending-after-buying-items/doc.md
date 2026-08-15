# Maximum Spending After Buying Items

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2931 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting, Heap (Priority Queue), Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-spending-after-buying-items/) |

## Problem Description

### Goal

An $m\times n$ matrix `values` describes different items in $m$ shops. Row
`i` lists that shop's item values in non-increasing order. On each day, buy
exactly one item from any shop, but only that shop's rightmost item that has
not already been bought is available.

If an item with value `values[i][j]` is bought on day $d$, its price is
$d\cdot\texttt{values[i][j]}$. Continue until all $mn$ items have been bought.
Return the maximum total amount that can be spent by choosing the purchase
order subject to each shop's right-to-left availability rule.

### Function Contract

**Inputs**

- `values`: The rectangular matrix of item values, with every row sorted in non-increasing order.

Let $m=\lvert\texttt{values}\rvert$ and
$n=\lvert\texttt{values[0]}\rvert$. The constraints are $1\le m\le10$,
$1\le n\le10^4$, and $1\le\texttt{values[i][j]}\le10^6$.

**Return value**

- The maximum total price paid for all $mn$ items.

### Examples

#### Example 1

- **Input:** `values = [[8, 5, 2], [6, 4, 1], [9, 7, 3]]`
- **Output:** `285`
- **Explanation:** Buying values in the feasible order `1, 2, 3, 4, 5, 6, 7, 8, 9` assigns the largest day multipliers to the largest values.

#### Example 2

- **Input:** `values = [[10, 8, 6, 4, 2], [9, 7, 5, 3, 2]]`
- **Output:** `386`
- **Explanation:** A valid ascending merge is `2, 2, 3, 4, 5, 6, 7, 8, 9, 10`, which maximizes the weighted sum.
