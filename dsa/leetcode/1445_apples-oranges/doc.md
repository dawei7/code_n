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
