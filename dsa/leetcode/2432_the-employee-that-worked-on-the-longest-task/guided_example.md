# Guided Example: The Employee That Worked on the Longest Task

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 10, "logs": [[0, 3], [2, 5], [0, 9], [1, 15]]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `n` employees, each with a unique id from `0` to $n - 1$.

The objective is to compute `1` from `{"n": 10, "logs": [[0, 3], [2, 5], [0, 9], [1, 15]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Logs contain end times, not durations

Each log entry gives an employee ID and the absolute time when that task ended. The first task begins at time zero. Every later task begins as soon as the previous task ends, so its duration is

$$
\text{current leave time} - \text{previous leave time}.
$$

The strictly increasing leave times ensure every duration is positive. The employee count `n` determines the valid ID range but is not otherwise needed by the scan.

The solution maintains:

- `last`, the previous task's leave time;
- `mx`, the longest duration seen so far;
- `ans`, the employee ID chosen for that longest duration.

All three start at zero. For the first task, subtracting `last = 0` from its leave time gives the correct duration from time zero.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 10, "logs": [[0, 3], [2, 5], [0, 9], [1, 15]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Understand the local reassignment of `t`

The loop receives `uid` and the raw leave time in `t`. It then executes `t -= last`, so the local variable `t` now means task duration rather than leave time.

After the best-answer test, the line `last += t` may look unusual. At that moment,

$$
\texttt{t}
=
\text{current leave time}
-
\texttt{last}_{old}.
$$

Therefore

$$
\texttt{last}_{old} + \texttt{t}
=
\text{current leave time}.
$$

The addition restores `last` to the absolute leave time of the current task. Writing `last = original_leave_time` would be more direct, but the original value has been overwritten in the local `t` variable. The algebra shows that the update is equivalent and keeps the next duration correct.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Update on a longer task or a better tie

The condition

`mx < t or (mx == t and ans > uid)`

implements both ranking rules. If the current duration `t` is larger, the current task must replace the previous choice. If durations tie, the current employee replaces `ans` only when `uid` is smaller.

The assignment `ans, mx = uid, t` updates the chosen employee and its duration together. If neither condition holds, the existing pair remains better: it has a longer duration, or it has the same duration with an equal or smaller employee ID.

Because durations are positive, the first log always has `t > mx` when `mx` is initially zero. Thus `ans` is initialized to the first actual worker through the normal update logic, even if that worker's ID is not zero.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 10, "logs": [[0, 3], [2, 5], [0, 9], [1, 15]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Precompute a duration array:** Subtract consecutive leave times, then find the best pair. This is also $O(m)$ time but uses $O(m)$ unnecessary storage.
- **Sort tasks by duration:** Sorting can apply a compound key of negative duration and employee ID, but costs $O(m\log m)$ when a single pass suffices.
- **Track totals per employee:** Summing all work by an employee answers a different question. The problem asks for the employee owning one longest task, not the greatest total time.
- **One log:** Its duration is its leave time minus zero, so its employee is returned regardless of ID.
- **Tie between tasks:** The condition replaces the answer only for a smaller ID, so log order cannot override the stated tie-break.
- **Same employee appears repeatedly:** Each task duration is evaluated independently; no accumulation is performed.
- **First worker has nonzero ID:** Positive first duration replaces the zero-initialized best and records the actual ID.
- **Strictly increasing leave times:** This guarantee makes durations positive and lets zero serve as a safe initial maximum.
- **Unused `n` parameter:** The scan does not need the number of possible employees because IDs are already present in logs and guaranteed valid.
- **Local variable mutation:** `t -= last` changes only the unpacked integer variable, not the nested entry stored in `logs`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(m)$. Let $m$ be `len(logs)`. The loop performs one subtraction, a constant number of comparisons, and constant-size assignments per entry, so time is $O(m)$. The solution never loops through all `n` employee IDs because employees without logged tasks cannot own the longest task.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
