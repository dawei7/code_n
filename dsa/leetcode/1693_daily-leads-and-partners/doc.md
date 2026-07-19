# Daily Leads and Partners

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1693 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/daily-leads-and-partners/) |

## Problem Description
### Goal

The `DailySales` table records a sale date, a lowercase product make name, a lead identifier, and a partner identifier. It has no primary key, so the same row may occur more than once. A make may appear on several dates, and a date may contain several makes.

Produce one result row for every distinct `(date_id, make_name)` pair. For that exact group, report how many different `lead_id` values and how many different `partner_id` values occur. Repeated occurrences of an identifier count once within its group, and the result rows may be returned in any order.

### Function Contract
**Inputs**

- `DailySales(date_id, make_name, lead_id, partner_id)`: the complete sales table, which may contain duplicate rows

Let $R$ be the number of rows in `DailySales`.

**Return value**

A table with columns `date_id`, `make_name`, `unique_leads`, and `unique_partners`, containing one row per date-and-make group.

### Examples
**Example 1**

- Input: rows for Toyota and Honda on `2020-12-07` and `2020-12-08`
- Output: four date-and-make groups

For Toyota on `2020-12-08`, lead IDs `{0, 1}` give `unique_leads = 2`, while partner IDs `{0, 1, 2}` give `unique_partners = 3`.

**Example 2**

- Input: three identical rows for one date and make
- Output: `unique_leads = 1, unique_partners = 1`

Source duplication does not increase either distinct count.

**Example 3**

- Input: one lead paired with three different partners in one group
- Output: `unique_leads = 1, unique_partners = 3`

The two distinct aggregates are computed independently rather than as distinct lead-partner pairs.
