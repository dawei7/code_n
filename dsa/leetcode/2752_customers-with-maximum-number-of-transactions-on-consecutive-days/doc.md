# Customers with Maximum Number of Transactions on Consecutive Days

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2752 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open problem](https://leetcode.com/problems/customers-with-maximum-number-of-transactions-on-consecutive-days/) |

## Problem Description

### Goal

The `Transactions` table records individual purchases. Every `transaction_id` is unique, and each customer-date pair is unique, so a customer has at most one transaction on a calendar day.

For each customer, divide their transaction dates into maximal streaks in which every date is exactly one day after the preceding date. Find the greatest streak length across the entire table and return the `customer_id` attached to every streak having that length, sorted by `customer_id` in ascending order. The judge preserves one row per winning streak; therefore, if one customer owns multiple separate globally longest streaks, that identifier appears multiple times.

The transaction `amount` does not affect whether dates are consecutive.

### Function Contract

**Inputs**

- `Transactions`: a table with integer columns `transaction_id`, `customer_id`, and `amount`, plus date column `transaction_date`.

`transaction_id` is unique, and the pair `(customer_id, transaction_date)` is unique.

**Return value**

A one-column relation named `customer_id`, containing one row for each globally longest consecutive-date streak and ordered by `customer_id` ascending.

### Examples

**Example 1**

- Input: customer 101 transacts on May 1, 2, and 3; customer 102 transacts on May 1, 3, and 4; customer 105 transacts on May 1, 2, and 3.
- Output: `[[101], [105]]`
- Explanation: customers 101 and 105 each have a three-day streak, while customer 102's longest streak has length two.

**Example 2**

- Input: customer 7 transacts on June 1, 2, 10, and 11.
- Output: `[[7], [7]]`
- Explanation: both separate two-day streaks attain the global maximum, so both winning streak rows remain.

**Example 3**

- Input: customer 4 transacts on four consecutive dates with arbitrary increasing, decreasing, and equal amounts.
- Output: `[[4]]`
- Explanation: only the dates determine the streak.
