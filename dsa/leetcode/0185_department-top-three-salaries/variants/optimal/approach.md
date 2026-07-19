## General
The ranking is independent inside each department and is based on distinct salary levels, while every employee tied at a qualifying level must remain in the result. `DENSE_RANK()` matches all three requirements when partitioned by `departmentId` and ordered by salary descending.

An employee's dense rank is one plus the number of distinct greater salaries in that department. Therefore ranks `1`, `2`, and `3` correspond exactly to the top three distinct salary values, no matter how many employees share any one value.

Compute the window rank in a derived table or common table expression, then filter `salary_rank <= 3` in an outer query. Joining to `Department` supplies the display name. Use the stable department id for partitioning and joining; display names are labels and need not be unique identifiers.

Suppose a department has salaries `100, 100, 90, 80, 80, 70`. Dense ranks are `1, 1, 2, 3, 3, 4`, so both employees at `80` remain and only `70` is excluded. `RANK()` would assign the next levels `3` and `4` after the top tie, incorrectly excluding `80`; `ROW_NUMBER()` would incorrectly split every tie.

Within each department, dense rank `r` means exactly $r - 1$ distinct salary values are greater. Thus every row with rank at most three has fewer than three greater distinct salaries and belongs to a top-three level. Conversely, every employee earning one of the top three distinct values has dense rank at most three and survives the filter. Because ranking is applied to employee rows rather than deduplicated output rows, all ties are preserved.

## Complexity detail
Without a supporting index, ordering `n` employees within department partitions costs $O(n \log n)$ overall and may require $O(n)$ sort/window storage. An index beginning with department id and salary can improve the physical plan; joining department labels is typically linear or indexed.

## Alternatives and edge cases
- Counting distinct greater salaries in a correlated subquery mirrors the definition directly, but may become $O(n^2)$ without optimizer support.
- Deduplicating department-salary pairs, selecting three levels, and joining back to employees is correct but requires more query stages.
- `ROW_NUMBER()` loses ties, and sparse `RANK()` can skip a distinct salary level after a large tie; `DENSE_RANK()` has the required semantics.
- Departments with fewer than three distinct salaries return every employee.
- A tie of any size at the third level is included in full; departments with no employees produce no rows.
