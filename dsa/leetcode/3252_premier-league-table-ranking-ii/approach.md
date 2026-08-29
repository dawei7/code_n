## General

The query must compute three related facts for every team: league points, competition position, and one of three tiers. A common table expression first calculates the reusable ranking context, and the outer query converts that context into tiers.

In CTE `T`, points are `wins * 3 + draws` because wins contribute three, draws one, and losses zero. `RANK() OVER (ORDER BY wins * 3 + draws DESC)` assigns position one to the greatest total. Equal totals share a position because points are the window's only ordering key.

`RANK` leaves competition gaps. If two teams share position seven, the following team is position nine. This matters to the tier calculation because a tied group is treated according to its shared first position.

`COUNT(1) OVER () AS total_teams` is a window count over the entire unpartitioned table. It returns the same number of teams on every CTE row without collapsing the rows as an aggregate `GROUP BY` would. The outer query can therefore compare each position with thresholds derived from the same total.

The first tier threshold is `CEIL(total_teams / 3.0)`. Using `3.0` forces non-integer division, and `CEIL` rounds a partial third upward. The second threshold is `CEIL(2 * total_teams / 3.0)`. Positions up through the first threshold receive `'Tier 1'`; remaining positions up through the second receive `'Tier 2'`; all later positions receive `'Tier 3'`.

For ten teams, the thresholds are four and seven. Positions one through four are nominally top tier, positions five through seven middle tier, and positions eight through ten bottom tier. In the example, Everton and Luton Town tie at position seven. Both satisfy the second `WHEN` and enter Tier 2, even though their two physical rows occupy the seventh and eighth slots. This is how the query places a boundary tie in the higher tier.

More generally, `RANK` assigns every tied team the ordinal position of the first row in its tie block. If that position lies at or above a tier cutoff, the entire tied block receives that higher tier. No secondary team-name ordering appears inside the window because it would split the tie and violate this rule.

The `CASE` is evaluated from top to bottom. A Tier 1 position also satisfies the looser Tier 2 upper bound, but the first matching branch wins, so it is correctly labeled Tier 1. The final `ELSE` covers all positions beyond the second cutoff.

After tier assignment, `ORDER BY 2 DESC, 1` sorts by select column two, `points`, descending, and then by select column one, `team_name`, ascending. Name sorting only controls display within a point tie. It cannot alter the already computed shared position or tier.

The CTE selects no `team_id` because the requested output contains only name, points, position, and tier. `matches_played` and `losses` are also unnecessary for the scoring formula.

**Why the query does not use `NTILE(3)`.** `NTILE` distributes physical rows into nearly equal buckets and can split rows with identical point totals across a boundary. The problem explicitly says a tie at the boundary belongs in the higher tier. Rank-based thresholds preserve the tie group.

**Rounding interpretation.** Calling the top group “33%” and middle group “33%” cannot always divide an integer number of teams exactly. The source makes the intended policy concrete with ceiling thresholds on cumulative thirds. Ties can then expand a tier beyond its nominal number of rows, as required.

The complete correctness chain is: the points expression implements the scoring system, `RANK` gives the required shared competition positions, total-team thresholds identify cumulative thirds, shared ranks keep boundary ties together in the higher branch, and the final order meets the presentation requirement.

## Complexity detail

Let $t$ be the number of teams. Calculating points and total count is linear. Ranking requires ordering rows by points, and final presentation may require an ordering by points and name. The general time bound is $O(t\log t)$.

Window processing and sorting may materialize $O(t)$ rows, so working space is $O(t)$. A database optimizer may reuse compatible sorting work or spill temporary data to disk. Exact runtime depends on indexes, collation, memory settings, and the MySQL plan.

The constant number of arithmetic expressions and `CASE` comparisons per row contributes only $O(t)$ beyond sorting.

## Alternatives and edge cases

- **`NTILE(3)`:** It balances row counts but can separate teams with equal points, so it does not honor the higher-tier tie rule.
- **`DENSE_RANK`:** It keeps ties together but changes numeric positions by removing gaps. The examples require competition positions from `RANK`.
- **Percent-rank functions:** `PERCENT_RANK` and `CUME_DIST` have different boundary semantics, especially for ties, and do not directly reproduce the stated ceiling thresholds.
- **CTE for points first, second CTE for windows:** This could avoid repeating the points expression inside `RANK` and make stages even more explicit. The source keeps both computations in one CTE.
- **Fewer than three teams:** Ceiling thresholds can overlap, but top-to-bottom `CASE` evaluation still gives a deterministic highest applicable tier.
- **Team count not divisible by three:** `CEIL` allocates cumulative cutoffs upward, with the remainder effectively reducing the bottom nominal group before tie expansion.
- **Tie at the first boundary:** A tied block whose rank is at most the first cutoff is entirely Tier 1, even if later rows extend beyond the nominal top-third row count.
- **Tie at the second boundary:** The same logic keeps the block in Tier 2.
- **Tie beginning after a boundary:** Its shared rank is already in the lower tier, so the whole block remains there; it does not actually straddle the ranked cutoff.
- **All teams tied:** Every team has position one and enters Tier 1. This follows the instruction that boundary ties go to the higher tier, even though it produces an expanded top tier.
- **Text ordering:** Team names use MySQL collation rules for the final ascending tie order.
- **Null wins or draws:** The source does not replace nulls with zero. Intended rows must contain usable statistics for the arithmetic and rank policy to be meaningful.
- **Ordinal order references:** `ORDER BY 2, 1` is concise but coupled to select-column positions; aliases would be more robust to later projection changes.
