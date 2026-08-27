# Guided Example: Longest Mountain in Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr": [2, 1, 4, 7, 3, 2, 5]}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You may recall that an array `arr` is a **mountain array** if and only if:

The objective is to compute `5` from `{"arr": [2, 1, 4, 7, 3, 2, 5]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A mountain is determined by a peak and two strict slopes

For index `i` to be the peak of a mountain:

- at least one strictly increasing step must lead into `i` from the left;
- at least one strictly decreasing step must leave `i` to the right.

If we know the longest increasing run ending at each index and the longest decreasing run starting at each index, then every valid peak's mountain length follows immediately.

The exact solution stores these two quantities in arrays `f` and `g`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr": [2, 1, 4, 7, 3, 2, 5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Increasing length ending at each index

Every `f[i]` begins at one because a single element is a trivial run of length one.

Scanning left to right, when `arr[i] > arr[i-1]`, the increasing run ending at `i-1` can extend through `i`:

`f[i] = f[i - 1] + 1`.

If the comparison is equal or decreasing, no strict increasing run crosses that boundary, so `f[i]` remains one.

Thus, `f[i]` is exactly the number of consecutive elements in the maximal strictly increasing suffix ending at `i`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Every `f[i]` begins at one because a single element is a tri... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Decreasing length starting at each index

Every `g[i]` also begins at one. Scanning right to left, when `arr[i] > arr[i+1]`, index `i` begins a descending step and can extend the decreasing run starting at `i+1`:

`g[i] = g[i + 1] + 1`.

If values are equal or rise to the right, `g[i]` remains one.

Therefore, `g[i]` is the length of the maximal strictly decreasing prefix starting at `i`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr": [2, 1, 4, 7, 3, 2, 5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **One-pass mountain window:** Skip flat/down reg:** - **One-pass mountain window:** Skip flat/down regions, climb strictly, then descend strictly while measuring boundaries. It achieves `O(1)` space and `O(n)` time but requires careful pointer transitions.
- **- **Expand left and right from every peak:** Witho:** - **Expand left and right from every peak:** Without reusing slope lengths, repeated expansion can become `O(n^2)`.
- **- **Entirely increasing array:** Every `g[i]` rema:** - **Entirely increasing array:** Every `g[i]` remains one, so no peak has a descending side and answer is zero.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n = len(arr)`. Initializing `f` and `g` takes `O(n)` time. The forward and backward scans each process `O(n)` positions with constant work. Total time is `O(n)`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
