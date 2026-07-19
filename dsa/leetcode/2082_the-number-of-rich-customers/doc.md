# The Number of Rich Customers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2082 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/the-number-of-rich-customers/) |

## Problem Description

### Goal

The `Store` table records individual bills. Each row has a unique bill identifier, the customer responsible for that bill, and its integer amount. A customer is considered rich when at least one of their bills has an amount strictly greater than 500.

Report how many distinct customers satisfy that condition. Multiple qualifying bills from the same customer must contribute only once, an amount equal to 500 does not qualify, and the result must be a single row with column name `rich_count`.

### Function Contract

**Inputs**

- `Store(bill_id, customer_id, amount)`: a relation of $B$ bills where `bill_id` is unique; each row associates one amount with one customer.
- Let $C$ be the number of distinct customers who have at least one qualifying bill.

**Return value**

- Return one row and one column named `rich_count`, containing $C$.

### Examples

**Example 1**

- Input: `Store = [[6,1,549],[8,1,834],[4,2,394],[11,3,657],[13,3,257]]`
- Output: `[[2]]`
- Explanation: Customers 1 and 3 each have a bill above 500; customer 1 still counts only once despite having two.

**Example 2**

- Input: `Store = [[1,7,500],[2,8,501]]`
- Output: `[[1]]`
- Explanation: The threshold is strict, so only customer 8 qualifies.

**Example 3**

- Input: `Store = [[1,4,100],[2,4,900],[3,5,300]]`
- Output: `[[1]]`
- Explanation: One qualifying bill is enough to make customer 4 rich.

### Required Complexity

- **Time:** $O(B\log B)$
- **Space:** $O(C)$

<details>
<summary>Approach</summary>

#### General

**Filter bills at the strict threshold**

Apply `WHERE amount > 500` before aggregation. This retains every bill that can establish a rich customer and rejects both lower amounts and the boundary value 500. A customer with any retained row qualifies regardless of their other bills.

**Count customers rather than bills**

Use `COUNT(DISTINCT customer_id)` over the filtered relation. `DISTINCT` collapses all qualifying bills for one customer to one identity before counting, directly matching the “at least one bill” condition. The aggregate returns one row even when no bill qualifies, in which case the count is zero.

**Name the scalar result exactly**

Alias the aggregate as `rich_count`. No grouping is needed because the requested result is one total across the complete table, and no ordering clause is relevant to a single-row relation.

#### Complexity detail

The filter reads $B$ rows. A sort-based implementation of `COUNT(DISTINCT ...)` takes $O(B\log B)$ time and stores up to $O(C)$ qualifying customer identities; a hash aggregate can achieve expected $O(B)$ time with the same asymptotic identity storage. Database indexes and optimizer choices may alter the physical plan without changing the query semantics.

#### Alternatives and edge cases

- **Group then count:** Selecting qualifying customers with `GROUP BY customer_id` in a subquery and applying `COUNT(*)` outside is equivalent but more verbose.
- **Count qualifying rows:** `COUNT(*)` after the filter is wrong when one customer has several bills above 500.
- **Conditional distinct aggregate:** `COUNT(DISTINCT CASE WHEN amount > 500 THEN customer_id END)` is equivalent because `COUNT` ignores nulls.
- **Exact threshold:** An amount of 500 is excluded by the strictly-greater comparison.
- **Mixed bills for one customer:** One qualifying bill is sufficient even when the same customer also has nonqualifying bills.
- **No qualifying rows:** The aggregate still returns `rich_count = 0`.

</details>
