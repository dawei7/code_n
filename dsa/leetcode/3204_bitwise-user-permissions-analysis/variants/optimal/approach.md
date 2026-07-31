## General

**Interpret the two permission masks**

A permission bit belongs to `common_perms` only when that bit is set in every input row. Bitwise AND implements exactly this universal condition: once any user lacks a bit, the accumulated AND clears it permanently.

A bit belongs to `any_perms` when at least one row sets it. Bitwise OR implements this existential condition: once an input mask contributes a bit, the accumulated OR retains it.

**Fold every row into both accumulators**

The remotely verified MySQL query applies `BIT_AND` and `BIT_OR` directly as whole-table aggregate functions. It therefore returns one row and assigns the required aliases without grouping by `user_id`.

The app-local SQLite dialect does not provide those two aggregate functions. It first gives the rows consecutive numbers, initializes both accumulators from the first mask, and recursively combines the next mask with `&` and `|`. The recursion ends after the last numbered row, and descending by the row number selects the final state.

After processing the first $k$ masks, the two recursive values equal their AND and OR respectively. This is true for the first row by initialization. Each transition combines exactly the next mask using the corresponding associative operation, preserving the claim for $k+1$. The final state therefore contains precisely the two requested aggregates.

## Complexity detail

Let $r$ be the number of rows in `user_permissions`. The native MySQL aggregate scans the column in $O(r)$ time and keeps constant-size accumulator state.

The app-local SQLite query numbers and materializes $r$ rows, then performs $r-1$ recursive lookups. Its conservative upper bound is $O(r\log r)$ time because SQLite may sort or index the numbered intermediate relation, with $O(r)$ auxiliary database storage. Both artifacts inspect every mask and return the same two columns.

## Alternatives and edge cases

- **Aggregate each bit separately:** Testing every supported bit with conditional aggregates is possible, but it hard-codes an integer width and repeats work for every bit position.
- **Pairwise self-joins:** Combining masks through a cross product performs unnecessary quadratic work and can duplicate contributions.
- **Arithmetic addition:** Adding permission values does not represent either universal or existential membership because carries mix neighboring bits.
- **Single user:** Both aggregates equal that user's permission mask.
- **Zero mask:** One zero clears `common_perms`, while it contributes no bits to `any_perms`.
- **Repeated masks:** Duplicate permission values do not change the AND or OR result.
- **Disjoint masks:** Their common mask is zero, while their OR contains the union of all set bits.
- **Aliases:** The two output columns must be named exactly `common_perms` and `any_perms`.

