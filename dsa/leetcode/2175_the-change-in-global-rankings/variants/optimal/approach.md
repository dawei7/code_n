## General

Every team has two positions to calculate:

- its original rank, based on `points DESC, name ASC`;
- its updated rank, based on `points + points_change DESC, name ASC`.

The requested change is original rank minus updated rank. A team that moves upward receives a positive difference because its new rank number is smaller. A team that moves downward receives a negative difference.

The exact SQL builds each team's point change, computes both rankings with window functions over the same joined rows, converts the ranks to signed integers, and subtracts them.

**Prepare one change value per team**

CTE `P` reads `PointsChange` and groups by `team_id`. It returns `SUM(points_change) AS delta`.

The schema already says `team_id` is unique in `PointsChange`, so each group normally contains one row and `delta` equals that row's `points_change`. The aggregation is therefore defensive rather than necessary under the stated contract. It would also combine multiple change records correctly if such rows were ever supplied.

Naming the value `delta` makes the later updated score expression concise: `points + delta`.

**Join changes to the team facts**

`TeamPoints JOIN P USING (team_id)` pairs every team's name and original points with its delta. The contract guarantees that every `team_id` in `TeamPoints` appears in `PointsChange`, so the inner join does not discard a team.

`USING (team_id)` also exposes one shared `team_id` column instead of two duplicate key columns. The select list can therefore refer to `team_id` without qualifying a table name.

The query calculates updated scores as expressions. It does not update either source table, which is appropriate because the task asks for a result table rather than a persistent data modification.

**Rank the original standings**

The first window expression is

`RANK() OVER (ORDER BY points DESC, name)`.

Higher point totals appear first because of `DESC`. When two teams have equal points, the second key `name` uses ascending order by default, giving the required lexicographical tie-break.

Window ranking sees the complete joined result because there is no `PARTITION BY`. This is a global ranking, not a separate rank per group or country.

**Rank the updated standings**

The second window expression changes only the primary sorting expression:

`RANK() OVER (ORDER BY (points + delta) DESC, name)`.

It therefore applies every team's delta before comparing standings, while preserving exactly the same name tie-break.

The two windows operate on the same team population. This matters because rank differences are meaningful only if no team is missing from either ordering.

**Why RANK gives ordinary positions here**

`RANK` can ordinarily leave gaps after tied rows. Here, a full tie would require both ordering expressions to be equal: the point total and the team name. The description guarantees no two teams represent the same country, so names are unique. Even when point totals match, names break the tie.

As a result, no two rows share the entire ordering key. `RANK` produces consecutive positions one through the number of teams, just as `ROW_NUMBER` would for this data. Using `RANK` is still semantically natural because the query is computing rankings.

**Subtract in the direction required by the examples**

The selected expression is original rank minus updated rank.

For Algeria in the example, the original rank is three and the new rank is two, so the result is $3-2=1$. A positive value means improvement. Croatia moves from two to three, producing $2-3=-1$. An unchanged team produces zero.

This direction is easy to reverse accidentally. Thinking in terms of rank numbers helps: moving up means the number decreases, so old minus new must be positive.

**Cast both ranks to signed values**

The query wraps each `RANK` result with `CAST(... AS SIGNED)` before subtraction. Ranking values are nonnegative, but the difference may be negative when a team falls.

In MySQL, arithmetic involving unsigned values can cause an out-of-range error or unwanted unsigned behavior when the mathematical result is negative. Casting both operands to signed integers ensures `rank_diff` can represent both improvements and declines.

The alias `'rank_diff'` names the output column expected by the contract. MySQL accepts the quoted alias syntax used in the exact source.

**Why the query returns the exact change**

The first window compares every team with the original ordering rules, so its result is that team's original position. The second compares the same teams after adding their individual changes and uses the required updated ordering rules, so it is the new position.

Subtracting these signed positions yields precisely how many places the rank number decreased or increased. Because the join retains every team and the select list produces one row per joined team, every national team appears exactly once with its correct name and difference.

The problem permits the result rows in any order. Window `ORDER BY` clauses define rank calculations but do not promise final presentation order, and no outer `ORDER BY` is necessary.

## Complexity detail

Let $N$ be the number of teams. CTE `P` scans and groups $O(N)$ change rows under the schema. The join processes $O(N)$ teams with an indexed, hash, or otherwise optimized key lookup in typical execution.

Each window ranking requires an ordering of the $N$ joined rows. Sorting dominates the algorithmic work, giving $O(N\log N)$ time overall; two sorts still have the same asymptotic order. A database optimizer may share work only when orderings are compatible, but these primary score expressions differ, so the bound should allow both sorts.

Window sorting, aggregation, and join execution may materialize $O(N)$ rows, giving an algorithmic auxiliary-space bound of $O(N)$. Actual memory versus temporary-disk use depends on the MySQL execution plan, indexes, and configured buffers.

## Alternatives and edge cases

- **ROW_NUMBER instead of RANK:** Unique names fully break point ties, so `ROW_NUMBER` with the same two ordering keys produces identical positions.
- **Two ranking CTEs:** Compute original and updated ranks in separate CTEs and join them by team. This is more verbose but can make the before-and-after columns visible for debugging.
- **Correlated counting:** A rank can be computed by counting teams ordered ahead of the current team, but doing so for every team can become quadratic without sophisticated optimization.
- **Unique change rows:** Under the schema, `SUM(points_change)` equals the sole change value; grouping remains harmless.
- **Zero point change:** A team's own score stays fixed, but its rank may still change because other teams move around it.
- **Negative point change:** `points + delta` correctly lowers the updated score; no special branch is needed.
- **Positive point change:** The same arithmetic raises the score.
- **Equal updated points:** Lexicographically smaller `name` ranks first because the secondary key is ascending.
- **Equal original points:** The identical name rule resolves the original ordering too.
- **Signed decline:** Casting before subtraction is necessary for teams whose new rank number is larger.
- **One team:** Both ranks are one, so `rank_diff` is zero regardless of its point change.
- **Every team changes equally:** All score differences remain the same, both orderings match, and every result is zero.
- **Guaranteed matching delta:** The inner join is safe only because every team is promised a `PointsChange` row; without that guarantee, a left join with `COALESCE(delta, 0)` would be needed.
- **No persistent update:** The expression `points + delta` affects ranking computation only and leaves both tables unchanged.
- **Any output order:** The window order is not a final output-order guarantee, but the contract explicitly allows arbitrary result order.
- **Unique team names:** This guarantee prevents complete ordering-key ties, so `RANK` has no gaps in the returned positions.
