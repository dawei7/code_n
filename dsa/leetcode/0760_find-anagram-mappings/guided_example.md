# Guided Example: Find Anagram Mappings

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums1": [12, 28, 46, 32, 50], "nums2": [50, 12, 32, 46, 28]}`
- **Required output:** `[1, 4, 3, 2, 0]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two integer arrays `nums1` and `nums2` where `nums2` is **an anagram** of `nums1`. Both arrays may contain duplicates.

The objective is to compute `[1, 4, 3, 2, 0]` from `{"nums1": [12, 28, 46, 32, 50], "nums2": [50, 12, 32, 46, 28]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Map each value to any valid index in the second array

The output requires `nums1[i] == nums2[mapping[i]]` for every position. Since `nums2` is an anagram of `nums1`, every source value occurs at least once in the second array.

The local contract permits any matching index for each output entry and does not require different duplicate occurrences to consume different indices. This lets one dictionary entry per value solve the problem.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums1": [12, 28, 46, 32, 50], "nums2": [50, 12, 32, 46, 28]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build the value-to-index dictionary

The comprehension

`d = {x: i for i, x in enumerate(nums2)}`

visits `nums2` from left to right. For a value seen once, it stores that position. If the value appears again, the later assignment overwrites the earlier one, so the final dictionary contains the last occurrence index.

Choosing the last occurrence is not required; it is simply the deterministic result of the comprehension. Any stored occurrence has the correct value.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The comprehension

`d = {x: i for i, x in enumerate(nums2)}`... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Construct the mapping

For every value `x` in `nums1`, the result appends `d[x]`. By dictionary construction, `nums2[d[x]] == x`, so each output position satisfies the required equality.

The anagram guarantee ensures `x` is always a key. No missing-value branch or default is necessary.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 4, 3, 2, 0]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums1": [12, 28, 46, 32, 50], "nums2": [50, 12, 32, 46, 28]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 4, 3, 2, 0]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Store all indices per value:** Use a dictionar:** - **Store all indices per value:** Use a dictionary of lists and pop an index for every source occurrence. This supports a stricter one-to-one occurrence mapping with the same asymptotic bounds.
- **- **Nested search:** Scan `nums2` for every source:** - **Nested search:** Scan `nums2` for every source value. It uses little extra storage but costs `O(n^2)`.
- **- **Sort both arrays with original indices:** This:** - **Sort both arrays with original indices:** This can pair duplicates uniquely but costs `O(n log n)` time.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the common array length. Building the dictionary visits `nums2` once in expected `O(n)` time. Constructing the output visits `nums1` once with expected constant-time lookups, also `O(n)`. Total expected time is `O(n)`.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
