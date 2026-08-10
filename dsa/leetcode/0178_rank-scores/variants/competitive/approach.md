## General

**Identify two separate intended alternatives**

The competitive file contains two different ranking queries. The first tries
to assign row numbers to distinct descending score levels with a MySQL user
variable, then joins those ranks back to all `Scores` rows. The second computes
rank with a correlated distinct-count subquery.

Either idea can be discussed independently. As stored, however, the statements
are adjacent without a semicolon separating them. SQL parses the second
`SELECT` as unexpected continuation text after the first query, so the file is
not a valid single statement.

A challenge submission must choose one complete alternative and remove the
other executable query.

**First intended alternative: number distinct levels**

Its deepest derived query selects distinct scores in descending order and
initializes `@curRow` to zero. The next layer evaluates:

`@curRow := @curRow + 1`.

The intent is to number the distinct score values as one, two, three, and so on.
The outer `LEFT JOIN` matches those numbered levels back to the original
`Scores` table by equal score, restoring one output row per game and giving
ties the same number.

Finally, it orders by score descending.

**Why the first alternative is fragile**

MySQL user-variable assignment and expression evaluation order have historically
been unsafe to rely on for deterministic ranking. An `ORDER BY` inside a
derived table also does not always guarantee the order in which an outer
variable assignment is evaluated after optimizer transformations.

Modern MySQL deprecates assigning user variables within expressions for this
kind of logic. `DENSE_RANK()` is the direct, deterministic replacement.

The `LEFT JOIN` also refers to `Ranks.Score` in the projection. If the derived
rank relation were unexpectedly missing a match, it would output null for the
score even though the preserved source row has a value; projecting
`Scores.Score` would express preservation more directly. Under intended
complete ranking, every distinct score does match.

**Second intended alternative: count greater levels**

The second query is:

`1 + COUNT(DISTINCT score values greater than the current score)`.

For each outer row `a`, the correlated subquery examines table alias `b` and
counts distinct `b.Score` values satisfying `b.Score > a.Score`. Adding one
turns the count into a descending dense rank.

The highest score has zero greater levels and receives rank one. Equal scores
observe the same set of greater values and receive the same rank. The next
lower distinct score has exactly one additional greater level, so ranks do not
skip.

This alternative ends with `ORDER BY Score DESC`, satisfying the required
result order.

**Trace the correlated calculation**

For score 4.00, there is no greater distinct score, so both 4.00 rows receive
one.

For 3.85, only 4.00 is greater, so the result is two. For 3.65, the greater
distinct levels are 4.00 and 3.85, giving three. Repeated 3.65 rows repeat the
same correlated result and remain tied.

For 3.50, three distinct levels are greater, yielding rank four.

**Why `DISTINCT` is essential**

Without `DISTINCT`, both rows at 4.00 would be counted separately above 3.85,
incorrectly producing rank three. Dense ranking counts value levels, not game
rows.

The strict operator `>` is also essential. Using `>=` and then adding one
would count the candidate's own level and shift every rank too high.

**Material exact-file defects**

There is no semicolon after the first query before the second `SELECT`, so the
file is syntactically invalid as a combined script. Even with a separator, a
single-result judge may reject multiple statements or receive two result sets.

The first alternative's user-variable behavior is additionally plan-dependent.
The second correlated query is the more logically stable choice if window
functions are unavailable, but it should be the only submitted statement.

**Null score behavior**

For a null outer score, `b.Score > a.Score` is unknown for every row, so the
count is zero and the second query would assign rank one. That is probably not
the intended treatment. The challenge data conventionally contains numeric
scores; nullable production data should be filtered or assigned an explicit
policy.

## Complexity detail

The correlated second query can scan $n$ rows for each of $n$ outer rows,
giving $O(n^2)$ naive time and up to $O(n)$ state for distinct aggregation.
This matches the source comment but contradicts the manifest's
$O(n\log n)$ time.

The first intended alternative sorts distinct levels and joins them back, with
a plausible $O(n\log n)$ plan and $O(n)$ working space, but its variable
evaluation is unreliable. Indexes and optimizer transformations can change
physical costs.

## Alternatives and edge cases

- **`DENSE_RANK()` window function:** The clean modern solution; add an outer ordering clause for guaranteed result order.
- **Submit only the correlated query:** Deterministic ranking semantics on non-null values, but potentially quadratic.
- **Self-join with distinct count:** Avoids correlation syntax but can generate a quadratic intermediate relation.
- **All ties:** Every row should receive rank one.
- **Multiple tie groups:** `DISTINCT` greater values keeps ranks consecutive.
- **Strict comparison:** Greater-than, not greater-than-or-equal, defines levels above the candidate.
- **Duplicate output rows:** They are required because every source game row must remain.
- **Two statements:** The exact file must be reduced to one executable query.
- **User variables:** Assignment order should not be used as a ranking guarantee.
- **Null score:** Needs an explicit policy if nullable values are allowed.
