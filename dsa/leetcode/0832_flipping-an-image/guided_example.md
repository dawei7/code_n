# Guided Example: Flipping an Image

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"image": [[1, 1, 0], [1, 0, 1], [0, 0, 0]]}`
- **Required output:** `[[1, 0, 0], [0, 1, 0], [1, 1, 1]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an `n x n` binary matrix `image`, flip the image **horizontally**, then invert it, and return *the resulting image*.

The objective is to compute `[[1, 0, 0], [0, 1, 0], [1, 1, 1]]` from `{"image": [[1, 1, 0], [1, 0, 1], [0, 0, 0]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Combine reversing and inverting instead of doing two full operations

For each row, the requested result first reverses the row and then flips every binary bit. Consider a mirrored pair at indices `i` and `j = n-1-i` with original values `a = row[i]` and `b = row[j]`.

After reverse and invert, the desired new values are:

$$
\text{new left}=1-b,
$$

$$
\text{new right}=1-a.
$$

Because values are binary, this leads to a useful shortcut based on whether `a` and `b` are equal.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"image": [[1, 1, 0], [1, 0, 1], [0, 0, 0]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Equal mirrored bits must both change

If `a == b`, reversing the pair has no visible effect because equal values trade places. Inversion then changes both:

- `(0,0)` becomes `(1,1)`;
- `(1,1)` becomes `(0,0)`.

The code performs these changes with

`row[i] ^= 1` and `row[j] ^= 1`.

XOR with 1 toggles a binary value: `0 ^ 1 = 1` and `1 ^ 1 = 0`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | If `a == b`, reversing the pair has no visible effect becaus... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Different mirrored bits need no change at all

If the pair differs, it is either `(0,1)` or `(1,0)`. Reversing swaps it, and inversion flips both swapped bits:

- `(0,1) -> (1,0) -> (0,1)`;
- `(1,0) -> (0,1) -> (1,0)`.

The combined operation returns the pair to its original values. Therefore, the exact source does nothing when `row[i] != row[j]`.

This may look surprising because the task says to reverse every row, but the two requested transformations cancel on unequal mirrored pairs. The algorithm computes the final state directly rather than materializing the intermediate reversed row.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[1, 0, 0], [0, 1, 0], [1, 1, 1]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"image": [[1, 1, 0], [1, 0, 1], [0, 0, 0]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[1, 0, 0], [0, 1, 0], [1, 1, 1]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Reverse then invert explicitly:** Reverse ever:** - **Reverse then invert explicitly:** Reverse every row and then scan again to toggle all bits. It is clear and still `O(n^2)`, but it performs two logical passes where the pair rule combines them.
- **- **Construct a new matrix with a comprehension:**:** - **Construct a new matrix with a comprehension:** Reading `1 - row[n-1-j]` directly is concise and nonmutating, but allocates `O(n^2)` new storage.
- **- **Unequal mirrored pair:** It must be left uncha:** - **Unequal mirrored pair:** It must be left unchanged in the combined operation; swapping alone would be incorrect.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. An `n \times n` image has `n^2` cells. Each row processes about `n/2` mirrored pairs and possibly one center, so every cell participates in constant work. Total time is `O(n^2)`.
- **Auxiliary Space Complexity:** $O(n^2)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
