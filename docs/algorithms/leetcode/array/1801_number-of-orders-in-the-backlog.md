# Number of Orders in the Backlog

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1801 |
| Difficulty | Medium |
| Topics | Array, Heap (Priority Queue), Simulation |
| Official Link | [number-of-orders-in-the-backlog](https://leetcode.com/problems/number-of-orders-in-the-backlog/) |

## Problem Description & Examples
### Goal
Process buy and sell orders for a stock exchange backlog. Buy orders match the cheapest sell orders whose price is at most the buy price; sell orders match the highest buy orders whose price is at least the sell price. Return the total remaining order amount.

### Function Contract
**Inputs**

- `orders`: a list of `[price, amount, orderType]`, where `0` is buy and `1` is sell.

**Return value**

Return the total amount left in both backlogs modulo `1_000_000_007`.

### Examples
**Example 1**

- Input: `orders = [[10,5,0],[15,2,1],[25,1,1],[30,4,0]]`
- Output: `6`

**Example 2**

- Input: `orders = [[7,1000000000,1],[15,3,0],[5,999999995,0],[5,1,1]]`
- Output: `999999984`

**Example 3**

- Input: `orders = [[19,28,0],[9,4,1],[25,15,1]]`
- Output: `39`

---

## Underlying Base Algorithm(s)
Use two heaps: a max-heap for buy orders by price and a min-heap for sell orders by price. When a new order arrives, repeatedly match it against the best opposite backlog while prices cross, reducing amounts. Any leftover amount is pushed into its own backlog.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)`
