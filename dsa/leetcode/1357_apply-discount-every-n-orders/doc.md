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

### Required Complexity

- **Time:** $O(P+L)$
- **Space:** $O(P)$

<details>
<summary>Approach</summary>

#### General

**Index the catalog once.** Build a hash map from every product ID to its unit price during construction. This makes each later price lookup constant expected time instead of searching the parallel catalog arrays.

**Track customer position.** Increment an order counter exactly once at the beginning of each `getBill` call. Compute the subtotal by summing `price_by_product[item] * quantity` for corresponding entries in the two order arrays.

If the updated counter is divisible by $n$, multiply the subtotal by `(100 - discount) / 100`; otherwise return the full subtotal. Divisibility selects exactly customers $n,2n,3n,\ldots$, and the line-item sum contains each requested quantity at its catalog price, so every returned bill follows the store rules.

#### Complexity detail

Constructing the price map takes $O(P)$ time and space. Processing all $L$ line items across the order sequence takes $O(L)$ expected time, while discount scheduling adds constant work per bill. Total time is $O(P+L)$ and auxiliary space is $O(P)$.

#### Alternatives and edge cases

- **Linear catalog lookup:** Searching `products` for every bill item is correct but can cost $O(PL)$ across a full-catalog order.
- **Precompute discounted prices:** This can reduce one multiplication per discounted line but duplicates catalog storage and is unnecessary because the discount applies to the subtotal.
- **Every customer discounted:** When $n=1$, each order receives the discount.
- **Full discount:** A $100\%$ discount makes each scheduled bill zero.
- **Multiple discount cycles:** The counter must use divisibility rather than reset incorrectly after only the first discounted order.
- **Several quantities:** Each unit price is multiplied by its parallel amount before the discount is applied.

</details>
