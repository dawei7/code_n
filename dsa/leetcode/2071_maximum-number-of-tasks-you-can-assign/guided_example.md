# Guided Example: Maximum Number of Tasks You Can Assign

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tasks": [3, 2, 1], "workers": [0, 3, 3], "pills": 1, "strength": 1}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You have `n` tasks and `m` workers. Each task has a strength requirement stored in a **0-indexed** integer array `tasks`, with the $$i^{\text{th}}$$ task requiring $\text{tasks}[i]$ strength to complete. The strength of each worker is stored in a **0-indexed** integer array `workers`, with the $$j^{\text{th}}$$ worker having $\text{workers}[j]$ strength. Each worker can only be assigned to a **single** task and must have a strength **greater than or equal** to the task's strength requirement (i.e., $\text{workers}[j] \ge \text{tasks}[i]$).

The objective is to compute `3` from `{"tasks": [3, 2, 1], "workers": [0, 3, 3], "pills": 1, "strength": 1}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Binary-search how many tasks can be completed

If `x` tasks can be assigned, then any smaller number can be assigned by discarding some task-worker pairs. Feasibility is monotone.

The source sorts tasks and workers, then binary-searches `x` from zero through `min(n,m)`. A successful midpoint moves the lower bound upward; a failure moves the upper bound downward.

The upper-middle expression prevents an infinite loop when two candidates remain.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tasks": [3, 2, 1], "workers": [0, 3, 3], "pills": 1, "strength": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Choose the easiest tasks and strongest workers

To test `x`, it is sufficient and optimal to use `tasks[0:x]`, the `x` easiest requirements. Replacing any selected task with a harder unselected task cannot improve feasibility.

Similarly, use `workers[m-x:m]`, the `x` strongest workers. Replacing one with a weaker excluded worker cannot help.

The check must decide whether these two selected groups can be paired using at most the available pills.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | To test `x`, it is sufficient and optimal to use `tasks[0:x]... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Process selected workers from weakest to strongest

The loop begins at worker index `m-x` and moves upward. At each worker, pointer `i` adds every still-unadded selected task satisfying

`tasks[i] <= workers[j] + strength`.

These are exactly the remaining tasks this worker could perform if given a pill. Because tasks are sorted, they enter deque `q` from easiest to hardest.

Tasks too hard even with a pill stay outside until a stronger worker is processed.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tasks": [3, 2, 1], "workers": [0, 3, 3], "pills": 1, "strength": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Sorted multiset check:** Process hardest tasks:** - **Sorted multiset check:** Process hardest tasks and remove chosen workers in $O(\log R)$ each, yielding an extra logarithmic factor.
- **Try every task count linearly:** Repeats feasibility work and loses monotonic binary search.
- **Zero pills:** Every assigned worker must meet its task directly.
- **Zero strength:** Pills provide no benefit, though the check can still spend them harmlessly only when equality permits.
- **More pills than tasks:** At most one is used per selected worker.
- **Worker handles task exactly:** No pill is needed because comparison is inclusive.
- **Task too hard even with pill:** It is not enqueued for that worker.
- **Empty deque:** Proves the current selected worker cannot be assigned.
- **Duplicate requirements or strengths:** Sorted ordering and deque multiplicity preserve separate tasks and workers.
- **Zero tasks feasible:** Provides the binary-search base.
- **Strongest workers:** Testing any weaker group cannot improve feasibility.
- **Input mutation:** Both arrays are sorted in place.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N\log N+M\log M+R\log R)$. Let $N$, $M$, and $R=\min(N,M)$ be task, worker, and maximum assignment counts. Sorting costs $O(N\log N+M\log M)$.
- **Auxiliary Space Complexity:** $O(R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
