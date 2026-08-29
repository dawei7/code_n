# Guided Example: Game Play Analysis III

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Activity": [{"player_id": 1, "device_id": 2, "event_date": "2016-03-01", "games_played": 5}, {"player_id": 1, "device_id": 2, "event_date": "2016-05-02", "games_played": 6}, {"player_id": 1, "device_id": 3, "event_date": "2017-06-25", "games_played": 1}, {"player_id": 3, "device_id": 1, "event_date": "2016-03-02", "games_played": 0}, {"player_id": 3, "device_id": 4, "event_date": "2018-07-03", "games_played": 5}]}}`
- **Required output:** `{"columns": ["player_id", "event_date", "games_played_so_far"], "rows": [[1, "2016-03-01", 5], [1, "2016-05-02", 11], [1, "2017-06-25", 12], [3, "2016-03-02", 0], [3, "2018-07-03", 5]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Activity`

The objective is to compute `{"columns": ["player_id", "event_date", "games_played_so_far"], "rows": [[1, "2016-03-01", 5], [1, "2016-05-02", 11], [1, "2017-06-25", 12], [3, "2016-03-02", 0], [3, "2018-07-03", 5]]}` from `{"tables": {"Activity": [{"player_id": 1, "device_id": 2, "event_date": "2016-03-01", "games_played": 5}, {"player_id": 1, "device_id": 2, "event_date": "2016-05-02", "games_played": 6}, {"player_id": 1, "device_id": 3, "event_date": "2017-06-25", "games_played": 1}, {"player_id": 3, "device_id": 1, "event_date": "2016-03-02", "games_played": 0}, {"player_id": 3, "device_id": 4, "event_date": "2018-07-03", "games_played": 5}]}}` while avoiding redundant calculations and unnecessary overhead.

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

The result needs one output row for every activity date, together with the player's cumulative number of games through that date. This is a running-sum problem, which SQL window functions express directly.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Activity": [{"player_id": 1, "device_id": 2, "event_date": "2016-03-01", "games_played": 5}, {"player_id": 1, "device_id": 2, "event_date": "2016-05-02", "games_played": 6}, {"player_id": 1, "device_id": 3, "event_date": "2017-06-25", "games_played": 1}, {"player_id": 3, "device_id": 1, "event_date": "2016-03-02", "games_played": 0}, {"player_id": 3, "device_id": 4, "event_date": "2018-07-03", "games_played": 5}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The query keeps `player_id` and `event_date` from each source row and computes:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

Unlike ordinary aggregation with `GROUP BY`, a window aggregate does not collapse many input rows into one row. It calculates a value over a related set of rows while preserving the current activity row. That is essential because the output needs every player-date combination, not one total per player.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["player_id", "event_date", "games_played_so_far"], "rows": [[1, "2016-03-01", 5], [1, "2016-05-02", 11], [1, "2017-06-25", 12], [3, "2016-03-02", 0], [3, "2018-07-03", 5]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Activity": [{"player_id": 1, "device_id": 2, "event_date": "2016-03-01", "games_played": 5}, {"player_id": 1, "device_id": 2, "event_date": "2016-05-02", "games_played": 6}, {"player_id": 1, "device_id": 3, "event_date": "2017-06-25", "games_played": 1}, {"player_id": 3, "device_id": 1, "event_date": "2016-03-02", "games_played": 0}, {"player_id": 3, "device_id": 4, "event_date": "2018-07-03", "games_played": 5}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["player_id", "event_date", "games_played_so_far"], "rows": [[1, "2016-03-01", 5], [1, "2016-05-02", 11], [1, "2017-06-25", 12], [3, "2016-03-02", 0], [3, "2018-07-03", 5]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Correlated cumulative subquery:** It is logically direct but may rescan one player's history for every date and become quadratic.
- **Non-equi self-join:** Join earlier rows to each current row and aggregate them. It works but can create a much larger intermediate relation.
- **Ordinary `GROUP BY player_id`:** It returns only one total per player and loses the required per-date history.
- **Window without partitioning:** It would mix games from different players.
- **Window without date ordering:** It would compute a partition total or an undefined running sequence rather than chronological progress.
- **Player with one event:** The running total is simply that row's `games_played`.
- **Zero games on a date:** The row remains in the output and carries forward the prior total.
- **Different players with interleaved calendar dates:** Partitioning keeps their totals independent even if physical rows are interleaved.
- **Unique player-date key:** It removes ambiguity among equal-date peers within one partition.
- **Output order:** The problem accepts any order; internal window ordering does not promise final row presentation.
- **Current-row inclusion:** The default cumulative frame includes the event's own games, matching “through that date.”
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(A)$. Let $A$ be the number of activity rows. A typical execution partitions and orders rows by player and date. Without a supporting order, sorting can take $O(A\log A)$ time and the window/result processing adds $O(A)$, giving the manifest's $O(A\log A)$ bound.
- **Auxiliary Space Complexity:** $O(A)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
