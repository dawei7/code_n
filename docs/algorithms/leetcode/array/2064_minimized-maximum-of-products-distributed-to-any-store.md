# Minimized Maximum of Products Distributed to Any Store

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2064 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Greedy |
| Official Link | [minimized-maximum-of-products-distributed-to-any-store](https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/) |

## Problem Description & Examples
### Goal
Distribute product quantities among `n` stores. Each store can receive only one product type, and the goal is to minimize the largest quantity assigned to any store.

### Function Contract
**Inputs**

- `n`: number of stores.
- `quantities`: item counts for each product type.

**Return value**

Return the minimum possible maximum items in a store.

### Examples
**Example 1**

- Input: `n = 6, quantities = [11,6]`
- Output: `3`

**Example 2**

- Input: `n = 7, quantities = [15,10,10]`
- Output: `5`

**Example 3**

- Input: `n = 1, quantities = [100000]`
- Output: `100000`

---

## Underlying Base Algorithm(s)
Binary search the answer `limit`. A product quantity `q` needs `ceil(q / limit)` stores. The limit is feasible when the total required stores is at most `n`.

---

## Complexity Analysis
- **Time Complexity**: `O(m log max(quantities))`
- **Space Complexity**: `O(1)`
