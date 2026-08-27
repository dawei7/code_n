# Guided Example: Design A Leaderboard

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operations": [["addScore", [1, 10]], ["addScore", [1, 15]], ["top", [1]]]}`
- **Required output:** `[null, null, 25]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Design a Leaderboard class, which has 3 functions:

The objective is to compute `[null, null, 25]` from `{"operations": [["addScore", [1, 10]], ["addScore", [1, 15]], ["top", [1]]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Maintain both player identity and sorted score order

The three operations need two different views of the same active players:

- `addScore` and `reset` must find a player by `playerId`.
- `top(K)` must access the greatest scores in sorted order.

One data structure is not ideal for both jobs, so the exact class keeps them synchronized:

- `d` maps every active player ID to that player’s current accumulated score.
- `rank` is a `SortedList` containing one score entry per active player, in nondecreasing order.

Tied scores appear multiple times in `rank` because different players still occupy different leaderboard positions.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operations": [["addScore", [1, 10]], ["addScore", [1, 15]], ["top", [1]]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Class invariant

After every mutating call:

1. the keys of `d` are exactly the active players;
2. `d[playerId]` is that player’s current score;
3. the multiset of values in `d` is exactly the multiset stored in `rank`.

All operation reasoning follows from preserving this invariant.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | After every mutating call:

1.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Adding a new player

If `playerId not in d`, the player has no active accumulated score. The code stores the supplied `score` in the dictionary and inserts that same value into the sorted list.

Both representations gain exactly one matching entry, so the invariant holds.

Although `d` is a `defaultdict(int)`, the source checks membership before reading a missing player. It therefore does not rely on automatic zero insertion for this operation.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[null, null, 25]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operations": [["addScore", [1, 10]], ["addScore", [1, 15]], ["top", [1]]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[null, null, 25]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Dictionary plus size-\(K\) heap per query:** U:** - **Dictionary plus size-\(K\) heap per query:** Updates are expected \(O(1)\), while `top(K)` costs \(O(p\log K)\), matching the manifest but repeating selection work.
- **Dictionary plus sort per query:** Simple, but each top call costs \(O(p\log p)\).
- **Score-frequency ordered map:** Store how many players have each score and traverse scores descending. It can reduce duplicated keys but needs an ordered-map implementation.
- **Tied scores:** `SortedList` stores duplicate values, so every tied player is counted separately.
- **Update an existing player:** The old score must be removed before the new total is inserted.
- **Reset then add again:** Reset erases the ID; a later score starts a new accumulation.
- **Guaranteed valid \(K\):** Negative slicing returns exactly \(K\) values because enough active players exist.
- **Guaranteed active reset:** The exact code raises if asked to reset an absent player, but such a call is outside the contract.
- **External dependency:** `SortedList` is not built into Python and must be available in the execution environment.
- **Input calls capped:** The source remains efficient across mixed operations without rebuilding the complete ranking.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(K)$. Let \(p\) be the number of active players.
- **Auxiliary Space Complexity:** $O(p)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
