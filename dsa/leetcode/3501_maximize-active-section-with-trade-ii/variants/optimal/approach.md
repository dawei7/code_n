## General

**Reuse the run-level gain formula for every query.** Inside one queried substring, a valid trade removes a one-run lying between two zero-runs. If neighboring zero pieces have lengths $a$ and $c$, the trade's net gain is $a+c$: the removed middle ones are restored when the merged zero block is activated.

The number of ones outside the queried substring never changes. The source starts every query answer from `active = s.count("1")` for the entire original string and adds only the best gain obtainable inside that query.

**Compress the full string into maximal runs.** Arrays `starts`, `ends`, and `bits` describe every run's inclusive boundaries and character. `run_at[position]` maps each character position to its run ID.

Runs alternate between zero and one. For an interior one-run, its immediately preceding and following runs are both zero-runs, so it is a potential trade center whenever all three relevant pieces lie within the query.

Compression lets queries reason about runs rather than inspect every character.

**Precompute full gains for interior one-runs.** For run IDs from one through `run_count - 2`, the source assigns a value only when the run is a one-run:

$$
\text{left zero-run length}
+
\text{right zero-run length}.
$$

These values are placed at leaves of an iterative maximum segment tree. A range maximum then returns the best full-run trade center among any interval of run IDs in $O(\log n)$ time.

Boundary runs of the entire string receive no value because they do not have two real neighboring runs. Query augmentation is handled separately through clipped boundary calculations.

**Determine the first and last candidate one-runs in a query.** Let `left_run` and `right_run` contain query endpoints.

If the query begins inside a zero-run, the next run is a one-run with a zero piece on its left, so it can be the first candidate. If it begins inside a one-run, that run touches the augmented left one and lacks a zero piece inside the query on its left; the first possible center is two runs later. This gives:

`first = left_run + 1` for a zero left run, otherwise `left_run + 2`.

The symmetric right-boundary logic gives:

`last = right_run - 1` for a zero right run, otherwise `right_run - 2`.

If `first > last`, no one-run inside the substring has zero pieces on both sides, so no trade gain exists.

**Compute clipped gains at the candidate boundaries.** The first candidate's left neighboring zero-run may begin before query `left`. Its usable length is

`starts[first] - max(left, starts[first - 1])`.

The right neighboring zero-run may extend beyond query `right`. Its usable length is

`min(right, ends[first + 1]) - ends[first]`.

Their sum is `first_gain`. The formulas count positions between the clipped zero boundary and the adjacent one-run boundary exactly.

`last_gain` applies the same formula to the final candidate. Computing both is necessary because either side of the query can truncate what would otherwise be a full precomputed zero-run.

**Use the segment tree only for strictly interior candidates.** Candidate IDs from `first + 1` through `last - 1` have both neighboring zero-runs wholly inside the query. Their precomputed full gains are exact, so `range_max` returns the best among them.

The query's gain is the maximum of `first_gain`, `last_gain`, and this interior range maximum. If `first == last`, the two boundary formulas describe the same center and still return the correct value; the interior range is empty and yields zero.

For a query cutting through a long boundary zero-run, clipping ensures the trade counts only zeros actually inside the selected substring. Conceptual augmented ones lie just outside `left` and `right` and never add to `active` or to zero lengths.

**Why the segment-tree query works.** The iterative routine converts run IDs to leaf indices. When the left boundary is a right child, that node is fully covered and consumed; similarly, an even right boundary is a covered left child. Moving both boundaries upward visits a disjoint set of tree nodes whose union is the requested run interval. Taking their maximum yields the best stored gain.

**Why the complete answer is correct.** Every valid trade center in the query is one of the candidate one-runs from `first` through `last`. The first and last are evaluated with exact query clipping. Every strictly interior center has full neighboring zero-runs and is covered by the segment-tree maximum. Thus every legal gain is considered and no gain uses characters outside the substring. Adding the maximum to the unchanged global active count gives the query's optimal total. Gain zero represents choosing no trade.

Queries are independent because the source never mutates the string or run data.

## Complexity detail

Run construction and `run_at` filling visit all $n$ characters, costing $O(n)$ time and space. Building the segment tree over at most $n$ runs costs $O(n)$.

Each query performs constant-time run-ID and boundary calculations plus one segment-tree range maximum in $O(\log n)$ time. For $q$ queries, total time is $O(n+q\log n)$ and auxiliary space is $O(n)$, matching the manifest.

The returned answer list uses $O(q)$ required output space in addition to the preprocessing structures.

## Alternatives and edge cases

- **Scan runs inside every query:** This can take $O(nq)$ for many large intervals.
- **Rollback Mo's algorithm:** The local editorial presents a square-root approach, but the protected source uses static run gains plus a segment tree.
- **Use full neighboring run lengths at query boundaries:** This overcounts zeros outside the requested substring; clipping is essential.
- **Count only ones inside the query:** The requested result is active sections in the full string after a trade restricted to the substring, so outside ones remain part of the answer.
- **Query inside one run:** No surrounded one-run with two zero neighbors exists, and gain is zero.
- **All-zero query:** There is no one-run to remove first, so no trade is possible.
- **All-one query:** There are no zero-runs to activate, so the unchanged global count is returned.
- **First and last candidate equal:** Evaluate that single center with both clipped neighbors; duplicate max arguments are harmless.
- **Empty interior range:** `range_max` returns zero when left exceeds right.
- **String boundary:** Conceptual augmented ones validate boundary zero blocks without being counted.
- **Queries cutting one-runs:** A one-run touching a query boundary cannot be the first-step surrounded block and is skipped by the candidate formulas.
- **Independent queries:** No tree update is needed because each asks about the unchanged original string.
