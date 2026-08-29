# Guided Example: Minimum Processing Time

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"processorTime": [8, 10], "tasks": [2, 2, 3, 1, 8, 7, 4, 5]}`
- **Required output:** `16`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You have a certain number of processors, each having 4 cores. The number of tasks to be executed is four times the number of processors. Each task must be assigned to a unique core, and each core can only be used once.

The objective is to compute `16` from `{"processorTime": [8, 10], "tasks": [2, 2, 3, 1, 8, 7, 4, 5]}` while avoiding redundant calculations and unnecessary overhead.

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

**Each processor receives exactly four simultaneous tasks.** A processor has four cores, and every core is used once. If a processor becomes available at time $p$ and receives task durations $d_1,d_2,d_3,d_4$, their completion times are $p+d_1$ through $p+d_4$. Since the cores run in parallel, that processor finishes its assigned work at

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"processorTime": [8, 10], "tasks": [2, 2, 3, 1, 8, 7, 4, 5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 3

The three shorter tasks in the group do not affect the global completion time once the group's longest task is known. The assignment problem can therefore be viewed as forming groups of four tasks, then pairing each group maximum with a processor availability time.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

**Sort processors from early to late.** `processorTime.sort()` places the smallest availability first. An early processor has more room to absorb a long task without creating a large sum, so it should receive a group with a large maximum. A late processor should receive a smaller group maximum.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `16` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"processorTime": [8, 10], "tasks": [2, 2, 3, 1, 8, 7, 4, 5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `16` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Heap assignment:** Repeatedly choosing processors and tasks with heaps adds complexity; one global sort exposes the optimal opposite ordering directly.
- **Arbitrary task groups:** Spreading the four largest tasks across four processors creates four large group maxima instead of one and can only hurt.
- **One processor:** All four tasks run on its cores, and the answer is its availability plus the longest duration.
- **Equal processor times:** Their relative ordering is irrelevant.
- **Equal task durations:** Any grouping among tied values has the same maxima.
- **Only group maxima matter:** The other three tasks still occupy cores but finish no later than the maximum-duration task.
- **Large values:** Availability plus duration can reach $2\times10^9$, which fits signed 32-bit only narrowly; wider arithmetic is safer in general.
- **Input mutation:** Both arrays finish sorted, so copy them first when original ordering must be retained.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(p\log p)$. Let $p$ be the number of processors; there are exactly $4p$ tasks. Sorting processors costs $O(p\log p)$. Sorting tasks costs $O(4p\log(4p))=O(p\log p)$. The final loop visits $p$ processors, so total time is $O(p\log p)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
