# Restaurant Growth

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1321 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/restaurant-growth/) |

## Problem Description
### Goal
The `Customer` table records restaurant visits. A row identifies a customer and visit date and stores the total amount that customer paid on that visit. The pair `(customer_id, visited_on)` is unique, while several customers may visit on the same date. At least one visit occurs on every calendar day covered by the data.

For each date with six earlier dates available, calculate the restaurant's total revenue during the seven-day window ending on that date and the corresponding daily average. The window includes the current date and the preceding six calendar days, and all visits on a date contribute to its daily revenue.

Name the results `visited_on`, `amount`, and `average_amount`, round the average to two decimal places, omit dates that do not yet have a complete seven-day window, and order the rows by `visited_on` ascending.

### Function Contract
**Inputs**

- `Customer(customer_id, name, visited_on, amount)`: visit rows with integer identifiers and amounts, customer names, and dates; `(customer_id, visited_on)` is the primary key.

Let $r$ be the number of visit rows and $d$ the number of distinct dates.

**Return value**

One row per complete seven-day window, containing its ending date, seven-day revenue total, and revenue divided by 7 rounded to two decimal places, in ascending date order.

### Examples
**Example 1**

- Input: daily totals `100, 110, 120, 130, 110, 140, 150, 80, 110, 280` from `2019-01-01` through `2019-01-10`
- Output: rows `(2019-01-07, 860, 122.86)`, `(2019-01-08, 840, 120.00)`, `(2019-01-09, 840, 120.00)`, and `(2019-01-10, 1000, 142.86)`
- Explanation: Each row sums its ending date and the previous six daily totals.

**Example 2**

- Input: seven consecutive days with one payment of 1 each day
- Output: `(seventh date, 7, 1.00)`
- Explanation: Exactly one complete window exists.

**Example 3**

- Input: eight daily totals `10, 20, 30, 40, 50, 60, 70, 80`
- Output: `(seventh date, 280, 40.00)` and `(eighth date, 350, 50.00)`
- Explanation: Advancing one day removes 10 and adds 80.

### Required Complexity
- **Time:** $O(r+d\log d)$
- **Space:** $O(d)$

<details>
<summary>Approach</summary>

#### General

**Aggregate visits before forming windows**

Group `Customer` by `visited_on` and sum `amount`. This produces exactly one revenue value per date, which is essential because a window frame over raw visits would count rows rather than calendar days when multiple customers share a date.

**Use ordered seven-row windows**

Because the contract guarantees at least one customer every day, seven consecutive rows in the daily table represent seven consecutive calendar dates. Over dates in ascending order, compute both `SUM(amount)` and `AVG(amount)` with `ROWS BETWEEN 6 PRECEDING AND CURRENT ROW`. A row number in the same order identifies the first six dates, whose frames are incomplete; retain only rows numbered 7 or later.

The retained sum contains precisely the current daily total and the six preceding daily totals. The average of those same seven values equals the requested total divided by 7. Rounding it and ordering by the ending date produces the required relation.

#### Complexity detail

Grouping scans $r$ visits and retains $d$ daily totals. Ordering those totals for the window functions costs $O(d\log d)$ in the general model, and the bounded rolling frame is evaluated in $O(d)$ additional time. The daily and windowed intermediate relations use $O(d)$ space.

#### Alternatives and edge cases

- **Correlated date-range sums:** For each ending date, a subquery can sum the previous six calendar days, but without a supporting index it repeatedly scans the daily relation and can take $O(d^2)$ time.
- **Self-join by date range:** Joining every ending date to its seven source dates is correct after daily aggregation, but creates more intermediate rows and requires another grouping step.
- **Multiple visits on one date:** Sum them first; they must not create extra positions in the seven-day frame.
- **First six dates:** Their windows contain fewer than seven days and must not appear.
- **Exactly seven dates:** Produce exactly one result row.
- **Average denominator:** Divide the seven-day total by 7, not by the number of customer visits.

</details>
