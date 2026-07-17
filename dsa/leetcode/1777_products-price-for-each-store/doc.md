# Product's Price for Each Store

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1777 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open problem](https://leetcode.com/problems/products-price-for-each-store/) |

## Problem Description

### Goal

The `Products` table records prices in row form. Each row identifies a product, one of the stores `"store1"`, `"store2"`, or `"store3"`, and that product's price at the store. The pair `(product_id, store)` is unique, so a product has at most one recorded price per store.

Pivot these rows into one row per product. The result must contain `product_id` followed by columns `store1`, `store2`, and `store3`. Put each recorded price in its store's column and use `NULL` when the product is not available at that store. The rows may be returned in any order.

### Function Contract

**Input table**

- `Products(product_id, store, price)`: `store` is one of `"store1"`, `"store2"`, or `"store3"`.
- `(product_id, store)` is the primary key.
- Let $R$ be the number of input rows and $P$ the number of distinct product IDs.

**Return value**

Return one row per product with columns `product_id`, `store1`, `store2`, and `store3`.

### Examples

**Example 1**

Input:

| product_id | store | price |
|---:|---|---:|
| 0 | store1 | 95 |
| 0 | store3 | 105 |
| 0 | store2 | 100 |
| 1 | store1 | 70 |
| 1 | store3 | 80 |

Output:

| product_id | store1 | store2 | store3 |
|---:|---:|---:|---:|
| 0 | 95 | 100 | 105 |
| 1 | 70 | null | 80 |

**Example 2**

A product recorded only at `"store2"` produces `NULL`, its price, and `NULL` in the three store columns.

**Example 3**

A product with one row for every store produces a completely populated result row.

### Required Complexity

- **Time:** $O(R)$
- **Space:** $O(P)$

<details>
<summary>Approach</summary>

#### General

**Form one group per product**

Group the source rows by `product_id`. Every output row then corresponds to exactly one product, regardless of the order in which that product's store records appeared.

**Route each store into its own aggregate**

For column `store1`, a `CASE` expression returns `price` only when `store = 'store1'` and returns `NULL` otherwise. `MAX` ignores those `NULL` values. Because the primary key permits at most one row for a given product and store, the remaining value is exactly the desired price rather than a maximum chosen among duplicates. Apply the same conditional aggregate to `"store2"` and `"store3"`.

**Preserve missing prices as NULL**

If a product has no row for one store, every value supplied to that store's aggregate is `NULL`, so the aggregate result is also `NULL`. This distinguishes an unavailable product-store pair from any actual stored price. Ordering by `product_id` is optional for LeetCode but makes the app-local output deterministic.

#### Complexity detail

A hash-aggregation plan examines each of the $R$ source rows once, giving $O(R)$ logical time. It keeps three fixed aggregate slots for each of the $P$ product groups, so its auxiliary grouping state is $O(P)$. A database may choose a sort-based physical plan with different implementation costs.

#### Alternatives and edge cases

- **Three correlated subqueries:** Look up each store separately for every product. This is correct with suitable indexes but can repeatedly scan the source table without them.
- **Database-specific `PIVOT`:** Some SQL systems provide a pivot operator, but conditional aggregation works in both MySQL and the app-local SQLite runtime.
- A product can be absent from one or two stores; those result cells must be `NULL`.
- Input row order has no effect on the grouped result.
- The composite primary key guarantees that no store column combines multiple prices for the same product.
- A product represented by only one source row must still appear exactly once.

</details>
