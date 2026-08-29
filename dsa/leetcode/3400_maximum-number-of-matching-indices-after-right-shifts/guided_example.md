# Guided Example: Maximum Number of Matching Indices After Right Shifts

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums1": [3, 1, 2, 3, 1, 2], "nums2": [1, 2, 3, 1, 2, 3]}`
- **Required output:** `6`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two integer arrays, `nums1` and `nums2`, of the same length.

The objective is to compute `6` from `{"nums1": [3, 1, 2, 3, 1, 2], "nums2": [1, 2, 3, 1, 2, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**Only n distinct shift states exist.** Right-shifting an array of length $n$ by $n$ positions returns it to its original arrangement. Any number of shifts is equivalent to one offset `k` from zero through `n-1`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums1": [3, 1, 2, 3, 1, 2], "nums2": [1, 2, 3, 1, 2, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The outer loop enumerates every such circular alignment.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Map output index back to the original source.** After a right shift by `k`, original element at index `j` moves to `(j+k)%n`. Therefore value appearing at final index `i` came from original index

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `6` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums1": [3, 1, 2, 3, 1, 2], "nums2": [1, 2, 3, 1, 2, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `6` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Materialize each rotation:** It keeps $O(n^2)$ time but spends $O(n)$ temporary space per shift.
- **Frequency correlation/FFT:** It can accelerate matching for compressible value domains but is much more complex for arbitrary integers.
- **Group indices by value:** Difference-frequency counting can derive best offsets in expected $O(n^2)$ worst case and may improve sparse matches.
- **Zero shift:** It is included by `k=0`.
- **Shift n times:** It duplicates zero shift and is omitted.
- **Physical shift mapping:** Loop offset `k` corresponds to right shift `(n-k)%n`.
- **Single element:** The only offset gives one match if values equal, otherwise zero.
- **All values equal:** Every offset has the same match count.
- **Duplicate values:** Each position comparison still contributes separately.
- **No common values:** Every offset count is zero.
- **Perfect circular match:** Answer is `n`.
- **Several best shifts:** They require no tie-breaking because shift index is not returned.
- **Global rotation:** Individual mismatches cannot be adjusted separately.
- **Plus versus right-shift sign:** Enumerating all residues makes the relabeling harmless.
- **Boolean summation:** true contributes one.
- **Modulo:** It guarantees source index remains within bounds.
- **Input preservation:** No sorting or rotation mutation occurs.
- **Annotation import:** `List` must be available.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. There are $n$ offsets and $n$ comparisons per offset, giving $O(n^2)$ time. With $n\le3000$, this is up to nine million comparisons.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
