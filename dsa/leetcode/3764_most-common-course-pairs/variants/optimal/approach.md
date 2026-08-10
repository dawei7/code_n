## General

**Build the result in three relational stages**

The query uses two common table expressions and one final aggregation:

1. `top_students` decides which users qualify.
2. `course_pairs` orders each qualifying user's history and attaches the next course to every current course.
3. The outer query removes rows with no next course, counts equal transitions, and applies the required output order.

Keeping these stages separate is useful because each one answers a different question: who is eligible, what each adjacency is, and how often each adjacency occurs.

**Filter users using their complete histories**

The first CTE groups `course_completions` by `user_id`. Each group contains all completion rows for one user. Its `HAVING` clause requires both

`COUNT(1) >= 5`

and

`AVG(course_rating) >= 4`.

`WHERE` cannot perform this group-level test because the decision depends on multiple rows. `HAVING` is evaluated after grouping and aggregation, which is exactly when the course count and average rating exist.

Both comparisons are inclusive. A user with exactly five completion rows qualifies, provided the average across all five is at least four. A user with more courses is tested across the entire history; the query does not select only the five best ratings. Likewise, a user with a 4.0 average qualifies, while a 3.999 average does not.

The CTE returns only `user_id`. This makes it a compact eligibility relation that can be joined back to the original rows.

**Restrict the sequence construction to qualifying users**

`top_students JOIN course_completions USING (user_id)` keeps all completion rows belonging to qualifying users and discards every row from other users.

The join happens before course pairs are counted. Therefore an ineligible user's transitions cannot accidentally contribute to the frequency and then be filtered afterward. Every row reaching the window function is already known to belong to a top performer.

**Use `LEAD` to identify the immediate next course**

The window expression is

`LEAD(course_name) OVER (PARTITION BY user_id ORDER BY completion_date)`.

`PARTITION BY user_id` creates a separate ordered history for each user. This boundary is essential: without it, the last course of one user could pair with the first course of another.

Inside each partition, `ORDER BY completion_date` places completions in chronological order. On each row, `LEAD(course_name)` returns the course name from the following row in that order. The current row's `course_name` becomes `first_course`, and the returned name becomes `second_course`.

This creates only consecutive pairs. If a user's order is A, B, C, the window produces A to B and B to C. It does not produce A to C because C is two rows ahead rather than the immediate `LEAD` row.

The final completion in each user partition has no following row, so its `second_course` is `NULL`. A user with $m$ completions consequently produces $m-1$ real adjacent transitions.

**Remove incomplete pairs before aggregation**

The outer `WHERE second_course IS NOT NULL` removes every partition's final row. This is necessary before grouping: a missing next course is not a transition and must not appear as a result pair.

The remaining rows each represent one occurrence of a valid adjacency in one qualifying history. Grouping by output positions `1, 2` means grouping by `first_course` and `second_course`. `COUNT(1)` then counts every occurrence in each group and names that count `transition_count`.

Course names, rather than course IDs, define the output pair because those are the selected grouping columns. If different course IDs share a name, their transitions are combined by name. If the same named transition occurs twice in one user's history, both rows are counted; the query does not deduplicate per user.

**Apply all three ordering rules**

`ORDER BY 3 DESC, 1, 2` uses output-column positions:

- column 3, `transition_count`, descending;
- column 1, `first_course`, ascending;
- column 2, `second_course`, ascending.

The two name columns provide deterministic tie-breaking between pairs with equal frequency. Positional references are compact, although spelling out the aliases would often be easier to maintain.

**Trace the example at the row level**

Users 1 and 2 pass the first CTE. User 1's six ordered rows create five non-null transitions, while user 2's five rows create four. The transition React Basics to Node.js appears once in each partition, so those two rows collapse into one group with count two. Node.js to Docker behaves the same way.

Transitions appearing in only one history remain at count one. The two count-two rows sort first; alphabetical ordering of their first-course names places Node.js before React Basics. The count-one rows then follow in their required lexical order.

**Why the result is exact**

Every counted row is sound: it belongs to a user who passed both aggregate conditions, and `LEAD` obtained its second course from the immediately following chronological row in the same user's partition.

Every required transition is complete: each qualifying user's ordered history has one current row for every course, and `LEAD` exposes the successor for every row except the last. The outer grouping counts all equal course-name pairs without dropping occurrences.

Thus the query neither crosses users nor skips intermediate courses, and its final sort matches the contract.

## Complexity detail

Let $R$ be the number of completion rows and $P$ the number of distinct output course-name pairs.

The exact physical cost depends on the MySQL optimizer, indexes, and chosen aggregation algorithms. Grouping by user and joining the qualifying IDs can be implemented with hashing or indexed access. The window function must establish `completion_date` order within user partitions; in a conservative comparison-based analysis, this contributes $O(R\log R)$ time across the qualifying rows.

Grouping the produced transitions is linear expected work with hash aggregation or sorting work under a sort-based plan. Sorting the $P$ final groups by count and two names costs $O(P\log P)$. The manifest's summary bound of $O(R\log R + P\log P)$ is therefore a reasonable high-level model, not a guarantee about every database execution plan.

Materializing groups, ordered partitions, transitions, and final pair counts may require $O(R+P)$ working space. Database engines may spill sorts or hashes to disk when memory is limited; asymptotic logical storage remains of that order.

## Alternatives and edge cases

- **Self-join on the next date:** Joining each row to the minimum later date can express adjacency, but it is more cumbersome and may perform repeated searches. `LEAD` states the sequence relation directly.
- **Correlated subquery for the next course:** This can also find a successor but risks one lookup per row and complicated tie handling.
- **Filter ratings before grouping:** That would change both the course count and average. Qualification must use every completion row in the user's history.
- **Use `WHERE COUNT(...)`:** Aggregate conditions belong in `HAVING` because they are defined only after grouping.
- **Omit `PARTITION BY user_id`:** This could create false cross-user pairs at partition boundaries.
- **Use a later course instead of `LEAD`:** The contract counts adjacent transitions only; skipping an intervening completion invents a pair.
- **User with exactly five courses and average exactly four:** Both inclusive conditions pass.
- **Qualifying user with one final course row:** Its `LEAD` value is `NULL` and that incomplete pair is discarded.
- **Repeated named transition within one user:** Every occurrence is counted, as required by the row-level `COUNT(1)`.
- **Different IDs with the same course name:** The source groups by names, so those IDs contribute to the same displayed transition.
- **Tied completion dates:** The exact window order contains no secondary key. If one user has multiple courses on the same date, their relative order is not guaranteed by this query; the data needs an unambiguous chronology or the source would need an authorized tie-break rule.
- **No qualifying users:** `course_pairs` is empty and the query returns an empty result table.
- **A qualifying user's first course:** It can be `first_course` but never appears as a `second_course` unless another completion precedes it.
- **A qualifying user's last course:** It may be `second_course` for the prior row, while its own generated row is removed because there is no successor.
- **Final tie ordering:** Omitting either name key would leave equal-frequency rows without the full specified order.
