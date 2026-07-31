## General

The required result is a fixed-length prefix of the DataFrame. pandas provides `head(3)` specifically for this operation: it selects positions from the beginning, keeps the existing column labels, and preserves row order. It also naturally returns every available row when the input has fewer than three records.

No condition, sorting key, or employee value affects membership. The first three positions alone determine the answer, so the method must not scan or copy rows beyond that prefix.

## Complexity detail

The requested prefix contains at most three rows and the schema has four fixed columns. Selecting and returning that bounded view takes $O(1)$ time and $O(1)$ output space with respect to the number of input rows.

## Alternatives and edge cases

- **Positional slicing:** `employees.iloc[:3]` selects the same prefix with the same asymptotic bounds, though `head(3)` communicates the intent directly.
- **Copying before selection:** Copying the entire DataFrame and then taking its first rows is correct but wastes $O(n)$ time and space for $n$ employees.
- **Fewer than three rows:** The result contains every available row; no padding is added.
- **Original ordering:** The method must not sort by `employee_id`, name, or another column.
- **Schema preservation:** All four columns and their labels remain in the result.
