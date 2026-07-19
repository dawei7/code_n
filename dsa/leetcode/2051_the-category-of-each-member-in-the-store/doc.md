# The Category of Each Member in the Store

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2051 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/the-category-of-each-member-in-the-store/) |

## Problem Description

### Goal

The `Members` table identifies store members. `Visits` records each member's trips to the store, and `Purchases` contains at most one purchase associated with a visit. A member's conversion rate is the percentage of visits that resulted in a purchase:

$$
\text{conversion rate}
=
\frac{100 \cdot \text{number of purchases}}{\text{number of visits}}.
$$

Report every member's ID, name, and category. A member with no visits is `Bronze`. Otherwise, a conversion rate of at least $80$ is `Diamond`, a rate from $50$ up to but not including $80$ is `Gold`, and a rate below $50$ is `Silver`. The result rows may appear in any order.

### Function Contract

**Inputs**

- `Members(member_id, name)`: one row per member, with unique `member_id`.
- `Visits(visit_id, member_id, visit_date)`: one row per store visit; `visit_id` is unique and `member_id` references `Members`.
- `Purchases(visit_id, charged_amount)`: one row per purchasing visit; `visit_id` is unique and references `Visits`.

Let $M$, $V$, and $P$ denote the numbers of rows in `Members`, `Visits`, and `Purchases`, respectively.

**Return value**

- Return the columns `member_id`, `name`, and `category` for every member.
- Result ordering is unrestricted.

### Examples

**Example 1**

- Input: members Alice, Bob, Winston, Hercy, and Narihan; their visits and purchases produce rates of $50\%$, approximately $33.33\%$, $0\%$, $100\%$, and no defined rate, respectively.
- Output: Alice is `Gold`, Bob and Winston are `Silver`, Hercy is `Diamond`, and Narihan is `Bronze`.

### Required Complexity

- **Time:** $O(M+V+P)$
- **Space:** $O(M+V+P)$

<details>
<summary>Approach</summary>

#### General

**Preserving members who never visited**

Begin with `Members` and left join both `Visits` and `Purchases`. The first left join retains a member even when no visit exists, which is necessary to produce the `Bronze` row. The second join marks which retained visits have a purchase. Because both visit identifiers are unique, one visit contributes at most one joined purchase row.

**Classifying aggregated activity**

Group by the member's ID and name. `COUNT(v.visit_id)` counts visits without counting the null placeholder created for an unvisited member, while `COUNT(p.visit_id)` counts only visits with purchases. Test the zero-visit case first to avoid division by zero and to distinguish `Bronze` from the zero-conversion `Silver` category. For visited members, evaluate thresholds from highest to lowest so that rates of exactly $80$ and $50$ enter `Diamond` and `Gold`, respectively.

The joins associate every visit and purchase with its owning member exactly once. Consequently, each group's two counts are precisely the denominator and numerator of that member's conversion rate, and the ordered `CASE` branches implement all category intervals without overlap or omission.

#### Complexity detail

With hash joins and hash aggregation, the three tables are scanned and indexed once, giving expected $O(M+V+P)$ time. Join and grouping state may contain all participating rows or member groups, requiring $O(M+V+P)$ auxiliary space. Physical costs can vary with the database optimizer and available indexes.

#### Alternatives and edge cases

- **Pre-aggregate visits and purchases:** Aggregate activity by member in a derived table before joining to `Members`. This is equally sound and can make the counting grain explicit.
- **Correlated subqueries:** Recounting visits and purchases separately for every member is readable but can rescan the activity tables $M$ times and become quadratic.
- An unvisited member is `Bronze`, whereas a visited member with no purchases has rate zero and is `Silver`.
- Rates exactly equal to $80$ or $50$ belong to the higher adjacent category.
- `charged_amount` does not affect conversion; the metric counts purchasing visits rather than revenue.

</details>
