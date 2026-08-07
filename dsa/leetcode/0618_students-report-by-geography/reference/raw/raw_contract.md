## Function Contract

Execute one SQL query against the `Student` table.

### Inputs

- `Student(name, continent)`: Student names and their corresponding continents. Duplicate rows are permitted.

### Output

Return exactly three columns named `America`, `Asia`, and `Europe`, in that order. Sort the names within each continent alphabetically and align equal one-based ranks on the same output row. Preserve duplicate rows as repeated names at successive ranks, and use `NULL` after a shorter continent list is exhausted.
