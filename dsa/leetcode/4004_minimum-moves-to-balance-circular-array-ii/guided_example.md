# Guided Example: Minimum Moves to Balance Circular Array II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"balance": [-1, 2, -1]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a circular array `balance` of length `n`, where $\text{balance}[i]$ is the net balance of person `i`.

The objective is to compute `2` from `{"balance": [-1, 2, -1]}` while avoiding redundant calculations and unnecessary overhead.

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

**Total balance gives the feasibility test.**  A move transfers one unit from one person to a neighbor. It changes where a unit is located but does not change the sum of all balances.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"balance": [-1, 2, -1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

If `sum(balance) < 0`, the circle has more total deficit than total supply. No sequence of transfers can make every entry non-negative, so the source returns `-1`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | If `sum(balance) < 0`, the circle has more total deficit tha... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

If the total is non-negative, the positive entries contain at least enough units to fill every negative entry. Because the circle is connected, units can be moved along neighbor edges from any surplus position to any deficit position. Feasibility then follows.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"balance": [-1, 2, -1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Greedily use the nearest surplus:** Local near:** - **Greedily use the nearest surplus:** Local nearest choices can consume supply needed more efficiently elsewhere. Residual min-cost flow supports global reassignment.
- **Expand every unit into a graph node:** This makes the graph depend on balance magnitudes. Capacities represent many identical units compactly.
- **Dijkstra without potentials:** Negative reverse-edge costs appear after augmentation, so ordinary Dijkstra is not valid on the residual graph.
- **Heap Dijkstra with reduced-cost potentials:** This is a standard faster min-cost-flow implementation and resembles the manifest summary, but it is not the algorithm in the exact source.
- **Specialized circular transport mathematics:** The ring structure may permit a more specialized optimization, but the stored solution uses a general residual flow network.
- **Negative total balance:** Conservation makes success impossible, and the early `-1` return avoids graph construction.
- **No deficits:** Positive and zero entries already satisfy the goal, so the answer is zero even if total balance is large.
- **Extra total supply:** Only `total_deficit` units are sent. Unused positive balance does not need to move.
- **Zero balances:** They create neither source nor sink edges but may carry flow through their neighbor edges.
- **One-element array:** A negative value fails the total check; a non-negative value has zero deficit. Both outcomes occur before circular self-edges matter.
- **Two-element circle:** Left and right neighbors are the same person, so the source creates parallel cost-one edges. They do not change the minimum cost.
- **Large balance magnitudes:** Capacities aggregate units, but the safe SPFA iteration bound still depends on total deficit `F`.
- **Reverse residual edges:** Their negative costs do not represent negative physical moves. They represent canceling previously sent flow during optimization.
- **Disconnected-path check:** With sufficient total supply and the fully connected circle, a path should exist until every deficit is filled. The final conditional still returns `-1` if the requested flow was not achieved.
- **Missing dependencies:** Actual execution requires `List`, `inf`, and `deque` to be defined or imported.
- **Manifest complexity:** `O(n^2 \log n)` should not be attributed to this exact SPFA implementation; its worst-case analysis must include `F` and SPFA's `O(VE)` behavior.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(Fn^2)$. Let `n` be the array length, and let
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
