# Guided Example: Range Module

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operations": [["queryRange", 1, 2], ["addRange", 1, 2], ["queryRange", 1, 2]]}`
- **Required output:** `[false, true]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A Range Module is a module that tracks ranges of numbers. Design a data structure to track the ranges represented as **half-open intervals** and query about them.

The objective is to compute `[false, true]` from `{"operations": [["queryRange", 1, 2], ["addRange", 1, 2], ["queryRange", 1, 2]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Meaning of a node

Each node represents one inclusive coordinate segment determined by recursive parameters `l,r`.

`node.v` is true exactly when the entire represented segment is tracked. A false value means at least one point is untracked; it may mean the whole segment is untracked or the segment is mixed.

`node.add` is a lazy assignment tag:

- `1` means the whole segment is tracked;
- `-1` means the whole segment is untracked;
- `0` means no uniform assignment is waiting to be propagated.

Children are created only when a partial operation needs them.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operations": [["queryRange", 1, 2], ["addRange", 1, 2], ["queryRange", 1, 2]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Initial state

The root is false with no children and no lazy tag. This represents an entirely untracked domain.

Not allocating all coordinates is essential: the domain has one billion positions, while at most ten thousand operations occur.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The root is false with no children and no lazy tag.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Full-cover modification

If a node's segment lies completely within the update interval, the method does not descend.

For an add update, it sets `add = 1` and `v = true`. For removal, it sets `add = -1` and `v = false`.

This assignment overwrites any earlier state throughout the covered segment, exactly matching range add/remove semantics.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[false, true]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operations": [["queryRange", 1, 2], ["addRange", 1, 2], ["queryRange", 1, 2]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[false, true]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Sorted disjoint intervals:** Maintain merged h:** - **Sorted disjoint intervals:** Maintain merged half-open intervals. Queries can be logarithmic, while additions/removals may touch many stored intervals.
- **- **Coordinate compression:** It is difficult onli:** - **Coordinate compression:** It is difficult online because future endpoints are unknown, but possible offline when all operations are available first.
- **- **Adjacent ranges:** Half-open ranges `[a,b)` an:** - **Adjacent ranges:** Half-open ranges `[a,b)` and `[b,c)` touch without overlapping but together fully cover `[a,c)` after both are added.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(q\log C)$. Let `C = 10^9` be the coordinate-domain width and `q` the number of operations.
- **Auxiliary Space Complexity:** $O(q\log C)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
