# Guided Example: Array With Elements Not Equal to Average of Neighbors

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3, 4, 5]}`
- **Required output:** `[2, 1, 4, 3, 5]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** array `nums` of **distinct** integers. You want to rearrange the elements in the array such that every element in the rearranged array is **not** equal to the **average** of its neighbors.

The objective is to compute `[2, 1, 4, 3, 5]` from `{"nums": [1, 2, 3, 4, 5]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Create alternating low and high values

After sorting, split the distinct values into a lower half and an upper half. Let

`m = (n + 1) // 2`,

so the lower half is `nums[0:m]` and the upper half is `nums[m:n]`. The lower half has the same number of values as the upper half when $n$ is even and one extra when $n$ is odd.

The solution alternates one lower value and one upper value:

`nums[0], nums[m], nums[1], nums[m + 1], ...`.

If $n$ is odd, the last unpaired lower value is appended at the end.

Because all input values are distinct and the list is sorted, every upper-half value is strictly greater than every lower-half value.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3, 4, 5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why every internal high value is safe

An upper-half value in the alternating result is surrounded by lower-half values, except when it is at an endpoint. Both neighbors are strictly smaller than it. The average of two numbers smaller than $h$ is also smaller than $h$:

$$
\frac{a+b}{2}<h.
$$

Therefore an internal high value cannot equal its neighbors' average.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why every internal low value is safe

An internal lower-half value is surrounded by upper-half values. Both neighbors are strictly greater than it, so their average is strictly greater:

$$
\frac{a+b}{2}>\ell.
$$

It also cannot equal the average.

Endpoints have only one neighbor and are not constrained by the problem. Thus the alternating low-high structure satisfies every required internal index.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[2, 1, 4, 3, 5]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3, 4, 5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[2, 1, 4, 3, 5]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Swap adjacent pairs after sorting:** A different local-peak construction can also work, but its proof must handle endpoints and parity carefully.
- **Random shuffling until valid:** It has no deterministic runtime guarantee and repeatedly checks the same condition.
- **Sort then interleave halves in another order:** Starting with high instead of low also works if strict alternation and half separation are maintained.
- **Odd length:** The lower half has one extra value, which becomes the final unconstrained endpoint.
- **Even length:** Every lower value pairs with one upper value.
- **Minimum allowed length three:** The result has one internal value that is strictly a peak or valley.
- **Large value gaps:** Actual distances do not matter; only strict less-than and greater-than relations are used.
- **Distinct values:** They guarantee strict half separation and prevent an average equality through equal neighbors.
- **No arithmetic in code:** The method enforces inequalities structurally and never computes a potentially floating-point average.
- **Input side effect:** The exact source sorts `nums` in place before returning a separate arrangement.
- **Any valid output:** There is no requirement to preserve relative order or choose a lexicographically smallest rearrangement.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N\log N)$. Let $N$ be the number of elements.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
