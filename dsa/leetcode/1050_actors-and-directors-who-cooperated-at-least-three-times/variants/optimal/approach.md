## General

**One row represents one cooperation event**

Each `ActorDirector` row names an actor, a director, and a unique `timestamp`. The timestamp primary key ensures no two table rows describe the same keyed event.

The question asks for pairs, not individual actors or directors. Rows must therefore be grouped by the combination `(actor_id, director_id)`. The number of rows in one such group is the number of recorded collaborations for that exact pair.

**Group by both selected columns**

The query selects `actor_id` first and `director_id` second, then writes `GROUP BY 1, 2`.

In MySQL, positional grouping references select-list positions:

- `1` means `actor_id`.
- `2` means `director_id`.

Writing `GROUP BY actor_id, director_id` would be equivalent and more explicit.

Grouping by only actor would combine work with different directors. Grouping by only director would combine different actors. Both identifiers are required to preserve pair identity.

**Count rows in each pair**

`COUNT(1)` counts one non-null constant for every row in the group. It is therefore the group row count.

The query could use `COUNT(*)` with the same meaning. It does not need `COUNT(DISTINCT timestamp)` because `timestamp` is already a primary key and hence unique across the entire table.

Every row contributes exactly one collaboration to exactly one actor-director group.

**Filter aggregates with `HAVING`**

The required threshold applies after rows have been grouped. `HAVING COUNT(1) >= 3` retains groups containing three or more cooperation records.

`WHERE` cannot express this aggregate condition directly because it filters individual rows before grouping. Removing rows before counting would change the meaning.

The comparison is `>= 3` rather than `= 3`. A pair with four, ten, or more collaborations also qualifies.

**Trace the example**

The pair `(1, 1)` appears at timestamps zero, one, and two. Its group count is three, so it passes.

The pair `(1, 2)` appears twice, at timestamps three and four, so it fails.

The pair `(2, 1)` also appears twice and fails.

Only `(1, 1)` is selected.

**Why one output row is produced per pair**

`GROUP BY` collapses every row sharing the two identifiers into a single result group. The select list contains only those grouping keys.

After `HAVING`, each qualifying group emits one row. No outer `DISTINCT` is necessary because groups are already unique combinations.

**Why timestamp is not returned**

The task asks which pairs meet the count threshold, not which events caused qualification. A group may contain several timestamps, so selecting an arbitrary timestamp would be irrelevant and could conflict with strict SQL grouping rules.

The aggregate uses timestamp uniqueness only as schema evidence that rows are distinct events; the output needs only actor and director identifiers.

**Conceptual SQL evaluation**

At a logical level, the database:

1. Reads all `ActorDirector` rows.
2. Partitions them by the two identifier columns.
3. Counts the rows in each partition.
4. Removes partitions whose count is below three.
5. Projects the two grouping keys.

The optimizer may use sorting, hashing, an index, or partial aggregation. SQL defines the result independently of that physical strategy.

**Why no ordering clause appears**

The source accepts the result in any order. `GROUP BY` does not provide a portable ordering guarantee even if a particular execution plan happens to emit sorted keys.

Omitting `ORDER BY` avoids unnecessary sorting solely for presentation.

**Null behavior**

`COUNT(1)` counts rows even if an identifier were null because it counts the constant one. SQL groups null identifier values together according to grouping semantics.

The local schema does not state additional nullability rules for the identifiers, so the exact query consistently treats each resulting identifier pair as a group. The primary-key timestamp itself is non-null by primary-key semantics.

**Why the query is sufficient**

For any actor-director pair, its group contains exactly all table rows with those two identifiers. The aggregate equals its recorded cooperation frequency.

The `HAVING` predicate accepts exactly frequencies of at least three. Therefore, every returned pair qualifies and every qualifying pair is returned.

## Complexity detail

Let `R` be the number of rows in `ActorDirector`.

A sort-based grouping plan takes `O(R \log R)` time to order rows by the pair, followed by a linear aggregation pass. This matches the manifest.

A hash-aggregation plan can take expected `O(R)` time, but database complexity depends on indexes, optimizer choices, memory, and spill behavior. The manifest uses the conservative sort-based expression.

Grouping state and sort/hash workspace can hold `O(R)` row or group information in the worst case, matching the `O(R)` space bound. The output contains at most one row per input pair.

## Alternatives and edge cases

- **Explicit column names in `GROUP BY`:** `GROUP BY actor_id, director_id` is clearer and more portable than positional references while producing the same result.
- **`COUNT(*)`:** It is semantically equivalent to `COUNT(1)` for counting group rows.
- **`COUNT(timestamp)`:** Because the primary key cannot be null, it also counts every row. The constant count avoids depending on that column detail.
- **`COUNT(DISTINCT timestamp)`:** It is correct but redundant because timestamp is globally unique and may add unnecessary distinct-processing work.
- **Window function:** Compute `COUNT(*) OVER (PARTITION BY actor_id, director_id)`, filter counts, and select distinct pairs. It works but needs an extra deduplication step.
- **Self-joining three copies:** Require three different timestamps for one pair. This is much more complex and can create large intermediate combinations.
- **Correlated subquery:** Count matching rows for every outer pair, then deduplicate. Repeated counting is typically less efficient than one aggregation.
- **Exactly three rows:** The group passes because the comparison is inclusive.
- **More than three rows:** The group also passes, as required by “at least.”
- **Two rows:** The group fails.
- **Same actor with several directors:** Each director forms a separate group and frequency.
- **Same director with several actors:** Each actor likewise remains separate.
- **Unique timestamp:** Every physical row is a distinct keyed cooperation event, so plain row counting is appropriate.
- **Result order:** No `ORDER BY` is required or implied by the problem.
