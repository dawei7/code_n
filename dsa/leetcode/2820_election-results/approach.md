## General

**Allocate each voter exactly one total vote.** A voter may have several non-null candidate rows. If that voter selected $c$ candidates, each selected candidate must receive $1/c$ of the voter's vote. A row with `candidate IS NULL` represents abstention and contributes nothing.

The query implements this rule in stages with common table expressions. Reading the stages from the innermost query outward makes the data flow easier to understand.

**Remove abstentions before counting choices.** The innermost query reads `Votes` and applies `WHERE candidate IS NOT NULL`. This removes rows that do not name a candidate. A voter who only abstained disappears from the allocation entirely, correctly contributing zero.

For each remaining row, the window expression

`COUNT(candidate) OVER (PARTITION BY voter)`

counts that voter's non-null candidate rows. Because the filter has already removed null candidates, this is exactly the number of candidates among which the one vote must be divided.

The primary key `(voter, candidate)` guarantees that the same voter cannot have a duplicate row for one candidate, so the count is also the number of distinct candidates selected by that voter.

**Assign a fraction to every selected candidate row.** The expression

`1 / (COUNT(candidate) OVER (PARTITION BY voter)) AS vote`

gives every remaining row its equal share. If a voter selected one candidate, the share is one. If the voter selected three, each of the three rows receives one third. Summing the shares inside one voter partition yields one.

In MySQL, the slash operator performs non-integer division for these numeric expressions, so a voter with multiple choices does not collapse to zero through integer truncation.

**Aggregate shares by candidate.** Common table expression `T` groups the allocated rows by candidate and computes `SUM(vote) AS tot`. After this grouping, there is one row per candidate who received at least one share, and `tot` is that candidate's complete vote total across all voters.

The shorthand `GROUP BY 1` means group by the first selected expression, which is `candidate`. It is functionally equivalent to writing `GROUP BY candidate` here.

**Rank totals while preserving ties.** Common table expression `P` applies

`RANK() OVER (ORDER BY tot DESC) AS rk`.

Descending order places the greatest total first. SQL `RANK` assigns the same rank to equal ordering values, so every candidate tied for the maximum receives rank one. A simple `LIMIT 1` would incorrectly discard tied winners, and `ROW_NUMBER` would arbitrarily separate them.

Although `DENSE_RANK` would also assign rank one to every maximum, differences between later ranks do not matter because the outer query keeps only rank one.

**Return winners in required name order.** The final query filters `WHERE rk = 1` and selects only `candidate`. `ORDER BY 1` sorts the first selected output column, candidate name, in ascending order. Ranking order was by vote total, but all retained rows have the same winning status; the final ordering fulfills the separate presentation requirement.

**A row-level walkthrough.** If Charles selects Ryan, Christine, and Kathy, each of his three rows receives $1/3$. A voter selecting only Ryan contributes one whole vote to Ryan. The group stage adds those fractions to the appropriate candidates. If Ryan and Christine obtain the same greatest `tot`, `RANK` labels both one, and the final sort displays Christine before Ryan.

**Why the query is correct.** Filtering ensures only actual candidate selections participate. Partition counting and reciprocal division distribute exactly one unit over each participating voter's choices. Grouping sums precisely those shares for each candidate. Ranking identifies all candidates whose total equals the global maximum, and the last filter returns exactly them. The final sort changes only display order, not membership.

**The query does not count abstainers as candidates.** A null value is removed before grouping, so there can be no null candidate result and no division by zero. Voters who chose at least one real candidate have a positive partition count.

**Precision considerations.** Fractions such as one third cannot be represented with a finite decimal expansion. MySQL evaluates division and aggregation with its numeric type rules and sufficient precision for the judge data. Conceptually, the algorithm compares exact rational vote totals. A production election system needing formal exactness could aggregate rational contributions with a deliberate fixed precision or common denominator policy.

## Complexity detail

Let $R$ be the number of rows in `Votes` and let $C$ be the number of candidates receiving votes. The database must scan the relevant rows, partition them by voter for the window count, group them by candidate, rank candidate totals, and finally sort tied winners by name.

A typical execution uses sorting or indexed grouping for the window and aggregate stages, leading to an upper-bound description of $O(R\log R)$ time. Ranking and final candidate ordering add at most $O(C\log C)$, which is dominated because $C\le R$. Exact performance depends on MySQL's optimizer, indexes, memory limits, and whether stages use hash aggregation or external sorting.

Intermediate rows for the filtered vote shares and grouped candidate totals can require $O(R)$ working storage in a materialized or sort-based execution. The manifest's $O(R)$ space is a reasonable logical upper bound, but SQL engines may spill temporary data to disk rather than retaining it all in memory.

The output contains one row per tied winner and is ordered by candidate.

## Alternatives and edge cases

- **Pre-aggregate voter counts and join:** Compute each participating voter's candidate count in one CTE, join it back to non-null vote rows, then aggregate shares. This expresses the same allocation without a window function but may require an explicit join.
- **Compare with a maximum subquery:** After candidate totals are computed, filter where `tot = (SELECT MAX(tot) ...)`. This also retains ties; `RANK` makes the intent compact.
- **`ROW_NUMBER`:** This is unsuitable because it would select only one arbitrary candidate when totals tie.
- **`LIMIT 1`:** Even with ordering by total, it violates the requirement to return all co-winners.
- **Voter chooses one candidate:** The partition count is one, so that candidate receives a full vote.
- **Voter chooses several candidates:** Every row gets the same reciprocal share, and their shares sum to one.
- **Voter abstains:** The null row is filtered out and contributes zero.
- **Candidate-name ordering:** The final `ORDER BY 1` is ascending by the sole selected column, independent of ranking order.
- **Primary-key guarantee:** Duplicate selections of the same candidate by one voter cannot inflate either the denominator or candidate total.
- **Fractional equality:** The logical comparison is between rational totals; database numeric precision should be chosen carefully outside the challenge environment.
- **No non-null votes outside expected data:** `T` and `P` would be empty and the result would have no winner. The problem context normally supplies participating votes.
