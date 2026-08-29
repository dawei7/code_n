## General

The query orders each employee’s reviews from newest to oldest, computes the two changes across the latest three ratings, and keeps employees whose two changes are both positive.

Summing those two adjacent changes telescopes to latest rating minus earliest rating, which is exactly the requested improvement score.

**Ranking reviews per employee**

`ROW_NUMBER() OVER (PARTITION BY employee_id ORDER BY review_date DESC)` assigns:

- `rn=1` to the latest review;
- `rn=2` to the second latest;
- `rn=3` to the third latest.

Ranking restarts independently for every employee.

Only rows two and three will be aggregated later, because each holds one comparison to the review immediately newer than itself.

**Computing chronological improvement while sorting backward**

The window order is newest to oldest. For a row, `LAG(rating)` returns the rating on the preceding row in that order, which is the next newer review chronologically.

The source calculates:

`delta = newer_rating - current_older_rating`.

For `rn=2`, delta is latest minus second-latest. For `rn=3`, delta is second-latest minus third-latest.

Both deltas must be positive for ratings to increase strictly from oldest to newest.

The latest row `rn=1` has no previous row in this descending order, so its lag and delta are null. It is intentionally excluded before grouping.

**Selecting exactly the two needed comparisons**

`WHERE rn > 1 AND rn <= 3` keeps rows with rank two and three.

An employee with at least three reviews contributes exactly two rows. Someone with only two reviews contributes only rank two; someone with one contributes none.

Older reviews beyond the latest three are ignored, even if they break or strengthen a longer trend.

**Requiring at least three and strict increase**

After joining employee names, the query groups by employee.

`HAVING COUNT(*)=2` proves both comparison rows exist, and therefore the employee has at least three reviews.

`MIN(delta)>0` proves each of the two deltas is positive. If either comparison is zero or negative, the minimum is not positive and the employee is excluded.

**Why SUM(delta) is the improvement score**

Let the last three chronological ratings be `a,b,c` from oldest to latest. The retained deltas are:

$$
c-b
\quad\text{and}\quad
b-a.
$$

Their sum is:

$$
(c-b)+(b-a)=c-a.
$$

The middle rating cancels, leaving latest minus earliest exactly as required.

**Joining names and ordering**

`recent JOIN employees USING(employee_id)` attaches each employee’s name. The final output contains identifier, name, and aggregated score.

`ORDER BY 3 DESC,2` sorts improvement score descending, then name ascending for ties.

**Date ties are an unstated dependency**

The window order uses only `review_date DESC`. If one employee has multiple reviews on the same date, their relative ordering is not deterministic, and “latest three” is ambiguous without another key.

The source relies on review dates being sufficient to order an employee’s reviews. If equal dates are allowed and `review_id` defines tie order, it should be added explicitly to both window orderings. The local schema does not state a same-date tie rule, so this is a boundary assumption rather than a claimed implemented tie-breaker.

## Complexity detail

Let `R` be review rows and `E` employee rows. Window functions generally require arranging reviews by employee and descending date, costing `O(R\log R)` under a sort-based plan. Joining and grouping may use hashes or indexes; sorting the qualifying output costs at most `O(E\log E)`.

A conservative bound is `O(R\log R+E\log E)`, matching the manifest. An index on `(employee_id,review_date)` can reduce physical sorting depending on the optimizer.

Window and grouped intermediate relations can occupy `O(R+E)` logical space. Actual memory depends on materialization, streaming, and disk spill.

## Alternatives and edge cases

- **Conditional aggregation after row numbering:** One can place latest, second, and third ratings into columns with CASE expressions, then compare them. The delta method is compact and makes the score telescope naturally.
- **Self-join reviews by dates:** Repeatedly finding the three latest rows per employee is more complex and can multiply rows.
- **Exactly three reviews:** Both required delta rows exist and are evaluated normally.
- **Fewer than three reviews:** COUNT is below two, so the employee is excluded.
- **More than three reviews:** Rows older than rank three are filtered out.
- **Equal adjacent ratings:** Delta zero fails strict improvement.
- **A decrease followed by a large rise:** One delta is negative, so a positive overall latest-minus-earliest difference alone is not enough.
- **Negative improvement score:** Such an employee necessarily fails MIN(delta)>0 and is excluded.
- **Tied scores:** Name ascending decides their output order.
- **Duplicate names:** The specified keys provide no further ordering; employee IDs remain distinct output rows.
- **Same review date:** The current source has nondeterministic relative order unless data guarantees uniqueness per employee.
- **Null ratings:** The schema narrative implies integer ratings; if null were allowed, MIN and SUM null behavior would need explicit handling.
- **Group by employee_id:** Name is functionally determined by the unique employee row; MySQL can permit selecting it under functional-dependency rules.
- **Latest-row delta:** It is null but filtered out through `rn>1` before aggregation.
