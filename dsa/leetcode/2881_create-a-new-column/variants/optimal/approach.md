## General

The new value is an element-wise transformation of the existing `salary` column: each salary is multiplied by two, and the resulting Series is assigned to `bonus`. pandas aligns that Series with the DataFrame's index, so each computed bonus stays with the employee from the same row. Assigning the column after the two existing columns also produces the required `name`, `salary`, `bonus` order.

The transformation does not depend on any other row. Consequently, vectorized multiplication computes exactly `2 * salary` once for every employee while leaving names, salaries, and row order unchanged.

## Complexity detail

Let $n$ be the number of employee rows. Multiplication and assignment each process the new column across the rows, giving $O(n)$ time. The computed Series and stored `bonus` column contain $n$ values, so the additional space is $O(n)$.

## Alternatives and edge cases

- **`assign` with Series multiplication:** Returning `employees.assign(bonus=employees["salary"] * 2)` has the same asymptotic bounds and avoids mutating the supplied object, but it may copy more of the DataFrame.
- **Row-wise `apply`:** Applying a Python callback to every salary is also $O(n)$, but it gives up the lower overhead of pandas vectorized arithmetic.
- **Repeated concatenation:** Building a one-row DataFrame and concatenating it for every employee is correct but can take $O(n^2)$ time because the growing result is repeatedly copied.
- **Column order:** `bonus` must follow `salary`; assigning this new column after the existing two columns preserves that schema.
- **Row order:** No sorting or grouping is needed, and doing either could violate the required employee order.
- **Repeated salaries:** Equal salaries yield equal bonuses independently; names do not affect the calculation.
