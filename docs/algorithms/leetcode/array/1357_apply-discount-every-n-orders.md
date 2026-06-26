# Apply Discount Every n Orders

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1357 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Design |
| Official Link | [apply-discount-every-n-orders](https://leetcode.com/problems/apply-discount-every-n-orders/) |

## Problem Description & Examples
### Goal
Design a cashier that knows product prices and applies a percentage discount to every `n`th customer order. Other orders are charged at full price.

### Function Contract
**Inputs**

- Constructor: `n`, `discount`, `products`, and `prices`.
- `getBill(product, amount)`: parallel lists describing the products bought and their quantities for one order.

**Return value**

`getBill` returns the order total after applying the scheduled discount when applicable.

### Examples
**Example 1**

- Input: `n = 3, discount = 50, products = [1,2], prices = [100,200]; getBill([1],[1])`
- Output: `100.0`

**Example 2**

- Input: `same cashier; getBill([2],[2])`
- Output: `400.0`

**Example 3**

- Input: `same cashier; getBill([1,2],[1,1])`
- Output: `150.0`

---

## Underlying Base Algorithm(s)
Hash map lookup with an order counter. Store product prices by id, increment the counter on each bill, compute the subtotal, and multiply by `(100 - discount) / 100` only when the counter is divisible by `n`.

---

## Complexity Analysis
- **Time Complexity**: `O(p)` to initialize `p` products and `O(k)` per bill with `k` line items.
- **Space Complexity**: `O(p)`
