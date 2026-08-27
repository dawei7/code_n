# Guided Example: Global and Local Inversions

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 0, 2]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` of length `n` which represents a permutation of all the integers in the range `[0, n - 1]`.

The objective is to compute `true` from `{"nums": [1, 0, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Local inversions are already global inversions

A local inversion compares adjacent indices `i` and `i + 1`. This pair also satisfies the definition of a global inversion.

Therefore the two counts are equal exactly when there is no additional global inversion whose indices are separated by at least two positions. Such a pair is called a nonlocal inversion.

The task becomes detecting whether any `j <= i - 2` has `nums[j] > nums[i]`.

This reformulation is the key optimization. Counting both kinds of inversions would compute much more information than the Boolean result needs. Once the shared local pairs are conceptually removed from both counts, only the existence of an unmatched, nonlocal pair matters.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 0, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Summarize all sufficiently earlier values with a maximum

When examining index `i`, only values through index `i - 2` can form a nonlocal inversion ending at `i`. If their maximum is no greater than `nums[i]`, none of them is greater. If the maximum is greater, it supplies an explicit violating earlier value.

Variable `mx` stores that prefix maximum.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | When examining index `i`, only values through index `i - 2` ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Update in the correct order

The loop begins at `i = 2`. Before comparing, it incorporates `nums[i - 2]`:

`mx = max(mx, nums[i - 2])`.

It then tests `mx > nums[i]`.

At index two, this includes only index zero, the only index at distance at least two. At the next step it includes indices zero and one, continuing correctly.

The code uses a walrus assignment to update and compare in one expression, but its meaning is exactly these two operations.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 0, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Check `abs(nums[i] - i) <= 1`:** For a permuta:** - **Check `abs(nums[i] - i) <= 1`:** For a permutation, this is another characterization of ideal permutations, but the prefix-maximum proof connects directly to nonlocal inversions.
- **- **Merge-sort inversion counting:** It can count :** - **Merge-sort inversion counting:** It can count all global inversions in `O(n log n)`, then compare with local count, but counting is unnecessary.
- **- **Nested pair loops:** Directly testing every gl:** - **Nested pair loops:** Directly testing every global pair costs `O(n^2)`.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the permutation length. The loop visits each index from two onward once and performs constant work, giving `O(n)` time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
