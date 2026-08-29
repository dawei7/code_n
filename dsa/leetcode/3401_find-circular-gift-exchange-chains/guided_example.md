# Guided Example: Find Circular Gift Exchange Chains

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tables": {"SecretSanta": [{"giver_id": 1, "receiver_id": 2, "gift_value": 20}, {"giver_id": 2, "receiver_id": 3, "gift_value": 30}, {"giver_id": 3, "receiver_id": 1, "gift_value": 40}, {"giver_id": 4, "receiver_id": 5, "gift_value": 25}, {"giver_id": 5, "receiver_id": 4, "gift_value": 35}]}}`
- **Required output:** `{"columns": ["chain_id", "chain_length", "total_gift_value"], "rows": [[1, 3, 90], [2, 2, 60]]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Table: `SecretSanta`

The objective is to compute `{"columns": ["chain_id", "chain_length", "total_gift_value"], "rows": [[1, 3, 90], [2, 2, 60]]}` from `{"tables": {"SecretSanta": [{"giver_id": 1, "receiver_id": 2, "gift_value": 20}, {"giver_id": 2, "receiver_id": 3, "gift_value": 30}, {"giver_id": 3, "receiver_id": 1, "gift_value": 40}, {"giver_id": 4, "receiver_id": 5, "gift_value": 25}, {"giver_id": 5, "receiver_id": 4, "gift_value": 35}]}}` while avoiding redundant calculations and unnecessary overhead.

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

**Start one recursive walk from every exchange row.** The anchor of recursive CTE `chains` treats each giver as `start_id`, its receiver as `current_id`, the gift value as initial total, and length as one.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tables": {"SecretSanta": [{"giver_id": 1, "receiver_id": 2, "gift_value": 20}, {"giver_id": 2, "receiver_id": 3, "gift_value": 30}, {"giver_id": 3, "receiver_id": 1, "gift_value": 40}, {"giver_id": 4, "receiver_id": 5, "gift_value": 25}, {"giver_id": 5, "receiver_id": 4, "gift_value": 35}]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The recursive branch follows an exchange whose `giver_id` equals the current receiver. It advances to that exchange's receiver, adds gift value, and increments chain length.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Stop expanding after returning to the start.** Predicate `chains.current_id <> chains.start_id` is evaluated on the prior row. Once a row has `current_id=start_id`, it represents a completed loop and does not generate another lap.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"columns": ["chain_id", "chain_length", "total_gift_value"], "rows": [[1, 3, 90], [2, 2, 60]]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tables": {"SecretSanta": [{"giver_id": 1, "receiver_id": 2, "gift_value": 20}, {"giver_id": 2, "receiver_id": 3, "gift_value": 30}, {"giver_id": 3, "receiver_id": 1, "gift_value": 40}, {"giver_id": 4, "receiver_id": 5, "gift_value": 25}, {"giver_id": 5, "receiver_id": 4, "gift_value": 35}]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"columns": ["chain_id", "chain_length", "total_gift_value"], "rows": [[1, 3, 90], [2, 2, 60]]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Canonical cycle ID:** Carry the minimum member ID and group by it to keep equal-statistic cycles separate.
- **Visited-path string/set:** Prevent revisiting a node other than the start, though SQL representation is more complex.
- **Functional-graph traversal:** Enforce one outgoing edge and discover each cycle once procedurally.
- **Single self-loop:** It completes at length one, if such a row is allowed.
- **Two-node cycle:** Both anchors produce the same statistics and DISTINCT collapses rotations.
- **Separate equal cycles:** Exact query incorrectly merges them.
- **Closing edge:** It is included before the completed row stops recursing.
- **Identity loss:** `cycle_stats` retains no employee or canonical cycle key.
- **Path entering another cycle:** Recursion may never return to its own start.
- **Branching giver:** Recursive rows branch into multiple walks.
- **No cycle:** No completed row is emitted for a terminating dead end.
- **UNION ALL:** It preserves repeated paths needed for recursion but offers no duplicate-cycle protection.
- **Descending order:** Longer chains rank first, then larger totals.
- **Row-number stability:** A corrected query would need a tie breaker for equal statistics.
- **Generated source:** No authoritative editorial supports stronger assumptions.
- **Read-only query:** Source table is unchanged.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(e^2)$. Under disjoint simple cycles with $e$ exchange rows, each of $e$ anchors can traverse up to $e$ edges, producing $O(e^2)$ recursive rows and work. Materializing them can use $O(e^2)$ space, matching the manifest's stated bounds.
- **Auxiliary Space Complexity:** $O(e^2)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
