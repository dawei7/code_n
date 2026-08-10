## General

**What the query is trying to measure.** For each user, the reference task compares two quantities within February 2024:

- the user's maximum number of posts in any inclusive seven-day period;
- the user's average weekly post count, defined as the February total divided by four.

A user is bursty when the maximum seven-day count is at least twice that average. The exact SQL source organizes this work into two common table expressions, `P` and `T`, and a final grouped query.

**How `P` forms seven-day windows.** `Posts p1 JOIN Posts p2` is a self-join. A row from `p1` acts as a window anchor. It matches rows from `p2` when they belong to the same user and satisfy:

`p2.post_date BETWEEN p1.post_date AND DATE_ADD(p1.post_date, INTERVAL 6 DAY)`.

`BETWEEN` is inclusive at both ends, so the interval contains the anchor date plus the next six dates: exactly seven calendar days. Grouping by `p1.user_id, p1.post_id` makes one group per anchor post. `COUNT(1)` is the number of that user's posts inside the anchored window, stored as `cnt`.

Anchoring only at a post date is enough to find a maximum for a correctly bounded data set. If a nonempty best seven-day window begins on a date with no post, slide its left boundary right until it reaches the earliest post it contains. No contained post is lost, and the resulting seven-day interval remains at least as good. Therefore, it is unnecessary to generate every calendar date.

**How `T` computes the baseline.** The second CTE filters:

`post_date BETWEEN '2024-02-01' AND '2024-02-28'`.

It groups February posts by user and calculates `COUNT(1) / 4`. The alias `avg_weekly_posts` represents the problem's prescribed four-week average. This is not the same as dividing by the exact number of days and multiplying by seven; the source follows the stated four-week definition.

The literal upper endpoint is February 28. Although 2024 is a leap year, the local reference explicitly says to analyze only February 1 through February 28 and to treat the interval as exactly four weeks. The predicate therefore implements the stated baseline boundary correctly; February 29 is intentionally outside this problem's analysis.

**Combining the two measures.** `P JOIN T USING(user_id)` attaches each user's February average to every window count produced by `P`. The final `GROUP BY 1` groups by `user_id`. Within that group, `MAX(cnt)` becomes `max_7day_posts`. The `HAVING` clause retains users satisfying:

$$
\texttt{max\_7day\_posts}
\ge
2\cdot\texttt{avg\_weekly\_posts}.
$$

`HAVING` is the right logical stage because it filters a value computed by aggregation. Finally, `ORDER BY 1` returns user IDs in ascending order.

**A material correctness defect in the exact source.** The first CTE contains no February predicate at all. Both `p1` and `p2` can be posts from any date in `Posts`. As a result, `MAX(cnt)` may describe a January, March, or entirely unrelated seven-day burst, while `avg_weekly_posts` still describes February. It can also count a window anchored late in February that extends into March. This mixes incompatible time scopes and can return a user who was not bursty during the requested February interval.

For example, suppose a user makes four February posts, giving an average of one per week, and then makes ten posts during one week in March. `T` produces `1`, while the unrestricted `P` can produce `10`. The final condition sees `10 >= 2` and returns the user even though the March activity should not participate.

This is not merely a performance preference or a manifest wording issue. It is a genuine semantic defect visible by comparing the exact query with the local description. A correct version must restrict the window evidence to the requested reporting interval. The precise boundary rule must also decide whether a seven-day interval may extend beyond February or must be clipped to it; the source currently imposes neither restriction.

Apart from the unrestricted `P` CTE, the relational mechanics are coherent: the self-join counts an anchored seven-day window, the second CTE calculates the four-week baseline over the exact stated dates, and the outer query takes a maximum and applies the threshold.

## Complexity detail

Let $P$ be the total number of rows in `Posts`, $U$ the number of users, and $M$ the number of matching self-join pairs. Constructing `P` requires work proportional to the join plan. Without a useful composite index, comparing same-user date candidates can approach $O(P^2)$ time in the worst case. With an index such as `(user_id, post_date)`, the engine can range-scan matching dates, giving a more output-sensitive cost near $O(P\log P+M)$.

The `T` scan and grouping are typically $O(P)$ expected with hash aggregation or $O(P\log P)$ with sorting. The final join and group depend on the number of rows produced by `P`, which is at most $P$ groups but was formed from $M$ matching pairs.

Working space can be $O(P+U)$ for materialized CTE results and aggregates, though the database may stream, index, or spill them. The local manifest's $O(n\log n)$ description does not capture the exact self-join's possible quadratic matching work. SQL performance remains plan and index dependent.

## Alternatives and edge cases

- **Correctly scoped self-join:** Add explicit reporting-period conditions for the anchor and counted posts. This fixes the exact source's major date-scope defect.
- **Sliding window per user:** Sorting posts by `(user_id, post_date)` and maintaining two date pointers can find maximum seven-day counts without enumerating every matching pair.
- **Window-function formulation:** Some SQL dialects can combine ordered analytics with date-range frames, although support for interval-based frames varies.
- **Index support:** A composite index on `(user_id, post_date)` materially improves the same-user date-range join.
- **Windows anchored on empty dates:** They need not be generated because any nonempty optimum can move its left boundary to its earliest included post.
- **Inclusive seven days:** `BETWEEN anchor AND anchor + 6 days` contains seven calendar dates, not six.
- **Multiple posts on one date:** Every row is counted; the measure is posts, not distinct active days.
- **February 29:** The local note deliberately excludes it by defining the analysis as February 1 through February 28, despite 2024 being a leap year.
- **Posts outside February:** The exact `P` CTE includes them, which is the principal correctness defect.
- **Window crossing into March:** The exact join includes such `p2` rows because it has no upper reporting boundary.
- **Users without February posts:** They do not appear in `T`, so the inner join removes them even if `P` finds activity elsewhere.
- **Zero average:** A user present in `T` has at least one February post, so its average is positive.
- **Threshold equality:** `>=` correctly includes a maximum exactly twice the average.
- **Functional dependency in grouping:** `avg_weekly_posts` is selected without being explicitly grouped or aggregated. Since `T` has one row per user it is functionally determined, but strict SQL modes or other engines may demand an aggregate or an added group key.
- **Result order:** `ORDER BY 1` sorts by `user_id` ascending, matching the expected deterministic output.
- **Not the manifest algorithm:** The checked-in query is a self-join, not a true linear sliding-window implementation, so its complexity must be assessed from the SQL actually present.
