## General

**Aggregate row totals.** Form `assignment1 + assignment2 + assignment3` for
each student. Apply `MAX` and `MIN` to that same row-total expression, then
subtract the latter from the former. Both extrema are accumulated during one
scan and the query returns their difference under the required alias.

It is essential to sum each row before taking extrema: the student with the
highest value can differ between assignments, so adding three independent
column ranges would not measure the spread between actual student totals.
Because `MAX` and `MIN` examine every row total, their subtraction is exactly
the requested highest-minus-lowest difference.

## Complexity detail

Let $R$ be the number of students. The aggregate scans the table once, taking
$O(R)$ time and $O(1)$ auxiliary aggregate state.

## Alternatives and edge cases

- **Row-total CTE:** Compute each total in a CTE and aggregate it afterward; this is equivalent but more verbose.
- **All pairs of students:** Maximizing the difference between every pair is correct but creates quadratic work.
- **Sum of column ranges:** This can combine extrema from different students and is not equivalent to the range of row totals.
- **Single student:** The maximum and minimum totals are equal, so the difference is zero.
- **Tied extrema:** Repeated highest or lowest totals do not change the scalar result.
