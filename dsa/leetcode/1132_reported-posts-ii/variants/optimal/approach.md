## General
**Deduplicate the reporting unit first.** Filter `Actions` to spam report rows and select distinct `(action_date, post_id)` pairs. A post reported multiple times on the same date must contribute only once to that day's numerator and denominator; the same post reported on different dates participates once in each date.

**Mark removed posts with a left join.** Join each distinct daily report to `Removals` by `post_id`. The primary key in `Removals` guarantees at most one match. For each `action_date`, divide the count of matched posts by the total number of distinct reported posts and multiply by `100.0`. The floating-point factor prevents integer division.

**Average days rather than posts.** Put those daily percentages in a common table expression, then apply `AVG` across its rows and round once at the end. This gives every qualifying date equal weight. A single global ratio would instead weight dates with more reported posts more heavily and can produce a different answer.

## Complexity detail
Deduplication and daily grouping may sort or hash up to $A$ action rows, while the join processes the filtered reports and $M$ removals. A conservative logical bound is $O(R \log R)$ time and $O(R)$ grouping/join space. Physical cost depends on indexes and the database optimizer.

## Alternatives and edge cases
- **Conditional `COUNT(DISTINCT ...)`:** Joining raw actions and counting distinct report and removal IDs per day is equivalent, but early deduplication makes the reporting unit explicit.
- **Correlated removal lookup:** An `EXISTS` subquery per reported post is correct, but without an index it can repeatedly scan `Removals` and approach $O(AM)$.
- **Duplicate reports:** Repeated rows or multiple users reporting the same post on one date count as one post.
- **Unequal daily report counts:** Average the percentages themselves; do not divide all removed posts by all reported posts globally.
- **Removal date:** A post counts as removed whenever its ID appears in `Removals`, regardless of the stored date.
- **Non-spam reports:** Rows with another `extra` value do not enter any daily percentage.
