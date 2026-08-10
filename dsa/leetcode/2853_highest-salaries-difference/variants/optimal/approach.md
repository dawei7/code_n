## General

**Compute a maximum salary for every department first.** The inner query groups `Salaries` by `department` and returns one value `s = MAX(salary)` per department.

For Engineering, this row is the greatest engineering salary. For Marketing, it is the greatest marketing salary. The primary key on employee name and department prevents duplicate identity rows but is not needed for the maximum itself.

**Turn two maxima into an absolute difference.** If the inner result contains exactly the Engineering and Marketing maxima, the larger one is `MAX(s)` and the smaller is `MIN(s)`. Their difference is nonnegative and equals the absolute difference:

$$
\max(E,M)-\min(E,M)=|E-M|.
$$

The outer query returns this as `salary_difference`.

This avoids needing to know which department has the higher salary.

**Why the stated existence guarantee matters.** There is at least one row in each required department, so both departmental maxima are non-null. With exactly those two department groups, the outer maximum and minimum are well-defined.
Grouping partitions salary rows by department and `MAX` selects the required top salary inside each group. The outer extrema select the larger and smaller of the two required values. Their subtraction equals the requested absolute difference. The query returns one row and one named column.

**A material assumption in the exact SQL.** The source does not filter `department` to Engineering and Marketing. It groups every department present in the table and subtracts the smallest departmental maximum from the largest departmental maximum.

The local description guarantees at least one Engineering and Marketing entry but does not explicitly state that no other departments can occur. If a third department has a maximum outside the interval between the required two maxima, this query returns the wrong value.

For example, if Engineering's maximum is 100, Marketing's is 50, and Sales has 1000, the required answer is 50 but the exact query returns 950.

Therefore, the source is correct only if the data domain contains exactly the two named departments, or if every additional department's maximum happens to lie between their maxima. A robust solution must filter or use conditional aggregation.

**The exact source also differs from the manifest.** The manifest describes computing both named maxima in one scan through conditional aggregation. The source performs a grouped subquery followed by an aggregate over its group results.

The grouped strategy may still be efficient, but it neither explicitly names the departments nor uses the one-row conditional form.

**How to make the grouped source faithful.** Adding

`WHERE department IN ('Engineering', 'Marketing')`

inside the subquery would ensure only the required two maxima reach the outer extrema. This retains the query's structure and makes the proof unconditional under the documented existence guarantee.

**Null salary assumptions.** The schema lists salary as an integer and examples use concrete values. If salaries could be null, `MAX` ignores nulls; an all-null department would produce null and complicate the result. The challenge's intended rows are ordinary salary values.

**No ordering is required.** The output is one aggregate row, so `ORDER BY` would add nothing.

## Complexity detail

Let $S$ be the number of salary rows and $D$ the number of departments.

With hash aggregation, computing departmental maxima can take $O(S)$ expected time and $O(D)$ group storage. The outer aggregate scans $D$ rows in $O(D)$ time and constant additional state.

With sort-based grouping, the database may take $O(S\log S)$ time and $O(S)$ temporary or external storage. Physical complexity depends on indexes and MySQL's optimizer.

Under a known two-department domain, $D=2$ and logical auxiliary aggregation state is $O(1)$, aligning with the manifest's one-scan spirit. Under the literal unfiltered query and arbitrary departments, group storage is $O(D)$.

The result is one scalar row.

## Alternatives and edge cases

- **Conditional aggregation:** Compute `MAX(CASE WHEN department = 'Engineering' THEN salary END)` and the analogous Marketing maximum, then apply `ABS` to their difference. This explicitly follows the requirement and matches the manifest.
- **Filter the grouped subquery:** Restrict to the two named departments before grouping, then `MAX(s) - MIN(s)` is safe.
- **Two scalar subqueries:** Query each department maximum separately and subtract with `ABS`. It is clear but may scan the table twice without optimization.
- **Engineering maximum is larger:** Outer max-minus-min returns Engineering minus Marketing.
- **Marketing maximum is larger:** The extrema reverse roles automatically and still return the absolute difference.
- **Equal maxima:** Both extrema are equal and the result is zero.
- **Multiple employees tied for maximum:** `MAX` returns the salary once; employee identity is irrelevant.
- **Additional department:** The exact unfiltered query can be wrong if its maximum changes the outer minimum or maximum.
- **Existence of both named departments:** It prevents a missing required maximum but does not by itself exclude unrelated groups.
- **One output row:** No result ordering is needed.
- **Manifest mismatch:** Conditional one-scan aggregation is the robust alternative, not the exact grouped-all-departments source.
