# Guided Example: Increasing Triplet Subsequence

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3, 4, 5]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums`, return `true`* if there exists a triple of indices *`(i, j, k)`* such that *`i < j < k`* and *$\text{nums}[i] < \text{nums}[j] < \text{nums}[k]$. If no such indices exists, return `false`.

The objective is to compute `true` from `{"nums": [1, 2, 3, 4, 5]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Keep the best possible tails, not the subsequence itself.

The task asks only whether some strictly increasing subsequence of length three exists. It does not ask for the indices or values of that subsequence. This allows the scan to summarize all useful earlier choices with two numbers:

- `mi`: the smallest value seen so far, which is the best possible tail of a length-one increasing subsequence;
- `mid`: the smallest possible second value of any increasing pair seen so far, which is the best possible tail of a length-two increasing subsequence.

A smaller tail is always at least as useful as a larger one. If a future number can extend a pair ending at a larger `mid`, it can also extend a pair ending at a smaller `mid`. Therefore the algorithm does not need to remember every candidate pair.

Both variables begin at positive infinity. Before any input is processed, no real length-one or length-two candidate exists. Any allowed integer can replace `mi`, and no ordinary integer can incorrectly exceed a real pair tail before one has been created.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3, 4, 5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Test whether the current value completes a triplet.

The first condition in the exact source is `if num > mid`. A finite `mid` certifies that two earlier indices form a strictly increasing pair ending at value `mid`. Because the scan moves left to right, the current `num` occurs at a later index. If it is strictly greater than `mid`, those two earlier elements followed by `num` form the required triplet, so the method can immediately return `true`.

Checking this condition first is safe. When `mid` is still infinity, no finite input can be larger, so the method cannot report a triplet before an increasing pair exists.

Strict `>` is essential. If `num == mid`, appending it would create equal second and third values, not a strictly increasing subsequence.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The first condition in the exact source is `if num > mid`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Update the best length-one tail.

If the current number does not complete a triplet, the source next checks `num <= mi`. In that case, it assigns `mi = num`.

This keeps `mi` equal to the smallest value encountered in the processed prefix. Replacing it with an equal value is harmless, and the `<=` condition ensures that equal values are not mistakenly used as a strictly increasing pair. For example, scanning `[2,2]` repeatedly updates `mi` but never creates a finite `mid`, which is correct.

A newly smaller `mi` makes future pair formation easier. Any later number above it can become a candidate second value.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3, 4, 5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate triples:** Testing all index triples:** - **Enumerate triples:** Testing all index triples directly takes $O(n^3)$ time and is impossible for up to $5\cdot10^5$ elements.
- **- **For every middle index, search both sides:** P:** - **For every middle index, search both sides:** Precomputed prefix minima and suffix maxima can detect a triplet in $O(n)$ time, but require $O(n)$ extra arrays. The two-tail scan compresses the same useful information into constants.
- **- **Longest-increasing-subsequence tails array:** :** - **Longest-increasing-subsequence tails array:** Standard binary-search LIS tracking can detect whether length reaches three in $O(n\log 3)=O(n)$ time and $O(1)$ bounded storage. The explicit two variables are simpler for the fixed target length.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be `len(nums)`. The method scans every element once and performs a constant number of comparisons or assignments per element. Its time complexity is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
