# Number of Orders in the Backlog

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/number-of-orders-in-the-backlog/) |
| Frontend ID | 1801 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Heap (Priority Queue), Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

A stream of stock orders arrives in the form `[price, amount, orderType]`. Type `0` is a buy order and type `1` is a sell order. Unfilled quantities remain in a backlog while later orders are processed.

For a buy order, repeatedly match against the backlog sell order with the lowest price while that price is at most the buy price. For a sell order, repeatedly match against the backlog buy order with the highest price while that price is at least the sell price. Each match removes the smaller remaining amount from both sides; any unmatched part of the arriving order joins its own backlog.

After processing every order, return the total amount still present across both backlogs, reduced modulo $10^9+7$.

### Function Contract

**Inputs**

- `orders`: a list of $n$ triples `[price, amount, orderType]`, where $1 \le n \le 10^5$.
- $1 \le \texttt{price},\texttt{amount} \le 10^9$.
- `orderType` is `0` for buy and `1` for sell.

**Return value**

- Return the sum of all unfilled order amounts modulo $10^9+7$.

### Examples

**Example 1**

- Input: `orders = [[10,5,0],[15,2,1],[25,1,1],[30,4,0]]`
- Output: `6`

The final buy consumes both sell orders, leaving two units of that buy and four units from the first buy.

**Example 2**

- Input: `orders = [[7,1000000000,1],[15,3,0],[5,999999995,0],[5,1,1]]`
- Output: `999999984`

The remaining total is reduced modulo $10^9+7$ only after matching is complete.

**Example 3**

- Input: `orders = [[19,28,0],[9,4,1],[25,15,1]]`
- Output: `39`

The price-nine sell consumes four units of the buy; the price-25 sell cannot match the remaining price-19 buy.
