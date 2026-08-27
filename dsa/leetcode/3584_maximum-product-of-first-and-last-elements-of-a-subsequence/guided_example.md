# Guided Example: Maximum Product of First and Last Elements of a Subsequence

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [-1, -9, 2, 3, -2, -3, 1], "m": 1}`
- **Required output:** `81`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums` and an integer `m`.

The objective is to compute `81` from `{"nums": [-1, -9, 2, 3, -2, -3, 1], "m": 1}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Eligibility boundary

The first possible last endpoint is `m-1`. At last index `i`, index `i-m+1` becomes newly eligible as a first endpoint.

The loop assigns:

`y=nums[i-m+1]`

and folds `y` into running `mi` and `mx`. Those extrema then cover exactly prefix indices zero through `i-m+1`.

Earlier eligible indices stay eligible for every later last endpoint, so no removal is needed.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [-1, -9, 2, 3, -2, -3, 1], "m": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why only minimum and maximum are needed

For fixed last value `x`, the product `x*y` is a linear function of eligible first value `y`.

- If `x` is positive, the largest `y` maximizes the product.
- If `x` is negative, the smallest, most negative `y` maximizes it.
- If `x=0`, every product is zero.

Checking both `x*mi` and `x*mx` covers every sign without branching. No interior eligible value can beat both extremes.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For fixed last value `x`, the product `x*y` is a linear func... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Subsequence existence

For endpoints `p` and `i` with `i-p\ge m-1`, there are at least `m-2` positions strictly between them. Selecting any `m-2` in increasing order creates a size-`m` subsequence with those endpoints.

If the gap is smaller, there are not enough positions. The eligibility boundary is therefore necessary and sufficient.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `81` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [-1, -9, 2, 3, -2, -3, 1], "m": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `81` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate endpoint pairs:** Testing all `p,i` :** - **Enumerate endpoint pairs:** Testing all `p,i` costs `O(n^2)`; the eligible extrema summarize every useful first value.
- **Sort eligible values:** Maintaining a sorted prefix is unnecessary because a linear product needs only two extremes.
- **All positive values:** The running maximum first value determines every endpoint’s best product.
- **All negative values:** Pairing a negative last value with the minimum eligible first value can produce the largest positive product.
- **Mixed signs:** Checking both extremes handles positive and negative last values uniformly.
- **Zero values:** They can produce zero, which may beat negative feasible products.
- **m equals n:** Only the complete array is a size-`n` subsequence, and the loop has one iteration using its endpoints.
- **m equals one:** The maximum square is returned as explained, despite extrema containing earlier values.
- **Duplicate values:** Not prohibited or needed for the proof; endpoints are chosen by index.
- **Large magnitude:** Products reach `10^{10}`, safely handled by Python integers.
- **Subsequence, not subarray:** Intermediate elements need not be contiguous, which is why endpoint distance alone establishes feasibility.
- **Input preservation:** The algorithm reads values without sorting or mutation.
- **Initialization with infinities:** The first loop iteration replaces both extrema before any product is evaluated.
- **Why middle values never affect the objective:** Once endpoint indices leave enough room, the remaining positions can be selected solely to reach size `m`. Their numeric values are not multiplied into the score, so optimizing or sorting them would solve a condition the problem never asks about.
- **Order-preserving endpoints:** The first index must precede the last, which is why only a growing prefix is summarized. A global minimum or maximum from the entire array could lie after `i` and would produce an invalid subsequence orientation.
- **Two extreme products:** Evaluating both is constant work and avoids fragile sign cases. It remains correct when an extreme is zero or when minimum and maximum are the same single eligible value.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. The loop processes each possible last endpoint once. Updating extrema and evaluating products are constant-time, so time is `O(n)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
