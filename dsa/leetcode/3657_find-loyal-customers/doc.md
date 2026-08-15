# Find Loyal Customers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3657 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/find-loyal-customers/) |

## Problem Description

### Goal

The `customer_transactions` table records every purchase and refund made by each customer. Identify customers whose history demonstrates all three required signs of loyalty.

A customer must have at least three purchase transactions, and the interval from that customer's earliest transaction date to the latest must span at least 30 days. The customer's refund rate must also be strictly less than 20%, where the rate is the number of refund transactions divided by the total number of purchase and refund transactions.

Return only the qualifying customer identifiers, ordered by `customer_id` in ascending order.

### Function Contract

**Inputs**

- `customer_transactions`: rows containing a unique `transaction_id`, a `customer_id`, a `transaction_date`, an `amount`, and a `transaction_type`.

Each `transaction_type` is either `purchase` or `refund`. The amount does not affect any loyalty criterion.

**Return value**

Return an ordered table with one column, `customer_id`. Include a customer exactly when they have at least three purchases, at least 30 days between their first and last transactions, and a refund rate below 20%.

### Examples

#### Example 1

A customer with four purchases, no refunds, and 46 days between the first and last transaction qualifies.

#### Example 2

A customer with three purchases and two refunds has a refund rate of $2/5=40\%$, so the customer is excluded even if the activity period is long enough.

#### Example 3

A customer with three purchases over exactly 30 days and no refunds qualifies because both the purchase and activity thresholds are inclusive.
