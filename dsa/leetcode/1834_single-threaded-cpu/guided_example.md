# Guided Example: Single-Threaded CPU

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tasks": [[1, 2], [2, 4], [3, 2], [4, 1]]}`
- **Required output:** `[0, 2, 3, 1]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given `n`​​​​​​ tasks labeled from `0` to $n - 1$ represented by a 2D integer array `tasks`, where $\text{tasks}[i] = [\text{enqueueTime}_{i}, \text{processingTime}_{i}]$ means that the $i^​​​​​​th$​​​​ task will be available to process at $\text{enqueueTime}_{i}$ and will take $\text{processingTime}_{i}$_ to finish processing.

The objective is to compute `[0, 2, 3, 1]` from `{"tasks": [[1, 2], [2, 4], [3, 2], [4, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

**Separate future tasks from currently available tasks.** At any CPU decision time, tasks fall into two groups. Future tasks have an enqueue time greater than the current time and cannot be selected. Available tasks have already arrived, and the CPU must choose the one with smallest processing time, breaking ties by original index.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tasks": [[1, 2], [2, 4], [3, 2], [4, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The solution represents those groups with two ordered structures:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The solution represents those groups with two ordered struct... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

- The mutated and sorted `tasks` list supplies future tasks in enqueue-time order.
- The min-heap `q` stores available tasks as pairs `(processing_time, original_index)`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[0, 2, 3, 1]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tasks": [[1, 2], [2, 4], [3, 2], [4, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[0, 2, 3, 1]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Repeatedly scan all tasks:** At each decision,:** - **Repeatedly scan all tasks:** At each decision, searching all unprocessed tasks for eligible minimum work can take `O(n^2)` time.
- **Sort the available list after every completion:** This models the policy but repeatedly sorts overlapping collections. A heap maintains the next minimum incrementally.
- **Build non-mutating triples:** Creating `(enqueue, processing, index)` tuples preserves the caller’s input and has the same `O(n log n)` time and `O(n)` space.
- **Long idle gap:** When `q` is empty, time jumps directly to the next enqueue time rather than advancing unit by unit.
- **Several tasks enqueue together:** The insertion loop pushes all of them before selection, so processing time and index decide correctly.
- **Equal processing times:** Tuple ordering uses original index as the second key, satisfying the required tie-break.
- **Task arrives exactly when another finishes:** Its enqueue time is `<= t`, so it enters the heap before the next selection.
- **Task arrives during execution:** Non-preemption means it waits until completion; the next insertion pass then makes it available.
- **One task:** Time jumps to its enqueue time, it is pushed and popped once, and its index is returned.
- **All tasks already available:** The heap receives them together and drains according to the scheduling priority.
- **Large accumulated time:** Python avoids overflow, while other languages should not store `t` in a 32-bit integer.
- **Input mutation:** Every inner list gains an index and the outer list is sorted. Callers requiring preservation must pass a copy or use a separate triple list.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n log n)$. Let `n = tasks.length`. Appending indices takes `O(n)` time. Sorting the task triples takes `O(n log n)`. Every task is pushed into the heap once and popped once; each heap operation costs `O(log n)` in the worst case. The total running time is therefore `O(n log n)`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
