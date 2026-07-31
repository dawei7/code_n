# Customer Purchasing Behavior Analysis

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3230 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/customer-purchasing-behavior-analysis/) |

## Problem Description

### Goal

The `Transactions` table records each purchase's customer, product, date, and amount. The `Products` table maps every product identifier to a category and listed price. Produce one purchasing-behavior summary for every customer who has a transaction.

For each customer, report the rounded total spend, transaction count, number of distinct purchased categories, and rounded average transaction amount. Also report the category purchased most often; if several categories have the same purchase count, choose the category whose most recent transaction is latest. Compute the loyalty score as transaction count times $10$ plus total spend divided by $100$, rounded to two decimal places.

Order customers by loyalty score descending, breaking equal scores by customer identifier ascending.

### Function Contract

**Inputs**

The `Transactions` table contains:

- `transaction_id`: The unique integer transaction identifier.
- `customer_id`: The integer identifier of the purchasing customer.
- `product_id`: The purchased product identifier.
- `transaction_date`: The purchase date.
- `amount`: The decimal amount paid in that transaction.

The `Products` table contains:

- `product_id`: The unique integer product identifier.
- `category`: The product's category.
- `price`: The product's listed decimal price.

Let $t$ be the number of transactions and $c$ the number of customer-category groups formed after joining the tables.

**Return value**

Return columns `customer_id`, `total_amount`, `transaction_count`, `unique_categories`, `avg_transaction_amount`, `top_category`, and `loyalty_score`. Round the three requested decimal metrics to two places and apply the specified loyalty-score/customer ordering.

### Examples

**Example 1**

Given purchases of `100.00`, `150.00`, and `200.00` by customer `101` in categories A, B, and C, and purchases of `100.00` and `200.00` by customer `102` in categories A and C, the result begins:

| customer_id | total_amount | transaction_count | unique_categories | avg_transaction_amount | top_category | loyalty_score |
|---:|---:|---:|---:|---:|:---|---:|
| 101 | 450.00 | 3 | 3 | 150.00 | C | 34.50 |
| 102 | 300.00 | 2 | 2 | 150.00 | C | 23.00 |

Each customer's categories tie on frequency, so the latest purchase date selects C.
