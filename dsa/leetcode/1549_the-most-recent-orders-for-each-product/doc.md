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

### Required Complexity

- **Time:** $O(r \log r)$
- **Space:** $O(r)$

<details>
<summary>Approach</summary>

#### General

**Rank dates independently for each product**

Apply `DENSE_RANK` to the orders, partitioned by `product_id` and ordered by `order_date DESC`. Every row on a product's latest date receives rank one. Using `ROW_NUMBER` would be incorrect because it would keep only one order when the latest date is tied.

**Join product information after identifying recency**

Filter the ranked rows to rank one and join them to `Products` by `product_id` to obtain the required name. Beginning from orders naturally omits products with no order. Customer data does not need to be joined because no customer column is requested and the customer identity does not affect which date is latest.

**Apply every required tie breaker**

Order the final rows first by `product_name`, then `product_id`, and finally `order_id`. The second key distinguishes products that share a name, and the third gives deterministic order among multiple latest-day orders for one product.

Each product partition is ranked solely by its own dates. Rank one is therefore assigned exactly to the rows whose date equals that product's maximum date, proving that the filter includes every required row and excludes every older order.

#### Complexity detail

For $r$ order rows, partition ordering and the final result ordering have a portable upper bound of $O(r \log r)$ time. The ranked intermediate relation and sorting workspace can contain $O(r)$ rows, giving $O(r)$ auxiliary space. Database indexes may reduce physical work, but the query does not rely on a particular index layout.

#### Alternatives and edge cases

- **Grouped maximum-date join:** compute `MAX(order_date)` per product and join that relation back to `Orders`; this has the same semantics and can also be efficient.
- **Correlated maximum subquery:** compare each order with a per-product `MAX` subquery, but without decorrelation or an index it can repeat scans and approach $O(r^2)$.
- **ROW_NUMBER:** selecting row number one loses additional orders tied on the latest date.
- Products with no orders do not appear.
- Multiple customers may create several rows for one product's most recent date.
- Older orders tied with one another remain excluded when a later date exists.
- Products can share a name, so `product_id` is a necessary second ordering key.
- `order_id` orders rows that still tie after the first two keys.
- Product price and customer name do not affect the result.

</details>
