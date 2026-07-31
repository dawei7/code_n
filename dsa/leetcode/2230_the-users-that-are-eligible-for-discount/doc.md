# The Users That Are Eligible for Discount

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2230 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/the-users-that-are-eligible-for-discount/) |

## Problem Description

### Goal

The `Purchases` table records each user's purchase timestamp and paid amount. Its composite primary key is (`user_id`, `time_stamp`), so a user cannot have two rows at the same instant.

Given `startDate`, `endDate`, and `minAmount`, report every user who made at least one purchase both within the inclusive interval from `startDate` through `endDate` and for an amount of at least `minAmount`. Each date parameter denotes the start of its day: in particular, the upper boundary is `endDate` at `00:00:00`, not the end of that calendar day. Return qualifying IDs once in ascending order.

### Function Contract

**Inputs**

- `Purchases`: Rows containing integer `user_id`, datetime `time_stamp`, and integer `amount`.
- `Parameters`: One app-local row containing `startDate`, `endDate`, and `minAmount`.

Let $r$ be the number of purchase rows.

**Return value**

Return a one-column table of distinct qualifying `user_id` values ordered numerically.

### Examples

**Example 1**

- Input: purchases `(1, "2022-04-20 09:03:00", 4416)`, `(2, "2022-03-19 19:24:02", 678)`, `(3, "2022-03-18 12:03:09", 4523)`, `(3, "2022-03-30 09:43:42", 626)`; dates `"2022-03-08"` through `"2022-03-20"`; minimum `1000`
- Output: user `3`

**Example 2**

- Input: a qualifying-amount purchase exactly at the start-date boundary
- Output: that purchase's user

**Example 3**

- Input: a purchase later than midnight on `endDate`
- Output: no row for that purchase alone
