# Guided Example: Team Scores in Football Tournament

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Teams": [{"team_id": 10, "team_name": "Leetcode FC"}, {"team_id": 20, "team_name": "NewYork FC"}, {"team_id": 30, "team_name": "Atlanta FC"}, {"team_id": 40, "team_name": "Chicago FC"}, {"team_id": 50, "team_name": "Toronto FC"}], "Matches": [{"match_id": 1, "host_team": 10, "guest_team": 20, "host_goals": 3, "guest_goals": 0}, {"match_id": 2, "host_team": 30, "guest_team": 10, "host_goals": 2, "guest_goals": 2}, {"match_id": 3, "host_team": 10, "guest_team": 50, "host_goals": 5, "guest_goals": 1}, {"match_id": 4, "host_team": 20, "guest_team": 30, "host_goals": 1, "guest_goals": 0}, {"match_id": 5, "host_team": 50, "guest_team": 30, "host_goals": 1, "guest_goals": 0}]}}`
- **Required output:** `{"columns": ["team_id", "team_name", "num_points"], "rows": [[10, "Leetcode FC", 7], [20, "NewYork FC", 3], [50, "Toronto FC", 3], [30, "Atlanta FC", 1], [40, "Chicago FC", 0]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Teams`

The objective is to compute `{"columns": ["team_id", "team_name", "num_points"], "rows": [[10, "Leetcode FC", 7], [20, "NewYork FC", 3], [50, "Toronto FC", 3], [30, "Atlanta FC", 1], [40, "Chicago FC", 0]]}` from `{"tables": {"Teams": [{"team_id": 10, "team_name": "Leetcode FC"}, {"team_id": 20, "team_name": "NewYork FC"}, {"team_id": 30, "team_name": "Atlanta FC"}, {"team_id": 40, "team_name": "Chicago FC"}, {"team_id": 50, "team_name": "Toronto FC"}], "Matches": [{"match_id": 1, "host_team": 10, "guest_team": 20, "host_goals": 3, "guest_goals": 0}, {"match_id": 2, "host_team": 30, "guest_team": 10, "host_goals": 2, "guest_goals": 2}, {"match_id": 3, "host_team": 10, "guest_team": 50, "host_goals": 5, "guest_goals": 1}, {"match_id": 4, "host_team": 20, "guest_team": 30, "host_goals": 1, "guest_goals": 0}, {"match_id": 5, "host_team": 50, "guest_team": 30, "host_goals": 1, "guest_goals": 0}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Start from teams so zero-point teams survive

The query uses:

`Teams LEFT JOIN Matches ON team_id = host_team OR team_id = guest_team`.

For a team that participated in a match, the join produces one row for that team-match relationship. Because the host and guest are different, one match cannot match both sides of the `OR` for the same team.

For a team with no matches, `LEFT JOIN` still produces one result row. All columns from `Matches` are `NULL` on that row. This preserved row is what lets the later aggregation return the team with zero points instead of omitting it.

An inner join would be wrong because it would remove every team that never appeared as host or guest, even though the contract asks for exactly one row per team.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Teams": [{"team_id": 10, "team_name": "Leetcode FC"}, {"team_id": 20, "team_name": "NewYork FC"}, {"team_id": 30, "team_name": "Atlanta FC"}, {"team_id": 40, "team_name": "Chicago FC"}, {"team_id": 50, "team_name": "Toronto FC"}], "Matches": [{"match_id": 1, "host_team": 10, "guest_team": 20, "host_goals": 3, "guest_goals": 0}, {"match_id": 2, "host_team": 30, "guest_team": 10, "host_goals": 2, "guest_goals": 2}, {"match_id": 3, "host_team": 10, "guest_team": 50, "host_goals": 5, "guest_goals": 1}, {"match_id": 4, "host_team": 20, "guest_team": 30, "host_goals": 1, "guest_goals": 0}, {"match_id": 5, "host_team": 50, "guest_team": 30, "host_goals": 1, "guest_goals": 0}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Translate one match appearance into points

The `CASE` expression is evaluated from the perspective of the current `Teams` row.

The first branch checks that the team is the host and that `host_goals > guest_goals`. A successful host win contributes three.

The second branch checks that the team is the guest and that `guest_goals > host_goals`. A successful guest win also contributes three.

If neither win branch applies but `host_goals = guest_goals`, the match was a draw. Both joined team rows—the host’s row and the guest’s row—receive one point.

Every remaining case contributes zero. This includes a loss and the unmatched synthetic row produced for a team with no matches. In the latter case, comparisons involving `NULL` are not true, so execution reaches `ELSE 0`.

The branch order is safe. A match cannot simultaneously be a win and a draw, and the host and guest IDs are distinct. The explicit team-role checks on the win branches ensure that a host win awards points only to the host and a guest win awards points only to the guest.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Sum all contributions for one team

`GROUP BY 1` groups by the first selected expression, `team_id`. The aggregate `SUM(CASE ... END)` adds the points from every match appearance and is aliased as `num_points`.

`team_id` is unique in `Teams`, so it functionally determines `team_name`. The selected name is therefore unambiguous within each group. Writing both columns in the `GROUP BY` would be more explicit for SQL dialects or modes that do not infer that dependency.

For Leetcode FC in the example, the joined rows contribute three for defeating NewYork, one for drawing Atlanta, and three for defeating Toronto. Their sum is seven.

Chicago has no match row. Its preserved left-join row contributes zero, so Chicago still appears with `num_points = 0`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["team_id", "team_name", "num_points"], "rows": [[10, "Leetcode FC", 7], [20, "NewYork FC", 3], [50, "Toronto FC", 3], [30, "Atlanta FC", 1], [40, "Chicago FC", 0]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Teams": [{"team_id": 10, "team_name": "Leetcode FC"}, {"team_id": 20, "team_name": "NewYork FC"}, {"team_id": 30, "team_name": "Atlanta FC"}, {"team_id": 40, "team_name": "Chicago FC"}, {"team_id": 50, "team_name": "Toronto FC"}], "Matches": [{"match_id": 1, "host_team": 10, "guest_team": 20, "host_goals": 3, "guest_goals": 0}, {"match_id": 2, "host_team": 30, "guest_team": 10, "host_goals": 2, "guest_goals": 2}, {"match_id": 3, "host_team": 10, "guest_team": 50, "host_goals": 5, "guest_goals": 1}, {"match_id": 4, "host_team": 20, "guest_team": 30, "host_goals": 1, "guest_goals": 0}, {"match_id": 5, "host_team": 50, "guest_team": 30, "host_goals": 1, "guest_goals": 0}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["team_id", "team_name", "num_points"], "rows": [[10, "Leetcode FC", 7], [20, "NewYork FC", 3], [50, "Toronto FC", 3], [30, "Atlanta FC", 1], [40, "Chicago FC", 0]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

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
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(t+m)$. Let $t$ be the number of teams and $m$ the number of matches.
- **Auxiliary Space Complexity:** $O(t)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
