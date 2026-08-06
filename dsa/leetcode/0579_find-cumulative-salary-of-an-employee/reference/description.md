## Description

Build one cumulative salary summary containing rows for every employee.

For each month in which an employee worked, its three-month sum is the salary from that month plus the salaries from the previous two calendar months. A month in which that employee did not work contributes zero; it must not cause an older recorded month to enter the interval.

Omit the three-month sum for the most recent month in which each employee worked. Also omit every month for which that employee has no salary row.

Order the result by `id` in ascending order and, for equal identifiers, by `month` in descending order.
