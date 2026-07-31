# Top Three Wineries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2991 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/top-three-wineries/) |

## Problem Description
### Goal
The `Wineries` table contains uniquely identified point awards associated with
a country and winery. A winery's score is the sum of all its `points` rows
within its country.

For each country, rank wineries by total points descending; when totals tie,
rank the winery whose name is alphabetically smaller first. Return one row per
country with strings `"name (total)"` for ranks one, two, and three under
`top_winery`, `second_winery`, and `third_winery`. If rank two is absent, use
`"No second winery"`; if rank three is absent, use `"No third winery"`.
Order countries ascending.

### Function Contract
**Inputs**

- `Wineries(id, country, points, winery)`: uniquely identified winery point rows

Let $R$ be the number of input rows.

**Return value**

Return each country's formatted top-three columns, with required placeholders
for missing ranks, ordered by `country` ascending.

### Examples
**Example 1**

- Input: The published Australia, Hungary, India, and USA winery rows
- Output: Australia ranks HarmonyHill, GrapesGalore, and WhisperingPines; USA aggregates RoyalVines to `86`.

**Example 2**

- Input: A country with one winery
- Output: Its top winery plus both missing-rank placeholders.

**Example 3**

- Input: Equal totals for wineries `Alpha` and `Beta`
- Output: `Alpha` ranks before `Beta`.
