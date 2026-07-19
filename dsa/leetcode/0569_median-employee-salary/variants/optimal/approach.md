## General
**Rank salaries independently inside each company**

Use `ROW_NUMBER()` partitioned by `company` and ordered by `salary, id`. The identifier provides deterministic ordering when salaries tie.

**Know each partition's size on every row**

Use `COUNT(*) OVER (PARTITION BY company)` alongside the row number. Window functions preserve the original employee columns while adding both positional values.

**Select the central position or positions**

For partition size `c` and one-based row number `r`, keep rows satisfying $c \le 2r \le c + 2$. When `c` is odd, only the single middle row satisfies it. When `c` is even, the two adjacent middle rows do.

**Why the inequality identifies the median rows**

For $c = 2t + 1$, the bounds become $2t + 1 \le 2r \le 2t + 3$, whose only integer solution is $r = t + 1$. For $c = 2t$, they become $2t \le 2r \le 2t + 2$, selecting $r = t$ and $r = t + 1$. These are exactly the required positions in salary order for every company.

## Complexity detail
For `E` employees, a typical window plan sorts rows by company, salary, and identifier in $O(E \log E)$ time and stores the ranked rows in $O(E)$ space. Suitable indexes may reduce sorting work. The final ordering makes local result serialization deterministic.

## Alternatives and edge cases
- **Correlated rank counts:** can count lower salaries for every employee but may rescan the table and take $O(E^2)$ time.
- **Self-join and grouping:** derives ranks by materializing lower-or-equal salary pairs, also risking quadratic intermediate size.
- **Separate odd and even queries:** works but duplicates ranking logic and requires a union.
- **One employee:** has row number one and is selected.
- **Even company size:** returns exactly two rows.
- **Salary ties:** ordering by `id` supplies deterministic median positions.
- **Independent companies:** partitioning prevents one company's size or salaries from affecting another.
