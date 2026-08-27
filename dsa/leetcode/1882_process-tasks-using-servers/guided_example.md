# Guided Example: Process Tasks Using Servers

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"servers": [3, 3, 2], "tasks": [1, 2, 3, 2, 1, 2]}`
- **Required output:** `[2, 2, 0, 2, 1, 2]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two **0-indexed** integer arrays `servers` and `tasks` of lengths `n`​​​​​​ and `m`​​​​​​ respectively. $\text{servers}[i]$ is the **weight** of the $i^​​​​​​th$​​​​ server, and $\text{tasks}[j]$ is the **time needed** to process the $j^​​​​​​th$​​​​ task **in seconds**.

The objective is to compute `[2, 2, 0, 2, 1, 2]` from `{"servers": [3, 3, 2], "tasks": [1, 2, 3, 2, 1, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

**Two different priorities require two heaps.** A free server is selected by smallest weight and then smallest index. A busy server becomes relevant first by earliest completion time, with weight and index breaking ties when several become free together. One ordering cannot represent both roles cleanly. The source therefore maintains `idle` entries as `(weight, index)` and `busy` entries as `(finish_time, weight, index)`. Python compares tuples lexicographically, exactly matching each required priority sequence.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"servers": [3, 3, 2], "tasks": [1, 2, 3, 2, 1, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

**Initialize every server as available.** The list comprehension creates `(x, i)` for each server weight `x` and index `i`, then `heapify(idle)` builds the free-server min-heap in linear time. `busy` starts empty because no task has been assigned. At all later times, each server appears in exactly one of these heaps: free in `idle` or running an assigned task in `busy`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | **Initialize every server as available.** The list comprehen... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Use task index as its arrival second.** The loop `for j, t in enumerate(tasks)` processes tasks in queue order, and task `j` arrives at second `j`. Before assigning it, the `while` loop moves every busy entry with `finish_time <= j` back into `idle`. Such a server has completed by the task's arrival, so it is legally free. Moving all of them—not just the first—ensures that the free-server heap can compare their weights and indices together.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[2, 2, 0, 2, 1, 2]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"servers": [3, 3, 2], "tasks": [1, 2, 3, 2, 1, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[2, 2, 0, 2, 1, 2]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Scan all servers for every task:** This can fi:** - **Scan all servers for every task:** This can find the right choice but costs $O(NM)$ and wastes work on servers that cannot win. Heaps expose only the relevant minimum.
- **One heap for all servers:** Free-server priority begins with weight, while busy-server priority begins with finish time. Combining the states without an availability distinction makes comparisons incorrect or forces repeated rebuilding.
- **Explicit second-by-second simulation:** Advancing through empty time intervals is unnecessary and can be enormous. The busy heap jumps directly to the next completion event.
- **One server:** Every task is assigned to index zero. When work queues up, the else branch repeatedly extends that server's finish time correctly.
- **Equal server weights:** The second tuple component, index, deterministically selects the smallest index in `idle` and after tied completion times in `busy`.
- **Several servers finish simultaneously:** Their busy tuples share the first component, so weight and index supply the specified order. Multiple queued tasks consume them in task order.
- **A server finishes exactly at task arrival:** The `<= j` release condition makes it free before assignment at second `j`, as required.
- **Long queue extending beyond all arrival times:** Tasks are still processed in input order. Repeated earliest-finish pops schedule each one at the next legal event even though the loop variable remains its original arrival index.
- **Output versus auxiliary memory:** The answer necessarily stores $M$ indices. The manifest's $O(N)$ describes heap state; including output makes the total $O(N+M)$.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O((N+M)$. Let $N$ be the number of servers and $M$ the number of tasks. Building and heapifying `idle` costs $O(N)$. Every task performs one server selection and one insertion, each involving a heap of at most $N$ servers and costing $O(\log N)$. A busy server moved to idle is popped and pushed, but across the algorithm such movements are associated with completed assignments and total $O(M)$ events. Total time is $O((N+M)\log N)$, with heap construction itself linear.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
