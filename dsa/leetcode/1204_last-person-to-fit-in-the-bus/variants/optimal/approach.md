## General

Whether a person can board depends on the cumulative weight of everyone from turn one through that person’s turn. The query computes that prefix sum for every candidate person with a self-join, filters candidates whose prefix is at most 1000, and chooses the feasible candidate with the greatest turn.

**Create every candidate-prefix relationship**

The `FROM` clause lists `Queue AS a, Queue AS b`, which is the older comma syntax for a cross join. Alias `a` represents a candidate last person. Alias `b` represents a person who may belong to that candidate’s boarding prefix.

The condition `a.turn >= b.turn` retains exactly the `b` rows whose turn is no later than candidate `a`. Thus candidate at turn one pairs with one row, candidate at turn two pairs with the first two rows, and candidate at turn $t$ pairs with all $t$ prefix rows.

The input guarantees that turns contain every integer from one through $n$, so there are no gaps or ties in boarding order.

**Group the joined rows back by candidate**

`GROUP BY a.person_id` gathers all retained prefix rows for one candidate. Because `person_id` is unique, it functionally determines that candidate’s name and turn. Selecting `a.person_name` and later ordering by `a.turn` therefore refers to one unambiguous candidate within each group.

Some strict SQL configurations express this dependency more clearly by grouping by every selected nonaggregate column as well. Under the intended MySQL semantics and unique-ID guarantee, grouping by the ID identifies the row.

**Use the prefix sum as the feasibility test**

`SUM(b.weight)` is the total weight of everyone whose turn is at most the candidate’s turn. The `HAVING` clause is used rather than `WHERE` because the condition depends on an aggregate:

`HAVING SUM(b.weight) <= 1000`.

A prefix totaling exactly 1000 is feasible. Only a value greater than 1000 is rejected.

For candidate John Cena at turn three in the example, the matching `b` rows are Alice, Alex, and John Cena. Their weights total 1000, so the candidate survives. Marie at turn four has a prefix total of 1200 and is filtered out.

**Choose the latest feasible turn**

After aggregation and filtering, `ORDER BY a.turn DESC` places later candidates first. `LIMIT 1` returns only the name of the latest feasible one.

The test data guarantees that the first person fits, so at least one group survives and the query returns one row.

Under the intended positive-person-weight model, prefix sums never decrease. Once a candidate exceeds the capacity, every later prefix also exceeds it, matching the physical rule that later people do not skip ahead after the bus can take no more weight. Even without using that monotonicity for execution, the query directly selects the greatest turn whose cumulative prefix is within the limit.

**Why the selected person is exactly the answer**

For every person `a`, the join condition includes all and only people who board no later than `a`. The grouped sum is therefore the bus weight immediately after `a` boards. `HAVING` retains exactly the people who can be included without exceeding capacity.

Ordering those feasible people by descending turn makes the first row the last feasible person in queue order. The unique turn values prevent ties. Returning that row’s name satisfies the requested schema.

The query does not calculate one running window in a single ordered pass. It reconstructs every prefix through pair rows. That distinction is important for performance even though the result is correct.

## Complexity detail

Let $n$ be the number of queue rows.

Candidate at turn $t$ joins with $t$ prefix rows. The total qualifying pair count is

$$
1+2+\cdots+n=\frac{n(n+1)}{2}=O(n^2).
$$

Materializing or processing this triangular self-join therefore takes $O(n^2)$ logical work. Grouping the pairs and ordering up to $n$ candidate groups add at most $O(n^2)$ aggregation work and $O(n\log n)$ ordering work, leaving $O(n^2)$ as the dominant bound.

The physical database optimizer may stream, hash, index, or rewrite parts of the plan, but the exact SQL expresses a quadratic self-join rather than an $O(n\log n)$ window plan.

Intermediate storage can be as large as $O(n^2)$ if pair rows are materialized, while grouped state is $O(n)$. Actual memory versus temporary-disk use depends on MySQL’s execution plan.

## Alternatives and edge cases

- **Window-function running sum:** Compute `SUM(weight) OVER (ORDER BY turn)` once, filter running totals at most 1000, and choose the greatest turn. This gives a clearer $O(n\log n)$ sort-based plan on modern MySQL.
- **Correlated prefix subquery:** Sum rows with turn no greater than each candidate’s turn. It expresses the same logic but may also become quadratic without optimizer help.
- **First person exactly reaches 1000:** The inclusive `<=` condition keeps that person, and every later positive weight makes later prefixes infeasible.
- **First-person guarantee:** It ensures `LIMIT 1` has a surviving row to return.
- **Unique turns:** Descending order identifies one last candidate without tie handling.
- **Unique person IDs:** Grouping by `a.person_id` identifies one candidate’s name and turn through functional dependency.
- **Positive weights:** They make cumulative totals monotone and match the boarding interpretation. Negative weights would make a later prefix feasible again, an unrealistic case not intended by the table semantics.
- **Any input row order:** The query uses `turn` values rather than physical table order, so shuffled storage does not change the result.
- **Capacity equality:** A total of exactly 1000 is allowed and must not be rejected.
- **Comma join syntax:** It is equivalent here to `CROSS JOIN` followed by the `WHERE` condition, but explicit join syntax is often easier to read.
