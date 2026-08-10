## General

**Reduce many session rows to one result row per book**

The result asks questions about groups, not individual reading sessions. For each book, we need the number of sessions, the highest and lowest ratings, the number of extreme ratings, and the descriptive columns from `books`. SQL aggregation is therefore the natural optimal approach: join each session to its book, group all joined rows by `book_id`, compute every required statistic in that one grouped pass, discard groups that do not satisfy the definition, and finally sort the qualifying result rows.

The query starts with an inner `JOIN`:

`books JOIN reading_sessions USING (book_id)`

`USING (book_id)` means the rows match on their common `book_id` column and the joined result exposes that shared column once. Because this is an inner join, a book with no reading sessions produces no joined row and therefore no group. Such a book could not satisfy the minimum of five sessions anyway, so an outer join is unnecessary.

Each joined row represents one reading session together with the metadata of its book. `GROUP BY book_id` then gathers all sessions for the same book into one group. Since `book_id` is unique in `books`, a group refers to exactly one `title`, `author`, `genre`, and `pages` value. MySQL can consequently return those functionally dependent book columns while grouping by the unique book identifier.

**Compute the spread from the rating endpoints**

The rating spread is the largest rating minus the smallest rating. The expression

`MAX(session_rating) - MIN(session_rating) AS rating_spread`

does exactly that within each book group. There is no need to sort all ratings merely to find the endpoints: aggregate implementations can update a running minimum and maximum as they consume each session row.

Those same endpoints also prove that both polarities exist. The condition `MAX(session_rating) >= 4` says that at least one high rating is present. The condition `MIN(session_rating) <= 2` says that at least one low rating is present. A maximum alone would not establish the existence of a low opinion, and a minimum alone would not establish the existence of a high opinion, so both tests are necessary.

**Count extreme ratings with MySQL Boolean arithmetic**

An extreme rating is either at most two or at least four. In MySQL, a comparison used in a numeric expression evaluates to one when true and zero when false. Therefore:

- `SUM(session_rating <= 2)` counts low-rating sessions.
- `SUM(session_rating >= 4)` counts high-rating sessions.
- `COUNT(1)` counts every joined session row in the book group.

The rating scale is from one to five, and the two extreme ranges are disjoint: no rating can simultaneously be at most two and at least four. Adding the two sums therefore counts every extreme session exactly once. A neutral rating of three contributes zero to both sums.

Dividing the extreme count by `COUNT(1)` gives the polarization ratio. The `SELECT` list rounds that quotient to two decimal places and exposes it as `polarization_score`:

`ROUND((SUM(session_rating <= 2) + SUM(session_rating >= 4)) / COUNT(1), 2)`

For example, ratings `[5, 1, 4, 2, 5]` contribute three high comparisons and two low comparisons. The extreme count is five, the session count is five, and the displayed score is `1.00`. Ratings `[5, 4, 3, 2, 3]` have three extremes among five sessions and produce `0.60`.

**Filter complete groups with `HAVING`**

`WHERE` filters individual rows before aggregation, whereas all four qualification tests depend on the completed group. They therefore belong in `HAVING`:

- `COUNT(1) >= 5` enforces the minimum number of reading sessions.
- `MAX(session_rating) >= 4` requires at least one high rating.
- `MIN(session_rating) <= 2` requires at least one low rating.
- `polarization_score >= 0.6` attempts to require at least sixty percent extreme ratings.

The first three conditions exactly match their corresponding requirements. The last condition has a subtle discrepancy in the stored source: `polarization_score` is the already rounded alias from the `SELECT` list. MySQL permits that alias in `HAVING`, so the query compares the two-decimal displayed value with `0.6` rather than comparing the unrounded quotient.

This distinction matters near the threshold. Suppose a book has 42 sessions and 25 are extreme. Its raw ratio is approximately `0.595238`, which is below `0.6` and should not qualify under the stated definition. Rounded to two decimal places, however, it becomes `0.60`, so the exact stored query admits it. The intended robust condition is to repeat the unrounded expression in `HAVING`, or equivalently compare the integer counts without division:

`5 * (SUM(session_rating <= 2) + SUM(session_rating >= 4)) >= 3 * COUNT(1)`

The multiplication form expresses “at least three fifths” exactly and avoids both rounding and floating-point boundary concerns. Rounding should be used only in the selected display column. This is a genuine semantic defect in the exact source, not merely a presentation choice.

**Order only the groups that survive**

After aggregation and filtering, `ORDER BY polarization_score DESC, title DESC` places the largest displayed polarization score first. When two rows have the same rounded score, the title with the greater descending text order comes first. Notice that sorting also uses the rounded alias. Two books with different raw ratios that round to the same two-decimal value are therefore tied on the first key and ordered by title. That agrees with ordering by the returned `polarization_score` column, though it may differ from an unstated preference to order by raw ratios.

The example leaves out the second book even though all five of its ratings are high: its maximum passes, but its minimum is not at most two, so it lacks polarized opinions. The fourth and fifth books have too few sessions. Books one and three meet the count requirement, contain both extremes, and have every rating in an extreme range, giving each a displayed score of `1.00`.

