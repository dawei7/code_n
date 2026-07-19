# Sales Analysis III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1084 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open problem](https://leetcode.com/problems/sales-analysis-iii/) |

## Problem Description

### Goal

The `Product` table identifies each product and stores its name and unit price. The `Sales` table contains sale information and may contain duplicate rows; every sale's `product_id` refers to a product.

Report the products that were sold only during the first quarter of 2019: every sale for the product must have a `sale_date` from `2019-01-01` through `2019-03-31`, inclusive. A reported product must actually have at least one sale, so an unsold product does not qualify vacuously. Return `product_id` and `product_name` in any order.

### Function Contract

**Inputs**

- `Product(product_id, product_name, unit_price)`: $P$ product rows keyed by `product_id`.
- `Sales(seller_id, product_id, buyer_id, sale_date, quantity, price)`: $R$ sale rows; duplicate rows are allowed and `product_id` refers to `Product`.

**Return value**

- Columns `product_id` and `product_name`.
- One row for each sold product whose earliest and latest sale dates both lie within the inclusive first-quarter window.
- Result order is unrestricted; the local reference orders by `product_id` for deterministic validation.

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
| 2 | 2 | 3 | 2019-06-02 | 1 | 800 |
| 3 | 3 | 4 | 2019-05-13 | 2 | 2800 |

Output:

| product_id | product_name |
|---:|---|
| 1 | S8 |

Product 1 has sales only inside the quarter. Product 2 also has a June sale, and product 3 has no sale inside the quarter.
