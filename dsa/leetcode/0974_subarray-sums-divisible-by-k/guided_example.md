# Guided Example: Subarray Sums Divisible by K

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [4, 5, 0, -2, -3, 1], "k": 5}`
- **Required output:** `7`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums` and an integer `k`, return *the number of non-empty **subarrays** that have a sum divisible by *`k`.

The objective is to compute `7` from `{"nums": [4, 5, 0, -2, -3, 1], "k": 5}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Replace subarray sums with differences of prefix sums

Let prefix sum through index `j` be `P[j]`, with an empty prefix sum zero before the array.

Sum of subarray after earlier prefix `i` through `j` is `P[j] - P[i]`. This difference is divisible by `k` exactly when both prefix sums have the same remainder modulo `k`.

The algorithm counts earlier prefixes by remainder while scanning once.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [4, 5, 0, -2, -3, 1], "k": 5}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: State variables

`s` is current prefix remainder, not the full potentially large sum.

`cnt[r]` is the number of prefixes seen so far whose remainder is `r`.

`ans` is the number of qualifying nonempty subarrays found.

The Counter begins with `{0: 1}`. This represents the empty prefix before index zero.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `s` is current prefix remainder, not the full potentially la... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the empty prefix matters

If a prefix from array start through current position is itself divisible by `k`, its remainder is zero.

Pairing it with the initial empty prefix creates that entire prefix as a valid subarray. Without initial zero count, all valid subarrays starting at index zero would be missed.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `7` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [4, 5, 0, -2, -3, 1], "k": 5}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `7` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Check every subarray:** Prefix sums reduce sum:** - **Check every subarray:** Prefix sums reduce sum lookup but still leave `O(N^2)` pairs.
- **Fixed array of `k` counts:** Avoid hash overhead and gives the same logic.
- **Set of remainders:** Cannot count multiple starts.
- **Single divisible element:** Matches an earlier equal remainder and is counted.
- **Zero element:** Preserves remainder and creates valid subarrays for every prior same remainder.
- **Negative numbers:** Python normalization keeps keys consistent.
- **Whole prefix divisible:** Initial zero entry counts it.
- **Update before query:** Would incorrectly count an empty subarray.
- **All prefix remainders equal:** Each new endpoint adds all earlier prefixes.
- **Nonempty requirement:** Enforced by count-before-increment order.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let `N` be array length.
- **Auxiliary Space Complexity:** $O(k)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
