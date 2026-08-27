# Guided Example: Maximum Difference Between Adjacent Elements in a Circular Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 4]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a **circular** array `nums`, find the **maximum** absolute difference between adjacent elements.

The objective is to compute `3` from `{"nums": [1, 2, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

**A circular array has one more adjacent pair than a linear scan suggests.** For a length-$n$ array, the ordinary internal adjacent pairs are

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

$$
(\texttt{nums}[0],\texttt{nums}[1]),\ldots,
(\texttt{nums}[n-2],\texttt{nums}[n-1]).
$$

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | $$
(\texttt{nums}[0],\texttt{nums}[1]),\ldots,
(\texttt{nums... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

$$
(\texttt{nums}[n-1],\texttt{nums}[0]).
$$

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Explicit wrap-around initialization:** Start w:** - **Explicit wrap-around initialization:** Start with `abs(nums[-1] - nums[0])` and scan indices $0$ through $n-2$. This preserves $O(n)$ time while using $O(1)$ auxiliary space.
- **Modulo indexing:** Evaluate `abs(nums[i] - nums[(i + 1) % n])` for every $i$. It is concise and avoids copying, though it performs a modulo operation per pair.
- **Compare every pair:** Considering all $\binom n2$ pairs is wrong as well as slower; only circular neighbors are eligible.
- **Two elements:** The internal and wrap-around pairs contain the same two values in opposite order, so both differences are equal and `max` returns the correct value.
- **All elements equal:** Every absolute difference is zero, so the answer is zero.
- **Negative values:** Absolute subtraction handles signs directly; sorting or taking absolute values of individual elements would not preserve pair differences.
- **Large change at wrap-around:** Appending the first value ensures the potentially best last-to-first pair is not forgotten.
- **Input preservation:** `nums + [...]` allocates a new list and leaves `nums` unchanged, despite the extra memory.
- **Non-empty guarantee:** Accessing `nums[0]` is safe because the constraints require at least two elements.
- **Iterator import:** The source relies on `pairwise` being available from the execution environment's imports; its algorithmic behavior is consecutive overlapping pairing.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n=\lvert\texttt{nums}\rvert$. Constructing the extended list copies $n+1$ references in $O(n)$ time. `pairwise` yields $n$ pairs, and each subtraction, absolute value, and maximum comparison is $O(1)$. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
