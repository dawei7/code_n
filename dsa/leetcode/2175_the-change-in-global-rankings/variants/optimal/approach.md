## General

**Build the original ranking**

Order `TeamPoints` by `points DESC, name ASC` and assign `ROW_NUMBER()`.
Country names are unique, so the points-plus-name ordering is total and every
team receives exactly one old position.

**Rank the updated totals independently**

Join each team to its `PointsChange` row and order by
`points + points_change DESC, name ASC`. A second `ROW_NUMBER()` produces the
new position under precisely the same tie rule. Keeping the rankings in
separate relations makes it explicit that one ordering cannot influence the
other.

**Subtract positions as signed values**

Join the two ranked relations by `team_id` and compute old rank minus new rank.
A smaller new rank means the team moved upward and therefore yields a positive
difference. MySQL exposes `ROW_NUMBER()` as an unsigned integer, so cast both
positions to a signed type before subtraction; otherwise a rank decline would
underflow instead of producing a negative result.

## Complexity detail

Let $n$ be the number of teams. Each window ranking sorts $n$ rows, so the
logical time is $O(n\log n)$. The ranked intermediate relations require
$O(n)$ execution space. Indexes and the optimizer may change physical details
without changing the ordering semantics.

## Alternatives and edge cases

- **Conditional pair counting:** Count how many teams precede each team before
  and after the update. It is correct but a direct correlated form takes
  $O(n^2)$ time.
- **One combined window query:** Both rankings can be computed in one joined
  relation, but separate CTEs make the two orderings and join key clearer.
- `ROW_NUMBER()` is required rather than point-only `RANK()` because names
  break every points tie into distinct positions.
- The name tie-break is ascending in both the old and new rankings.
- A positive `rank_diff` means improvement; reversing the subtraction changes
  the required sign.
- MySQL unsigned window positions must be converted before a potentially
  negative subtraction.
- Input table order has no effect on either ranking.
