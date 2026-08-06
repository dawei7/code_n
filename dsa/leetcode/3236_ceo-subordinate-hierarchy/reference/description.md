## Description

The `Employees` table stores an organization's reporting hierarchy. Every employee has a unique identifier, name, salary, and manager identifier; the CEO is the row whose `manager_id` is `NULL`.

Return every direct and indirect subordinate of the CEO. For each subordinate, report the employee's identifier and name, the number of reporting edges from the CEO, and the subordinate's salary minus the CEO's salary. Direct reports are at level $1$, their reports are at level $2$, and the pattern continues through any depth.

Order the result by hierarchy level ascending and then subordinate identifier ascending. Do not include the CEO in the output.
