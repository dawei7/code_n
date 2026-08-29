# Guided Example: Move Zeroes

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [0, 1, 0, 3, 12]}`
- **Required output:** `[1, 3, 12, 0, 0]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

The objective is to compute `[1, 3, 12, 0, 0]` from `{"nums": [0, 1, 0, 3, 12]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Reframe the task as stable compaction

Moving every zero to the end while preserving nonzero order is equivalent to compacting all nonzero values into the earliest array positions. Once every nonzero has been placed in front, all remaining positions must be zeros because the operation only rearranges existing elements.

The exact solution performs this compaction with two conceptual pointers:

- `i`, supplied by `enumerate`, scans every original position from left to right;
- `k` is the next position where an encountered nonzero value belongs.

The scan pointer discovers values, while the write pointer marks the boundary between the compacted nonzero prefix and the zeros waiting behind it.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [0, 1, 0, 3, 12]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Maintain three regions during the scan

Immediately before processing index `i`, the array has this logical structure:



More precisely:

1. indices before `k` contain exactly the nonzero values encountered so far, in their original relative order;
2. indices from `k` through `i - 1` contain zeros; and
3. indices from `i` onward have not yet been processed by the scan.

This invariant explains why an adjacent-looking swap between `k` and `i` is safe even when those indices are far apart.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: When the current value is zero, leave it in the zero region

The source stores the current enumerated value in `x` and checks `if x`. For integer inputs, Python treats zero as false and every positive or negative nonzero integer as true.

If `x` is zero, no compaction write is needed. The scan advances to the next index while `k` stays fixed. The zero at `i` simply enlarges the middle zero region by one position.

Skipping writes for zeros is useful: a two-pass overwrite solution might later rewrite many positions with zero even when they already contain zero. This swap-based method lets zeros move into their final suffix positions as a consequence of relocating nonzero values.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 3, 12, 0, 0]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [0, 1, 0, 3, 12]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 3, 12, 0, 0]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Overwrite then fill zeros:** Copy nonzeros forward with a write pointer, then assign zero to every remaining suffix position. This is also stable, $O(n)$ time, and $O(1)$ space, but it always performs a second filling phase.
- **Extra result array:** Append all nonzeros and then enough zeros to a new list. It is simple but violates the in-place $O(1)$-space requirement.
- **Unstable two-ended partition:** Swapping zeros with arbitrary nonzeros from the right can group zeros at the end but reverses or otherwise changes nonzero relative order.
- **No zeros:** `k == i` at every iteration, so the exact source self-swaps every value and leaves the list unchanged.
- **All zeros:** The condition is never true, `k` remains zero, and no writes occur.
- **Leading zeros:** Early nonzeros swap into the prefix, pushing those zeros rightward one at a time.
- **Trailing zeros:** Nonzeros already occupy their stable prefix positions; trailing zeros are skipped and remain in place.
- **Consecutive zeros:** They simply widen the middle zero region. The next nonzero jumps over the entire region with one swap.
- **Negative values:** Any negative integer is truthy in Python and is correctly treated as nonzero.
- **Duplicate nonzero values:** Stability concerns occurrences, not distinct values. Encounter order is preserved even when values compare equal.
- **Length one:** Either the single zero is skipped or the single nonzero is self-swapped; both outcomes are valid.
- **Cached loop value `x`:** `enumerate` supplies the current value before the swap. The decision is therefore based on the element originally encountered at index `i`, while subsequent iterations read the array's then-current contents. The invariant ensures swaps only place zero into an already processed index `i`, never corrupting the unprocessed suffix.
- **Input mutation:** In-place modification is required. Callers that need the original arrangement must make their own copy before invoking the method.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the array length. `enumerate` visits each position exactly once. Each iteration performs a constant-time truth test and, for a nonzero, one constant-time tuple swap. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
