# Rearrange Products Table

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/rearrange-products-table/) |
| Frontend ID | 1795 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |

## Problem Description

### Goal

The `Products` table stores one row per product. Its primary key is `product_id`, and the nullable integer columns `store1`, `store2`, and `store3` contain that product's price in each named store. A `NULL` price means the product is unavailable at that store.

Rearrange this wide representation into rows with the columns `(product_id, store, price)`. For every non-null store price, emit one row whose `store` value is the corresponding literal name `"store1"`, `"store2"`, or `"store3"`. Do not emit unavailable product-store combinations. The result may be returned in any order.

### Function Contract

**Inputs**

- `Products`: a table with unique integer `product_id` values and nullable integer columns `store1`, `store2`, and `store3`.
- Let $R$ be the number of product rows and $K$ the number of non-null price fields, so $0 \le K \le 3R$.

**Return value**

- Return columns `product_id`, `store`, and `price`, with exactly one row for each of the $K$ available product-store combinations.
- `store` must identify the source price column, and `price` must preserve its non-null integer value.

### Examples

**Example 1**

- Input: `Products = [[0,95,100,105],[1,70,NULL,80]]`
- Output: `[[0,"store1",95],[0,"store2",100],[0,"store3",105],[1,"store1",70],[1,"store3",80]]`

Product `0` contributes three rows, while product `1` contributes none for `store2`.

**Example 2**

- Input: `Products = [[7,NULL,42,NULL]]`
- Output: `[[7,"store2",42]]`

Only the non-null second-store price becomes a result row.

**Example 3**

- Input: `Products = [[8,NULL,NULL,NULL]]`
- Output: `[]`

A product unavailable in every store contributes no rows.

### Required Complexity

- **Time:** $O(R)$
- **Space:** $O(K)$

<details>
<summary>Approach</summary>

#### General

**Give each store column its own projection**

Create one `SELECT` branch per store. Every branch projects `product_id`, a literal store label, and that store's price column. For example, the first branch maps `store1` into the common output names `store` and `price`.

**Filter unavailable combinations at their source**

Apply `WHERE store1 IS NOT NULL`, and analogously for the other branches. A branch then emits a product exactly when that specific store price is available. Values such as zero remain valid because the condition distinguishes `NULL` from all non-null integers.

**Concatenate without duplicate elimination**

Join the three branches with `UNION ALL`. Even when two stores charge the same price, their literal `store` labels describe different required rows. Ordinary `UNION` would spend work checking for duplicates that the `(product_id, store)` identity already rules out.

For every non-null source field, its corresponding branch emits exactly one row with the correct product, label, and value. Every emitted row comes from such a field because of the branch's null filter. This is a bijection between available product-store fields and result rows, proving the transformation is exact.

#### Complexity detail

Each of the three branches scans the $R$ product rows once and performs constant work per row. Three is a fixed schema constant, so $3R$ operations are $O(R)$ time. The result contains $K$ rows and uses $O(K)$ output space; `UNION ALL` requires no duplicate set, and the logical transformation needs only constant auxiliary state when streamed.

#### Alternatives and edge cases

- **Use ordinary `UNION`:** It returns the same rows under the key guarantees but adds unnecessary duplicate-elimination work.
- **Cross join store labels plus `CASE`:** A three-row label relation can drive one generalized projection, but it creates three candidates per product before filtering and is less direct for a fixed schema.
- **Vendor-specific `UNPIVOT`:** Some databases provide concise unpivot syntax, but the portable `UNION ALL` form matches the available MySQL interface.
- **All prices null:** Emit no rows for that product.
- **All stores available:** Emit exactly three rows with distinct store labels.
- **Equal store prices:** Preserve one row per store; equal numeric values do not make combinations duplicates.
- **Zero or negative prices:** They are non-null integers and must not be filtered by truthiness.
- **Output order:** The contract permits any order, so no sorting clause is required.

</details>
