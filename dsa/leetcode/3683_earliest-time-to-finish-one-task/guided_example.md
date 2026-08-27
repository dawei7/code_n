# Guided Example: Earliest Time to Finish One Task

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tasks": [[1, 6], [2, 3]]}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a 2D integer array `tasks` where $\text{tasks}[i] = [s_{i}, t_{i}]$.

The objective is to compute `5` from `{"tasks": [[1, 6], [2, 3]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Unpacking each task

The expression `for s, t in tasks` visits the task rows one at a time. Since every row has the required form `[s_i, t_i]`, Python unpacking assigns its first entry to `s` and its second entry to `t`.

This avoids index-heavy expressions such as `task[0] + task[1]`, but the meaning is identical. The variable `t` is a duration, not an absolute finish timestamp. That distinction is why the two entries must be added.

For example, a task `[2, 3]` starts at time $2$ and then runs for $3$ units. Its finish time is $2+3=5$. Returning just the duration $3$, or taking the larger of the two fields, would misinterpret the contract.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tasks": [[1, 6], [2, 3]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Producing completion times lazily

For every row, the generator expression yields `s + t`. It does not construct a separate list containing all completion times. Instead, `min` requests one generated value at a time and keeps only the smallest value seen so far.

Conceptually, the running state is:

- after the first task, the best finishing time is that task's `s + t`;
- for each later task, compare its `s + t` with the current best; and
- retain the smaller of the two.

The generator syntax merely packages this ordinary one-pass minimum scan compactly.

For `tasks = [[1, 6], [2, 3]]`, the generated finishing times are $7$ and $5$. The minimum is $5$, so the second task is the first one that can be completed.

For `tasks = [[100, 100], [100, 100], [100, 100]]`, every generated value is $200$. The minimum is still $200$; ties do not require identifying which task finishes first because the function returns only the time.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For every row, the generator expression yields `s + t`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why taking the minimum answers “at least one”

Let the finishing times be

$$
f_i=s_i+t_i.
$$

Before time $\min_i f_i$, every task has a finishing time later than the current time, so zero tasks have completed. At time $\min_i f_i$, the task attaining that minimum has completed, so at least one task is finished. This is exactly the first moment at which the requested condition becomes true.

Any value larger than the minimum would not be the earliest such time. Any value smaller than the minimum would occur before every task's completion. Thus the minimum is both attainable and minimal.

The algorithm does not need to compare start times separately. A task that starts earlier may take much longer, while a later-starting task may finish first. Only the sum captures both effects. In the first example, the first task starts at $1$ but finishes at $7$, whereas the task starting at $2$ finishes at $5$.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tasks": [[1, 6], [2, 3]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Sort all finishing times:** Sorting would plac:** - **Sort all finishing times:** Sorting would place the earliest completion first, but it costs $O(n \log n)$ time and may require $O(n)$ additional storage. A single minimum scan is sufficient.
- **Build a list and call `min`:** `min([s + t for s, t in tasks])` produces the same value but materializes $n$ sums. The generator used by the source preserves $O(1)$ auxiliary space.
- **Choose the earliest start time:** The earliest-starting task is not necessarily the earliest-finishing task because durations differ. The relevant quantity is always `s + t`.
- **Choose the shortest duration:** A short task may begin much later than a longer one. Duration alone also cannot determine the earliest absolute finish time.
- **One task:** Its completion time is automatically both the minimum and the answer. The nonempty guarantee lets `min` handle this without a branch.
- **Several tasks tie:** If multiple tasks share the earliest finish time, `min` returns that time once. The problem does not ask for a task index or tie-breaking rule.
- **Identical tasks:** Repeated rows generate repeated completion values, which do not change the minimum and require no deduplication.
- **Largest permitted values:** With `s = 100` and `t = 100`, the sum is $200$. Python integers handle this directly, and the constraints make overflow irrelevant in any standard integer type.
- **No task interaction:** The statement does not say tasks run sequentially or compete for a resource. Introducing such a restriction would solve a different scheduling problem.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be `len(tasks)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
