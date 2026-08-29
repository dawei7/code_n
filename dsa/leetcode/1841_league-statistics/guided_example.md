# Guided Example: League Statistics

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Teams": [{"team_id": 1, "team_name": "Ajax"}, {"team_id": 4, "team_name": "Dortmund"}, {"team_id": 6, "team_name": "Arsenal"}], "Matches": [{"home_team_id": 1, "away_team_id": 4, "home_team_goals": 0, "away_team_goals": 1}, {"home_team_id": 1, "away_team_id": 6, "home_team_goals": 3, "away_team_goals": 3}, {"home_team_id": 4, "away_team_id": 1, "home_team_goals": 5, "away_team_goals": 2}, {"home_team_id": 6, "away_team_id": 1, "home_team_goals": 0, "away_team_goals": 0}]}}`
- **Required output:** `{"columns": ["team_name", "matches_played", "points", "goal_for", "goal_against", "goal_diff"], "rows": [["Dortmund", 2, 6, 6, 2, 4], ["Arsenal", 2, 2, 3, 3, 0], ["Ajax", 4, 2, 5, 9, -4]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Teams`

The objective is to compute `{"columns": ["team_name", "matches_played", "points", "goal_for", "goal_against", "goal_diff"], "rows": [["Dortmund", 2, 6, 6, 2, 4], ["Arsenal", 2, 2, 3, 3, 0], ["Ajax", 4, 2, 5, 9, -4]]}` from `{"tables": {"Teams": [{"team_id": 1, "team_name": "Ajax"}, {"team_id": 4, "team_name": "Dortmund"}, {"team_id": 6, "team_name": "Arsenal"}], "Matches": [{"home_team_id": 1, "away_team_id": 4, "home_team_goals": 0, "away_team_goals": 1}, {"home_team_id": 1, "away_team_id": 6, "home_team_goals": 3, "away_team_goals": 3}, {"home_team_id": 4, "away_team_id": 1, "home_team_goals": 5, "away_team_goals": 2}, {"home_team_id": 6, "away_team_id": 1, "home_team_goals": 0, "away_team_goals": 0}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Turn every match into one row per team perspective.** A row in `Matches` contains both teams, but league statistics are grouped by a single team. The common table expression `Scores` normalizes each match into two rows:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Teams": [{"team_id": 1, "team_name": "Ajax"}, {"team_id": 4, "team_name": "Dortmund"}, {"team_id": 6, "team_name": "Arsenal"}], "Matches": [{"home_team_id": 1, "away_team_id": 4, "home_team_goals": 0, "away_team_goals": 1}, {"home_team_id": 1, "away_team_id": 6, "home_team_goals": 3, "away_team_goals": 3}, {"home_team_id": 4, "away_team_id": 1, "home_team_goals": 5, "away_team_goals": 2}, {"home_team_id": 6, "away_team_id": 1, "home_team_goals": 0, "away_team_goals": 0}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

- The first `SELECT` describes the home team.
- The second `SELECT` describes the away team.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

`UNION ALL` combines them without deduplication. This matters because two rows with equal numeric statistics can still represent two real match appearances and must both be counted.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["team_name", "matches_played", "points", "goal_for", "goal_against", "goal_diff"], "rows": [["Dortmund", 2, 6, 6, 2, 4], ["Arsenal", 2, 2, 3, 3, 0], ["Ajax", 4, 2, 5, 9, -4]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Teams": [{"team_id": 1, "team_name": "Ajax"}, {"team_id": 4, "team_name": "Dortmund"}, {"team_id": 6, "team_name": "Arsenal"}], "Matches": [{"home_team_id": 1, "away_team_id": 4, "home_team_goals": 0, "away_team_goals": 1}, {"home_team_id": 1, "away_team_id": 6, "home_team_goals": 3, "away_team_goals": 3}, {"home_team_id": 4, "away_team_id": 1, "home_team_goals": 5, "away_team_goals": 2}, {"home_team_id": 6, "away_team_id": 1, "home_team_goals": 0, "away_team_goals": 0}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["team_name", "matches_played", "points", "goal_for", "goal_against", "goal_diff"], "rows": [["Dortmund", 2, 6, 6, 2, 4], ["Arsenal", 2, 2, 3, 3, 0], ["Ajax", 4, 2, 5, 9, -4]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Conditional aggregation without a union:** Join each team to matches where it is home or away and use `CASE` for perspective. It avoids doubling through a CTE but makes every aggregate expression more complex.
- **Start from `Teams` with a left join:** This is necessary if teams with zero matches must appear with zero statistics.
- **Plain `UNION`:** It can erase distinct match appearances that happen to produce identical projected values and must not replace `UNION ALL`.
- **Draw:** Both perspective rows receive score one, and each side’s goals for equal the other side’s goals against.
- **Home win:** Home receives three and away zero; the second branch deliberately reverses the comparison outcome.
- **Away win:** Away receives three and home zero.
- **Repeated scorelines:** `UNION ALL` retains all appearances, so identical match statistics still count separately.
- **Negative goal difference:** Subtracting aggregate goals against naturally produces a negative value and descending sorting ranks it below a larger difference.
- **Complete standings tie:** Team name ascending supplies the final deterministic order.
- **Team with no matches:** The exact inner-join query omits it rather than returning zeros.
- **Unique team name dependency:** Grouping by `team_id` relies on its unique Teams row to determine `team_name`; stricter SQL modes or other engines may prefer grouping by both.
- **Indexes:** Indexes on team identifiers help joins, but they do not change the query’s logical result.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(m + t\log t)$. Let `m` be the number of matches and `t` the number of teams. The CTE produces `2m` rows. Scanning matches and calculating perspective fields is `O(m)` logical work. Joining teams can be near linear with an index or hash plan, grouping processes the perspective rows, and final ordering of up to `t` participating teams costs `O(t log t)`. A representative overall bound is `O(m + t log t)`, subject to the database optimizer and available indexes.
- **Auxiliary Space Complexity:** $O(m + t)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
