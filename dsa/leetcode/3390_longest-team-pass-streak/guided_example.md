# Guided Example: Longest Team Pass Streak

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Teams": [{"player_id": 1, "team_name": "Arsenal"}, {"player_id": 2, "team_name": "Arsenal"}, {"player_id": 3, "team_name": "Arsenal"}, {"player_id": 4, "team_name": "Arsenal"}, {"player_id": 5, "team_name": "Chelsea"}, {"player_id": 6, "team_name": "Chelsea"}, {"player_id": 7, "team_name": "Chelsea"}, {"player_id": 8, "team_name": "Chelsea"}], "Passes": [{"pass_from": 1, "time_stamp": "00:05", "pass_to": 2}, {"pass_from": 2, "time_stamp": "00:07", "pass_to": 3}, {"pass_from": 3, "time_stamp": "00:08", "pass_to": 4}, {"pass_from": 4, "time_stamp": "00:10", "pass_to": 5}, {"pass_from": 6, "time_stamp": "00:15", "pass_to": 7}, {"pass_from": 7, "time_stamp": "00:17", "pass_to": 8}, {"pass_from": 8, "time_stamp": "00:20", "pass_to": 6}, {"pass_from": 6, "time_stamp": "00:22", "pass_to": 5}, {"pass_from": 1, "time_stamp": "00:25", "pass_to": 2}, {"pass_from": 2, "time_stamp": "00:27", "pass_to": 3}]}}`
- **Required output:** `{"columns": ["team_name", "longest_streak"], "rows": [["Arsenal", 3], ["Chelsea", 4]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Teams`

