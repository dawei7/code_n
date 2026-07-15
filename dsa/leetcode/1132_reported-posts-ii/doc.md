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

### Required Complexity

- **Time:** $O(R \log R)$
- **Space:** $O(R)$

<details>
<summary>Approach</summary>

#### General

**Deduplicate the reporting unit first.** Filter `Actions` to spam report rows and select distinct `(action_date, post_id)` pairs. A post reported multiple times on the same date must contribute only once to that day's numerator and denominator; the same post reported on different dates participates once in each date.

**Mark removed posts with a left join.** Join each distinct daily report to `Removals` by `post_id`. The primary key in `Removals` guarantees at most one match. For each `action_date`, divide the count of matched posts by the total number of distinct reported posts and multiply by `100.0`. The floating-point factor prevents integer division.

**Average days rather than posts.** Put those daily percentages in a common table expression, then apply `AVG` across its rows and round once at the end. This gives every qualifying date equal weight. A single global ratio would instead weight dates with more reported posts more heavily and can produce a different answer.

#### Complexity detail

Deduplication and daily grouping may sort or hash up to $A$ action rows, while the join processes the filtered reports and $M$ removals. A conservative logical bound is $O(R \log R)$ time and $O(R)$ grouping/join space. Physical cost depends on indexes and the database optimizer.

#### Alternatives and edge cases

- **Conditional `COUNT(DISTINCT ...)`:** Joining raw actions and counting distinct report and removal IDs per day is equivalent, but early deduplication makes the reporting unit explicit.
- **Correlated removal lookup:** An `EXISTS` subquery per reported post is correct, but without an index it can repeatedly scan `Removals` and approach $O(AM)$.
- **Duplicate reports:** Repeated rows or multiple users reporting the same post on one date count as one post.
- **Unequal daily report counts:** Average the percentages themselves; do not divide all removed posts by all reported posts globally.
- **Removal date:** A post counts as removed whenever its ID appears in `Removals`, regardless of the stored date.
- **Non-spam reports:** Rows with another `extra` value do not enter any daily percentage.

</details>
