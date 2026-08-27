# Guided Example: Image Overlap

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"img1": [[1, 1, 0], [0, 1, 0], [0, 1, 0]], "img2": [[0, 0, 0], [0, 1, 1], [0, 0, 1]]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two images, `img1` and `img2`, represented as binary, square matrices of size `n x n`. A binary matrix has only `0`s and `1`s as values.

The objective is to compute `3` from `{"img1": [[1, 1, 0], [0, 1, 0], [0, 1, 0]], "img2": [[0, 0, 0], [0, 1, 1], [0, 0, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A translation is completely determined by one matched pair of one-cells

Suppose `img1[i][j] == 1` and `img2[h][k] == 1`. To place these two one-cells on the same final position, `img1` must be translated by the row and column displacement that takes `(i,j)` to `(h,k)`.

The exact source records this displacement as

`(i - h, j - k)`.

Using the opposite sign would describe moving the other image instead, but consistency is all that matters: every pair aligned by one physical translation must produce the same key.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"img1": [[1, 1, 0], [0, 1, 0], [0, 1, 0]], "img2": [[0, 0, 0], [0, 1, 1], [0, 0, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Turn the problem into voting for a displacement

The solution examines every one-cell in `img1` and every one-cell in `img2`. Their coordinate difference votes for the translation that would align them:

`cnt[(i - h, j - k)] += 1`.

Fix one displacement `d`. Every counted pair with key `d` represents one cell of `img1` and one cell of `img2` that coincide under that translation. Conversely, every overlapping pair of one-cells under `d` produces exactly that key.

Therefore, `cnt[d]` is exactly the overlap achieved by displacement `d`.

The maximum counter value is consequently the largest possible overlap.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The solution examines every one-cell in `img1` and every one... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why it is enough to consider differences between one-cells

Any translation with positive overlap aligns at least one one-cell from `img1` with one one-cell from `img2`. Its displacement therefore appears as the coordinate difference of that pair and receives votes in the counter.

A translation with zero overlap cannot improve on any positive one. If every possible translation has zero overlap—because at least one image has no one-cells—the counter stays empty and the correct answer is zero.

There is no need to enumerate an arbitrary unbounded range of shifts. Only shifts capable of aligning at least one relevant pair can matter, and the pair differences enumerate all of them.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"img1": [[1, 1, 0], [0, 1, 0], [0, 1, 0]], "img2": [[0, 0, 0], [0, 1, 1], [0, 0, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Shift and compare every matrix cell:** There a:** - **Shift and compare every matrix cell:** There are `O(n^2)` shifts and `O(n^2)` cells per shift, also giving `O(n^4)` time in a direct implementation.
- **- **Extract one-cell coordinate lists first:** Thi:** - **Extract one-cell coordinate lists first:** This makes the work visibly `O(ab)` and avoids repeatedly testing zero-cells, while retaining the same voting proof.
- **- **Bitset rows:** Encode rows as integers, shift :** - **Bitset rows:** Encode rows as integers, shift bits, and use bit counts. This can reduce practical and asymptotic factors and more closely support the manifest's tighter target.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `a` be the number of one-cells in `img1` and `b` the number in `img2`. The loops inspect every matrix cell to find one-cells and, for each one in the first image, scan the second matrix for its ones. The exact number of successful pair votes is `a b`, while the loop structure performs up to `O(n^2 + a n^2)` cell checks.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
