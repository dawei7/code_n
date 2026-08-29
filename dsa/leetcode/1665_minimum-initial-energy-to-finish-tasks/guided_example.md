# Guided Example: Minimum Initial Energy to Finish Tasks

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tasks": [[1, 2], [2, 4], [4, 8]]}`
- **Required output:** `8`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array `tasks` where $\text{tasks}[i] = [\text{actual}_{i}, \text{minimum}_{i}]$:

The objective is to compute `8` from `{"tasks": [[1, 2], [2, 4], [4, 8]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Two different numbers describe a task

A task `[a, m]` consumes `a` energy but requires at least `m` energy before it begins. Since `a <= m`, completing it leaves at least `m - a` energy when started at the minimum. The difference

$$
m-a
$$

measures how much starting threshold remains after paying the task’s actual cost. Tasks with a larger difference impose a relatively high entry requirement compared with what they consume.

The exact source sorts with key `a - m` in ascending order. Because `a - m = -(m - a)`, this is equivalent to ordering tasks by `m - a` in descending order: the largest threshold-minus-cost gap comes first.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tasks": [[1, 2], [2, 4], [4, 8]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why that order is optimal

Consider two adjacent tasks `A = [a, m]` and `B = [b, q]`. If `A` is performed before `B`, the starting energy must satisfy both `E >= m` and `E - a >= q`. The minimum sufficient energy for this pair is

$$
R_{AB} = \max(m, a+q).
$$

If the order is reversed, it is

$$
R_{BA} = \max(q, b+m).
$$

Suppose `A` has at least as large a gap as `B`:

$$
m-a \ge q-b.
$$

Rearranging gives `a + q <= b + m`. Also `m <= b + m` because `b` is positive. Therefore both arguments of `R_{AB}` are at most `b + m`, and `b + m` is one argument of `R_{BA}`. Hence

$$
R_{AB} \le R_{BA}.
$$

So whenever a smaller-gap task appears before a larger-gap task, swapping the pair cannot increase the required initial energy. Repeatedly removing such inversions leads to descending `m-a` order. This exchange argument proves that the sorting key used by the source admits an optimal schedule.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Simulate the chosen schedule by buying only missing energy

The variables have concrete meanings:

- `ans` is the total initial energy committed so far;
- `cur` is the energy currently left after completing the already processed tasks.

Both begin at zero. For a task `[a, m]`, if `cur >= m`, the task can start without changing the chosen initial amount. If `cur < m`, the schedule lacks exactly `m - cur` energy at this point. The source adds that deficit to `ans` and sets `cur = m`.

This can be understood as increasing the original starting budget. Any energy added to the initial budget would survive through all previous fixed task costs and appear as the same extra amount now. Raising by precisely the deficit is necessary—anything less cannot start the current task—and sufficient. Adding more would never help minimize `ans`, so the greedy simulation adds only what is forced.

After the threshold is met, `cur -= a` pays the actual energy cost. Because `a <= m` and `cur >= m`, remaining energy never becomes negative.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `8` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tasks": [[1, 2], [2, 4], [4, 8]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `8` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Sort by `m-a` descending:** This is mathematically identical to sorting `a-m` ascending and may express the scheduling intuition more directly.
- **Reverse construction with ascending gap:** One can derive the necessary initial budget while conceptually placing tasks from the end. It reaches the same order but often makes the energy invariant harder to explain.
- **Binary search the initial energy:** For a fixed order feasibility is easy, but choosing the right order remains the main problem. Binary search adds a logarithmic factor and does not replace the exchange proof.
- **Sort only by minimum requirement:** A large minimum may also have a large actual cost; minimum alone does not capture how much useful energy remains afterward. The gap is the correct comparison key.
- **Task with `a == m`:** Its gap is zero, so it appears late. Starting at its threshold leaves zero energy, making it less valuable to schedule before high-gap tasks.
- **Several equal gaps:** Either relative order is safe because the pairwise proof gives equality or non-increase in both directions for the ordering criterion.
- **One task:** The loop raises `ans` directly to that task’s minimum and returns it, which is plainly optimal.
- **Leftover energy after all tasks:** The objective minimizes initial energy, not final energy. Some leftover may be unavoidable because a high starting threshold can exceed total consumption.
- **Already sufficient current energy:** The branch does not add anything to `ans` and spends only `a`.
- **Large deficit:** Raising `cur` to exactly `m` is sufficient even after previous tasks because added initial energy propagates unchanged through their fixed costs.
- **Input mutation:** Using `sorted` preserves the original order in `tasks`. An in-place `sort` could reduce the list-allocation distinction but would modify the caller’s array.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the number of tasks. Computing sort keys and sorting the tasks takes $O(n\log n)$ time. The subsequent loop visits every task once and performs constant-time arithmetic, adding $O(n)$ time. Total running time is $O(n\log n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
