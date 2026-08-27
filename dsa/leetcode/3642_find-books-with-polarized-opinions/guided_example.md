# Guided Example: Find Books with Polarized Opinions

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"books": [{"book_id": 1, "title": "The Great Gatsby", "author": "F. Scott", "genre": "Fiction", "pages": 180}, {"book_id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction", "pages": 281}, {"book_id": 3, "title": "1984", "author": "George Orwell", "genre": "Dystopian", "pages": 328}, {"book_id": 4, "title": "Pride and Prejudice", "author": "Jane Austen", "genre": "Romance", "pages": 432}, {"book_id": 5, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "genre": "Fiction", "pages": 277}], "reading_sessions": [{"session_id": 1, "book_id": 1, "reader_name": "Reader 1", "pages_read": 12, "session_rating": 5}, {"session_id": 2, "book_id": 1, "reader_name": "Reader 2", "pages_read": 13, "session_rating": 1}, {"session_id": 3, "book_id": 1, "reader_name": "Reader 3", "pages_read": 14, "session_rating": 4}, {"session_id": 4, "book_id": 1, "reader_name": "Reader 4", "pages_read": 15, "session_rating": 2}, {"session_id": 5, "book_id": 1, "reader_name": "Reader 5", "pages_read": 16, "session_rating": 5}, {"session_id": 6, "book_id": 2, "reader_name": "Reader 6", "pages_read": 17, "session_rating": 4}, {"session_id": 7, "book_id": 2, "reader_name": "Reader 7", "pages_read": 18, "session_rating": 4}, {"session_id": 8, "book_id": 2, "reader_name": "Reader 8", "pages_read": 19, "session_rating": 5}, {"session_id": 9, "book_id": 2, "reader_name": "Reader 9", "pages_read": 20, "session_rating": 4}, {"session_id": 10, "book_id": 2, "reader_name": "Reader 10", "pages_read": 21, "session_rating": 4}, {"session_id": 11, "book_id": 3, "reader_name": "Reader 11", "pages_read": 22, "session_rating": 2}, {"session_id": 12, "book_id": 3, "reader_name": "Reader 12", "pages_read": 23, "session_rating": 1}, {"session_id": 13, "book_id": 3, "reader_name": "Reader 13", "pages_read": 24, "session_rating": 2}, {"session_id": 14, "book_id": 3, "reader_name": "Reader 14", "pages_read": 25, "session_rating": 1}, {"session_id": 15, "book_id": 3, "reader_name": "Reader 15", "pages_read": 26, "session_rating": 4}, {"session_id": 16, "book_id": 3, "reader_name": "Reader 16", "pages_read": 10, "session_rating": 5}, {"session_id": 17, "book_id": 4, "reader_name": "Reader 17", "pages_read": 11, "session_rating": 3}, {"session_id": 18, "book_id": 4, "reader_name": "Reader 18", "pages_read": 12, "session_rating": 3}, {"session_id": 19, "book_id": 5, "reader_name": "Reader 19", "pages_read": 13, "session_rating": 1}, {"session_id": 20, "book_id": 5, "reader_name": "Reader 20", "pages_read": 14, "session_rating": 2}]}}`
- **Required output:** `{"columns": ["book_id", "title", "author", "genre", "pages", "rating_spread", "polarization_score"], "rows": [[1, "The Great Gatsby", "F. Scott", "Fiction", 180, 4, 1], [3, "1984", "George Orwell", "Dystopian", 328, 4, 1]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `books`

The objective is to compute `{"columns": ["book_id", "title", "author", "genre", "pages", "rating_spread", "polarization_score"], "rows": [[1, "The Great Gatsby", "F. Scott", "Fiction", 180, 4, 1], [3, "1984", "George Orwell", "Dystopian", 328, 4, 1]]}` from `{"tables": {"books": [{"book_id": 1, "title": "The Great Gatsby", "author": "F. Scott", "genre": "Fiction", "pages": 180}, {"book_id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction", "pages": 281}, {"book_id": 3, "title": "1984", "author": "George Orwell", "genre": "Dystopian", "pages": 328}, {"book_id": 4, "title": "Pride and Prejudice", "author": "Jane Austen", "genre": "Romance", "pages": 432}, {"book_id": 5, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "genre": "Fiction", "pages": 277}], "reading_sessions": [{"session_id": 1, "book_id": 1, "reader_name": "Reader 1", "pages_read": 12, "session_rating": 5}, {"session_id": 2, "book_id": 1, "reader_name": "Reader 2", "pages_read": 13, "session_rating": 1}, {"session_id": 3, "book_id": 1, "reader_name": "Reader 3", "pages_read": 14, "session_rating": 4}, {"session_id": 4, "book_id": 1, "reader_name": "Reader 4", "pages_read": 15, "session_rating": 2}, {"session_id": 5, "book_id": 1, "reader_name": "Reader 5", "pages_read": 16, "session_rating": 5}, {"session_id": 6, "book_id": 2, "reader_name": "Reader 6", "pages_read": 17, "session_rating": 4}, {"session_id": 7, "book_id": 2, "reader_name": "Reader 7", "pages_read": 18, "session_rating": 4}, {"session_id": 8, "book_id": 2, "reader_name": "Reader 8", "pages_read": 19, "session_rating": 5}, {"session_id": 9, "book_id": 2, "reader_name": "Reader 9", "pages_read": 20, "session_rating": 4}, {"session_id": 10, "book_id": 2, "reader_name": "Reader 10", "pages_read": 21, "session_rating": 4}, {"session_id": 11, "book_id": 3, "reader_name": "Reader 11", "pages_read": 22, "session_rating": 2}, {"session_id": 12, "book_id": 3, "reader_name": "Reader 12", "pages_read": 23, "session_rating": 1}, {"session_id": 13, "book_id": 3, "reader_name": "Reader 13", "pages_read": 24, "session_rating": 2}, {"session_id": 14, "book_id": 3, "reader_name": "Reader 14", "pages_read": 25, "session_rating": 1}, {"session_id": 15, "book_id": 3, "reader_name": "Reader 15", "pages_read": 26, "session_rating": 4}, {"session_id": 16, "book_id": 3, "reader_name": "Reader 16", "pages_read": 10, "session_rating": 5}, {"session_id": 17, "book_id": 4, "reader_name": "Reader 17", "pages_read": 11, "session_rating": 3}, {"session_id": 18, "book_id": 4, "reader_name": "Reader 18", "pages_read": 12, "session_rating": 3}, {"session_id": 19, "book_id": 5, "reader_name": "Reader 19", "pages_read": 13, "session_rating": 1}, {"session_id": 20, "book_id": 5, "reader_name": "Reader 20", "pages_read": 14, "session_rating": 2}]}}` while avoiding redundant calculations and unnecessary overhead.

A naive or brute-force exploration risks evaluating infeasible states or repeating subproblem computations. The optimal method establishes a clear invariant that advances deterministically toward the goal.

---

## 2. Conceptual Foundation & Invariants

We maintain the core conceptual parameters and state variables:

| State Parameter | Role & Purpose | Initial State |
|---|---|---|
| Primary State | Tracks active elements, frontier indices, or DP table cells | Initialized at boundary |
| Accumulator | Preserves confirmed optimal sub-answers or counts | Empty / Neutral |

> **Invariant.** At every processing step, all previously evaluated subproblems strictly satisfy the problem constraints, and no viable candidate solution has been omitted.

---

## 3. Step-by-Step Worked Execution

### Step 1: Reduce many session rows to one result row per book

The result asks questions about groups, not individual reading sessions. For each book, we need the number of sessions, the highest and lowest ratings, the number of extreme ratings, and the descriptive columns from `books`. SQL aggregation is therefore the natural optimal approach: join each session to its book, group all joined rows by `book_id`, compute every required statistic in that one grouped pass, discard groups that do not satisfy the definition, and finally sort the qualifying result rows.

The query starts with an inner `JOIN`:

`books JOIN reading_sessions USING (book_id)`

`USING (book_id)` means the rows match on their common `book_id` column and the joined result exposes that shared column once. Because this is an inner join, a book with no reading sessions produces no joined row and therefore no group. Such a book could not satisfy the minimum of five sessions anyway, so an outer join is unnecessary.

Each joined row represents one reading session together with the metadata of its book. `GROUP BY book_id` then gathers all sessions for the same book into one group. Since `book_id` is unique in `books`, a group refers to exactly one `title`, `author`, `genre`, and `pages` value. MySQL can consequently return those functionally dependent book columns while grouping by the unique book identifier.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"books": [{"book_id": 1, "title": "The Great Gatsby", "author": "F. Scott", "genre": "Fiction", "pages": 180}, {"book_id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction", "pages": 281}, {"book_id": 3, "title": "1984", "author": "George Orwell", "genre": "Dystopian", "pages": 328}, {"book_id": 4, "title": "Pride and Prejudice", "author": "Jane Austen", "genre": "Romance", "pages": 432}, {"book_id": 5, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "genre": "Fiction", "pages": 277}], "reading_sessions": [{"session_id": 1, "book_id": 1, "reader_name": "Reader 1", "pages_read": 12, "session_rating": 5}, {"session_id": 2, "book_id": 1, "reader_name": "Reader 2", "pages_read": 13, "session_rating": 1}, {"session_id": 3, "book_id": 1, "reader_name": "Reader 3", "pages_read": 14, "session_rating": 4}, {"session_id": 4, "book_id": 1, "reader_name": "Reader 4", "pages_read": 15, "session_rating": 2}, {"session_id": 5, "book_id": 1, "reader_name": "Reader 5", "pages_read": 16, "session_rating": 5}, {"session_id": 6, "book_id": 2, "reader_name": "Reader 6", "pages_read": 17, "session_rating": 4}, {"session_id": 7, "book_id": 2, "reader_name": "Reader 7", "pages_read": 18, "session_rating": 4}, {"session_id": 8, "book_id": 2, "reader_name": "Reader 8", "pages_read": 19, "session_rating": 5}, {"session_id": 9, "book_id": 2, "reader_name": "Reader 9", "pages_read": 20, "session_rating": 4}, {"session_id": 10, "book_id": 2, "reader_name": "Reader 10", "pages_read": 21, "session_rating": 4}, {"session_id": 11, "book_id": 3, "reader_name": "Reader 11", "pages_read": 22, "session_rating": 2}, {"session_id": 12, "book_id": 3, "reader_name": "Reader 12", "pages_read": 23, "session_rating": 1}, {"session_id": 13, "book_id": 3, "reader_name": "Reader 13", "pages_read": 24, "session_rating": 2}, {"session_id": 14, "book_id": 3, "reader_name": "Reader 14", "pages_read": 25, "session_rating": 1}, {"session_id": 15, "book_id": 3, "reader_name": "Reader 15", "pages_read": 26, "session_rating": 4}, {"session_id": 16, "book_id": 3, "reader_name": "Reader 16", "pages_read": 10, "session_rating": 5}, {"session_id": 17, "book_id": 4, "reader_name": "Reader 17", "pages_read": 11, "session_rating": 3}, {"session_id": 18, "book_id": 4, "reader_name": "Reader 18", "pages_read": 12, "session_rating": 3}, {"session_id": 19, "book_id": 5, "reader_name": "Reader 19", "pages_read": 13, "session_rating": 1}, {"session_id": 20, "book_id": 5, "reader_name": "Reader 20", "pages_read": 14, "session_rating": 2}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Compute the spread from the rating endpoints

The rating spread is the largest rating minus the smallest rating. The expression

`MAX(session_rating) - MIN(session_rating) AS rating_spread`

does exactly that within each book group. There is no need to sort all ratings merely to find the endpoints: aggregate implementations can update a running minimum and maximum as they consume each session row.

Those same endpoints also prove that both polarities exist. The condition `MAX(session_rating) >= 4` says that at least one high rating is present. The condition `MIN(session_rating) <= 2` says that at least one low rating is present. A maximum alone would not establish the existence of a low opinion, and a minimum alone would not establish the existence of a high opinion, so both tests are necessary.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The rating spread is the largest rating minus the smallest r... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count extreme ratings with MySQL Boolean arithmetic

An extreme rating is either at most two or at least four. In MySQL, a comparison used in a numeric expression evaluates to one when true and zero when false. Therefore:

- `SUM(session_rating <= 2)` counts low-rating sessions.
- `SUM(session_rating >= 4)` counts high-rating sessions.
- `COUNT(1)` counts every joined session row in the book group.

The rating scale is from one to five, and the two extreme ranges are disjoint: no rating can simultaneously be at most two and at least four. Adding the two sums therefore counts every extreme session exactly once. A neutral rating of three contributes zero to both sums.

Dividing the extreme count by `COUNT(1)` gives the polarization ratio. The `SELECT` list rounds that quotient to two decimal places and exposes it as `polarization_score`:

`ROUND((SUM(session_rating <= 2) + SUM(session_rating >= 4)) / COUNT(1), 2)`

For example, ratings `[5, 1, 4, 2, 5]` contribute three high comparisons and two low comparisons. The extreme count is five, the session count is five, and the displayed score is `1.00`. Ratings `[5, 4, 3, 2, 3]` have three extremes among five sessions and produce `0.60`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["book_id", "title", "author", "genre", "pages", "rating_spread", "polarization_score"], "rows": [[1, "The Great Gatsby", "F. Scott", "Fiction", 180, 4, 1], [3, "1984", "George Orwell", "Dystopian", 328, 4, 1]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"books": [{"book_id": 1, "title": "The Great Gatsby", "author": "F. Scott", "genre": "Fiction", "pages": 180}, {"book_id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction", "pages": 281}, {"book_id": 3, "title": "1984", "author": "George Orwell", "genre": "Dystopian", "pages": 328}, {"book_id": 4, "title": "Pride and Prejudice", "author": "Jane Austen", "genre": "Romance", "pages": 432}, {"book_id": 5, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "genre": "Fiction", "pages": 277}], "reading_sessions": [{"session_id": 1, "book_id": 1, "reader_name": "Reader 1", "pages_read": 12, "session_rating": 5}, {"session_id": 2, "book_id": 1, "reader_name": "Reader 2", "pages_read": 13, "session_rating": 1}, {"session_id": 3, "book_id": 1, "reader_name": "Reader 3", "pages_read": 14, "session_rating": 4}, {"session_id": 4, "book_id": 1, "reader_name": "Reader 4", "pages_read": 15, "session_rating": 2}, {"session_id": 5, "book_id": 1, "reader_name": "Reader 5", "pages_read": 16, "session_rating": 5}, {"session_id": 6, "book_id": 2, "reader_name": "Reader 6", "pages_read": 17, "session_rating": 4}, {"session_id": 7, "book_id": 2, "reader_name": "Reader 7", "pages_read": 18, "session_rating": 4}, {"session_id": 8, "book_id": 2, "reader_name": "Reader 8", "pages_read": 19, "session_rating": 5}, {"session_id": 9, "book_id": 2, "reader_name": "Reader 9", "pages_read": 20, "session_rating": 4}, {"session_id": 10, "book_id": 2, "reader_name": "Reader 10", "pages_read": 21, "session_rating": 4}, {"session_id": 11, "book_id": 3, "reader_name": "Reader 11", "pages_read": 22, "session_rating": 2}, {"session_id": 12, "book_id": 3, "reader_name": "Reader 12", "pages_read": 23, "session_rating": 1}, {"session_id": 13, "book_id": 3, "reader_name": "Reader 13", "pages_read": 24, "session_rating": 2}, {"session_id": 14, "book_id": 3, "reader_name": "Reader 14", "pages_read": 25, "session_rating": 1}, {"session_id": 15, "book_id": 3, "reader_name": "Reader 15", "pages_read": 26, "session_rating": 4}, {"session_id": 16, "book_id": 3, "reader_name": "Reader 16", "pages_read": 10, "session_rating": 5}, {"session_id": 17, "book_id": 4, "reader_name": "Reader 17", "pages_read": 11, "session_rating": 3}, {"session_id": 18, "book_id": 4, "reader_name": "Reader 18", "pages_read": 12, "session_rating": 3}, {"session_id": 19, "book_id": 5, "reader_name": "Reader 19", "pages_read": 13, "session_rating": 1}, {"session_id": 20, "book_id": 5, "reader_name": "Reader 20", "pages_read": 14, "session_rating": 2}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["book_id", "title", "author", "genre", "pages", "rating_spread", "polarization_score"], "rows": [[1, "The Great Gatsby", "F. Scott", "Fiction", 180, 4, 1], [3, "1984", "George Orwell", "Dystopian", 328, 4, 1]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Pre-aggregate in a common table expression:** :** - **Pre-aggregate in a common table expression:** A CTE can first produce one row per `book_id` with `session_count`, `low_count`, `high_count`, `min_rating`, and `max_rating`, then join qualifying summaries to `books`. This makes the data flow and raw-score filter clearer, while a capable optimizer can produce essentially the same physical plan.
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
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(R + B log B)$. Let `R` be the number of rows in `reading_sessions` and `B` the number of distinct book groups produced by the join. With an index or hash lookup on `books.book_id`, associating each session with its unique book is expected `O(R)`. A hash aggregate can update the constant-sized state for each book in expected `O(1)` per session, also totaling `O(R)`. Filtering the completed groups costs `O(B)`.
- **Auxiliary Space Complexity:** $O(B)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
