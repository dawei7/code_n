# Guided Example: Premier League Table Ranking

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"TeamStats": [{"team_id": 1, "team_name": "Manchester City", "matches_played": 10, "wins": 6, "draws": 2, "losses": 2}, {"team_id": 2, "team_name": "Liverpool", "matches_played": 10, "wins": 6, "draws": 2, "losses": 2}, {"team_id": 3, "team_name": "Chelsea", "matches_played": 10, "wins": 5, "draws": 3, "losses": 2}, {"team_id": 4, "team_name": "Arsenal", "matches_played": 10, "wins": 4, "draws": 4, "losses": 2}, {"team_id": 5, "team_name": "Tottenham", "matches_played": 10, "wins": 3, "draws": 5, "losses": 2}]}}`
- **Required output:** `{"columns": ["team_id", "team_name", "points", "position"], "rows": [[2, "Liverpool", 20, 1], [1, "Manchester City", 20, 1], [3, "Chelsea", 18, 3], [4, "Arsenal", 16, 4], [5, "Tottenham", 14, 5]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `TeamStats`

The objective is to compute `{"columns": ["team_id", "team_name", "points", "position"], "rows": [[2, "Liverpool", 20, 1], [1, "Manchester City", 20, 1], [3, "Chelsea", 18, 3], [4, "Arsenal", 16, 4], [5, "Tottenham", 14, 5]]}` from `{"tables": {"TeamStats": [{"team_id": 1, "team_name": "Manchester City", "matches_played": 10, "wins": 6, "draws": 2, "losses": 2}, {"team_id": 2, "team_name": "Liverpool", "matches_played": 10, "wins": 6, "draws": 2, "losses": 2}, {"team_id": 3, "team_name": "Chelsea", "matches_played": 10, "wins": 5, "draws": 3, "losses": 2}, {"team_id": 4, "team_name": "Arsenal", "matches_played": 10, "wins": 4, "draws": 4, "losses": 2}, {"team_id": 5, "team_name": "Tottenham", "matches_played": 10, "wins": 3, "draws": 5, "losses": 2}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

League points depend only on wins and draws. Every win contributes three, every draw contributes one, and every loss contributes zero. Therefore the points expression for one row is

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"TeamStats": [{"team_id": 1, "team_name": "Manchester City", "matches_played": 10, "wins": 6, "draws": 2, "losses": 2}, {"team_id": 2, "team_name": "Liverpool", "matches_played": 10, "wins": 6, "draws": 2, "losses": 2}, {"team_id": 3, "team_name": "Chelsea", "matches_played": 10, "wins": 5, "draws": 3, "losses": 2}, {"team_id": 4, "team_name": "Arsenal", "matches_played": 10, "wins": 4, "draws": 4, "losses": 2}, {"team_id": 5, "team_name": "Tottenham", "matches_played": 10, "wins": 3, "draws": 5, "losses": 2}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 3

The query selects each team's identifier and name, evaluates that expression as `points`, and uses the same expression inside a window function to assign the league position.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

`RANK() OVER (ORDER BY (wins * 3 + draws) DESC)` considers all rows in descending point order. The highest point total receives rank one. Teams tied on points receive the same rank because the window's ordering key contains only points. It deliberately does not include `team_name` or `team_id`: adding either would break point ties and assign different ranks, contrary to the statement.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["team_id", "team_name", "points", "position"], "rows": [[2, "Liverpool", 20, 1], [1, "Manchester City", 20, 1], [3, "Chelsea", 18, 3], [4, "Arsenal", 16, 4], [5, "Tottenham", 14, 5]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"TeamStats": [{"team_id": 1, "team_name": "Manchester City", "matches_played": 10, "wins": 6, "draws": 2, "losses": 2}, {"team_id": 2, "team_name": "Liverpool", "matches_played": 10, "wins": 6, "draws": 2, "losses": 2}, {"team_id": 3, "team_name": "Chelsea", "matches_played": 10, "wins": 5, "draws": 3, "losses": 2}, {"team_id": 4, "team_name": "Arsenal", "matches_played": 10, "wins": 4, "draws": 4, "losses": 2}, {"team_id": 5, "team_name": "Tottenham", "matches_played": 10, "wins": 3, "draws": 5, "losses": 2}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["team_id", "team_name", "points", "position"], "rows": [[2, "Liverpool", 20, 1], [1, "Manchester City", 20, 1], [3, "Chelsea", 18, 3], [4, "Arsenal", 16, 4], [5, "Tottenham", 14, 5]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **`DENSE_RANK`:** This also gives equal numbers to tied teams but removes gaps after ties. It would produce positions one, one, two in the example and therefore does not match the shown competition ranking.
- **`ROW_NUMBER`:** This always gives distinct positions, so equal-point teams would not share a rank.
- **Correlated rank count:** Position can be calculated as one plus the number of teams with strictly more points. It reproduces `RANK` but repeats the points expression and is usually less clear and potentially slower.
- **Compute points in a CTE:** A CTE can name `points` once, then rank and sort that column. This avoids textual repetition, while the compact source repeats the simple expression only in the window definition.
- **Tied teams:** They share `position` because the window ordering uses only points. The outer name sort decides presentation but not rank.
- **Several teams tied for first:** If $k$ teams share first, the next position is $k+1$, as required by `RANK` semantics.
- **Zero wins and draws:** Points are zero. Such teams tie with every other zero-point team and sort by name.
- **Losses:** They do not appear in the expression because each loss adds zero. Their stored count has no direct effect on rank.
- **Name collation:** MySQL sorts `team_name` according to the column or connection collation, which controls case and accent behavior. The query follows the database's ascending text semantics.
- **Null statistics:** If `wins` or `draws` were null, the points expression would be null and MySQL's null ordering would apply. The intended sports-statistics contract assumes usable integer counts; the source does not coalesce nulls to zero.
- **Ordinal `ORDER BY` references:** `3` and `2` are concise but depend on select-column order. Writing `ORDER BY points DESC, team_name` would be more resilient to column reordering while producing the same result.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(t log t)$. Let $t$ be the number of teams. Computing points is $O(1)$ per row, or $O(t)$ total. The window function generally needs rows ordered by descending points, and the final result needs points descending with names ascending. A database may share or optimize sorts, but the general upper bound is $O(t\log t)$ time.
- **Auxiliary Space Complexity:** $O(t)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
