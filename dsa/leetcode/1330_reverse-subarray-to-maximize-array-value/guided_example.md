# Guided Example: Reverse Subarray To Maximize Array Value

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 3, 1, 5, 4]}`
- **Required output:** `10`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`. The *value* of this array is defined as the sum of $|\text{nums}[i] - nums[i + 1]|$ for all $0 \le i < \text{nums.length} - 1$.

The objective is to compute `10` from `{"nums": [2, 3, 1, 5, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Original value and no-improvement option

`s` is the sum of `abs(x - y)` for every adjacent pair. `ans` begins equal to `s`.

This preserves the option of reversing a one-element subarray or choosing a reversal with no gain. The algorithm never has to accept a negative improvement.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 3, 1, 5, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Reversal beginning at index zero

Suppose a reversed prefix ends at element `x`, followed by `y` outside the prefix. The old crossing edge contributes `abs(x - y)`.

After reversal, the original first element `nums[0]` becomes the prefix's right endpoint, so the new crossing edge is `abs(nums[0] - y)`.

The candidate value is:

`s + abs(nums[0] - y) - abs(x - y)`.

The first loop tests this for every adjacent pair `(x, y)`, covering every possible non-full prefix endpoint.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Suppose a reversed prefix ends at element `x`, followed by `... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Reversal ending at the last index

For a reversed suffix beginning immediately after outside element `x`, its original first element is `y` and the array's last element moves next to `x`.

The old boundary cost is `abs(x - y)`, and the new cost is `abs(nums[-1] - x)`. The second candidate line tests:

`s + abs(nums[-1] - x) - abs(x - y)`.

Together, these two formulas cover every reversal touching exactly one array end. Reversing the whole array changes no absolute adjacent differences and is already represented by `ans = s`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `10` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 3, 1, 5, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `10` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Try every subarray and recompute:** It can tak:** - **Try every subarray and recompute:** It can take cubic time and repeats unchanged internal contributions.
- **Try every boundary pair using the gain formula:** Recognizing boundary-only changes reduces recomputation but remains $O(n^2)$.
- **Prefix reversal:** Exactly one original adjacent edge changes, handled by the first candidate formula.
- **Suffix reversal:** Exactly one edge changes, handled by the second formula.
- **Whole-array reversal:** Every edge merely changes orientation, so total value is unchanged.
- **Length two:** Any reversal preserves the sole absolute difference, and `ans` remains `s`.
- **Repeated equal values:** Zero-cost edges participate normally in the formulas.
- **Negative numbers:** Absolute differences and sign identities work without a nonnegative-value assumption.
- **No beneficial reversal:** Initializing `ans = s` and clipping interior gain at zero returns the original value.
- **Four sign pairs:** Omitting any can miss an absolute-value orientation and therefore the optimal reversal.
- **Lazy `pairwise`:** It does not allocate all adjacent tuples, preserving constant auxiliary space.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the array length.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
