## General

**Start one recursive walk from every exchange row.** The anchor of recursive CTE `chains` treats each giver as `start_id`, its receiver as `current_id`, the gift value as initial total, and length as one.

The recursive branch follows an exchange whose `giver_id` equals the current receiver. It advances to that exchange's receiver, adds gift value, and increments chain length.

**Stop expanding after returning to the start.** Predicate `chains.current_id <> chains.start_id` is evaluated on the prior row. Once a row has `current_id=start_id`, it represents a completed loop and does not generate another lap.

Completed rows are selected by `WHERE current_id = start_id`.

**Why each real cycle appears once per starting edge.** In a simple cycle of length $L$, each of its $L$ exchanges serves as an anchor. Following successors returns to that anchor after $L$ steps with the same total gift value. Thus recursive output contains $L$ completed rows with identical `chain_length` and `total_gift_value`.

**Use DISTINCT to collapse rotational duplicates.** `cycle_stats` selects distinct pairs `(chain_length,total_gift_value)`. For the sample, three rotations of the length-three cycle all reduce to one row.

However, this does not preserve cycle identity.

**A genuine correctness defect for equal-statistic cycles.** If two separate cycles have the same length and same total gift value, `DISTINCT` merges them into one row even though they are different circular chains. The query should carry a canonical cycle identifier, such as the minimum employee ID, to distinguish them. The exact source does not.

**Assign display IDs after sorting.** `ROW_NUMBER` orders surviving statistic rows by length descending and total descending. The final `ORDER BY` repeats that order, producing sequential `chain_id` values.

If rows tie on both fields they would already have been merged by `DISTINCT`. A corrected identity-preserving query would need an additional deterministic tie breaker.

**Strong structural assumptions are implicit.** The description defines a circular chain where every participant gives to and receives from exactly one participant. The table key on `(giver_id,receiver_id)` alone does not enforce one outgoing or incoming edge per employee.

If a path enters a cycle that does not contain its anchor `start_id`, `current_id <> start_id` remains true forever and `UNION ALL` can repeat the cycle until MySQL's recursion limit. Branching outgoing exchanges can also generate many walks. The exact query is safe only when data behaves like disjoint cycles or similarly terminating successor chains.

**Why the recursive predicate is one step delayed.** A row that has just returned to `start_id` is produced by joining from the preceding row, because that preceding row still satisfied the inequality. On the next recursive round, the completed row fails the predicate and stops. This allows the closing edge to be included exactly once.

**What DISTINCT actually compares.** It does not see `start_id`, member IDs, or edge identities. Only the two numeric statistics survive. Rotations of one cycle collapse as intended, but any unrelated cycle with the same pair collapses for the same reason. This loss of identity is intrinsic to the selected columns.

**Trace the sample three-cycle.** Anchor 1 follows 1-to-2, 2-to-3, and 3-to-1, reaching total 90 at length three. Anchors 2 and 3 produce the same statistics. DISTINCT retains one row.

**Why totals are accumulated correctly along a terminating cycle.** Each recursion step adds the edge just followed exactly once. The completed row includes the anchor edge and every successor edge through the return, so total and length match that rotation's cycle.

**Generated-source caveat.** No local editorial exists. The query demonstrates recursive traversal, but its statistic-only deduplication and termination assumptions mean it is not a universally correct cycle enumerator under the table schema alone.

## Complexity detail

Under disjoint simple cycles with $e$ exchange rows, each of $e$ anchors can traverse up to $e$ edges, producing $O(e^2)$ recursive rows and work. Materializing them can use $O(e^2)$ space, matching the manifest's stated bounds.

Without the one-successor/disjoint-cycle assumption, branching can create far more walks and non-returning cycles can hit the recursion cap rather than obeying the bound.

## Alternatives and edge cases

- **Canonical cycle ID:** Carry the minimum member ID and group by it to keep equal-statistic cycles separate.
- **Visited-path string/set:** Prevent revisiting a node other than the start, though SQL representation is more complex.
- **Functional-graph traversal:** Enforce one outgoing edge and discover each cycle once procedurally.
- **Single self-loop:** It completes at length one, if such a row is allowed.
- **Two-node cycle:** Both anchors produce the same statistics and DISTINCT collapses rotations.
- **Separate equal cycles:** Exact query incorrectly merges them.
- **Closing edge:** It is included before the completed row stops recursing.
- **Identity loss:** `cycle_stats` retains no employee or canonical cycle key.
- **Path entering another cycle:** Recursion may never return to its own start.
- **Branching giver:** Recursive rows branch into multiple walks.
- **No cycle:** No completed row is emitted for a terminating dead end.
- **UNION ALL:** It preserves repeated paths needed for recursion but offers no duplicate-cycle protection.
- **Descending order:** Longer chains rank first, then larger totals.
- **Row-number stability:** A corrected query would need a tie breaker for equal statistics.
- **Generated source:** No authoritative editorial supports stronger assumptions.
- **Read-only query:** Source table is unchanged.
