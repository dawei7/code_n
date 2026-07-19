# Apply Discount Every n Orders

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1357 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Design |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/apply-discount-every-n-orders/) |

## Problem Description

### Goal

Design a `Cashier` for a store with a fixed product catalog. Parallel arrays `products` and `prices` associate each product ID with its unit price. Each call to `getBill(product, amount)` describes one customer's order using parallel product-ID and quantity arrays.

Charge the full subtotal to ordinary customers. Every $n$th customer receives the configured percentage `discount` on the entire order, after which counting continues so that every subsequent multiple of $n$ is also discounted. Return each bill as a floating-point value.

### Function Contract

**Inputs**

- Constructor arguments `n`, `discount`, `products`, and `prices`.
- `getBill(product, amount)`: parallel arrays of distinct catalog product IDs and positive quantities for one customer.
- The app-local adapter receives an `orders` list of `[product, amount]` pairs.
- Let $P$ be the catalog size and $L$ be the total number of line items across all processed orders.

**Return value**

- Native `getBill` returns that customer's subtotal after applying the scheduled discount when appropriate.
- The app-local `solve` returns all bill values in customer order.

### Examples

**Example 1**

- Configuration: `n = 3, discount = 50, products = [1,2], prices = [100,200]`.
- First order: product `1`, quantity `1`.
- Output: `100.0`.

**Example 2**

- Under the same configuration, the second order buys two units of product `2`.
- Output: `400.0`.

**Example 3**

- The third order buys one unit each of products `1` and `2`.
- Output: `150.0`, because the $50\%$ discount applies to the $300$ subtotal.
