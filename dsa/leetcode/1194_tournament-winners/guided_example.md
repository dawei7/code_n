# Guided Example: Tournament Winners

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Players": [{"player_id": 15, "group_id": 1}, {"player_id": 25, "group_id": 1}, {"player_id": 30, "group_id": 1}, {"player_id": 45, "group_id": 1}, {"player_id": 10, "group_id": 2}, {"player_id": 35, "group_id": 2}, {"player_id": 50, "group_id": 2}, {"player_id": 20, "group_id": 3}, {"player_id": 40, "group_id": 3}], "Matches": [{"match_id": 1, "first_player": 15, "second_player": 45, "first_score": 3, "second_score": 0}, {"match_id": 2, "first_player": 30, "second_player": 25, "first_score": 1, "second_score": 2}, {"match_id": 3, "first_player": 30, "second_player": 15, "first_score": 2, "second_score": 0}, {"match_id": 4, "first_player": 40, "second_player": 20, "first_score": 5, "second_score": 2}, {"match_id": 5, "first_player": 35, "second_player": 50, "first_score": 1, "second_score": 1}]}}`
- **Required output:** `{"columns": ["group_id", "player_id"], "rows": [[1, 15], [2, 35], [3, 40]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Players`

The objective is to compute `{"columns": ["group_id", "player_id"], "rows": [[1, 15], [2, 35], [3, 40]]}` from `{"tables": {"Players": [{"player_id": 15, "group_id": 1}, {"player_id": 25, "group_id": 1}, {"player_id": 30, "group_id": 1}, {"player_id": 45, "group_id": 1}, {"player_id": 10, "group_id": 2}, {"player_id": 35, "group_id": 2}, {"player_id": 50, "group_id": 2}, {"player_id": 20, "group_id": 3}, {"player_id": 40, "group_id": 3}], "Matches": [{"match_id": 1, "first_player": 15, "second_player": 45, "first_score": 3, "second_score": 0}, {"match_id": 2, "first_player": 30, "second_player": 25, "first_score": 1, "second_score": 2}, {"match_id": 3, "first_player": 30, "second_player": 15, "first_score": 2, "second_score": 0}, {"match_id": 4, "first_player": 40, "second_player": 20, "first_score": 5, "second_score": 2}, {"match_id": 5, "first_player": 35, "second_player": 50, "first_score": 1, "second_score": 1}]}}` while avoiding redundant calculations and unnecessary overhead.

A naive or brute-force exploration risks evaluating infeasible states or repeating subproblem computations. The optimal method establishes a clear invariant that advances deterministically toward the goal.

---

## 2. Conceptual Foundation & Invariants

We maintain the core conceptual parameters and state variables:

| State Parameter | Role & Purpose | Initial State |
|---|---|---|
| Primary State | Tracks active elements, frontier indices, or DP table cells | Initialized at boundary |
| Accumulator | Preserves confirmed optimal sub-answers or counts | Empty / Neutral |

> **Invariant.** At every processing step, all previously evaluated subproblems strictly satisfy the problem constraints, and no viable candidate solution has been omitted.

---

## 3. Step-by-Step Worked Execution

### Step 1: Expand each match into two score rows

The first common table expression, `s`, has two branches joined by `UNION ALL`.

The first branch selects `first_player AS player_id` and `first_score AS score`. It joins `Matches` to `Players` on the first player ID to attach that player’s `group_id`.

The second branch does the symmetric work for `second_player` and `second_score`.

`UNION ALL` is crucial. Two identical score rows can come from different matches or roles and must both contribute to the total. Plain `UNION` would remove duplicates and could undercount a player.

The guarantee that both players in a match belong to the same group is consistent with either role’s join. Attaching the group from the player table also avoids trying to infer membership from opponents.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Players": [{"player_id": 15, "group_id": 1}, {"player_id": 25, "group_id": 1}, {"player_id": 30, "group_id": 1}, {"player_id": 45, "group_id": 1}, {"player_id": 10, "group_id": 2}, {"player_id": 35, "group_id": 2}, {"player_id": 50, "group_id": 2}, {"player_id": 20, "group_id": 3}, {"player_id": 40, "group_id": 3}], "Matches": [{"match_id": 1, "first_player": 15, "second_player": 45, "first_score": 3, "second_score": 0}, {"match_id": 2, "first_player": 30, "second_player": 25, "first_score": 1, "second_score": 2}, {"match_id": 3, "first_player": 30, "second_player": 15, "first_score": 2, "second_score": 0}, {"match_id": 4, "first_player": 40, "second_player": 20, "first_score": 5, "second_score": 2}, {"match_id": 5, "first_player": 35, "second_player": 50, "first_score": 1, "second_score": 1}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Aggregate all roles and matches per player

