## General

**Create one ordered stream per column**

Sorting entire input rows cannot work because it preserves the original
association between `first_col` and `second_col`. Instead, read `Data` twice.
In the first stream, assign `ROW_NUMBER()` in ascending `first_col` order. In
the second, assign row numbers in descending `second_col` order.

**Pair equal positions**

Join the two streams on their generated row number. Rank $r$ from the first
stream is the $r$-th smallest first-column value, while rank $r$ from the
second is the $r$-th largest second-column value. Their joined row therefore
has exactly the required independent ordering. An outer `ORDER BY` on the rank
makes the result sequence explicit.

`ROW_NUMBER()` assigns a distinct position to every input occurrence, so
duplicates are neither collapsed nor multiplied. Their internal tie order is
irrelevant because tied values are equal.

## Complexity detail

Let $n$ be the number of rows in `Data`. The two window orderings each require
$O(n\log n)$ sorting work; ranking and joining are linear after those sorts.
The total logical cost is $O(n\log n)$ time and $O(n)$ execution space, subject
to the database engine's physical plan and indexes.

## Alternatives and edge cases

- **Sort rows once:** Ordering by `first_col ASC, second_col DESC` retains row
  associations and does not independently reorder the columns.
- **Correlated ranks:** Counting smaller or larger values for every occurrence
  can reproduce the result but requires duplicate tie identifiers and may take
  $O(n^2)$ time.
- **Aggregate by value:** Grouping frequencies and expanding them is possible,
  but SQL expansion is more complicated than row numbering.
- Duplicate rows and duplicate individual values must retain every occurrence.
- Negative integers use ordinary numeric ascending and descending order.
- The final `ORDER BY` is required because a join alone does not guarantee row
  order.
