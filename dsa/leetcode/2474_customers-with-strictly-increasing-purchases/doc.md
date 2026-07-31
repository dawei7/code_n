# Customers With Strictly Increasing Purchases

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2474 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/customers-with-strictly-increasing-purchases/) |

## Problem Description

### Goal

The `Orders` table records individual purchases. Each row has a unique order identifier, the customer who placed it, its date, and its price. A customer's total purchases for a calendar year are the sum of all their order prices during that year.

Report every customer whose yearly totals are strictly increasing from the year of their first order through the year of their last order. Every intervening calendar year participates in the comparison; if a customer placed no order in such a year, that year's total is zero. The output order is unrestricted.

### Function Contract

**Inputs**

- `Orders(order_id, customer_id, order_date, price)`: One row per order, with `order_id` unique.

**Return value**

Return a relation with one column:

- `customer_id`: A customer whose total for every considered year is strictly greater than the preceding year's total.

A customer represented in only one calendar year qualifies because there is no adjacent-year comparison that can fail.

### Examples

**Example 1**

- Input: Customer 1 has yearly totals `2300, 3000, 3100, 4700`; customer 2 skips its middle year; customer 3 has totals `900, 900`.
- Output: `customer_id = 1`
- Explanation: Only customer 1 has consecutive years and a strict increase at every transition.

**Example 2**

- Input: Customer 4 has one order in 2022.
- Output: `customer_id = 4`
- Explanation: A one-year interval contains no decreasing or equal transition.

**Example 3**

- Input: Customer 5 has yearly totals `10, 10, 12` from 2020 through 2022.
- Output: An empty relation.
- Explanation: Equality between the first two totals violates strict increase.
