# Guided Example: Smallest Rotation with Highest Score

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 3, 1, 4, 0]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array `nums`. You can rotate it by a non-negative integer `k` so that the array becomes `[nums[k], nums[k + 1], ... nums[nums.length - 1], nums[0], nums[1], ..., nums[k-1]]`. Afterward, any entries that are less than or equal to their index are worth one point.

The objective is to compute `3` from `{"nums": [2, 3, 1, 4, 0]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Follow one element across every rotation

Let an element `v = nums[i]` start at index `i` in an array of length `n`. After a left rotation by `k`, its new index is:

$$
j(k)=(i-k+n)\bmod n.
$$

The element contributes one point exactly when:

$$
v \le j(k).
$$

Computing this condition for every pair of element and rotation would cost $O(n^2)$. The optimization is to describe, for each element, the whole interval of rotations where it scores and add all intervals with a difference array.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 3, 1, 4, 0]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Understand how the new index changes

As `k` increases by one, the element's new index decreases by one. When it would go below zero, it wraps to `n-1`.

For a positive value `v`, the element is good while its index runs through:

`n-1, n-2, ..., v`.

It is bad while its index is:

`v-1, v-2, ..., 0`.

Thus its scoring rotations form one consecutive interval on the circular rotation axis.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Find where the good circular interval begins

At rotation `k = i`, the element has moved to index zero. At the next rotation it wraps to index `n-1`, which is always at least `v` because `v < n`.

Therefore the first rotation in its good interval is:

$$
l=(i+1)\bmod n.
$$

This is the code's `l`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 3, 1, 4, 0]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Recompute every score:** Applying each of $n$ rotations to all $n$ elements costs $O(n^2)$ time.
- **Explicit circular range updates:** Add the missing baseline for wrapped intervals and initialize the score exactly. It is easier to interpret numerically but not necessary for finding the argmax.
- **Event sweep from rotation zero's actual score:** Compute score zero, then record which elements gain or lose as rotation advances. This gives another $O(n)$ difference formulation.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. The first pass processes each of the $n$ elements once and performs constant arithmetic and two difference updates. The second pass takes $O(n)$ time to recover all shifted scores. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
