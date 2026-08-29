# Guided Example: Grand Slam Titles

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Players": [{"player_id": 1, "player_name": "Nadal"}, {"player_id": 2, "player_name": "Federer"}, {"player_id": 3, "player_name": "Novak"}], "Championships": [{"year": 2018, "Wimbledon": 1, "Fr_open": 1, "US_open": 1, "Au_open": 1}, {"year": 2019, "Wimbledon": 1, "Fr_open": 1, "US_open": 2, "Au_open": 2}, {"year": 2020, "Wimbledon": 2, "Fr_open": 1, "US_open": 2, "Au_open": 2}]}}`
- **Required output:** `{"columns": ["player_id", "player_name", "grand_slams_count"], "rows": [[1, "Nadal", 7], [2, "Federer", 5]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Players`

The objective is to compute `{"columns": ["player_id", "player_name", "grand_slams_count"], "rows": [[1, "Nadal", 7], [2, "Federer", 5]]}` from `{"tables": {"Players": [{"player_id": 1, "player_name": "Nadal"}, {"player_id": 2, "player_name": "Federer"}, {"player_id": 3, "player_name": "Novak"}], "Championships": [{"year": 2018, "Wimbledon": 1, "Fr_open": 1, "US_open": 1, "Au_open": 1}, {"year": 2019, "Wimbledon": 1, "Fr_open": 1, "US_open": 2, "Au_open": 2}, {"year": 2020, "Wimbledon": 2, "Fr_open": 1, "US_open": 2, "Au_open": 2}]}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Unpivot four winner columns into one stream

Each `Championships` row stores four tournament winners in separate columns. Counting titles by player is easier when every title is represented as one row with one `player_id`.

The common table expression `T` selects `Wimbledon`, `Fr_open`, `US_open`, and `Au_open` in four branches, aliasing each as `player_id`. `UNION ALL` concatenates those branches.

For every championship year, `T` therefore contains exactly four rows, one per Grand Slam title.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Players": [{"player_id": 1, "player_name": "Nadal"}, {"player_id": 2, "player_name": "Federer"}, {"player_id": 3, "player_name": "Novak"}], "Championships": [{"year": 2018, "Wimbledon": 1, "Fr_open": 1, "US_open": 1, "Au_open": 1}, {"year": 2019, "Wimbledon": 1, "Fr_open": 1, "US_open": 2, "Au_open": 2}, {"year": 2020, "Wimbledon": 2, "Fr_open": 1, "US_open": 2, "Au_open": 2}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why UNION ALL is essential

The same player can win several tournaments or win across several years. Every occurrence is a separate title and must be counted.

Plain `UNION` would remove duplicate player identifiers and destroy multiplicity. `UNION ALL` preserves every winner occurrence, so repeated IDs correctly represent repeated victories.

The `year` column is not needed after unpivoting because the task asks only for total titles, not a year-by-year report.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Join winner identifiers to player names

`T JOIN Players USING (player_id)` matches every title occurrence to its player row.

The inner join returns only winner IDs that exist in `Players` and supplies `player_name` for output. Under the schema's intended referential data, every championship winner corresponds to a player.

Players who never won have no row in `T`, so they cannot enter the join. This naturally satisfies the requirement to omit zero-title players without a `HAVING` clause.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["player_id", "player_name", "grand_slams_count"], "rows": [[1, "Nadal", 7], [2, "Federer", 5]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Players": [{"player_id": 1, "player_name": "Nadal"}, {"player_id": 2, "player_name": "Federer"}, {"player_id": 3, "player_name": "Novak"}], "Championships": [{"year": 2018, "Wimbledon": 1, "Fr_open": 1, "US_open": 1, "Au_open": 1}, {"year": 2019, "Wimbledon": 1, "Fr_open": 1, "US_open": 2, "Au_open": 2}, {"year": 2020, "Wimbledon": 2, "Fr_open": 1, "US_open": 2, "Au_open": 2}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["player_id", "player_name", "grand_slams_count"], "rows": [[1, "Nadal", 7], [2, "Federer", 5]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Four joins or correlated counts:** They repeat logic and are more verbose than unpivoting once.
- **UNION instead of UNION ALL:** It is incorrect because it removes repeated wins by the same player.
- **Conditional aggregation per Players row:** Count matches across four columns, but it can require cumbersome joins and expressions.
- **Player wins multiple tournaments in one year:** Each column contributes a separate CTE row and title.
- **Player wins across years:** Repeated rows remain and are all counted.
- **Player wins nothing:** No CTE occurrence exists, so the player is omitted.
- **One winning player:** All title rows group under one identifier.
- **Primary-key player name:** Grouping by ID determines one consistent name.
- **Year not selected:** It is irrelevant to the requested lifetime total.
- **Four fixed tournaments:** Exactly four UNION ALL branches cover the schema.
- **COUNT(1):** It counts every joined title row, equivalent to `COUNT(*)` here.
- **Inner join:** It deliberately begins from winners rather than retaining every player.
- **Ordinal grouping:** `GROUP BY 1` depends on `player_id` being the first selected expression.
- **Any output order:** No ordering clause is required.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(C + K)$. Let $C$ be the number of championship-year rows and $K$ the number of distinct winning players. The four CTE branches scan or project $4C=O(C)$ title occurrences.
- **Auxiliary Space Complexity:** $O(C + K)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
