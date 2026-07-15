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

### Required Complexity

- **Time:** $O(R \log R)$
- **Space:** $O(R)$

<details>
<summary>Approach</summary>

#### General

**Classify each user-date once.** Group by `(user_id, spend_date)`. Sum all amounts for that user on that date. A group containing two platform rows is `both`; because of the composite primary key and two-value platform domain, a one-row group is classified by its sole platform. This avoids counting a user twice in the `both` category while still adding both purchase amounts.

**Build the complete reporting grid.** Extract distinct dates and cross join them with an explicit three-row relation containing `desktop`, `mobile`, and `both`. This produces every required `(spend_date, platform)` pair even when no classified user-date belongs to it.

**Aggregate through a left join.** Left join the classified user-date rows onto the grid. For each grid cell, `SUM(amount)` gives the total spending and `COUNT(user_id)` gives the number of classified users. `COUNT` naturally returns zero for an unmatched cell, while `COALESCE` converts the unmatched sum from `NULL` to `0`. Every source user-date joins exactly once, so totals are neither omitted nor duplicated.

#### Complexity detail

Grouping the $R$ purchase rows by user and date and grouping the joined result may require sorting, giving a conservative $O(R \log R)$ logical time bound. The classified user-date relation, distinct dates, and grouping state require $O(R)$ space. Physical database costs depend on indexes and the chosen execution plan.

#### Alternatives and edge cases

- **Three `UNION ALL` branches:** Separate queries for mobile-only, desktop-only, and both can work, but each branch repeats classification logic and still needs explicit zero rows for missing categories.
- **Correlated counterpart lookup:** Testing for an opposite-platform row separately for every purchase is correct, but without a supporting index it can repeatedly scan `Spending` and approach $O(R^2)$.
- **Both-platform user:** Add both row amounts but count the user once in `total_users`.
- **Missing category:** The date-platform grid must retain a row with `total_amount = 0` and `total_users = 0`.
- **Same user on different dates:** Platform classification is independent for each date; activity on one date cannot change another date's category.

</details>
