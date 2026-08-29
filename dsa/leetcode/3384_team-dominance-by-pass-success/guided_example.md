# Guided Example: Team Dominance by Pass Success

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"Teams": [{"player_id": 1, "team_name": "Arsenal"}, {"player_id": 2, "team_name": "Arsenal"}, {"player_id": 3, "team_name": "Arsenal"}, {"player_id": 4, "team_name": "Chelsea"}, {"player_id": 5, "team_name": "Chelsea"}, {"player_id": 6, "team_name": "Chelsea"}], "Passes": [{"pass_from": 1, "time_stamp": "00:15", "pass_to": 2}, {"pass_from": 2, "time_stamp": "00:45", "pass_to": 3}, {"pass_from": 3, "time_stamp": "01:15", "pass_to": 1}, {"pass_from": 4, "time_stamp": "00:30", "pass_to": 1}, {"pass_from": 2, "time_stamp": "46:00", "pass_to": 3}, {"pass_from": 3, "time_stamp": "46:15", "pass_to": 4}, {"pass_from": 1, "time_stamp": "46:45", "pass_to": 2}, {"pass_from": 5, "time_stamp": "46:30", "pass_to": 6}]}}`
- **Required output:** `{"columns": ["team_name", "half_number", "dominance"], "rows": [["Arsenal", 1, 3], ["Arsenal", 2, 1], ["Chelsea", 1, -1], ["Chelsea", 2, 1]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `Teams`

The objective is to compute `{"columns": ["team_name", "half_number", "dominance"], "rows": [["Arsenal", 1, 3], ["Arsenal", 2, 1], ["Chelsea", 1, -1], ["Chelsea", 2, 1]]}` from `{"tables": {"Teams": [{"player_id": 1, "team_name": "Arsenal"}, {"player_id": 2, "team_name": "Arsenal"}, {"player_id": 3, "team_name": "Arsenal"}, {"player_id": 4, "team_name": "Chelsea"}, {"player_id": 5, "team_name": "Chelsea"}, {"player_id": 6, "team_name": "Chelsea"}], "Passes": [{"pass_from": 1, "time_stamp": "00:15", "pass_to": 2}, {"pass_from": 2, "time_stamp": "00:45", "pass_to": 3}, {"pass_from": 3, "time_stamp": "01:15", "pass_to": 1}, {"pass_from": 4, "time_stamp": "00:30", "pass_to": 1}, {"pass_from": 2, "time_stamp": "46:00", "pass_to": 3}, {"pass_from": 3, "time_stamp": "46:15", "pass_to": 4}, {"pass_from": 1, "time_stamp": "46:45", "pass_to": 2}, {"pass_from": 5, "time_stamp": "46:30", "pass_to": 6}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Attribute each pass to the passer's team.** `Passes.pass_from` identifies the player attempting the pass. Joining `Teams t1` on that ID obtains the team whose dominance score must change.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"Teams": [{"player_id": 1, "team_name": "Arsenal"}, {"player_id": 2, "team_name": "Arsenal"}, {"player_id": 3, "team_name": "Arsenal"}, {"player_id": 4, "team_name": "Chelsea"}, {"player_id": 5, "team_name": "Chelsea"}, {"player_id": 6, "team_name": "Chelsea"}], "Passes": [{"pass_from": 1, "time_stamp": "00:15", "pass_to": 2}, {"pass_from": 2, "time_stamp": "00:45", "pass_to": 3}, {"pass_from": 3, "time_stamp": "01:15", "pass_to": 1}, {"pass_from": 4, "time_stamp": "00:30", "pass_to": 1}, {"pass_from": 2, "time_stamp": "46:00", "pass_to": 3}, {"pass_from": 3, "time_stamp": "46:15", "pass_to": 4}, {"pass_from": 1, "time_stamp": "46:45", "pass_to": 2}, {"pass_from": 5, "time_stamp": "46:30", "pass_to": 6}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

A second join, `Teams t2` on `pass_to`, obtains the receiver's team. Foreign-key guarantees make both inner joins appropriate: each pass endpoint should match exactly one player row because `player_id` is unique.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Classify the match half from the timestamp.** The CTE assigns

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["team_name", "half_number", "dominance"], "rows": [["Arsenal", 1, 3], ["Arsenal", 2, 1], ["Chelsea", 1, -1], ["Chelsea", 2, 1]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"Teams": [{"player_id": 1, "team_name": "Arsenal"}, {"player_id": 2, "team_name": "Arsenal"}, {"player_id": 3, "team_name": "Arsenal"}, {"player_id": 4, "team_name": "Chelsea"}, {"player_id": 5, "team_name": "Chelsea"}, {"player_id": 6, "team_name": "Chelsea"}], "Passes": [{"pass_from": 1, "time_stamp": "00:15", "pass_to": 2}, {"pass_from": 2, "time_stamp": "00:45", "pass_to": 3}, {"pass_from": 3, "time_stamp": "01:15", "pass_to": 1}, {"pass_from": 4, "time_stamp": "00:30", "pass_to": 1}, {"pass_from": 2, "time_stamp": "46:00", "pass_to": 3}, {"pass_from": 3, "time_stamp": "46:15", "pass_to": 4}, {"pass_from": 1, "time_stamp": "46:45", "pass_to": 2}, {"pass_from": 5, "time_stamp": "46:30", "pass_to": 6}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["team_name", "half_number", "dominance"], "rows": [["Arsenal", 1, 3], ["Arsenal", 2, 1], ["Chelsea", 1, -1], ["Chelsea", 2, 1]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

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
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(p log t + g log g)$. Let $p$ be the number of passes and $t$ the number of players. With indexes on unique/foreign-key player IDs, endpoint joins are typically $O(p\log t)$ or better via indexed lookups. Grouping $g$ team-half buckets and ordering them adds engine-dependent hashing/sorting work, summarized by the manifest as $O(p\log t+g\log g)$.
- **Auxiliary Space Complexity:** $O(g)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
