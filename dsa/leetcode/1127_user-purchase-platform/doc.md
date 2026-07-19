# User Purchase Platform

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1127 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open problem](https://leetcode.com/problems/user-purchase-platform/) |

## Problem Description

### Goal

The `Spending` table records purchases made through an online shop's desktop and mobile applications. Each row identifies a user, purchase date, platform, and amount. The combination `(user_id, spend_date, platform)` is the primary key, and `platform` is either `desktop` or `mobile`, so a user can have at most one row for each platform on a given date.

For every date present in `Spending`, report three categories: users who purchased through mobile only that day, users who purchased through desktop only, and users who used both platforms. For each category, return the total amount those users spent and their total number. Every date must have all three category rows, with `0` for both totals when nobody belongs to a category. Return the result rows in any order.

### Function Contract

**Input table**

- `Spending(user_id, spend_date, platform, amount)`: purchase records with primary key `(user_id, spend_date, platform)` and `platform` restricted to `desktop` or `mobile`.

Let $R$ be the number of rows in `Spending`.

**Return value**

A table with columns `spend_date`, `platform`, `total_amount`, and `total_users`. For each distinct date, `platform` must contain exactly one row each for `desktop`, `mobile`, and `both`.

### Examples

**Example 1**

`Spending`

| user_id | spend_date | platform | amount |
|---:|---|---|---:|
| 1 | 2019-07-01 | mobile | 100 |
| 1 | 2019-07-01 | desktop | 100 |
| 2 | 2019-07-01 | mobile | 100 |
| 2 | 2019-07-02 | mobile | 100 |
| 3 | 2019-07-01 | desktop | 100 |
| 3 | 2019-07-02 | desktop | 100 |

Output:

| spend_date | platform | total_amount | total_users |
|---|---|---:|---:|
| 2019-07-01 | desktop | 100 | 1 |
| 2019-07-01 | mobile | 100 | 1 |
| 2019-07-01 | both | 200 | 1 |
| 2019-07-02 | desktop | 100 | 1 |
| 2019-07-02 | mobile | 100 | 1 |
| 2019-07-02 | both | 0 | 0 |

On `2019-07-01`, user `1` used both platforms, user `2` used only mobile, and user `3` used only desktop. On `2019-07-02`, no user used both platforms, but its zero-valued row is still required.
