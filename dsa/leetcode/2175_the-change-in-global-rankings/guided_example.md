# Guided Example: The Change in Global Rankings

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"TeamPoints": [{"team_id": 3, "name": "Algeria", "points": 1431}, {"team_id": 1, "name": "Senegal", "points": 2132}, {"team_id": 2, "name": "New Zealand", "points": 1402}, {"team_id": 4, "name": "Croatia", "points": 1817}], "PointsChange": [{"team_id": 3, "points_change": 399}, {"team_id": 2, "points_change": 0}, {"team_id": 4, "points_change": 13}, {"team_id": 1, "points_change": -22}]}}`
- **Required output:** `{"columns": ["team_id", "name", "rank_diff"], "rows": [[1, "Senegal", 0], [4, "Croatia", -1], [3, "Algeria", 1], [2, "New Zealand", 0]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `TeamPoints`

The objective is to compute `{"columns": ["team_id", "name", "rank_diff"], "rows": [[1, "Senegal", 0], [4, "Croatia", -1], [3, "Algeria", 1], [2, "New Zealand", 0]]}` from `{"tables": {"TeamPoints": [{"team_id": 3, "name": "Algeria", "points": 1431}, {"team_id": 1, "name": "Senegal", "points": 2132}, {"team_id": 2, "name": "New Zealand", "points": 1402}, {"team_id": 4, "name": "Croatia", "points": 1817}], "PointsChange": [{"team_id": 3, "points_change": 399}, {"team_id": 2, "points_change": 0}, {"team_id": 4, "points_change": 13}, {"team_id": 1, "points_change": -22}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Prepare one change value per team

CTE `P` reads `PointsChange` and groups by `team_id`. It returns `SUM(points_change) AS delta`.

The schema already says `team_id` is unique in `PointsChange`, so each group normally contains one row and `delta` equals that row's `points_change`. The aggregation is therefore defensive rather than necessary under the stated contract. It would also combine multiple change records correctly if such rows were ever supplied.

Naming the value `delta` makes the later updated score expression concise: `points + delta`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"TeamPoints": [{"team_id": 3, "name": "Algeria", "points": 1431}, {"team_id": 1, "name": "Senegal", "points": 2132}, {"team_id": 2, "name": "New Zealand", "points": 1402}, {"team_id": 4, "name": "Croatia", "points": 1817}], "PointsChange": [{"team_id": 3, "points_change": 399}, {"team_id": 2, "points_change": 0}, {"team_id": 4, "points_change": 13}, {"team_id": 1, "points_change": -22}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Join changes to the team facts

`TeamPoints JOIN P USING (team_id)` pairs every team's name and original points with its delta. The contract guarantees that every `team_id` in `TeamPoints` appears in `PointsChange`, so the inner join does not discard a team.

`USING (team_id)` also exposes one shared `team_id` column instead of two duplicate key columns. The select list can therefore refer to `team_id` without qualifying a table name.

The query calculates updated scores as expressions. It does not update either source table, which is appropriate because the task asks for a result table rather than a persistent data modification.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Rank the original standings

The first window expression is

`RANK() OVER (ORDER BY points DESC, name)`.

Higher point totals appear first because of `DESC`. When two teams have equal points, the second key `name` uses ascending order by default, giving the required lexicographical tie-break.

Window ranking sees the complete joined result because there is no `PARTITION BY`. This is a global ranking, not a separate rank per group or country.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["team_id", "name", "rank_diff"], "rows": [[1, "Senegal", 0], [4, "Croatia", -1], [3, "Algeria", 1], [2, "New Zealand", 0]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"TeamPoints": [{"team_id": 3, "name": "Algeria", "points": 1431}, {"team_id": 1, "name": "Senegal", "points": 2132}, {"team_id": 2, "name": "New Zealand", "points": 1402}, {"team_id": 4, "name": "Croatia", "points": 1817}], "PointsChange": [{"team_id": 3, "points_change": 399}, {"team_id": 2, "points_change": 0}, {"team_id": 4, "points_change": 13}, {"team_id": 1, "points_change": -22}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["team_id", "name", "rank_diff"], "rows": [[1, "Senegal", 0], [4, "Croatia", -1], [3, "Algeria", 1], [2, "New Zealand", 0]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

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
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n \log n)$. Let $N$ be the number of teams. CTE `P` scans and groups $O(N)$ change rows under the schema. The join processes $O(N)$ teams with an indexed, hash, or otherwise optimized key lookup in typical execution.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
