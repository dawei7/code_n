# Guided Example: Dota2 Senate

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"senate": "RD"}`
- **Required output:** `"Radiant"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

In the world of Dota2, there are two parties: the Radiant and the Dire.

The objective is to compute `"Radiant"` from `{"senate": "RD"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Model turns instead of repeatedly editing the string

The procedure repeatedly visits senators in circular left-to-right order. Banned senators disappear from all future rounds, while surviving senators eventually act again. Physically deleting characters and restarting scans would be expensive and difficult to reason about.

The solution instead stores the future turn positions of currently eligible senators:

- `qr` contains Radiant turn positions in increasing order;
- `qd` contains Dire turn positions in increasing order.

Initially, these positions are the original string indices. A surviving senator's position in the next round is represented by adding `n` to the position just used. This creates one increasing global timeline across all rounds.

For example, original index two acts at positions two, `2 + n`, `2 + 2n`, and so on if the senator survives that long. The numeric value is not a literal compacted-array index; it is an ordering label that tells us when the turn occurs.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"senate": "RD"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build one queue per party

The initialization scans `senate` from left to right. Each `R` index is appended to `qr` and each `D` index to `qd`. Because the scan indices increase, both queues start sorted by future turn order.

Keeping the parties separate makes the next active member of either party available at the front. A `deque` is used because removing from the front and appending to the back both take constant time.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why only the two queue fronts need to be compared

Suppose `qr[0]` is the earliest future Radiant turn and `qd[0]` is the earliest future Dire turn. Whichever number is smaller acts first. A smart senator should ban an opposing senator, and banning the earliest opposing turn is safe: that opponent is the most immediate threat and would otherwise act before all later opponents.

If the Radiant index is smaller, that Radiant senator acts first and bans the Dire senator at `qd[0]`. The Radiant senator remains eligible for a future round, while that Dire senator disappears permanently. The opposite happens when the Dire index is smaller.

Original indices and requeued timeline positions are unique, so the two fronts cannot be equal.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"Radiant"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"senate": "RD"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"Radiant"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Repeated string simulation:** Mark or remove banned senators and scan round after round. Physical deletion from a list or string can cost linear time per ban and lead to quadratic behavior.
- **One queue with a party balance:** A single queue can track pending bans for each side and requeue survivors. It can also achieve `O(N)` time, but the two-queue timeline makes the next opposing turns explicit.
- **Boolean banned array:** Keep original indices and search circularly for the next unbanned opponent. Without an efficient index structure, repeated searching can scan many inactive positions.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let `N` be the original number of senators.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
