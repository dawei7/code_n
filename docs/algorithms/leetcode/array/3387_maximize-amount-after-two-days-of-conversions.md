# Maximize Amount After Two Days of Conversions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3387 |
| Difficulty | Medium |
| Topics | Array, String, Depth-First Search, Breadth-First Search, Graph Theory |
| Official Link | [maximize-amount-after-two-days-of-conversions](https://leetcode.com/problems/maximize-amount-after-two-days-of-conversions/) |

## Problem Description & Examples
### Goal
Given an initial amount of a starting currency, calculate the maximum possible amount of that same currency you can obtain after two days of trading. On each day, you are provided with a list of currency pairs and their corresponding exchange rates. You start with the initial currency on Day 1, convert it through various pairs to maximize the amount of a target currency, and then on Day 2, use those proceeds to perform further conversions to maximize the final amount of the starting currency.

### Function Contract
**Inputs**

- `initialCurrency`: A string representing the starting currency.
- `pairs1`: A list of lists where each inner list contains two strings (currency A, currency B) and a float (rate).
- `rates1`: A list of floats representing the exchange rate from currency A to currency B for `pairs1`.
- `pairs2`: A list of lists where each inner list contains two strings (currency A, currency B) and a float (rate).
- `rates2`: A list of floats representing the exchange rate from currency A to currency B for `pairs2`.

**Return value**

- A float representing the maximum possible amount of `initialCurrency` obtainable after two days of conversions.

### Examples
**Example 1**

- Input: `initialCurrency = "EUR", pairs1 = [["EUR","USD"],["USD","JPY"]], rates1 = [2.0, 3.0], pairs2 = [["JPY","USD"],["USD","EUR"]], rates2 = [0.5, 0.5]`
- Output: `1.5`

**Example 2**

- Input: `initialCurrency = "NGN", pairs1 = [["NGN","EUR"]], rates1 = [9.0], pairs2 = [["EUR","NGN"]], rates2 = [6.0]`
- Output: `54.0`

**Example 3**

- Input: `initialCurrency = "USD", pairs1 = [["USD","EUR"]], rates1 = [1.0], pairs2 = [["EUR","JPY"],["JPY","USD"]], rates2 = [1.0, 1.0]`
- Output: `1.0`

---

## Underlying Base Algorithm(s)
The problem is modeled as a directed graph where currencies are nodes and exchange rates are edge weights. Since we want to find the maximum conversion rate between any two currencies, we can use the Bellman-Ford algorithm or simply perform a Breadth-First Search (BFS) / Depth-First Search (DFS) from the source node to all reachable nodes, keeping track of the maximum product of rates found so far.

---

## Complexity Analysis
- **Time Complexity**: O(N + M), where N is the number of pairs in day 1 and M is the number of pairs in day 2. We perform a traversal (BFS/DFS) on the graph constructed from each day's rates.
- **Space Complexity**: O(V), where V is the number of unique currencies, used to store the adjacency list and the maximum rates found during traversal.
