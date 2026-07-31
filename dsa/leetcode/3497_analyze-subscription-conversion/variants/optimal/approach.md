## General

Discard `cancelled` rows before aggregation because they contribute to neither requested average nor the conversion test. Group the remaining rows by `user_id`.

Within each group, use conditional expressions inside `AVG`: a free-trial row contributes its duration to `trial_avg_duration` and produces `NULL` for the paid average, while a paid row behaves symmetrically. SQL aggregates ignore those `NULL` values, so both averages are computed independently in the same grouped pass. Apply `ROUND(..., 2)` to the two results.

The grouped `HAVING` condition counts the rows belonging to each stage and retains a user only when both counts are positive. This exactly matches the conversion criterion without joining separate summaries. Finally, sort the qualifying groups by `user_id` ascending.

## Complexity detail

Let $A$ be the number of activity rows and $U$ the number of distinct users. Filtering scans $A$ rows. In a general comparison-based execution plan, grouping and final ordering take $O(A\log A)$ time and maintain $O(U)$ aggregate state; a hash aggregate can make grouping expected $O(A)$ before the $O(U\log U)$ output sort.

The benchmark size is $A$. Every user has two free-trial and two paid rows, so all groups survive and all relevant rows participate. The accepted query aggregates once, while the calibrated slower query runs correlated table scans for each distinct user and scales quadratically without supporting indexes.

## Alternatives and edge cases

- **Separate free-trial and paid summaries joined by user:** Correct and still efficient, but it scans or groups the source twice instead of producing both aggregates together.
- **Correlated average subqueries:** Easy to read for one user, but repeating full-table scans for every user can take $O(A^2)$ time.
- **Include cancelled durations:** This corrupts both stage averages; cancelled rows are not part of either requested period.
- **Only free-trial activity:** The user did not convert and must be excluded.
- **Only paid activity:** Both required stages are not present, so the user must also be excluded.
- **Paid activity followed by cancellation:** The user still has both trial and paid stages and remains in the output.
- **Several rows per day or stage:** The unique key distinguishes activity types, and every qualifying stage row contributes once to its corresponding average.
- **Rounding:** Round each stage average after aggregation, not each daily duration before averaging.
- **Output order:** Sorting by `user_id` is part of the contract and cannot depend on the database's incidental group order.
