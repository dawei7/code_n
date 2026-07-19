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
