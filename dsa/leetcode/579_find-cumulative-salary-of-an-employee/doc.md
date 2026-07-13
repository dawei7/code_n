# Find Cumulative Salary of an Employee

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 579 |
| Difficulty | Hard |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/find-cumulative-salary-of-an-employee/) |

## Problem Description
### Goal
Given monthly salary rows for multiple employees, calculate a three-month cumulative salary for each employee and recorded month. The value for month `M` is that employee's salary in calendar months `M`, $M - 1$, and $M - 2$; when one of those months has no row, it contributes nothing rather than being replaced by an older recorded month.

Exclude the latest recorded month for each employee from the result. Return `Id`, `Month`, and the cumulative value as `Salary`, ordering rows first by `Id` in ascending order and then by `Month` in descending order. An employee with only one recorded month therefore contributes no output row.

### Function Contract
**Inputs**

- `Employee(Id, Month, Salary)`: one salary record per employee and month

**Return value**

- Columns `Id`, `Month`, and `Salary`, where `Salary` is the sum over months from `Month - 2` through `Month` for the same employee
- Exclude each employee's greatest recorded month
- Order rows by `Id` ascending and then `Month` descending

### Examples
**Example 1**

- Input: employee 1 has salaries `20`, `30`, `40`, and `60` in months 1 through 4
- Output: months 3, 2, and 1 with cumulative salaries `90`, `50`, and `20`; month 4 is excluded

**Example 2**

- Input: one employee has records only in months 1 and 4
- Output: month 1 with only its own salary; month 4 is excluded

**Example 3**

- Input: an employee has a single salary row
- Output: no rows for that employee

### Required Complexity

- **Time:** $O(R \log R)$
- **Space:** $O(R)$

<details>
<summary>Approach</summary>

#### General

**Use a calendar-month window**

Partition rows by employee and order them by `Month`. For each row, sum salaries over a numeric range from two months before the current month through the current month. A `RANGE` frame expresses calendar distance, so a missing month contributes nothing rather than causing an older recorded row to enter the window.

**Mark the latest row independently**

Compute the greatest month in each employee partition, or equivalently assign descending row numbers. These values must be calculated in the same inner relation as the cumulative salary so all salary rows remain available to the window.

**Filter only after both windows are complete**

In an outer query, discard the row whose month equals the partition maximum. Filtering it before window evaluation could remove data needed for another row's cumulative total in a more general ordering. Finally, apply the required employee-ascending and month-descending order.

**Why every reported total is exact**

The partition prevents salaries from different employees from mixing. The numeric frame contains exactly the existing records whose months satisfy `currentMonth - 2 <= Month <= currentMonth`, which is the requested three-calendar-month interval. The outer maximum-month filter removes exactly one latest row per employee while preserving every earlier computed total.

#### Complexity detail

For `R` salary rows, partition ordering costs $O(R \log R)$ time in the general case. Window state and the sorted relation use $O(R)$ working space; database indexes may reduce sorting work.

#### Alternatives and edge cases

- **Correlated range sum:** directly sums matching rows for each output month but may rescan the table per row and take $O(R^2)$ time.
- **Self-join on the month interval:** is expressive, though it can create several joined rows per output before aggregation.
- **`ROWS BETWEEN 2 PRECEDING`:** is incorrect when recorded months have gaps because it means two prior rows, not two prior calendar months.
- **Filter latest month before the salary window:** risks changing the rows available to window calculations; compute first and filter outside.
- **Missing months:** contribute zero and do not pull an older month into the three-month interval.
- **Fewer than three months of history:** sum only the existing in-range rows.
- **Single recorded month:** is the employee's latest and produces no output row.
- **Independent employees:** each employee has a separate latest month and rolling total.
- **Required ordering:** sort by `Id` ascending, then `Month` descending.

</details>
