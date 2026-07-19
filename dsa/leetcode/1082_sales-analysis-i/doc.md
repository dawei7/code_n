# Sales Analysis I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1082 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open problem](https://leetcode.com/problems/sales-analysis-i/) |

## Problem Description

### Goal

The `Product` table identifies each product and records its name and unit price. The `Sales` table records individual sales, including the seller, product, buyer, date, quantity, and the total `price` of that sale.

Add the `price` values for each seller and report the `seller_id` of the seller or sellers with the greatest total sales price. If several sellers tie for the greatest total, return all of them. Result rows may be returned in any order.

### Function Contract

**Inputs**

- `Product(product_id, product_name, unit_price)`: product details keyed by `product_id`.
- `Sales(seller_id, product_id, buyer_id, sale_date, quantity, price)`: $R$ sale rows; `price` is the total price recorded for the sale.

**Return value**

- One column named `seller_id`.
- One row for every seller whose sum of `Sales.price` equals the greatest seller total.
- Result order is unrestricted; the local reference orders by `seller_id` for deterministic validation.

### Examples

**Example 1**

`Sales`

| seller_id | product_id | buyer_id | sale_date | quantity | price |
|---:|---:|---:|---|---:|---:|
| 1 | 1 | 1 | 2019-01-21 | 2 | 2000 |
| 1 | 2 | 2 | 2019-02-17 | 1 | 800 |
| 2 | 2 | 3 | 2019-06-02 | 1 | 800 |
| 3 | 3 | 4 | 2019-05-13 | 2 | 2800 |

Output:

| seller_id |
|---:|
| 1 |
| 3 |

Sellers 1 and 3 each have a total recorded sales price of 2800, greater than seller 2's total of 800.
