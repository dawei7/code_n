# Reported Posts II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1132 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open problem](https://leetcode.com/problems/reported-posts-ii/) |

## Problem Description

### Goal

The `Actions` table records user activity on posts and may contain duplicate rows. Its `action` value is one of `view`, `like`, `reaction`, `comment`, `report`, or `share`; `extra` optionally describes the action, such as a report reason. A spam report is a row with `action = 'report'` and `extra = 'spam'`.

The `Removals` table has one row for each removed post. For every date having at least one distinct spam-reported post, compute the percentage of those distinct posts that appear in `Removals`. Then return the unweighted average of these daily percentages, rounded to two decimal places. Days without spam reports do not participate, and only whether a post was eventually removed matters—not its `remove_date`.

### Function Contract

**Input tables**

- `Actions(user_id, post_id, action_date, action, extra)`: user actions; duplicate rows may occur.
- `Removals(post_id, remove_date)`: removed posts, with `post_id` as the primary key.

Let $A$ be the number of `Actions` rows, $M$ the number of `Removals` rows, and $R=A+M$.

**Return value**

A one-row, one-column table named `average_daily_percent`, containing the average daily removal percentage rounded to two decimal places.

### Examples

**Example 1**

Spam reports occur for posts `2` and `4` on `2019-07-04`, and for post `3` on `2019-07-02`. Posts `2` and `3` appear in `Removals`. The daily percentages are therefore $50\%$ and $100\%$, so the result is:

| average_daily_percent |
|---:|
| 75.00 |

Reports with another reason, such as `extra = 'racism'`, and days containing no spam reports are excluded.
