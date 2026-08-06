## Function Contract

**Input**

- `Employee`: the employee-to-team table described above.

Let $n$ be the number of employees and $t$ the number of distinct team identifiers.

**Return value**

Return a table with these columns:

- `employee_id`: an identifier from the input table.
- `team_size`: the number of input rows having that employee's `team_id`.

Return exactly $n$ rows—one for every employee. Team identifiers and employee identifiers need not be contiguous, and result order is unrestricted.
