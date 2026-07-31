## General

The new salary for each employee depends only on that row's current salary. Multiplying the entire `salary` Series by two performs this element-wise transformation in pandas, and assigning the resulting Series back to `salary` replaces the original values without changing the rest of the DataFrame.

Series assignment aligns values with the existing index, so every doubled salary remains attached to the correct employee. No row is inserted, removed, or reordered, and the column list stays `name`, `salary`, which proves that the returned table has exactly the requested structure and values.

## Complexity detail

Let $n$ be the number of employee rows. Vectorized multiplication and assignment process the salary column once, giving $O(n)$ time. The computed Series contains $n$ doubled values before assignment, so the additional space is $O(n)$.

## Alternatives and edge cases

- **`assign` with multiplication:** Returning `employees.assign(salary=employees["salary"] * 2)` has the same asymptotic bounds and avoids mutating the supplied object, but it may copy more of the DataFrame.
- **In-place arithmetic syntax:** Writing `employees["salary"] *= 2` is concise and also linear, though explicit assignment makes the replacement value clear.
- **Row-wise `apply`:** Applying a Python callback to each salary remains $O(n)$ but adds unnecessary per-row callback overhead.
- **Repeated concatenation:** Rebuilding the DataFrame one doubled row at a time is correct but can take $O(n^2)$ time as the growing result is copied repeatedly.
- **Schema preservation:** The operation must replace `salary`, not add a separate pay or bonus column.
- **Independent rows:** Equal input salaries produce equal doubled salaries; employee names do not affect the calculation.
