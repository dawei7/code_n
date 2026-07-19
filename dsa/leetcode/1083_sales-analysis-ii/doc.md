# Sales Analysis II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1083 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open problem](https://leetcode.com/problems/sales-analysis-ii/) |

## Problem Description

### Goal

The `Product` table maps each `product_id` to its product name and unit price. The `Sales` table records purchases, including the product and buyer involved in each sale along with seller, date, quantity, and price details.

Report the `buyer_id` of every buyer who purchased the product named `S8` and never purchased the product named `iPhone`. Purchases of other products neither qualify nor disqualify a buyer. Return each qualifying buyer once; result rows may appear in any order.

### Function Contract

**Inputs**

- `Product(product_id, product_name, unit_price)`: $P$ product rows keyed by `product_id`.
- `Sales(seller_id, product_id, buyer_id, sale_date, quantity, price)`: $R$ sale rows whose `product_id` values refer to `Product`.

**Return value**

- One column named `buyer_id`.
- One row for each buyer with at least one `S8` purchase and zero `iPhone` purchases.
- Result order is unrestricted; the local reference orders by `buyer_id` for deterministic validation.

### Examples

**Example 1**

`Product`

| product_id | product_name | unit_price |
|---:|---|---:|
| 1 | S8 | 1000 |
| 2 | G4 | 800 |
| 3 | iPhone | 1400 |

`Sales`

| seller_id | product_id | buyer_id | sale_date | quantity | price |
|---:|---:|---:|---|---:|---:|
| 1 | 1 | 1 | 2019-01-21 | 2 | 2000 |
| 1 | 2 | 2 | 2019-02-17 | 1 | 800 |
| 2 | 1 | 3 | 2019-06-02 | 1 | 800 |
| 3 | 3 | 3 | 2019-05-13 | 2 | 2800 |

Output:

| buyer_id |
|---:|
| 1 |

Buyer 1 purchased `S8` and no `iPhone`. Buyer 3 purchased both named products, while buyer 2 never purchased `S8`.
