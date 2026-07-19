# Customers Who Bought All Products

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1045 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open problem](https://leetcode.com/problems/customers-who-bought-all-products/) |

## Problem Description

### Goal

The `Customer` table records purchases using `customer_id` and `product_key`. It may contain duplicate rows, `customer_id` is not null, and each `product_key` references the `Product` table. The `Product` table lists each catalog key exactly once because `product_key` is its primary key.

Report the identifiers of customers whose purchase records cover every product listed in `Product`. Repeated purchases of one product do not compensate for a missing different product. Return one `customer_id` column; the platform accepts the result rows in any order.

### Function Contract

**Inputs**

- `Customer(customer_id, product_key)`: $R$ purchase rows, possibly including duplicate customer-product pairs.
- `Product(product_key)`: $Q$ distinct product rows defining the complete catalog.

**Return value**

- One row containing `customer_id` for each customer who has bought all $Q$ distinct products.
- Result order is unrestricted by the problem; the local reference orders identifiers ascending for deterministic validation.

### Examples

**Example 1**

`Customer`

| customer_id | product_key |
|---:|---:|
| 1 | 5 |
| 2 | 6 |
| 3 | 5 |
| 3 | 6 |
| 1 | 6 |

`Product`

| product_key |
|---:|
| 5 |
| 6 |

Output:

| customer_id |
|---:|
| 1 |
| 3 |

Customers `1` and `3` each bought products `5` and `6`; customer `2` did not buy product `5`.
