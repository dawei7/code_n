# Guided Example: Sum of Distances

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 3, 1, 1, 2]}`
- **Required output:** `[5, 0, 3, 4, 0]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** integer array `nums`. There exists an array `arr` of length `nums.length`, where $\text{arr}[i]$ is the sum of $|i - j|$ over all `j` such that $\text{nums}[j] = \text{nums}[i]$ and $j \neq i$. If there is no such `j`, set $\text{arr}[i]$ to be `0`.

The objective is to compute `[5, 0, 3, 4, 0]` from `{"nums": [1, 3, 1, 1, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Only equal values interact

For index $i$, the answer sums distances only to indices $j$ satisfying `nums[j] == nums[i]`. Indices holding different values never contribute to one another.

The dictionary `d` groups indices by value. Scanning `nums` from left to right appends each index to its value's list, so every group is automatically sorted:

$$
a_0<a_1<\cdots<a_{m-1}.
$$

The groups are independent. Once the solution can compute all distance sums for one sorted list, it can repeat that work for every value and write results into the corresponding original positions.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 3, 1, 1, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Split every absolute distance by side

At group position $i$, all earlier indices are smaller than $a_i$, while all later indices are larger. Therefore,

$$
\sum_{j=0}^{m-1}|a_i-a_j|
=
\sum_{j<i}(a_i-a_j)
+
\sum_{j>i}(a_j-a_i).
$$

Call the first quantity `left` and the second `right`. The distance to $a_i$ itself is zero and need not be handled separately.

A direct computation for each $i$ would repeat most of the same subtractions and take $O(m^2)$ for one large group. The exact solution instead maintains how `left` and `right` change when moving from one group index to the next.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Initialize at the first occurrence

At $a_0$, there are no earlier positions, so `left = 0`.

Every other occurrence lies to the right. Its total distance from $a_0$ is

$$
\sum_{j=0}^{m-1}(a_j-a_0)
=
\sum_{j=0}^{m-1}a_j-ma_0.
$$

The code computes this as

`right = sum(idx) - len(idx) * idx[0]`.

Including $j=0$ is harmless because its term is zero. Thus `left + right` is already the complete answer for the first index.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[5, 0, 3, 4, 0]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 3, 1, 1, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[5, 0, 3, 4, 0]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Prefix sums per group:** Store cumulative index sums and calculate left and right formulas independently for each occurrence. This is also $O(n)$ but uses an additional prefix structure or variables.
- **Two global passes:** Maintain count and index-sum maps left-to-right, then right-to-left, adding each side's contribution directly to the answer.
- **Pairwise comparison:** Comparing every equal-value pair and adding its distance to both endpoints can take $O(n^2)$ when all values match.
- **Singleton group:** Both side contributions are zero, so the answer is zero.
- **All values distinct:** Every group is a singleton and the entire output is zeroes.
- **All values equal:** One group contains all indices; the recurrence still processes it in linear time.
- **Adjacent equal occurrences:** A gap of one is handled by the same weighted update.
- **Widely separated occurrences:** The actual gap scales both contribution changes correctly.
- **Large input values:** They are dictionary keys only; distances depend on indices, not value magnitude.
- **Input preservation:** Grouping reads `nums` without sorting or modifying it.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n=|\texttt{nums}|$. Group construction visits every index once, taking expected $O(n)$ time with hash-map operations.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
