# Apples & Oranges

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1445 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/apples-oranges/) |

## Problem Description
### Goal

The `Sales` table records how many units of one fruit were sold on a date.
Each row identifies the date, whether the fruit is `"apples"` or
`"oranges"`, and the corresponding quantity. The pair
`(sale_date, fruit)` uniquely identifies a row, so each date has at most one
record for each fruit.

For every recorded sale date, calculate the number of apples sold minus the
number of oranges sold. Return one row per date with columns `sale_date` and
`diff`, ordered by `sale_date` in ascending order. A negative difference
is valid and means that more oranges than apples were sold that day.

### Function Contract
**Inputs**

- `Sales(sale_date, fruit, sold_num)`: a relation containing $R$ sales rows.
- `sale_date` is the date of the recorded sales.
- `fruit` is either `"apples"` or `"oranges"`.
- `sold_num` is the number of units sold for that fruit and date.
- `(sale_date, fruit)` is unique.

Let $D$ be the number of distinct sale dates.

**Return value**

Return a relation with columns `sale_date` and `diff`, where `diff` is
apple sales minus orange sales for that date. Produce exactly one row for each
of the $D$ dates and order the rows by `sale_date` ascending.

### Examples
**Example 1**

- Input: `Sales = [("2020-05-01", "apples", 10), ("2020-05-01", "oranges", 8), ("2020-05-02", "apples", 15), ("2020-05-02", "oranges", 15)]`
- Output: `[("2020-05-01", 2), ("2020-05-02", 0)]`

**Example 2**

- Input: `Sales = [("2020-05-03", "apples", 20), ("2020-05-03", "oranges", 0)]`
- Output: `[("2020-05-03", 20)]`

**Example 3**

- Input: `Sales = [("2020-05-04", "apples", 15), ("2020-05-04", "oranges", 16)]`
- Output: `[("2020-05-04", -1)]`

### Required Complexity
- **Time:** $O(R + Dlog D)$
- **Space:** $O(D)$

<details>
<summary>Approach</summary>

#### General

**Turn the two fruit rows into signed contributions**

Map each apple row to the positive value `sold_num` and each orange row to
the negative value `-sold_num` with a `CASE` expression. The sum of these
signed values for a date is then

$$
\text{apples sold}-\text{oranges sold},
$$

which is exactly the requested `diff`.

**Aggregate once per date**

Group the signed rows by `sale_date` and compute one `SUM` for each group.
The uniqueness of `(sale_date, fruit)` means the apple and orange quantities
cannot be duplicated within a date. More generally, the conditional sum still
uses every input row exactly once, so each daily result is isolated from every
other date.

This single aggregation is preferable to looking up each fruit separately for
every date. It scans the source relation once and maintains one accumulator per
date instead of repeatedly rescanning `Sales`.

**Preserve the required chronological output**

Finish with `ORDER BY sale_date`. Grouping determines which rows exist but
does not guarantee their presentation order; the explicit ordering clause is
therefore part of the result contract rather than cosmetic formatting.

For each output date, the `CASE` expression includes its apple quantity with
a plus sign and its orange quantity with a minus sign. Their group sum must be
the requested difference, including zero and negative results. Since
`GROUP BY` produces one and only one row per distinct date, the query is both
complete and free of duplicates.

#### Complexity detail

A hash aggregation reads all $R$ source rows once and keeps one accumulator for
each of the $D$ dates, requiring $O(R)$ expected aggregation time and $O(D)$
grouping state. Ordering the $D$ output groups costs $O(D\log D)$, for total
logical time $O(R+D\log D)$. An engine that can stream rows in date order from
an index may reduce the grouping or ordering work, but the stated bound does
not depend on that optimization.

#### Alternatives and edge cases

- **Two conditional sums:** Compute the apple sum and orange sum separately
  inside the same grouped query, then subtract them. This is also a single-pass
  solution but is more verbose than assigning the sign in one expression.
- **Join filtered apple and orange relations:** Pair the two fruit rows by
  date and subtract their quantities. The uniqueness guarantee makes this
  correct, but it introduces an avoidable join and depends more directly on
  both rows being materialized.
- **Correlated lookups per date:** Select distinct dates and run separate
  apple and orange subqueries for each one. Without suitable indexes this
  repeatedly scans `Sales` and can take $O(DR)$ time.
- **Equal sales:** Return `0`; do not remove the date with a `HAVING`
  clause.
- **More oranges than apples:** Preserve the negative result rather than using
  an absolute value.
- **Zero units:** A fruit row with `sold_num = 0` still participates normally
  and contributes zero.
- **Row order:** Never rely on the physical insertion or grouping order;
  `ORDER BY sale_date` is required.

</details>
