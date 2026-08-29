# Guided Example: Premier League Table Ranking III

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"SeasonStats": [{"season_id": 2021, "team_id": 1, "team_name": "Manchester City", "matches_played": 38, "wins": 29, "draws": 6, "losses": 3, "goals_for": 99, "goals_against": 26}, {"season_id": 2021, "team_id": 2, "team_name": "Liverpool", "matches_played": 38, "wins": 28, "draws": 8, "losses": 2, "goals_for": 94, "goals_against": 26}, {"season_id": 2021, "team_id": 3, "team_name": "Chelsea", "matches_played": 38, "wins": 21, "draws": 11, "losses": 6, "goals_for": 76, "goals_against": 33}, {"season_id": 2021, "team_id": 4, "team_name": "Tottenham", "matches_played": 38, "wins": 22, "draws": 5, "losses": 11, "goals_for": 69, "goals_against": 40}, {"season_id": 2021, "team_id": 5, "team_name": "Arsenal", "matches_played": 38, "wins": 22, "draws": 3, "losses": 13, "goals_for": 61, "goals_against": 48}, {"season_id": 2022, "team_id": 1, "team_name": "Manchester City", "matches_played": 38, "wins": 28, "draws": 5, "losses": 5, "goals_for": 94, "goals_against": 33}, {"season_id": 2022, "team_id": 2, "team_name": "Arsenal", "matches_played": 38, "wins": 26, "draws": 6, "losses": 6, "goals_for": 88, "goals_against": 43}, {"season_id": 2022, "team_id": 3, "team_name": "Manchester United", "matches_played": 38, "wins": 23, "draws": 6, "losses": 9, "goals_for": 58, "goals_against": 43}, {"season_id": 2022, "team_id": 4, "team_name": "Newcastle", "matches_played": 38, "wins": 19, "draws": 14, "losses": 5, "goals_for": 68, "goals_against": 33}, {"season_id": 2022, "team_id": 5, "team_name": "Liverpool", "matches_played": 38, "wins": 19, "draws": 10, "losses": 9, "goals_for": 75, "goals_against": 47}]}}`
- **Required output:** `{"columns": ["season_id", "team_id", "team_name", "points", "goal_difference", "position"], "rows": [[2021, 1, "Manchester City", 93, 73, 1], [2021, 2, "Liverpool", 92, 68, 2], [2021, 3, "Chelsea", 74, 43, 3], [2021, 4, "Tottenham", 71, 29, 4], [2021, 5, "Arsenal", 69, 13, 5], [2022, 1, "Manchester City", 89, 61, 1], [2022, 2, "Arsenal", 84, 45, 2], [2022, 3, "Manchester United", 75, 15, 3], [2022, 4, "Newcastle", 71, 35, 4], [2022, 5, "Liverpool", 67, 28, 5]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `SeasonStats`

The objective is to compute `{"columns": ["season_id", "team_id", "team_name", "points", "goal_difference", "position"], "rows": [[2021, 1, "Manchester City", 93, 73, 1], [2021, 2, "Liverpool", 92, 68, 2], [2021, 3, "Chelsea", 74, 43, 3], [2021, 4, "Tottenham", 71, 29, 4], [2021, 5, "Arsenal", 69, 13, 5], [2022, 1, "Manchester City", 89, 61, 1], [2022, 2, "Arsenal", 84, 45, 2], [2022, 3, "Manchester United", 75, 15, 3], [2022, 4, "Newcastle", 71, 35, 4], [2022, 5, "Liverpool", 67, 28, 5]]}` from `{"tables": {"SeasonStats": [{"season_id": 2021, "team_id": 1, "team_name": "Manchester City", "matches_played": 38, "wins": 29, "draws": 6, "losses": 3, "goals_for": 99, "goals_against": 26}, {"season_id": 2021, "team_id": 2, "team_name": "Liverpool", "matches_played": 38, "wins": 28, "draws": 8, "losses": 2, "goals_for": 94, "goals_against": 26}, {"season_id": 2021, "team_id": 3, "team_name": "Chelsea", "matches_played": 38, "wins": 21, "draws": 11, "losses": 6, "goals_for": 76, "goals_against": 33}, {"season_id": 2021, "team_id": 4, "team_name": "Tottenham", "matches_played": 38, "wins": 22, "draws": 5, "losses": 11, "goals_for": 69, "goals_against": 40}, {"season_id": 2021, "team_id": 5, "team_name": "Arsenal", "matches_played": 38, "wins": 22, "draws": 3, "losses": 13, "goals_for": 61, "goals_against": 48}, {"season_id": 2022, "team_id": 1, "team_name": "Manchester City", "matches_played": 38, "wins": 28, "draws": 5, "losses": 5, "goals_for": 94, "goals_against": 33}, {"season_id": 2022, "team_id": 2, "team_name": "Arsenal", "matches_played": 38, "wins": 26, "draws": 6, "losses": 6, "goals_for": 88, "goals_against": 43}, {"season_id": 2022, "team_id": 3, "team_name": "Manchester United", "matches_played": 38, "wins": 23, "draws": 6, "losses": 9, "goals_for": 58, "goals_against": 43}, {"season_id": 2022, "team_id": 4, "team_name": "Newcastle", "matches_played": 38, "wins": 19, "draws": 14, "losses": 5, "goals_for": 68, "goals_against": 33}, {"season_id": 2022, "team_id": 5, "team_name": "Liverpool", "matches_played": 38, "wins": 19, "draws": 10, "losses": 9, "goals_for": 75, "goals_against": 47}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Derive the two football metrics directly from each row.** Every `SeasonStats` row already represents one team in one season. Points are three per win plus one per draw, so `wins * 3 + draws` is exact; losses contribute zero and need not appear. Goal difference is `goals_for - goals_against`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"SeasonStats": [{"season_id": 2021, "team_id": 1, "team_name": "Manchester City", "matches_played": 38, "wins": 29, "draws": 6, "losses": 3, "goals_for": 99, "goals_against": 26}, {"season_id": 2021, "team_id": 2, "team_name": "Liverpool", "matches_played": 38, "wins": 28, "draws": 8, "losses": 2, "goals_for": 94, "goals_against": 26}, {"season_id": 2021, "team_id": 3, "team_name": "Chelsea", "matches_played": 38, "wins": 21, "draws": 11, "losses": 6, "goals_for": 76, "goals_against": 33}, {"season_id": 2021, "team_id": 4, "team_name": "Tottenham", "matches_played": 38, "wins": 22, "draws": 5, "losses": 11, "goals_for": 69, "goals_against": 40}, {"season_id": 2021, "team_id": 5, "team_name": "Arsenal", "matches_played": 38, "wins": 22, "draws": 3, "losses": 13, "goals_for": 61, "goals_against": 48}, {"season_id": 2022, "team_id": 1, "team_name": "Manchester City", "matches_played": 38, "wins": 28, "draws": 5, "losses": 5, "goals_for": 94, "goals_against": 33}, {"season_id": 2022, "team_id": 2, "team_name": "Arsenal", "matches_played": 38, "wins": 26, "draws": 6, "losses": 6, "goals_for": 88, "goals_against": 43}, {"season_id": 2022, "team_id": 3, "team_name": "Manchester United", "matches_played": 38, "wins": 23, "draws": 6, "losses": 9, "goals_for": 58, "goals_against": 43}, {"season_id": 2022, "team_id": 4, "team_name": "Newcastle", "matches_played": 38, "wins": 19, "draws": 14, "losses": 5, "goals_for": 68, "goals_against": 33}, {"season_id": 2022, "team_id": 5, "team_name": "Liverpool", "matches_played": 38, "wins": 19, "draws": 10, "losses": 9, "goals_for": 75, "goals_against": 47}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The query selects both expressions with aliases `points` and `goal_difference`. It does not need grouping because the documented unique key `(season_id, team_id)` guarantees at most one statistics row for that team-season pair.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Rank each season independently.** The window function partitions by `season_id`. Rows from different seasons never compete, and rank restarts at one for every season.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["season_id", "team_id", "team_name", "points", "goal_difference", "position"], "rows": [[2021, 1, "Manchester City", 93, 73, 1], [2021, 2, "Liverpool", 92, 68, 2], [2021, 3, "Chelsea", 74, 43, 3], [2021, 4, "Tottenham", 71, 29, 4], [2021, 5, "Arsenal", 69, 13, 5], [2022, 1, "Manchester City", 89, 61, 1], [2022, 2, "Arsenal", 84, 45, 2], [2022, 3, "Manchester United", 75, 15, 3], [2022, 4, "Newcastle", 71, 35, 4], [2022, 5, "Liverpool", 67, 28, 5]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"SeasonStats": [{"season_id": 2021, "team_id": 1, "team_name": "Manchester City", "matches_played": 38, "wins": 29, "draws": 6, "losses": 3, "goals_for": 99, "goals_against": 26}, {"season_id": 2021, "team_id": 2, "team_name": "Liverpool", "matches_played": 38, "wins": 28, "draws": 8, "losses": 2, "goals_for": 94, "goals_against": 26}, {"season_id": 2021, "team_id": 3, "team_name": "Chelsea", "matches_played": 38, "wins": 21, "draws": 11, "losses": 6, "goals_for": 76, "goals_against": 33}, {"season_id": 2021, "team_id": 4, "team_name": "Tottenham", "matches_played": 38, "wins": 22, "draws": 5, "losses": 11, "goals_for": 69, "goals_against": 40}, {"season_id": 2021, "team_id": 5, "team_name": "Arsenal", "matches_played": 38, "wins": 22, "draws": 3, "losses": 13, "goals_for": 61, "goals_against": 48}, {"season_id": 2022, "team_id": 1, "team_name": "Manchester City", "matches_played": 38, "wins": 28, "draws": 5, "losses": 5, "goals_for": 94, "goals_against": 33}, {"season_id": 2022, "team_id": 2, "team_name": "Arsenal", "matches_played": 38, "wins": 26, "draws": 6, "losses": 6, "goals_for": 88, "goals_against": 43}, {"season_id": 2022, "team_id": 3, "team_name": "Manchester United", "matches_played": 38, "wins": 23, "draws": 6, "losses": 9, "goals_for": 58, "goals_against": 43}, {"season_id": 2022, "team_id": 4, "team_name": "Newcastle", "matches_played": 38, "wins": 19, "draws": 14, "losses": 5, "goals_for": 68, "goals_against": 33}, {"season_id": 2022, "team_id": 5, "team_name": "Liverpool", "matches_played": 38, "wins": 19, "draws": 10, "losses": 9, "goals_for": 75, "goals_against": 47}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["season_id", "team_id", "team_name", "points", "goal_difference", "position"], "rows": [[2021, 1, "Manchester City", 93, 73, 1], [2021, 2, "Liverpool", 92, 68, 2], [2021, 3, "Chelsea", 74, 43, 3], [2021, 4, "Tottenham", 71, 29, 4], [2021, 5, "Arsenal", 69, 13, 5], [2022, 1, "Manchester City", 89, 61, 1], [2022, 2, "Arsenal", 84, 45, 2], [2022, 3, "Manchester United", 75, 15, 3], [2022, 4, "Newcastle", 71, 35, 4], [2022, 5, "Liverpool", 67, 28, 5]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **`ROW_NUMBER` instead of `RANK`:** It guarantees unique sequential positions but needs a deterministic final tie-break, such as `team_id`, when names also tie.
- **`DENSE_RANK`:** It would avoid gaps after complete ties but still assign the same position to identical ordering tuples; the statement does not request that behavior specifically.
- **CTE for derived metrics:** Computing points and goal difference in a CTE can avoid repeating expressions in the window order and improve readability without changing semantics.
- **Equal points:** Goal difference decides the higher team.
- **Equal points and goal difference:** Alphabetically smaller team name receives the earlier position.
- **Identical names and metrics:** Exact `RANK` ties them and may create a later rank gap because no team-ID tie-break exists.
- **Negative goal difference:** Descending numeric order correctly treats $-1$ as better than $-5$.
- **No wins:** Draws still contribute one point each.
- **Losses:** They add zero and are correctly absent from the point expression.
- **Several seasons:** `PARTITION BY` restarts positions, while final order groups seasons ascending.
- **Positional final order:** `ORDER BY 1, 6, 3` is valid but fragile if projection order changes; named aliases are clearer.
- **One team in a season:** It receives position one regardless of metrics.
- **No aggregation:** The unique team-season row already contains totals, so grouping would be redundant.
- **Team names and collation:** Alphabetical comparison follows the database column's configured collation. Case, accents, and locale rules could affect order outside the example, so SQL “alphabetical” order is not necessarily raw byte order.
- **Repeated expressions:** Points and goal difference are calculated again inside the window order. This is logically consistent with the displayed aliases, though a CTE would make future formula changes less error-prone.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of `SeasonStats` rows. Computing arithmetic expressions is $O(n)$. A general execution plan sorts rows within seasons for the window function and may sort again for final output, giving $O(n\log n)$ time in the worst case. Suitable indexes or optimizer reuse can reduce physical sorting work.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
