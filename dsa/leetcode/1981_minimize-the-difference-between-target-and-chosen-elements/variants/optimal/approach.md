## General
**Track reachable sums row by row**

Begin with only sum `0` reachable. For each matrix row, combine every currently
retained sum with every distinct value in that row. The resulting set contains
exactly the sums obtainable after choosing one value from each row processed so
far. Deduplicating equal sums prevents different choice histories with the same
total from creating redundant states.

**Why one above-target sum is sufficient**

Retain every new sum at most $T$. Among sums greater than $T$, retain only the
smallest. All unprocessed values are positive, so future choices can only
increase every partial sum. Consequently, if $a$ and $b$ are both above $T$
and $a < b$, then extending $a$ with any fixed future choices remains closer
to $T$ than extending $b$ with those choices. The larger state can never lead
to a better final answer.

This rule leaves at most one state above $T$ and at most $T + 1$ nonnegative
states at or below it. It is important not to discard every above-target sum:
when even the minimum possible total exceeds the target, that smallest excess
is the answer.

**Why the final minimum is optimal**

Before pruning, the transition enumerates every choice from the current row.
The only removed states are dominated above-target totals, as established
above. Thus at least one representative capable of attaining the optimum
survives every row. After the last transition, minimizing
$\lvert s - T \rvert$ over the retained sums returns the globally smallest
difference.

## Complexity detail
There are $M$ rows and $C$ columns. At most $T + 2$ sums are retained, so
combining a row with the current states takes $O(CT)$ time. Across all rows,
the total time is $O(MCT)$. The current and next reachable-sum sets contain
$O(T)$ values, giving $O(T)$ auxiliary space.

## Alternatives and edge cases
- **Unpruned reachable-sum set:** Keeping every possible total is correct, but
  the state range can grow to $70M$ even when the small target makes most large
  totals permanently irrelevant.
- **Boolean array or integer bitset:** Shift a reachable-sum representation for
  each distinct row value. This also performs dynamic programming and can be
  efficient, but it must preserve enough above-target information to compare
  the closest excess.
- **Enumerate all row choices:** Trying every combination is straightforward
  but requires up to $C^M$ work.
- Repeated values within a row create the same transition and may be
  deduplicated without changing the set of achievable sums.
- When `target` is below every possible total, the smallest retained
  above-target state determines the answer.
- When `target` exceeds every possible total, the largest achievable sum is
  closest, and all reachable sums remain at or below the target.
- A one-row matrix still requires exactly one choice; the answer is the closest
  value in that row.
