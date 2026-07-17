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

### Required Complexity

- **Time:** $O(R)$
- **Space:** $O(R)$

<details>
<summary>Approach</summary>

#### General

**Form the exact reporting groups**

Group rows by both `date_id` and `make_name`. Neither column alone is sufficient: grouping only by date would merge different products, while grouping only by make would combine separate days. Each distinct pair produces exactly one output row.

**Count each identifier domain independently**

Within a group, apply `COUNT(DISTINCT lead_id)` and name it `unique_leads`. Apply a separate `COUNT(DISTINCT partner_id)` and name it `unique_partners`. SQL's distinct aggregate removes repeated identifiers before counting, so duplicated source rows and repeated leads or partners do not inflate the corresponding result.

The two aggregates must not be replaced by a distinct count of `(lead_id, partner_id)`: one lead may be associated with several partners, and each requested column asks for the cardinality of only its own identifier set. Because the contract permits any row order, no `ORDER BY` is needed.

#### Complexity detail

A hash aggregation inspects the $R$ input rows once and updates the date-and-make group's two distinct sets, taking expected $O(R)$ time. Across all groups, at most $R$ distinct lead entries and $R$ distinct partner entries are stored, so auxiliary space is $O(R)$. The database engine may choose another equivalent physical plan.

#### Alternatives and edge cases

- **Pre-deduplicate full rows:** a `SELECT DISTINCT` subquery remains correct but is unnecessary because each aggregate already removes duplicates in its own column.
- **Count distinct identifier pairs:** this answers a different question and can exceed either requested individual count.
- **Group by date only:** makes sold on the same day would be incorrectly merged.
- **Group by make only:** sales of the same make on different dates would be incorrectly merged.
- **Duplicate rows:** exact duplicates contribute only one value to each distinct identifier set.
- **Repeated lead with new partners:** `unique_leads` stays unchanged while `unique_partners` grows.
- **Output order:** the problem accepts any order, so sorting is not part of the required query.

</details>
