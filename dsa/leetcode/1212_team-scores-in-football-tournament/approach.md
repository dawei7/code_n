## General

Each match contributes points to two different teams, but the requested output must also include teams that never played. The exact SQL starts from the complete `Teams` table, left-joins every matching host or guest appearance, converts each joined match into that team’s point contribution, sums by team, and finally applies the required ranking order.

**Start from teams so zero-point teams survive**

The query uses:

`Teams LEFT JOIN Matches ON team_id = host_team OR team_id = guest_team`.

For a team that participated in a match, the join produces one row for that team-match relationship. Because the host and guest are different, one match cannot match both sides of the `OR` for the same team.

For a team with no matches, `LEFT JOIN` still produces one result row. All columns from `Matches` are `NULL` on that row. This preserved row is what lets the later aggregation return the team with zero points instead of omitting it.

An inner join would be wrong because it would remove every team that never appeared as host or guest, even though the contract asks for exactly one row per team.

**Translate one match appearance into points**

The `CASE` expression is evaluated from the perspective of the current `Teams` row.

The first branch checks that the team is the host and that `host_goals > guest_goals`. A successful host win contributes three.

The second branch checks that the team is the guest and that `guest_goals > host_goals`. A successful guest win also contributes three.

If neither win branch applies but `host_goals = guest_goals`, the match was a draw. Both joined team rows—the host’s row and the guest’s row—receive one point.

Every remaining case contributes zero. This includes a loss and the unmatched synthetic row produced for a team with no matches. In the latter case, comparisons involving `NULL` are not true, so execution reaches `ELSE 0`.

The branch order is safe. A match cannot simultaneously be a win and a draw, and the host and guest IDs are distinct. The explicit team-role checks on the win branches ensure that a host win awards points only to the host and a guest win awards points only to the guest.

**Sum all contributions for one team**

`GROUP BY 1` groups by the first selected expression, `team_id`. The aggregate `SUM(CASE ... END)` adds the points from every match appearance and is aliased as `num_points`.

`team_id` is unique in `Teams`, so it functionally determines `team_name`. The selected name is therefore unambiguous within each group. Writing both columns in the `GROUP BY` would be more explicit for SQL dialects or modes that do not infer that dependency.

For Leetcode FC in the example, the joined rows contribute three for defeating NewYork, one for drawing Atlanta, and three for defeating Toronto. Their sum is seven.

Chicago has no match row. Its preserved left-join row contributes zero, so Chicago still appears with `num_points = 0`.

**Apply the exact result ordering**

`ORDER BY 3 DESC, 1` refers to the third selected expression, `num_points`, and then the first, `team_id`.

Descending points place better tournament totals first. The second key defaults to ascending order and therefore resolves equal totals with the lower team ID first. In the example, NewYork and Toronto both have three points, so team 20 precedes team 50.

**Why every total is correct**

Every played match joins once to its host team and once to its guest team. For each relationship, the `CASE` returns exactly the points that the rules award to that role. Grouped summation therefore accumulates every earned point once and only once.

Every catalog team produces a group because the left side of the join is preserved. Teams without appearances receive the explicit zero contribution. The final ordering exactly matches both required sort keys, so the query returns the complete and correctly ranked table.

## Complexity detail

Let $t$ be the number of teams and $m$ the number of matches.

At the logical result level, the join emits $2m$ matched team appearances plus unmatched team rows. With effective indexes and an optimizer able to handle the disjunctive host-or-guest condition, the data can be processed near $O(t+m)$ before ordering. Group state uses $O(t)$ entries, and sorting the $t$ result rows costs $O(t\log t)$.

The `OR` inside the join is important for physical performance. A database that cannot use separate indexes or rewrite the condition may compare many team-match combinations, approaching $O(tm)$ work. Thus the manifest’s $O(t+m)$ describes an optimized join-and-aggregate model, while the exact SQL text does not by itself guarantee that plan.

Output space is $O(t)$. Temporary join, grouping, and sorting storage depends on MySQL’s chosen execution plan.

## Alternatives and edge cases

- **Expand match scores with `UNION ALL`:** Produce one point row for the host and one for the guest, aggregate them, then left-join totals to `Teams`. This avoids an `OR` join and often gives the optimizer simpler inputs.
- **Correlated score subqueries:** Compute host and guest points separately per team. This can be readable but may rescan `Matches` repeatedly.
- **Team with no matches:** `LEFT JOIN` preserves it, and `ELSE 0` makes the sum zero.
- **Draw:** Both participant rows reach the equality branch and receive one point each.
- **Host win:** Only the host-role branch succeeds; the guest row falls to zero.
- **Guest win:** Only the guest-role branch succeeds; the host row falls to zero.
- **Equal point totals:** The secondary ascending team-ID key supplies deterministic tie ordering.
- **Unique team ID:** It makes `team_name` functionally dependent on the grouping key.
- **Ordinal clauses:** `GROUP BY 1` and `ORDER BY 3 DESC, 1` depend on select-list positions; explicit names are more resilient to column reordering.
- **Null match columns:** They occur only for an unmatched left-join row and safely reach `ELSE 0`.
