## General

**Attribute each pass to the passer's team.** `Passes.pass_from` identifies the player attempting the pass. Joining `Teams t1` on that ID obtains the team whose dominance score must change.

A second join, `Teams t2` on `pass_to`, obtains the receiver's team. Foreign-key guarantees make both inner joins appropriate: each pass endpoint should match exactly one player row because `player_id` is unique.

**Classify the match half from the timestamp.** The CTE assigns

`IF(time_stamp <= '45:00', 1, 2)`.

Timestamps use fixed-width `MM:SS` text from `00:00` through `90:00`. Lexicographic comparison therefore follows chronological order. Exactly `45:00` belongs to half one, while `45:01` and later belong to half two.

The example time `01:15` means one minute fifteen seconds, so it correctly belongs to the first half even though its row appears after a `00:45` entry in the displayed table.

**Score success versus interception.** The CTE computes

`IF(t1.team_name = t2.team_name, 1, -1)`.

A receiver on the passer's team makes a successful pass worth plus one. A receiver on the other team makes the pass an interception from the passer team's perspective and contributes negative one.

Only the passer team's row receives this score. The query does not simultaneously add a positive point to the receiving opponent.

**Create one normalized row per pass.** CTE `T` projects exactly three derived fields:

- passer's `team_name`;
- `half_number`;
- signed `dominance` contribution.

This converts the relational endpoint data into records ready for aggregation.

**Aggregate by team and half.** The outer `SUM(dominance)` adds every signed pass contribution in each `(team_name,half_number)` group. Two successful passes and one interception become $1+1-1=1$.

`GROUP BY 1,2` uses select-list ordinals for `team_name` and `half_number`. The alias on `SUM` gives the required output name `dominance`.

**Return deterministic ordering.** `ORDER BY 1,2` sorts team names ascending, then half number ascending within each team. This places a team's first-half row before its second-half row.

**Why pass direction determines ownership.** An interception is still recorded as an attempted pass from `pass_from`. Consequently its negative point belongs to `t1.team_name`, even though `pass_to` belongs to the opponent. Grouping by the receiver's team would reverse the meaning of the metric. The two aliases keep these roles explicit.

**Why fixed-width text comparison works at the boundary.** Every minute and second field has two digits. Therefore the first differing character in two timestamps represents the same place value, so lexicographic and chronological order agree. A value such as `'9:00'` without the leading zero would violate this assumption, but the stated `00:00-90:00` format and examples use fixed width.

**Understand absent groups.** The exact query emits groups only when at least one pass by that team exists in that half. It does not cross-join all teams with both half numbers and fill missing dominance with zero. If the intended output requires explicit zero rows for pass-free halves, this source would be incomplete; the local examples do not exercise that case.

**Trace Arsenal's second half.** The passes 2-to-3 and 1-to-2 remain within Arsenal and contribute plus one each. Pass 3-to-4 goes to Chelsea and contributes negative one. Their sum is one, which appears under Arsenal, half two.

**Why the aggregate is exact.** Each pass joins to its unique passer and receiver teams, receives exactly one correct half and one signed contribution, and enters exactly one grouping bucket. Summing those records implements the definition directly; final ordering changes presentation only.

## Complexity detail

Let $p$ be the number of passes and $t$ the number of players. With indexes on unique/foreign-key player IDs, endpoint joins are typically $O(p\log t)$ or better via indexed lookups. Grouping $g$ team-half buckets and ordering them adds engine-dependent hashing/sorting work, summarized by the manifest as $O(p\log t+g\log g)$.

The CTE and aggregation may materialize $O(p)$ intermediate data, although a database can stream or hash it. The manifest's $O(g)$ space is an optimistic logical aggregation-state bound; physical execution and sort memory depend on MySQL's chosen plan.

## Alternatives and edge cases

- **Conditional aggregation without a CTE:** It can compute the same sum inline but is less readable.
- **Left joins:** Foreign keys guarantee endpoints, so inner joins correctly retain all valid passes.
- **Exactly `45:00`:** It belongs to half one.
- **`45:01`:** It belongs to half two.
- **Same-team pass:** Adds one to the passer team.
- **Opposing-team receiver:** Subtracts one from the passer team only.
- **Passer ownership:** Every group key comes from `t1`, never `t2`.
- **Negative dominance:** More interceptions than successes legitimately produces a negative sum.
- **No pass in a half:** The exact query omits that team-half row rather than returning zero.
- **Fixed timestamp width:** It makes string comparison chronological; inconsistent formatting would break the test.
- **Displayed row order:** Aggregation does not depend on the input table's presentation order.
- **Unique player ID:** Each endpoint join returns one team.
- **Primary key:** A passer cannot have two pass rows at the same timestamp.
- **Ordinal clauses:** `GROUP BY 1,2` and `ORDER BY 1,2` depend on select-list order.
- **Team names:** Equality, grouping, and ordering follow the database collation.
- **No row mutation:** This is a read-only query.
