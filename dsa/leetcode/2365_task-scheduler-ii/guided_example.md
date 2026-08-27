# Guided Example: Task Scheduler II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tasks": [1, 2, 1, 2, 3, 1], "space": 3}`
- **Required output:** `9`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** array of positive integers `tasks`, representing tasks that need to be completed **in order**, where $\text{tasks}[i]$ represents the **type** of the $$i^{\text{th}}$$ task.

The objective is to compute `9` from `{"tasks": [1, 2, 1, 2, 3, 1], "space": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The order removes scheduling freedom

Tasks must be completed in the given order. At any point, the only productive action is to execute the next task; tasks cannot be swapped to fill a waiting period. Therefore, if that next task is temporarily illegal because the same type was completed too recently, every intervening day is forced to be a break.

This makes an earliest-possible greedy schedule optimal: execute each task on the first day that is both after the previous processed day and legal for its type. Delaying it voluntarily cannot help, because every later task is blocked behind it in the fixed sequence.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tasks": [1, 2, 1, 2, 3, 1], "space": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Track the next legal day for each type

The dictionary `day` maps a task type to the earliest day on which that type may next be completed. Suppose a type is completed on day $d$. The problem requires `space` full days to pass after completion, so the next completion may occur on:

$$
d+\texttt{space}+1.
$$

For example, if a task runs on day `2` and `space = 3`, days `3`, `4`, and `5` must pass. The next same-type task can run on day `6`. Storing the next legal day directly avoids repeatedly reconstructing it from the last completion day.

`day` is a `defaultdict(int)`, so an unseen task type has stored availability zero. Real completion days begin at one, making zero safely mean “no restriction from an earlier occurrence.”

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The dictionary `day` maps a task type to the earliest day on... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Advance the global clock

`ans` represents the day on which the most recently processed task was completed. It begins at zero, before any work has occurred. For each next task, the code first performs:



This gives the earliest calendar day immediately after the preceding task. Even when the next task has a different type and needs no cooling period, two tasks cannot be performed on the same day, so at least this one-day advance is necessary.

The line



then compares that chronological next day with this type's availability. If `day[task]` is smaller, the task can run immediately. If it is larger, all days between are forced breaks, and assigning that larger value jumps directly over them.

After executing the task on the chosen `ans` day, the algorithm records:



This prepares the exact legal boundary for the next occurrence.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `9` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tasks": [1, 2, 1, 2, 3, 1], "space": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `9` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Day-by-day simulation:** It can produce the sa:** - **Day-by-day simulation:** It can produce the same schedule, but long cooling gaps cause runtime proportional to the answer rather than the number of tasks.
- **Store last completion days:** One can save `last[task]` and compute `max(ans + 1, last[task] + space + 1)`. This is equivalent; storing the next legal day makes the lookup directly usable.
- **Reordering with a priority queue:** That solves a different task-scheduling problem. Here the input order is mandatory, so no choice of another ready task is allowed.
- **First occurrence of a type:** Its default availability is zero, so it runs on the next chronological day.
- **Consecutive equal tasks:** The second jumps to the first completion day plus `space + 1`.
- **Alternating types:** A type's cooling interval can elapse while intervening different tasks are completed, so the maximum may require no jump.
- **`space = 1`:** One full day must occur between equal types; they can be executed two calendar days apart.
- **All task types distinct:** No stored availability blocks anything, and the answer is exactly `len(tasks)`.
- **Every task has the same type:** Each consecutive execution is `space + 1` days apart, and direct jumping handles the large total efficiently.
- **Large task identifiers:** They are dictionary keys, so their numeric magnitude does not require a value-sized array.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of tasks. The loop processes each task exactly once. Dictionary lookup and update are expected $O(1)$, and all arithmetic is constant time under the usual model. Total expected time is $O(n)$, independent of how many break days the schedule contains.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