**Why one grouped query is sufficient**

Every condition and output metric can be derived from a constant-sized aggregate state per book: session count, low count, high count, minimum, and maximum. No pairwise comparison between sessions is needed. As the database processes a session row, it can update those five values for that row’s `book_id`. Once all rows are consumed, the group state contains everything needed to compute the output and decide qualification.

This is why the conceptual plan is optimal with respect to reading the input. Any correct method must inspect the session ratings relevant to the result; otherwise an unseen rating could change the minimum, maximum, extreme count, or eligibility. The query inspects each joined session once during aggregation and retains only per-book summaries before sorting the qualifying books.

## Complexity detail

Let `R` be the number of rows in `reading_sessions` and `B` the number of distinct book groups produced by the join. With an index or hash lookup on `books.book_id`, associating each session with its unique book is expected `O(R)`. A hash aggregate can update the constant-sized state for each book in expected `O(1)` per session, also totaling `O(R)`. Filtering the completed groups costs `O(B)`.

If at most `B` books qualify, the final ordering costs `O(B log B)` in the worst case. This gives the manifest’s expected overall bound `O(R + B log B)`. The hash table for aggregate states and the rows awaiting the final sort require `O(B)` auxiliary working space.

SQL complexity depends on the physical plan selected by the database. If indexes are absent, the join may require building a hash table or scanning additional rows. If MySQL chooses a sort-based grouping plan rather than a hash or index-assisted aggregate, grouping can cost `O(R log R)` and use `O(R)` temporary space. The manifest bound describes the normal one-pass grouped plan followed by sorting the book-level output, not a guarantee that every database configuration chooses that plan.

The query computes several aggregates more than once textually—for example, `MAX` and `MIN` appear in both `SELECT` or `HAVING`—but a database optimizer normally maintains and reuses the group aggregates rather than rescanning the underlying sessions for each textual occurrence. The asymptotic bound therefore remains a single aggregation pass plus the result sort.

## Alternatives and edge cases

- **Pre-aggregate in a common table expression:** A CTE can first produce one row per `book_id` with `session_count`, `low_count`, `high_count`, `min_rating`, and `max_rating`, then join qualifying summaries to `books`. This makes the data flow and raw-score filter clearer, while a capable optimizer can produce essentially the same physical plan.
- **Correlated subqueries per book:** Separate subqueries for the count, minimum, maximum, and extreme count are easier to write piecemeal but may repeatedly scan `reading_sessions` for every book. One grouped aggregation exposes all required statistics together and is generally more efficient.
- **Conditional `CASE` expressions:** `SUM(CASE WHEN session_rating <= 2 THEN 1 ELSE 0 END)` is more portable across SQL dialects than summing Boolean comparisons. The stored solution intentionally uses MySQL’s numeric Boolean behavior.
- **Rounded-threshold defect:** Filtering with `polarization_score >= 0.6` compares the rounded alias. Raw ratios in `[0.595, 0.6)` can round to `0.60` and pass incorrectly. Compare the unrounded numerator and denominator—preferably by cross multiplication—then round only the displayed result.
- **Both polarities are mandatory:** A score of `1.00` does not by itself imply polarization. A book whose ratings are all five has one hundred percent extreme ratings but no low opinion, so the separate `MAX` and `MIN` conditions are essential.
- **Exactly five sessions:** Five is allowed because the requirement and the query both use `>= 5`. With five sessions, at least three must be extreme to meet a raw sixty-percent threshold, and the group must include both a high and a low rating.
- **Rating three:** A rating of three counts toward `COUNT(1)` but toward neither extreme sum. It therefore lowers the polarization score without helping either polarity condition.
- **No sessions or fewer than five sessions:** The inner join removes books with zero sessions, while `HAVING COUNT(1) >= 5` removes groups with one through four sessions. Neither category can qualify.
- **Duplicate reader names:** The unit being counted is a reading-session row, not a distinct reader. Repeated `reader_name` values still contribute separately because the requirement is phrased in sessions and the query uses `COUNT(1)`.
- **Potential `NULL` ratings:** The reference describes ratings on a one-to-five scale and does not present `NULL` as valid. If `NULL` were possible, `COUNT(1)` would count that row while comparisons, `MIN`, and `MAX` would ignore its rating, changing the denominator semantics; a production schema allowing nulls would need an explicit policy.
- **Functional dependency in `GROUP BY`:** Selecting `title`, `author`, `genre`, and `pages` while grouping only by `book_id` relies on `book_id` being unique in `books` and on MySQL recognizing that dependency. A stricter or different SQL dialect may require listing all selected metadata columns in `GROUP BY`.
- **Ties after rounding:** `ORDER BY polarization_score` sorts the returned two-decimal scores. Distinct raw ratios that round to the same value are broken by `title DESC`, not by their hidden raw ratios.
- **Descending title order:** The secondary order is deliberately `DESC`. Replacing it with the more common ascending alphabetical order would contradict the requested output ordering.
- **Division behavior:** MySQL’s `/` operator performs non-integer division here. In a dialect where integer division truncates, the numerator or denominator would need an explicit decimal cast.
