# The Most Recent Orders for Each Product

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1549 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/the-most-recent-orders-for-each-product/) |

## Problem Description
### Goal
The database contains customers, products, and individual orders. Every order records its date, customer, and product, and a customer cannot order the same product more than once on one day.

For each product that has at least one order, find the latest date on which that product was ordered and return every order placed for it on that date. A product can therefore contribute multiple rows when different customers placed orders on its most recent day. Products with no orders are omitted. Sort the result by product name, then product identifier, then order identifier, all in ascending order.

### Function Contract
**Inputs**

- `Customers(customer_id, name)`: customers keyed by the unique `customer_id`.
- `Orders(order_id, order_date, customer_id, product_id)`: $r$ orders keyed by the unique `order_id`. One customer does not order the same product more than once on a single date.
- `Products(product_id, product_name, price)`: products keyed by the unique `product_id`.

**Return value**

A table with columns `product_name`, `product_id`, `order_id`, and `order_date`. It contains every order whose date is the maximum date for its product, ordered by `product_name`, `product_id`, and `order_id`, all ascending.

### Examples
**Example 1**

- Input: orders for keyboard, mouse, and screen across several dates, plus an unordered hard-disk product
- Output: keyboard orders 6 and 7 from `2020-08-01`, mouse order 8 from `2020-08-03`, and screen order 3 from `2020-08-29`
- Explanation: Both keyboard orders share that product's latest date, while the never-ordered hard disk is absent.

**Example 2**

- Input: one product with orders 10 and 11 on its latest day
- Output: both rows, ordered by order identifier
- Explanation: The query returns all most-recent orders rather than choosing one arbitrary row.

**Example 3**

- Input: two products named `"pen"` with identifiers 2 and 1
- Output: the product with identifier 1 appears first
- Explanation: Product identifier breaks a tie in the primary product-name ordering.
