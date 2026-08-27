# Guided Example: Find All K-Distant Indices in an Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [3, 4, 9, 1, 3, 9, 5], "key": 9, "k": 1}`
- **Required output:** `[1, 2, 3, 4, 5, 6]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** integer array `nums` and two integers `key` and `k`. A **k-distant index** is an index `i` of `nums` for which there exists at least one index `j` such that $|i - j| \le k$ and $\text{nums}[j] = key$.

The objective is to compute `[1, 2, 3, 4, 5, 6]` from `{"nums": [3, 4, 9, 1, 3, 9, 5], "key": 9, "k": 1}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Choose each candidate output index

The outer loop visits `i` from zero through `n - 1`. Each index is considered once as a possible k-distant index.

The decision for one `i` is an existence question: does at least one valid `j` exist? The method does not need to count how many key positions are nearby.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [3, 4, 9, 1, 3, 9, 5], "key": 9, "k": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Search all possible witness positions lazily

The generator iterates `j` over the complete array. For each position it evaluates

`abs(i - j) <= k and nums[j] == key`.

The absolute difference handles witnesses on either side of `i`. Equality at distance exactly `k` is accepted because the contract uses `<=`.

The expression checks distance first. If it is too large, Python short-circuits `and` and does not read the value comparison for logical purposes, though index generation still continues.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The generator iterates `j` over the complete array.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Use `any` to stop at the first witness

`any(...)` returns true as soon as one generated predicate is true. It does not examine later `j` values after a witness has been found.

If every position fails, it consumes the entire generator and returns false.

This matches the existential definition exactly. One witness is sufficient, and several witnesses must still cause only one output occurrence.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 2, 3, 4, 5, 6]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [3, 4, 9, 1, 3, 9, 5], "key": 9, "k": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 2, 3, 4, 5, 6]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Emit uncovered interval suffixes:** Scan key p:** - **Emit uncovered interval suffixes:** Scan key positions left to right and append only indices beyond the last emitted endpoint. This achieves the manifest's $O(n)$ time.
- **Boolean difference array:** Mark the start and end of every key neighborhood, prefix-sum coverage, and emit covered indices in $O(n)$ time and space.
- **Precollect key positions:** Binary search the nearest key for each `i` in $O(n\log q)$ time, where $q$ is the number of key occurrences.
- **Candidate equals key position:** Distance zero is within every positive `k`, so all key positions qualify.
- **Overlapping neighborhoods:** `any` and one outer append prevent duplicates.
- **Key guaranteed present:** At least one neighborhood exists.
- **`k >= n - 1`:** Every index is within range of every key position, so all indices are returned.
- **Key at an endpoint:** Absolute distance and complete `j` enumeration handle one-sided neighborhoods.
- **Exact boundary distance:** `<= k` includes it.
- **First witness:** `any` short-circuits and avoids unnecessary later checks for that candidate.
- **No witness:** The complete inner range is consumed and `i` is skipped.
- **Sorted output:** Increasing outer iteration supplies the order directly.
- **Input preservation:** The array, key, and distance are only read.
- **Manifest discrepancy:** The stored code is quadratic enumeration rather than linear interval merging.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. There are $n$ outer candidates. In the worst case, `any` examines $O(n)$ positions for each one—for example, when the only key lies near the end and no early witness is found for many candidates. Worst-case time is $O(n^2)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
