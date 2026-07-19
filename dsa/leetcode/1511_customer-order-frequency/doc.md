# Customer Order Frequency

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1511 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/customer-order-frequency/) |

## Problem Description
### Goal

The `Customers` table identifies customers, the `Product` table stores each product's unit price, and `Orders` records which product a customer bought, on which date, and in what quantity. An order's monetary value is its quantity multiplied by the joined product price.

Report each customer whose total order value was at least 100 during June 2020 and also at least 100 during July 2020. Spending from other months does not contribute. Return the qualifying customer's identifier and name.

### Function Contract
**Inputs**

Let $C$, $P$, and $O$ denote the row counts of `Customers`, `Product`, and `Orders`.

- `Customers(customer_id, name, country)`: one row per customer.
- `Product(product_id, description, price)`: one row per product, with its unit price.
- `Orders(order_id, customer_id, product_id, order_date, quantity)`: order facts referencing a customer and product.
- June covers dates from `2020-06-01` through `2020-06-30`; July covers `2020-07-01` through `2020-07-31`.

**Return value**

Return columns `customer_id` and `name` for customers whose June spending is at least 100 and whose July spending is independently at least 100. Return one row per qualifying customer.

### Examples
**Example 1**

- Input: Winston spends 300 in June and 100 in July; Jonathan spends 600 in June but only 20 in July; Moustafa has qualifying June spending but no July order.
- Output: `[[1, "Winston"]]`

**Example 2**

- Input: A customer spends exactly 100 on `2020-06-01` and exactly 100 on `2020-07-31`.
- Output: That customer qualifies because both thresholds are inclusive and both dates belong to their respective months.

**Example 3**

- Input: A customer spends 200 in June and 99 in July, plus 500 in August.
- Output: `[]`
- Explanation: August spending cannot repair the July shortfall.
