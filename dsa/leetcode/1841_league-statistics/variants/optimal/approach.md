## General
**Express every match from both perspectives**

A match row stores the home and away sides in different columns, but the requested aggregates are team-centric. Normalize each match with `UNION ALL`: its home perspective contains the home team, home goals as `goal_for`, and away goals as `goal_against`; its away perspective swaps those roles. `UNION ALL` is essential because both perspective rows must remain, even when their numeric values happen to match.

After this transformation, every participating team has exactly one normalized row per match played. The team identifier no longer needs home-versus-away conditionals, while comparing `goal_for` with `goal_against` consistently determines whether that row contributes three, one, or zero points.

**Aggregate the standings**

Join the normalized rows to `Teams`, group by team identity and name, and compute the six requested values. `COUNT(*)` gives matches played. Separate sums give points, goals for, and goals against, while summing each row's goal difference gives the same result as subtracting the two goal totals.

For every original match, normalization creates exactly one row for each participant with mutually reversed goal totals. Therefore each appearance is counted once, each goal enters the scorer's `goal_for` and the opponent's `goal_against`, and the score comparison awards precisely the specified points. Grouping those rows consequently produces exactly the league totals. The final three-key sort implements the complete tie-breaking order.

## Complexity detail
Normalizing $m$ matches produces $2m$ rows, and joining and aggregating them takes $O(m+t)$ expected work with hash-based execution. Sorting the $t$ standings rows costs $O(t\log t)$, for $O(m+t\log t)$ total time. The normalized relation and grouped standings require $O(m+t)$ working space.

## Alternatives and edge cases
- **Direct conditional aggregation:** Join a team whenever it appears in either match column and use `CASE` for every metric; this is correct but repeats home/away branching and an `OR` join can be harder to optimize.
- **Correlated subqueries per team:** Independently scan `Matches` for every aggregate and team; this can revisit the match table $O(tm)$ times.
- **`UNION` instead of `UNION ALL`:** Duplicate elimination can incorrectly remove one perspective when the projected rows coincide and adds needless sorting or hashing.
- **Away wins:** Goals and the win comparison must be reversed for the away perspective.
- **Draws:** Equal goal totals award one point to both participants, including `0-0`.
- **Negative difference:** `goal_diff` may be negative and must not be clamped.
- **Repeated opponents:** Reversed home and away fixtures are distinct because their ordered team pair differs.
- **Complete ordering:** Equal points use descending goal difference; only a remaining tie uses ascending team name.
