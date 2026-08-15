# Consecutive Transactions with Increasing Amounts

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2701 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open problem](https://leetcode.com/problems/consecutive-transactions-with-increasing-amounts/) |

## Problem Description

### Goal

The `Transactions` table records a transaction identifier, its customer, the calendar date of the transaction, and its amount. A customer has at most one transaction on any particular date.

Find every maximal period in which the same customer made transactions on at least three consecutive calendar days and each day's `amount` was strictly greater than the preceding day's amount. A customer may have more than one qualifying period when a missing date or a non-increasing amount separates the periods.

For each qualifying period, report the customer and its first and last dates. Sort the rows by `customer_id`, then `consecutive_start`, then `consecutive_end`, all in ascending order.

### Function Contract

**Inputs**

- `Transactions`: A table with integer columns `transaction_id`, `customer_id`, and `amount`, plus date column `transaction_date`. `transaction_id` is the primary key, and each `(customer_id, transaction_date)` pair is unique.

**Return value**

Return the columns `customer_id`, `consecutive_start`, and `consecutive_end`. Each row represents one maximal qualifying run of at least three dates, in the required ascending order.

### Examples

#### Example 1

- **Input:** Customer `101` has amounts `100`, `150`, and `200` on `2023-05-01` through `2023-05-03`.
- **Output:** `(101, 2023-05-01, 2023-05-03)`
- **Explanation:** All three dates are consecutive and both amount transitions are strictly increasing.

#### Example 2

- **Input:** Customer `102` transacts on `2023-05-01`, `2023-05-03`, and `2023-05-04` with increasing amounts.
- **Output:** No row for customer `102`.
- **Explanation:** The missing transaction on May 2 breaks calendar-day consecutiveness.

#### Example 3

- **Input:** Customer `105` has increasing daily transactions from May 1 through May 4 and another increasing run from May 12 through May 14.
- **Output:** `(105, 2023-05-01, 2023-05-04)` and `(105, 2023-05-12, 2023-05-14)`
- **Explanation:** The gap separates two maximal qualifying periods for the same customer.
