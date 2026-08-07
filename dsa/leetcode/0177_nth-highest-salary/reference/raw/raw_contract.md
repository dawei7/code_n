## Function Contract

**Inputs**

- `N`: The positive, 1-based rank requested by the native database function. App fixtures expose the same value through `Request(N)`.

`Employee(id, salary)` contains employee rows whose salary values may repeat.

**Return value**

Return the $N$th-highest distinct salary under the column `getNthHighestSalary`, or null when that rank does not exist.
