## General

**Measure every state independently.** Use window functions partitioned by
`state`. `COUNT(*)` supplies the state's population, while `RANK()` ordered by
`fraud_score DESC` assigns equal scores the same position and leaves the
correct gap afterward. A global rank would let large states distort small
states and is therefore invalid.

**Convert five percent into a whole-position cutoff.** A state with $n_s$
policies retains ranks through $\lceil0.05n_s\rceil$. Ceiling ensures that a
nonempty state always contributes at least one position and that 21 through 40
rows contribute two positions. Filter the ranked rows at that cutoff. Because
`RANK` gives every equal score the same rank, all ties at the final selected
score survive even when this returns more than exactly five percent of rows.

Project the original three columns and apply the required ordering: state
ascending, score descending, then policy ID ascending. Those keys also make
ties deterministic.

## Complexity detail

Let $n$ be the total number of policies. Partitioned score ordering and the
final output ordering take $O(n\log n)$ time in the worst case. Window state
and sorted rows use $O(n)$ working space. Indexes or reused physical order may
reduce constants but do not change the stated general bound.

## Alternatives and edge cases

- **Maximum score per state:** This matches states smaller than 21 rows but fails once the five-percent ceiling includes multiple ranked positions.
- **`ROW_NUMBER`:** It returns exactly the nominal row count but improperly drops score ties at the boundary.
- **`DENSE_RANK`:** It does not leave gaps after ties and can admit a lower score whose row position lies beyond the percentile cutoff.
- **Global percentile:** Percentile size and ranking are defined separately for each state.
- A nonempty state with fewer than twenty policies still contributes rank one.
- At 21 policies the ceiling cutoff becomes two, not one.
- Every tie at the cutoff score is included and then ordered by `policy_id`.