The next CTE, `t`, groups the score stream by `player_id` and calculates `SUM(score) AS scores`. A player who appeared as first player in some matches and second player in others now has all contributions in one total.

The query also selects `group_id`. Player IDs are unique in `Players`, so one player belongs to exactly one group and `player_id` functionally determines `group_id`. Under the intended MySQL semantics, grouping by the player ID therefore has one unambiguous group value. Writing `GROUP BY group_id, player_id` would make this dependency explicit and be more portable under strict grouping rules.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Rank independently within every group

The `p` CTE computes:

`RANK() OVER (PARTITION BY group_id ORDER BY scores DESC, player_id)`.

`PARTITION BY group_id` restarts ranking for each group. Ordering `scores DESC` places the largest total first. Adding `player_id` in ascending order implements the tie rule: among equal totals, the lower player ID comes first.

Because `player_id` is unique, no two rows in one partition can tie on both ordering keys. Consequently, exactly one row receives rank one in each represented group. `RANK` works here, although `ROW_NUMBER` would communicate the one-winner intention more directly.

The outer query keeps `WHERE rk = 1` and returns only `group_id` and `player_id`. Result ordering is unspecified, which is allowed.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["group_id", "player_id"], "rows": [[1, 15], [2, 35], [3, 40]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Players": [{"player_id": 15, "group_id": 1}, {"player_id": 25, "group_id": 1}, {"player_id": 30, "group_id": 1}, {"player_id": 45, "group_id": 1}, {"player_id": 10, "group_id": 2}, {"player_id": 35, "group_id": 2}, {"player_id": 50, "group_id": 2}, {"player_id": 20, "group_id": 3}, {"player_id": 40, "group_id": 3}], "Matches": [{"match_id": 1, "first_player": 15, "second_player": 45, "first_score": 3, "second_score": 0}, {"match_id": 2, "first_player": 30, "second_player": 25, "first_score": 1, "second_score": 2}, {"match_id": 3, "first_player": 30, "second_player": 15, "first_score": 2, "second_score": 0}, {"match_id": 4, "first_player": 40, "second_player": 20, "first_score": 5, "second_score": 2}, {"match_id": 5, "first_player": 35, "second_player": 50, "first_score": 1, "second_score": 1}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["group_id", "player_id"], "rows": [[1, 15], [2, 35], [3, 40]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **`ROW_NUMBER` instead of `RANK`:** With the complete score-and-ID ordering, `ROW_NUMBER() = 1` directly selects one winner. It avoids relying on the uniqueness of the final ordering key to make rank one unique.
- **Correlated maximum query:** Compare each player against better players in the same group. This can express the rule but is often harder to optimize and read.
- **Start from all players:** Left-join aggregated scores and use zero for missing totals when players with no matches must remain eligible.
- **Use `UNION` instead of `UNION ALL`:** This is incorrect because equal score contributions from different matches are separate facts and must not be deduplicated.
- **Player appears in both roles:** Both branches contribute, and grouping correctly combines all points.
- **Tie on total score:** Ascending `player_id` makes the lower ID win.
- **No tie:** Descending score alone places the unique maximum first.
- **One player in a group:** That represented player receives rank one automatically.
- **Inactive player:** The exact query omits it because candidates originate in `Matches`; correctness requires the participation assumption described above or a query redesign.
- **Grouping portability:** Selecting `group_id` while grouping only by `player_id` relies on the functional dependency. Grouping by both columns would be clearer across strict SQL systems.
- **Any result order:** The outer query has no `ORDER BY` because the contract permits arbitrary row order.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(p+m)$. Let $m$ be the number of matches, $p$ the number of players, and $r$ the number of players represented in the match stream.
- **Auxiliary Space Complexity:** $O(p+m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
