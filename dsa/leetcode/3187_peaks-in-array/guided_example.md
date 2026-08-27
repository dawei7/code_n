# Guided Example: Peaks in Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [3, 1, 4, 2, 5], "queries": [[2, 3, 4], [1, 0, 4]]}`
- **Required output:** `[0]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A **peak** in an array `arr` is an element that is **greater** than its previous and next element in `arr`.

The objective is to compute `[0]` from `{"nums": [3, 1, 4, 2, 5], "queries": [[2, 3, 4], [1, 0, 4]]}` while avoiding redundant calculations and unnecessary overhead.

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

**Separate the changing array from the information queries need.** A position `i` is a peak exactly when all three conditions hold:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [3, 1, 4, 2, 5], "queries": [[2, 3, 4], [1, 0, 4]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

$$
0<i<n-1,\qquad \texttt{nums}[i-1]<\texttt{nums}[i],\qquad
\texttt{nums}[i]>\texttt{nums}[i+1].
$$

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | $$
0<i<n-1,\qquad \texttt{nums}[i-1]<\texttt{nums}[i],\qquad... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

A type-1 query does not need the peak values themselves. It only needs to count how many positions in a range currently satisfy that predicate. Imagine an indicator array `peak` in which `peak[i]` is $1$ for a peak and $0$ otherwise. Then a range answer is simply a range sum over this indicator array.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[0]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [3, 1, 4, 2, 5], "queries": [[2, 3, 4], [1, 0, 4]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[0]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Segment tree:** Store peak indicators in a seg:** - **Segment tree:** Store peak indicators in a segment tree and use point updates plus range-sum queries. It has the same $O(\log n)$ operation bounds but uses more code and a larger constant factor than a Fenwick tree for this sum-only task.
- **Recount every requested subarray:** Scanning `left + 1` through `right - 1` is simple and needs no tree, but a long interval costs $O(n)$ and up to $10^5$ such queries can make the total quadratic.
- **Rebuild after each value change:** Recomputing all peaks after a type-2 query ignores the local three-center dependency and also costs $O(n)$ per update.
- **Ordered set of peak indices:** A balanced ordered set can update the same three positions, but counting how many stored indices lie in an interval requires order-statistics support. A basic Python set or sorted list does not provide both updates and rank queries efficiently.
- **Subarray endpoints:** Even when `nums[left]` is greater than its global neighbors, it is the first element of the queried subarray and must not count. Shifting to `left + 1` and `right - 1` enforces this rule.
- **Intervals of length one or two:** They have no interior position. The `l > r` check returns zero without issuing a misleading range query.
- **Global endpoints:** Candidate centers `0` and `n - 1` are rejected by the helper. This makes updates at either end safe: only the adjacent interior position can acquire or lose peak status.
- **Strict inequality and equal neighbors:** A plateau such as `[..., 4, 4, ...]` contains no peak at either equal value. The source uses `<` and `>`, not non-strict comparisons.
- **Assigning the same value:** The code still removes the old local indicators and adds them back. The result is unchanged and remains correct; no special case is required.
- **Sequential query semantics:** `nums[idx] = val` deliberately mutates the array. Every subsequent query operates on the accumulated state, not the original input.
- **Fenwick index zero:** Standard Fenwick updates cannot start at zero because `x & -x` would also be zero and the loop would not advance. The wrapper's endpoint rejection guarantees `tree.update` is never called with zero.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let $n$ be the array length and $q$ the number of queries. A Fenwick update or prefix query follows parent links determined by the least significant set bit, so it performs $O(\log n)$ iterations.
- **Auxiliary Space Complexity:** $O(q)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
