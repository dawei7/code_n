# Find Customers With Positive Revenue this Year

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/find-customers-with-positive-revenue-this-year/) |
| Frontend ID | 1821 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |

## Problem Description

### Goal

The `Customers` table stores one customer's revenue for a particular calendar year. Revenue is allowed to be positive, zero, or negative, and the same customer may have separate rows for different years.

Report the identifiers of customers whose revenue in the year 2021 is strictly greater than zero. A positive value from another year does not qualify, while zero or a negative 2021 value must be excluded. The result may be returned in any order.

### Function Contract

**Inputs**

- `Customers(customer_id, year, revenue)`: one row per `(customer_id, year)` pair.
- `customer_id` identifies a customer, `year` identifies the calendar year, and `revenue` is that customer's possibly non-positive revenue for the year.
- Let $r$ be the number of rows in `Customers`, and let $o$ be the number of qualifying output rows.

**Return value**

- Return one column named `customer_id`, containing exactly those customers whose row has `year = 2021` and `revenue > 0`.
- Result row order is not significant.

### Examples

**Example 1**

`Customers`

| customer_id | year | revenue |
|---:|---:|---:|
| 1 | 2018 | 50 |
| 1 | 2021 | 30 |
| 1 | 2020 | 70 |
| 2 | 2021 | -50 |
| 3 | 2018 | 10 |
| 3 | 2016 | 50 |
| 4 | 2021 | 20 |

Output:

| customer_id |
|---:|
| 1 |
| 4 |

Customers 1 and 4 have positive 2021 revenue. Customer 2 has a 2021 row but its revenue is negative, and customer 3 has no row for 2021.

### Required Complexity

- **Time:** $O(r)$
- **Space:** $O(o)$

<details>
<summary>Approach</summary>

#### General

**Apply both qualifications to the same table row**

Read `Customers` once and retain a row only when its `year` equals 2021 and its `revenue` is strictly greater than zero. These predicates must be joined with `AND`: satisfying only the year condition or only the revenue condition is insufficient.

**Project only the requested identifier**

Select `customer_id` from the qualifying rows. The `(customer_id, year)` key guarantees at most one 2021 row for each customer, so the filter cannot produce duplicate identifiers and no `DISTINCT`, grouping, join, or aggregation is required.

**Why the result is exact**

Every returned row comes from 2021 and has positive revenue because it passes both predicates. Conversely, every customer meeting the definition has a corresponding table row that passes those same predicates and is therefore returned. Rows for other years cannot influence the decision about the 2021 row.

#### Complexity detail

Without assuming a particular index, the database scans the $r$ table rows once and evaluates two constant-time predicates, giving $O(r)$ time. The result contains $o$ identifiers and therefore uses $O(o)$ output space; the query requires no additional relation proportional to the input.

#### Alternatives and edge cases

- **Filter only positive revenue:** This incorrectly includes customers whose positive revenue occurred outside 2021.
- **Filter only the year:** This incorrectly includes zero and negative revenue.
- **Group by customer and sum revenue:** There is already at most one row per customer-year, and combining other years changes the required semantics.
- **Self-join or correlated subquery:** These can reproduce the filter but add unnecessary repeated table work.
- **Zero revenue:** The comparison is strict, so zero does not qualify.
- **Negative revenue:** Exclude it even when the year is 2021.
- **Positive revenue in another year:** It has no effect on this report.
- **Empty result:** Return the correct column with no rows when nobody qualifies.

</details>
