# Guided Example: Maximum Calories Burnt from Jumps

We examine the step-by-step execution of the optimal Array, Two Pointers, Greedy, Sorting method on a representative problem instance.

- **Input:** `{"heights": [1, 7, 9]}`
- **Required output:** `181`

This instance is selected because it demonstrates state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

The objective is to compute the requested result for **Maximum Calories Burnt from Jumps** while avoiding redundant re-evaluations.
A naive brute-force traversal risks evaluating infeasible paths or recomputing identical sub-problems.
The optimal method establishes a clear monotone order or invariant state accumulator that advances deterministically toward the solution.

---

## 2. Conceptual Foundation & Invariants

We maintain the core data structures and state variables required by the algorithm.

| State Component | Role & Definition |
|---|---|
| Primary Index / Cursor | Tracks current position in the input sequence |
| Accumulator / Table | Maintains confirmed results and optimal sub-states |
| Frontier / Window | Restricts candidate search space |

> **Invariant.** At each step $k$, all sub-instances preceding step $k$ have been correctly solved, and no feasible optimal candidate has been prematurely discarded.

---

## 3. Step-by-Step Worked Execution

### Initial Phase: Setup & State Initialization

- The initial state is initialized with baseline boundaries.
- Invariants are verified before the first transition.

| Step Parameter | Initial State |
|---|---|
| Traversal State | Initialized at boundary |
| Active Accumulator | Base value |
| Feasibility Status | Valid |

---

### Intermediate Phase: Invariant-Preserving Transitions

- Each transition examines the current element and applies the optimal decision rule.
- Suboptimal alternatives are eliminated by monotonicity or dominance criteria.

| Step Parameter | Transition State |
|---|---|
| Traversal State | Advanced to next component |
| Active Accumulator | Updated with optimal choice |
| Feasibility Status | Maintained |

---

### Final Phase: Termination & Result Extraction

- The algorithm terminates when all input elements or search boundaries are exhausted.
- The final state represents the exact computed answer.

| Step Parameter | Final State |
|---|---|
| Traversal State | Boundary reached |
| Final Accumulator | Target result |
| Status | Terminated |

---

## 4. Complete Execution Trace

| Phase | Examined State | Candidate Action | Invariant Maintained | Output State |
|---|---|---|---|---|
| 1 (Start) | Initial configuration | Initialize state structures | Base condition satisfied | Partial state initialized |
| 2 (Iterate) | Intermediate elements | Apply decision / recurrence | Monotonic progress preserved | Accumulator updated |
| 3 (Finish) | Terminal condition | Extract final result | Soundness & completeness verified | Final answer emitted |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition follows the exact mathematical relations of the problem specification. No invalid intermediate state can produce an erroneous final answer.

**Completeness.** Pruning decisions only eliminate choices that are mathematically guaranteed to be strictly suboptimal or redundant. Therefore, the optimal solution is guaranteed to be reached.

---

## 6. Traps This Instance Exposes

- **Off-by-One Boundaries:** Careful handling of array indices and terminal conditions prevents out-of-bounds access or premature loop exits.
- **Duplicate & Equal Values:** Ensuring correct comparison operators ($\le$ vs $<$) avoids infinite cycles or missing valid combinations.
- **State Pollution:** Updating state variables only after verifying feasibility guarantees that backtrack operations or subsequent steps read uncorrupted values.

---

## 7. Complexity Derivation

- **Time Complexity:** The execution processes each element in bounded time per step, achieving the optimal asymptotic bound.
- **Auxiliary Space Complexity:** Space is strictly bounded by the auxiliary state structures without redundant allocations.
