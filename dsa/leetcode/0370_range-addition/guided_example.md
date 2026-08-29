# Guided Example: Range Addition

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"length": 5, "updates": [[1, 3, 2], [2, 4, 3], [0, 2, -2]]}`
- **Required output:** `[-2, 0, 3, 5, 3]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `length` and an array `updates` where $\text{updates}[i] = [\text{startIdx}_{i}, \text{endIdx}_{i}, \text{inc}_{i}]$.

The objective is to compute `[-2, 0, 3, 5, 3]` from `{"length": 5, "updates": [[1, 3, 2], [2, 4, 3], [0, 2, -2]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: From array values to boundary changes.

Suppose an update adds `c` to every index from `l` through `r`, inclusive. The running value should increase by `c` when the scan enters index `l`. It should remain elevated through index `r`. At index `r + 1`, it should decrease by `c` so later positions are unaffected.

The source records exactly those events:



No interior index needs a direct change. A later prefix sum carries the starting increment across the complete range.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"length": 5, "updates": [[1, 3, 2], [2, 4, 3], [0, 2, -2]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the right boundary is `r + 1`.

The update interval includes index `r`, so subtracting at `r` would cancel the increment one position too early. The cancellation belongs at the first index outside the range, `r + 1`.

If `r` is the last valid index, there is no later array position at which the effect must stop. The condition `r + 1 < length` skips the subtraction rather than indexing beyond `d`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Reconstructing values with a prefix sum.

After all boundaries have been marked, `accumulate(d)` yields the running prefix sums:

$$
\texttt{answer}[i]=\sum_{p=0}^{i}\texttt{d}[p].
$$

Every update whose start is at or before `i` has contributed its positive boundary by this point. If that update ended before `i`, its negative boundary has also been included and cancels it. Therefore the running sum contains exactly the increments from updates satisfying

$$
\texttt{startIdx}\le i\le\texttt{endIdx}.
$$

Converting the `accumulate` iterator to a list produces the required concrete result array.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[-2, 0, 3, 5, 3]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"length": 5, "updates": [[1, 3, 2], [2, 4, 3], [0, 2, -2]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[-2, 0, 3, 5, 3]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Apply every range directly:** Loop from `l` through `r` for each update. This is simple but takes $O(nq)$ time in the worst case when ranges are large.
- **One extra sentinel slot:** Allocate `length + 1` difference entries and always subtract at `r + 1`. This removes the boundary branch, after which only the first `length` prefix sums are returned.
- **Fenwick tree:** Supports interleaved range updates and point queries efficiently. It is unnecessary when every update arrives before one final full-array read.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+q)$. Let $n$ be `length` and let $q$ be the number of updates.
- **Auxiliary Space Complexity:** $O(length)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
