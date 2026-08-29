# Guided Example: Maximum Employees to Be Invited to a Meeting

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"favorite": [2, 2, 1, 2]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A company is organizing a meeting and has a list of `n` employees, waiting to be invited. They have arranged for a large **circular** table, capable of seating **any number** of employees.

The objective is to compute `3` from `{"favorite": [2, 2, 1, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: View favorites as a functional directed graph

Each employee has exactly one outgoing edge to their favorite. Every connected component of such a graph contains exactly one directed cycle, with directed trees feeding into its cycle vertices.

The circular seating constraint produces two fundamentally different usable structures:

- one directed cycle of length at least three;
- any number of mutual-favorite cycles of length two, each extended by incoming chains.

The source computes the best value for both categories and returns their maximum.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"favorite": [2, 2, 1, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Find the longest directed cycle

`max_cycle` uses a global `vis` array. From each unvisited employee `i`, it follows favorite edges and records the newly visited path in `cycle` until it reaches a globally visited vertex `j`.

If `j` occurs inside the current `cycle` list, the suffix beginning at that occurrence is the new directed cycle. The loop over `cycle` finds `j` and updates with `len(cycle) - k`.

If `j` belongs to an earlier traversal, it does not occur in the current list. No new cycle is counted because the current path merely feeds into a component whose cycle was already handled.

Taking the maximum gives the largest cycle length.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why a long cycle cannot accept an incoming chain

For a directed cycle of length at least three, every invited cycle employee needs their favorite, the next cycle vertex, adjacent. Arranging all directed favorite edges around the circular table consumes the cycle's seating adjacencies.

Inserting a chain employee between two cycle members would separate at least one employee from their favorite. Therefore, the usable invitation based on such a component is exactly the cycle itself.

Only one such long cycle can form the table arrangement, so the relevant value is the maximum cycle length rather than a sum over long cycles.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"favorite": [2, 2, 1, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Brute-force seating subsets:** Exponential and unnecessary once functional-graph structure is recognized.
- **Count only the longest cycle:** This misses the ability to combine multiple extended two-cycles.
- **Sum all cycles:** Long cycles cannot be concatenated while preserving every directed favorite adjacency.
- **Use every incoming branch:** Only one chain can attach to each free side of a two-cycle endpoint; `max` propagation keeps the longest.
- **Pure cycle of length three or more:** Its cycle length is the full contribution.
- **Single mutual pair:** Contribution is at least two and may include two chains.
- **Several mutual pairs:** Their extended segments are summed.
- **Path entering an old component:** `max_cycle` does not recount its already discovered cycle.
- **Self-favorites absent:** Makes the two-step return test identify only genuine pairs.
- **Distance initialization:** One counts the endpoint employee itself.
- **Topological leftovers:** They are exactly cycle vertices in a functional graph.
- **Input preservation:** Favorite edges are read but not changed.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of employees.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
