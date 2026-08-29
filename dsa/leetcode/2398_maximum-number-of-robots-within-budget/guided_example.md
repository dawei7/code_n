# Guided Example: Maximum Number of Robots Within Budget

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"chargeTimes": [3, 6, 1, 3, 4], "runningCosts": [2, 1, 3, 4, 5], "budget": 25}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You have `n` robots. You are given two **0-indexed** integer arrays, `chargeTimes` and `runningCosts`, both of length `n`. The $i^{\text{th}}$ robot costs $\text{chargeTimes}[i]$ units to charge and costs $\text{runningCosts}[i]$ units to run. You are also given an integer `budget`.

The objective is to compute `3` from `{"chargeTimes": [3, 6, 1, 3, 4], "runningCosts": [2, 1, 3, 4, 5], "budget": 25}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use a variable-length consecutive window

The chosen robots must be consecutive, so every candidate is a window `[l, r]`. Its length is:

$$
k=r-l+1,
$$

and its cost is:

$$
\max(\texttt{chargeTimes}[l..r])
+k\sum_{i=l}^{r}\texttt{runningCosts}[i].
$$

The algorithm moves `r` from left to right. It maintains the running-cost sum and maximum charge time for the current window, then advances `l` only while the budget is exceeded.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"chargeTimes": [3, 6, 1, 3, 4], "runningCosts": [2, 1, 3, 4, 5], "budget": 25}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Maintain the running-cost sum

`s` is the sum of `runningCosts[l..r]`. When a new right endpoint arrives, its cost `c` is added. When the window shrinks from the left, `runningCosts[l]` is subtracted before `l` advances.

All running costs are positive. Therefore, removing a left endpoint never increases this sum or the window length, so shrinking moves the total-cost expression toward feasibility.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Maintain the maximum charge with a decreasing deque

Deque `q` stores indices in increasing position order, but their charge values are strictly decreasing from front to back.

Before appending new index `r` with charge `t`, the code removes back indices whose charge is less than or equal to `t`. Those indices can never become the maximum while `r` remains in the window: `r` is newer, stays at least as long, and has an equal or larger charge.

After appending `r`, `q[0]` is the index of the current maximum charge.

When `l` leaves the window, the code removes the deque front only if that stored maximum index equals `l`. Other expired dominated indices were already removed from the back or will never sit before a valid front under the maintained index order.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"chargeTimes": [3, 6, 1, 3, 4], "runningCosts": [2, 1, 3, 4, 5], "budget": 25}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Binary search window length:** For each candidate length, use sliding sums and maxima to test feasibility. It can work in $O(n\log n)$ but is slower than the direct variable window.
- **Heap for maximum charge:** Lazy deletion can maintain maxima in $O(\log n)$ operations, while the monotonic deque gives amortized $O(1)$.
- **No single robot fits:** Every window shrinks to empty and the answer remains zero.
- **Exactly budget:** The while condition uses `>`, so equal cost is correctly accepted.
- **Equal charge times:** Older equal charges are removed because the newer one dominates and expires later.
- **Maximum at the left boundary:** It is popped exactly when `l` passes it, exposing the next maximum.
- **All windows fit:** `l` stays zero and the answer grows to `n`.
- **Positive costs:** They supply the monotonicity that makes shrinking safe.
- **Empty current window:** The `q and ...` guard avoids reading a missing maximum.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Each robot index is appended to the deque once. It is removed at most once, either from the back when dominated or from the front when leaving the window. The left pointer advances at most $n$ times across the entire scan. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