The objective is to compute `{"columns": ["team_name", "longest_streak"], "rows": [["Arsenal", 3], ["Chelsea", 4]]}` from `{"tables": {"Teams": [{"player_id": 1, "team_name": "Arsenal"}, {"player_id": 2, "team_name": "Arsenal"}, {"player_id": 3, "team_name": "Arsenal"}, {"player_id": 4, "team_name": "Arsenal"}, {"player_id": 5, "team_name": "Chelsea"}, {"player_id": 6, "team_name": "Chelsea"}, {"player_id": 7, "team_name": "Chelsea"}, {"player_id": 8, "team_name": "Chelsea"}], "Passes": [{"pass_from": 1, "time_stamp": "00:05", "pass_to": 2}, {"pass_from": 2, "time_stamp": "00:07", "pass_to": 3}, {"pass_from": 3, "time_stamp": "00:08", "pass_to": 4}, {"pass_from": 4, "time_stamp": "00:10", "pass_to": 5}, {"pass_from": 6, "time_stamp": "00:15", "pass_to": 7}, {"pass_from": 7, "time_stamp": "00:17", "pass_to": 8}, {"pass_from": 8, "time_stamp": "00:20", "pass_to": 6}, {"pass_from": 6, "time_stamp": "00:22", "pass_to": 5}, {"pass_from": 1, "time_stamp": "00:25", "pass_to": 2}, {"pass_from": 2, "time_stamp": "00:27", "pass_to": 3}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Join each pass to both endpoint teams.** `PassesWithTeams` joins `pass_from` to `Teams t1` and `pass_to` to `Teams t2`. Unique player IDs and foreign keys make each pass produce one enriched row.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Teams": [{"player_id": 1, "team_name": "Arsenal"}, {"player_id": 2, "team_name": "Arsenal"}, {"player_id": 3, "team_name": "Arsenal"}, {"player_id": 4, "team_name": "Arsenal"}, {"player_id": 5, "team_name": "Chelsea"}, {"player_id": 6, "team_name": "Chelsea"}, {"player_id": 7, "team_name": "Chelsea"}, {"player_id": 8, "team_name": "Chelsea"}], "Passes": [{"pass_from": 1, "time_stamp": "00:05", "pass_to": 2}, {"pass_from": 2, "time_stamp": "00:07", "pass_to": 3}, {"pass_from": 3, "time_stamp": "00:08", "pass_to": 4}, {"pass_from": 4, "time_stamp": "00:10", "pass_to": 5}, {"pass_from": 6, "time_stamp": "00:15", "pass_to": 7}, {"pass_from": 7, "time_stamp": "00:17", "pass_to": 8}, {"pass_from": 8, "time_stamp": "00:20", "pass_to": 6}, {"pass_from": 6, "time_stamp": "00:22", "pass_to": 5}, {"pass_from": 1, "time_stamp": "00:25", "pass_to": 2}, {"pass_from": 2, "time_stamp": "00:27", "pass_to": 3}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

`team_from` is the team whose streak is being measured. `same_team_flag` is one when passer and receiver team names match and zero for an interception.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `team_from` is the team whose streak is being measured.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Treat streaks independently per passer team.** The window in `StreakGroups` partitions by `team_from`. Passes made by another team do not enter this team's ordered sequence. Within one team's passes, an interception breaks its streak.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["team_name", "longest_streak"], "rows": [["Arsenal", 3], ["Chelsea", 4]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Teams": [{"player_id": 1, "team_name": "Arsenal"}, {"player_id": 2, "team_name": "Arsenal"}, {"player_id": 3, "team_name": "Arsenal"}, {"player_id": 4, "team_name": "Arsenal"}, {"player_id": 5, "team_name": "Chelsea"}, {"player_id": 6, "team_name": "Chelsea"}, {"player_id": 7, "team_name": "Chelsea"}, {"player_id": 8, "team_name": "Chelsea"}], "Passes": [{"pass_from": 1, "time_stamp": "00:05", "pass_to": 2}, {"pass_from": 2, "time_stamp": "00:07", "pass_to": 3}, {"pass_from": 3, "time_stamp": "00:08", "pass_to": 4}, {"pass_from": 4, "time_stamp": "00:10", "pass_to": 5}, {"pass_from": 6, "time_stamp": "00:15", "pass_to": 7}, {"pass_from": 7, "time_stamp": "00:17", "pass_to": 8}, {"pass_from": 8, "time_stamp": "00:20", "pass_to": 6}, {"pass_from": 6, "time_stamp": "00:22", "pass_to": 5}, {"pass_from": 1, "time_stamp": "00:25", "pass_to": 2}, {"pass_from": 2, "time_stamp": "00:27", "pass_to": 3}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["team_name", "longest_streak"], "rows": [["Arsenal", 3], ["Chelsea", 4]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **`LAG` plus cumulative breaks:** Compare rows a:** - **`LAG` plus cumulative breaks:** Compare rows and assign islands explicitly; the flag already makes cumulative failures sufficient.
- **Procedural scan per team:** It works after sorting but is less natural in SQL.
- **First successful streak:** It uses group zero.
- **Interception:** It increments the group and is excluded from length.
- **Consecutive interceptions:** They create empty group IDs, which cause no harm.
- **Filter timing:** Failures must influence the window before being removed.
- **First success after failures:** It starts the group with the current cumulative failure count.
- **No successful passes:** The exact query omits the team instead of returning zero.
- **Other-team pass between attempts:** It does not break this query's team-partitioned streak.
- **Same timestamp peers:** Ordering and default window-frame behavior are not fully specified.
- **Duplicate pass row:** Primary-key rules prevent the same passer/timestamp pair.
- **Team-name collation:** It controls equality, grouping, and final sort.
- **Receiver team:** It determines success but does not own the streak row.
- **Ordinal grouping:** `GROUP BY 1,2` depends on select-list order.
- **Final ordering:** Only team name is returned as the sort key.
- **Read-only behavior:** The CTE chain does not modify source tables.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(p\log p)$. Let $p$ be the number of passes and $t$ the player count. Indexed joins are typically $O(p\log t)$ or better. Partitioned timestamp ordering costs up to $O(p\log p)$, and subsequent grouping is linear or hash/sort dependent. This matches the manifest's high-level time bound.
- **Auxiliary Space Complexity:** $O(p)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
